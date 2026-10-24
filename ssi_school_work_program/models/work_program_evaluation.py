# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.ssi_decorator import ssi_decorator


class WorkProgramEvaluation(models.Model):
    """
    Represents the evaluation of one work program: what was really
    achieved after (or halfway through) the activity planned in the
    program. A program can have a mid-term evaluation and a final one.
    The evaluation records the actual number of participants per target,
    the achievement of every objective indicator with its evidence, a
    note per implementation date, and the conclusion (note, lesson
    learned and recommendation). It is approved through the multiple
    approval workflow and moves from Confirm straight to Done. All the
    actual data lives here; the work program itself only holds the plan.
    """

    _name = "work_program_evaluation"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
    ]
    _description = "Work Program Evaluation"
    _order = "date desc, id desc"

    # Multiple Approval Attribute
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_done_policy_fields = False
    _automatically_insert_done_button = False

    _statusbar_visible_label = "draft,confirm,done"
    _policy_field_order = [
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "action_reload_approval_template",
        "action_load_lines",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_confirm",
        "dom_reject",
        "dom_done",
        "dom_cancel",
    ]

    # Sequence attribute
    _create_sequence_state = "done"

    work_program_id = fields.Many2one(
        string="Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="restrict",
        domain=[("state", "in", ["open", "done"])],
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Work program that is evaluated. Only a program that is on "
            "progress or done can be evaluated."
        ),
    )
    school_id = fields.Many2one(
        string="School",
        comodel_name="school",
        related="work_program_id.school_id",
        store=True,
        readonly=True,
        help="School that carries out the evaluated work program.",
    )
    academic_year_id = fields.Many2one(
        string="Academic Year",
        comodel_name="school_academic_year",
        related="work_program_id.academic_year_id",
        store=True,
        readonly=True,
        help="Academic year of the evaluated work program.",
    )
    evaluation_type = fields.Selection(
        string="Evaluation Type",
        selection=[
            ("mid", "Mid-term"),
            ("final", "Final"),
        ],
        required=True,
        default="final",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Mid-term evaluates the program while it is still running; "
            "final evaluates it once it is over. Only one non-cancelled "
            "final evaluation is allowed for each work program."
        ),
    )
    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help=(
            "Date of the evaluation. It is also the date used by the "
            "document number sequence and cannot be earlier than the "
            "start date of the work program."
        ),
    )
    evaluation_note = fields.Text(
        string="Evaluation Note",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Overall conclusion about how the work program went.",
    )
    lesson_learned = fields.Text(
        string="Lesson Learned",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="What was learned from carrying out the work program.",
    )
    recommendation = fields.Text(
        string="Recommendation",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="What should be done differently the next time.",
    )
    participant_ids = fields.One2many(
        string="Participants",
        comodel_name="work_program_evaluation_participant",
        inverse_name="evaluation_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Actual number of participants for each participant target.",
    )
    objective_ids = fields.One2many(
        string="Objectives",
        comodel_name="work_program_evaluation_objective",
        inverse_name="evaluation_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Achievement of each objective indicator, with its evidence.",
    )
    occurrence_ids = fields.One2many(
        string="Occurrences",
        comodel_name="work_program_evaluation_occurrence",
        inverse_name="evaluation_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="What happened on each planned implementation date.",
    )
    participant_achievement_percent = fields.Float(
        string="Participant Achievement (%)",
        compute="_compute_participant_achievement_percent",
        store=True,
        compute_sudo=True,
        help=(
            "Average achievement of the participant lines. It is zero "
            "when there is no participant line."
        ),
    )
    objective_achievement_percent = fields.Float(
        string="Objective Achievement (%)",
        compute="_compute_objective_achievement_percent",
        store=True,
        compute_sudo=True,
        help=(
            "Average achievement of the objective lines. It is zero when "
            "there is no objective line."
        ),
    )
    load_lines_ok = fields.Boolean(
        string="Can Load Lines",
        compute="_compute_policy",
        store=False,
        compute_sudo=True,
        help="Policy that determines whether the Load Lines button is visible.",
    )

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "done_ok",
            "cancel_ok",
            "manual_number_ok",
            "load_lines_ok",
        ]
        res += policy_field
        return res

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

    @api.depends("participant_ids.achievement_percent")
    def _compute_participant_achievement_percent(self):
        """Average the achievement of the participant lines.

        The result is zero when the evaluation has no participant line.
        """
        for record in self:
            result = 0.0
            lines = record.participant_ids
            if lines:
                result = sum(lines.mapped("achievement_percent")) / len(lines)
            record.participant_achievement_percent = result

    @api.depends("objective_ids.achievement_percent")
    def _compute_objective_achievement_percent(self):
        """Average the achievement of the objective lines.

        The result is zero when the evaluation has no objective line.
        """
        for record in self:
            result = 0.0
            lines = record.objective_ids
            if lines:
                result = sum(lines.mapped("achievement_percent")) / len(lines)
            record.objective_achievement_percent = result

    @api.constrains("work_program_id", "evaluation_type", "state")
    def _check_unique_final(self):
        """Allow one non-cancelled final evaluation per work program.

        :raises ValidationError: the program already has another final
            evaluation that is not cancelled.
        """
        for record in self.sudo():
            if not record._check_unique_final_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation type
Database ID: %s
Problem: The work program already has a final evaluation
Solution: Cancel the other final evaluation or make this one mid-term
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_unique_final_condition(self):
        """Tell whether the program has at most one live final evaluation.

        Extension point of ``_check_unique_final``.

        :return: ``True`` unless this is a non-cancelled final evaluation
            and another one of the same program exists.
        """
        self.ensure_one()
        if self.evaluation_type != "final" or self.state == "cancel":
            return True
        criteria = [
            ("id", "!=", self.id),
            ("work_program_id", "=", self.work_program_id.id),
            ("evaluation_type", "=", "final"),
            ("state", "!=", "cancel"),
        ]
        return not self.search_count(criteria)

    @api.constrains("date", "work_program_id")
    def _check_date(self):
        """Reject an evaluation dated before its work program starts.

        :raises ValidationError: ``date`` is earlier than the start date
            of the work program.
        """
        for record in self.sudo():
            if not record._check_date_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation date
Database ID: %s
Problem: The date is earlier than the start date of the work program
Solution: Enter a date on or after the start date of the work program
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_date_condition(self):
        """Tell whether the evaluation date is not before the program.

        Extension point of ``_check_date``.

        :return: ``True`` when ``date`` is on or after ``date_start`` of
            the work program, or one of them is missing.
        """
        self.ensure_one()
        start = self.work_program_id.date_start
        if not self.date or not start:
            return True
        return self.date >= start

    def action_load_lines(self):
        """Load the lines of the evaluation from the work program.

        For every record of the recordset, creates a participant line for
        each target, an objective line for each objective and an
        occurrence line for each occurrence that is not cancelled, unless
        the evaluation already has a line for it. Existing lines are
        never changed or deleted, so the action can be run again safely.
        Nothing is returned.
        """
        for record in self.sudo():
            record._load_lines()

    def _load_lines(self):
        """Create the missing lines of the three line sections."""
        self.ensure_one()
        program = self.work_program_id
        done_targets = self.participant_ids.mapped("target_id")
        for target in program.target_ids - done_targets:
            self.env["work_program_evaluation_participant"].create(
                self._prepare_participant_data(target)
            )
        done_objectives = self.objective_ids.mapped("objective_id")
        for objective in program.objective_ids - done_objectives:
            self.env["work_program_evaluation_objective"].create(
                self._prepare_objective_data(objective)
            )
        done_occurrences = self.occurrence_ids.mapped("occurrence_id")
        live = program.occurrence_ids.filtered(lambda r: r.state != "cancel")
        for occurrence in live - done_occurrences:
            self.env["work_program_evaluation_occurrence"].create(
                self._prepare_occurrence_data(occurrence)
            )

    def _prepare_participant_data(self, target):
        """Build the values of one loaded participant line.

        Extension point of ``_load_lines``.

        :param target: the ``work_program_target`` to report on
        :return: dict of ``work_program_evaluation_participant`` values
        """
        self.ensure_one()
        return {
            "evaluation_id": self.id,
            "target_id": target.id,
        }

    def _prepare_objective_data(self, objective):
        """Build the values of one loaded objective line.

        Extension point of ``_load_lines``.

        :param objective: the ``work_program_objective`` to report on
        :return: dict of ``work_program_evaluation_objective`` values
        """
        self.ensure_one()
        return {
            "evaluation_id": self.id,
            "objective_id": objective.id,
        }

    def _prepare_occurrence_data(self, occurrence):
        """Build the values of one loaded occurrence line.

        Extension point of ``_load_lines``.

        :param occurrence: the ``work_program_occurrence`` to report on
        :return: dict of ``work_program_evaluation_occurrence`` values
        """
        self.ensure_one()
        return {
            "evaluation_id": self.id,
            "occurrence_id": occurrence.id,
        }
