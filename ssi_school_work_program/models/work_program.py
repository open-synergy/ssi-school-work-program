# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

from odoo.addons.ssi_decorator import ssi_decorator

PLANNING_SECTIONS = [
    "occurrence",
    "target",
    "objective",
    "committee",
    "material",
    "resource",
    "need",
    "rundown",
]


class WorkProgram(models.Model):
    """
    Represents one item of the annual work plan of a school (a "program
    kerja"): a planned activity of one school in one academic year, with
    its background, participant targets, objectives and indicators,
    committee, materials, resources, needs, implementation dates and
    rundown. Only the plan is recorded here; the realization and the
    evaluation belong to separate documents. The document is approved
    through the multiple approval workflow (Draft, Confirm, Open, Done),
    owns an analytic account that other features can attach to, and can
    generate its recurring implementation dates from a frequency set.
    """

    _name = "work_program"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_open",
        "mixin.transaction_confirm",
        "mixin.status_check",
        "mixin.company_currency",
    ]
    _description = "Work Program"
    _order = "date_start desc, id desc"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_open_policy_fields = False
    _automatically_insert_open_button = False

    _status_check_create_page = True

    _statusbar_visible_label = "draft,confirm,open,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "done_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_reload_approval_template",
        "action_generate_occurrence",
        "action_create_analytic_account",
        "action_done",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_open",
        "dom_done",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "open"

    title = fields.Char(
        string="Title",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Short name of the activity planned by this work program.",
    )
    school_id = fields.Many2one(
        string="School",
        comodel_name="school",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="School that carries out this work program.",
    )
    academic_year_id = fields.Many2one(
        string="Academic Year",
        comodel_name="school_academic_year",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Academic year this work program is planned for.",
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="work_program_type",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Type of the work program. It decides which planning sections "
            "are mandatory and the analytic group of the analytic account."
        ),
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="work_program_category",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Category used to classify and group the work program.",
    )
    strategic_objective_id = fields.Many2one(
        string="Strategic Objective",
        comodel_name="work_program_strategic_objective",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Strategic objective of the school this program contributes to.",
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "First day of the period in which the program is carried out. "
            "It is also the date used by the document number sequence."
        ),
    )
    date_end = fields.Date(
        string="Date End",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Last day of the period in which the program is carried out.",
    )
    background_need = fields.Text(
        string="Background: Need",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="The need or problem that makes this program necessary.",
    )
    background_context = fields.Text(
        string="Background: Context",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="The context and circumstances surrounding the program.",
    )
    participant_criteria = fields.Text(
        string="Participant Criteria",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Criteria used to select the participants of the program.",
    )
    pic_id = fields.Many2one(
        string="Person in Charge",
        comodel_name="hr.employee",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Employee who is responsible for the whole program.",
    )
    budget_ceiling = fields.Monetary(
        string="Budget Ceiling",
        currency_field="company_currency_id",
        default=0.0,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Maximum budget the program may use. The budget itself is "
            "managed on the analytic account of the program, not here."
        ),
    )
    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
        readonly=True,
        copy=False,
        ondelete="restrict",
        help=(
            "Analytic account of the program, used by other features to "
            "attach their records to it. It is created from the button or "
            "automatically when the program is opened."
        ),
    )
    frequency_set_id = fields.Many2one(
        string="Frequency Set",
        comodel_name="frequency_set",
        readonly=True,
        states={
            "draft": [("readonly", False)],
            "open": [("readonly", False)],
        },
        help=(
            "Recurrence rules used to generate the occurrence dates of the "
            "program between its start and end date."
        ),
    )
    planning_cycle = fields.Selection(
        string="Planning Cycle",
        selection=[
            ("regular", "Regular"),
            ("additional", "Additional"),
        ],
        compute="_compute_planning_cycle",
        store=True,
        compute_sudo=True,
        readonly=False,
        required=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Regular when the program is planned on or before the planning "
            "deadline of its academic year (or the year has no deadline); "
            "Additional otherwise. It is proposed automatically and can be "
            "changed while the program is in draft."
        ),
    )
    target_ids = fields.One2many(
        string="Participant Targets",
        comodel_name="work_program_target",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Groups of intended participants and their planned numbers.",
    )
    objective_ids = fields.One2many(
        string="Objectives",
        comodel_name="work_program_objective",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Planned objectives with their indicators, baseline and target.",
    )
    committee_ids = fields.One2many(
        string="Committee",
        comodel_name="work_program_committee",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Employees who form the committee of the program.",
    )
    material_ids = fields.One2many(
        string="Materials",
        comodel_name="work_program_material",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Materials prepared for the program.",
    )
    resource_ids = fields.One2many(
        string="Resource Persons",
        comodel_name="work_program_resource",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="People taking part in the program who are not in the committee.",
    )
    need_ids = fields.One2many(
        string="Needs",
        comodel_name="work_program_need",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Equipment, venues and supplies the program needs.",
    )
    occurrence_ids = fields.One2many(
        string="Occurrences",
        comodel_name="work_program_occurrence",
        inverse_name="work_program_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Planned implementation dates of the program.",
    )
    section_occurrence_ok = fields.Boolean(
        string="Occurrence Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the occurrence section is filled in, i.e. there is "
            "at least one occurrence that is not cancelled."
        ),
    )
    section_target_ok = fields.Boolean(
        string="Target Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the target section is filled in, i.e. there is "
            "at least one participant target line."
        ),
    )
    section_objective_ok = fields.Boolean(
        string="Objective Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the objective section is filled in, i.e. there is "
            "at least one objective line."
        ),
    )
    section_committee_ok = fields.Boolean(
        string="Committee Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the committee section is filled in, i.e. there is "
            "at least one committee member line."
        ),
    )
    section_material_ok = fields.Boolean(
        string="Material Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the material section is filled in, i.e. there is "
            "at least one material line."
        ),
    )
    section_resource_ok = fields.Boolean(
        string="Resource Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the resource section is filled in, i.e. there is "
            "at least one resource person line."
        ),
    )
    section_need_ok = fields.Boolean(
        string="Need Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the need section is filled in, i.e. there is "
            "at least one need line."
        ),
    )
    section_rundown_ok = fields.Boolean(
        string="Rundown Section Complete",
        compute="_compute_section_ok",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when the rundown section is filled in, i.e. there is "
            "at least one occurrence that is not cancelled and every such "
            "occurrence has at least one rundown line."
        ),
    )
    planning_complete = fields.Boolean(
        string="Planning Complete",
        compute="_compute_planning_complete",
        store=True,
        compute_sudo=True,
        help=(
            "Checked when every planning section required by the type of "
            "the program is filled in. It is informative only and does not "
            "block the confirmation of the program."
        ),
    )
    generate_occurrence_ok = fields.Boolean(
        string="Can Generate Occurrence",
        compute="_compute_policy",
        store=False,
        compute_sudo=True,
        help=(
            "Policy that determines whether the Generate Occurrence button "
            "is visible."
        ),
    )
    create_analytic_account_ok = fields.Boolean(
        string="Can Create Analytic Account",
        compute="_compute_policy",
        store=False,
        compute_sudo=True,
        help=(
            "Policy that determines whether the Create Analytic Account "
            "button is visible."
        ),
    )

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "done_ok",
            "cancel_ok",
            "open_ok",
            "restart_ok",
            "manual_number_ok",
            "restart_approval_ok",
            "generate_occurrence_ok",
            "create_analytic_account_ok",
        ]
        res += policy_field
        return res

    @api.model
    def _get_planning_cycle(self, academic_year):
        """Return the planning cycle for a work program of a given year.

        The cycle is ``regular`` when the academic year has no
        ``work_program_planning_deadline`` or today (in the timezone of the
        user) is not after it, and ``additional`` otherwise.

        :param academic_year: ``school_academic_year`` record, may be empty
        :return: ``"regular"`` or ``"additional"``
        """
        today = fields.Date.context_today(self)
        deadline = academic_year.work_program_planning_deadline
        result = "regular"
        if deadline and today > deadline:
            result = "additional"
        return result

    @api.depends("academic_year_id")
    def _compute_planning_cycle(self):
        """Propose the planning cycle from the year planning deadline.

        The value only depends on ``academic_year_id`` and is not
        recomputed when the deadline moves, so a program keeps the cycle it
        was planned in. The rule itself is in ``_get_planning_cycle``.
        """
        for record in self:
            result = record._get_planning_cycle(record.academic_year_id)
            record.planning_cycle = result

    @api.model_create_multi
    def create(self, vals_list):
        """Fill a missing planning cycle before the row is inserted.

        ``planning_cycle`` is a required stored computed field; the
        database row is inserted before computed values exist, so the
        value has to be given up front or the NOT NULL constraint would
        reject the row.

        :param vals_list: list of value dicts of the records to create.
        :return: the created records.
        """
        year_model = self.env["school_academic_year"]
        for vals in vals_list:
            if not vals.get("planning_cycle"):
                year = year_model.browse(vals.get("academic_year_id"))
                vals["planning_cycle"] = self._get_planning_cycle(year)
        return super().create(vals_list)

    @api.depends(
        "target_ids",
        "objective_ids",
        "committee_ids",
        "material_ids",
        "resource_ids",
        "need_ids",
        "occurrence_ids.state",
        "occurrence_ids.rundown_ids",
    )
    def _compute_section_ok(self):
        """Tell which of the eight planning sections are filled in.

        Seven sections are complete when their lines exist; the occurrence
        section needs at least one occurrence that is not cancelled, and
        the rundown section needs at least one such occurrence and a
        rundown line on each of them. Cancelled occurrences are ignored.
        """
        for record in self:
            live = record.occurrence_ids.filtered(lambda r: r.state != "cancel")
            result = {
                "occurrence": bool(live),
                "target": bool(record.target_ids),
                "objective": bool(record.objective_ids),
                "committee": bool(record.committee_ids),
                "material": bool(record.material_ids),
                "resource": bool(record.resource_ids),
                "need": bool(record.need_ids),
                "rundown": bool(live) and all(rec.rundown_ids for rec in live),
            }
            for key in PLANNING_SECTIONS:
                record["section_%s_ok" % key] = result[key]

    @api.depends(
        "section_occurrence_ok",
        "section_target_ok",
        "section_objective_ok",
        "section_committee_ok",
        "section_material_ok",
        "section_resource_ok",
        "section_need_ok",
        "section_rundown_ok",
        "type_id.require_occurrence",
        "type_id.require_target",
        "type_id.require_objective",
        "type_id.require_committee",
        "type_id.require_material",
        "type_id.require_resource",
        "type_id.require_need",
        "type_id.require_rundown",
    )
    def _compute_planning_complete(self):
        """Tell whether every section required by the type is complete.

        A section only counts when the matching ``require_<section>`` flag
        of ``type_id`` is checked; the other sections are ignored.
        """
        for record in self:
            result = True
            for key in PLANNING_SECTIONS:
                required = record.type_id["require_%s" % key]
                if required and not record["section_%s_ok" % key]:
                    result = False
            record.planning_complete = result

    @api.constrains("date_start", "date_end")
    def _check_period(self):
        """Reject a work program that ends before it starts.

        :raises ValidationError: ``date_end`` is earlier than
            ``date_start``.
        """
        for record in self.sudo():
            if not record._check_period_condition():
                error_message = (
                    _(
                        """
Context: Set work program period
Database ID: %s
Problem: Date End is earlier than Date Start
Solution: Enter a Date End on or after the Date Start
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_period_condition(self):
        """Tell whether the period of the program is in order.

        Extension point of ``_check_period``.

        :return: ``True`` when ``date_end`` is on or after ``date_start``.
        """
        self.ensure_one()
        if not self.date_start or not self.date_end:
            return True
        return self.date_end >= self.date_start

    def action_generate_occurrence(self):
        """Generate the occurrence dates from the frequency set.

        Creates, for every record of the recordset, one occurrence per
        date given by ``frequency_set_id`` between the start and end date
        of the program. Dates that already have an occurrence are skipped
        and existing occurrences are never deleted, so the action can be
        run again safely. Nothing is returned.
        """
        for record in self.sudo():
            record._generate_occurrence()

    def _generate_occurrence(self):
        """Create the missing occurrences of the program.

        Reads the dates from ``_get_occurrence_dates`` and creates one
        occurrence, starting and ending on that day, for each date that is
        not yet the start date of an existing occurrence.

        :raises UserError: the program has no frequency set.
        """
        self.ensure_one()
        if not self.frequency_set_id:
            error_message = (
                _(
                    """
Context: Generate work program occurrence
Database ID: %s
Problem: The work program has no frequency set
Solution: Select a frequency set, then generate the occurrence again
"""
                )
                % (self.id,)
            )
            raise UserError(error_message)
        existing = set(self.occurrence_ids.mapped("date_start"))
        occurrence_model = self.env["work_program_occurrence"]
        for day in self._get_occurrence_dates():
            if day in existing:
                continue
            occurrence_model.create(self._prepare_occurrence_data(day))
            existing.add(day)

    def _get_occurrence_dates(self):
        """Return the dates produced by the frequency set of the program.

        The series runs from ``date_start`` to ``date_end`` in UTC, so the
        calendar dates are not shifted by a timezone. Extension point to
        change how the dates are chosen.

        :return: sorted list of ``datetime.date``
        """
        self.ensure_one()
        rule_set = self.frequency_set_id._get_rruleset(
            dtstart=self.date_start,
            until=self.date_end,
            tz="UTC",
        )
        return sorted({value.date() for value in rule_set})

    def _prepare_occurrence_data(self, day):
        """Build the values of one generated occurrence.

        Extension point of ``_generate_occurrence``.

        :param day: the date of the occurrence
        :return: dict of ``work_program_occurrence`` values
        """
        self.ensure_one()
        return {
            "work_program_id": self.id,
            "name": self.title,
            "date_start": day,
            "date_end": day,
        }

    def action_create_analytic_account(self):
        """Create the analytic account of the program.

        For every record that has no analytic account yet, creates one and
        links it to ``analytic_account_id``. Records that already have one
        are left alone, so no duplicate is ever created. Nothing is
        returned.
        """
        for record in self.sudo():
            record._create_analytic_account()

    def _create_analytic_account(self):
        """Create and link the analytic account if it is still missing."""
        self.ensure_one()
        if self.analytic_account_id:
            return
        account = self.env["account.analytic.account"].create(
            self._prepare_analytic_account_data()
        )
        self.write({"analytic_account_id": account.id})

    def _prepare_analytic_account_data(self):
        """Build the values of the analytic account of the program.

        The account is named after the title and coded after the document
        number (when the number is already assigned), placed in the
        analytic group of the type, and linked to the partner of the
        company. The currency follows the company by itself. Extension
        point of ``_create_analytic_account``.

        :return: dict of ``account.analytic.account`` values
        """
        self.ensure_one()
        code = False
        if self.name and self.name != "/":
            code = self.name
        return {
            "name": self.title,
            "code": code,
            "group_id": self.type_id.analytic_group_id.id,
            "partner_id": self.company_id.partner_id.id,
            "company_id": self.company_id.id,
        }

    @ssi_decorator.post_open_action()
    def _10_create_analytic_account(self):
        """Create the analytic account when the program is opened.

        Post-open hook: runs right after the program reaches ``open`` and
        creates the analytic account unless one was already created from
        the button.
        """
        self.ensure_one()
        self._create_analytic_account()
