# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class WorkProgramOccurrence(models.Model):
    """
    Detail line of a work program holding one planned implementation date
    (or a run of consecutive days) of the program, with an optional time
    window and venue. Each occurrence has its own status so that the
    planned dates can be marked done or cancelled one by one, and it can
    be generated in bulk from a recurrence rule of the work program.
    """

    _name = "work_program_occurrence"
    _description = "Work Program Occurrence"
    _order = "date_start, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this occurrence belongs to.",
    )
    name = fields.Char(
        string="Name",
        help="Short label of the occurrence, for example the session name.",
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
        help="First day of the occurrence.",
    )
    date_end = fields.Date(
        string="Date End",
        compute="_compute_date_end",
        store=True,
        compute_sudo=True,
        readonly=False,
        required=True,
        help=(
            "Last day of the occurrence. It starts equal to the start date "
            "and can be moved forward for an occurrence lasting several days."
        ),
    )
    time_start = fields.Float(
        string="Time Start",
        help="Optional start time of day of the occurrence.",
    )
    time_end = fields.Float(
        string="Time End",
        help="Optional end time of day of the occurrence.",
    )
    location = fields.Char(
        string="Location",
        help="Venue where the occurrence takes place.",
    )
    state = fields.Selection(
        string="Status",
        selection=[
            ("planned", "Planned"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        required=True,
        default="planned",
        readonly=True,
        copy=False,
        help=(
            "Planned = still to be carried out, Done = carried out, "
            "Cancelled = will not take place."
        ),
    )
    rundown_ids = fields.One2many(
        string="Rundown",
        comodel_name="work_program_rundown",
        inverse_name="occurrence_id",
        help="Schedule of activities that make up this occurrence.",
    )

    @api.depends("date_start")
    def _compute_date_end(self):
        """Propose the start date as the end date of the occurrence.

        The end date starts equal to ``date_start``; it stays editable, so a
        value typed by the user is kept until the start date changes again.
        """
        for record in self:
            result = record.date_start
            record.date_end = result

    @api.model_create_multi
    def create(self, vals_list):
        """Fill a missing end date with the start date before inserting.

        ``date_end`` is a required stored computed field; the database row
        is inserted before computed values exist, so the value has to be
        given up front or the NOT NULL constraint would reject the row.

        :param vals_list: list of value dicts of the records to create.
        :return: the created records.
        """
        for vals in vals_list:
            if not vals.get("date_end") and vals.get("date_start"):
                vals["date_end"] = vals["date_start"]
        return super().create(vals_list)

    @api.constrains("date_start", "date_end")
    def _check_date_order(self):
        """Reject an occurrence that ends before it starts.

        :raises ValidationError: ``date_end`` is earlier than
            ``date_start``.
        """
        for record in self.sudo():
            if not record._check_date_order_condition():
                error_message = (
                    _(
                        """
Context: Set work program occurrence dates
Database ID: %s
Problem: Date End is earlier than Date Start
Solution: Enter a Date End on or after the Date Start
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_date_order_condition(self):
        """Tell whether the occurrence ends on or after its start.

        Extension point of ``_check_date_order``.

        :return: ``True`` when the dates are in order or one is missing.
        """
        self.ensure_one()
        if not self.date_start or not self.date_end:
            return True
        return self.date_end >= self.date_start

    @api.constrains("work_program_id", "date_start", "date_end")
    def _check_within_program(self):
        """Reject an occurrence outside the date range of its program.

        :raises ValidationError: a date falls before the program start or
            after the program end.
        """
        for record in self.sudo():
            if not record._check_within_program_condition():
                error_message = (
                    _(
                        """
Context: Set work program occurrence dates
Database ID: %s
Problem: The occurrence dates are outside the work program period
Solution: Choose dates between %s and %s
"""
                    )
                    % (
                        record.id,
                        record.work_program_id.date_start,
                        record.work_program_id.date_end,
                    )
                )
                raise ValidationError(error_message)

    def _check_within_program_condition(self):
        """Tell whether the occurrence lies inside its program period.

        Extension point of ``_check_within_program``.

        :return: ``True`` when both dates are inside the period of the
            work program, or when a date needed for the test is missing.
        """
        self.ensure_one()
        program = self.work_program_id
        if not (program.date_start and program.date_end):
            return True
        if not (self.date_start and self.date_end):
            return True
        return (
            program.date_start <= self.date_start and self.date_end <= program.date_end
        )

    @api.constrains("time_start", "time_end")
    def _check_time_order(self):
        """Reject a time window that ends before it starts.

        :raises ValidationError: both times are filled in and ``time_end``
            is not later than ``time_start``.
        """
        for record in self.sudo():
            if not record._check_time_order_condition():
                error_message = (
                    _(
                        """
Context: Set work program occurrence time
Database ID: %s
Problem: Time End must be later than Time Start
Solution: Enter an end time later than the start time
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_time_order_condition(self):
        """Tell whether the time window is in order.

        Extension point of ``_check_time_order``. A time of ``0.0`` is
        treated as not filled in, so the test only applies when both times
        are set.

        :return: ``True`` when a time is missing or the end is later.
        """
        self.ensure_one()
        if not (self.time_start and self.time_end):
            return True
        return self.time_end > self.time_start

    def action_done(self):
        """Mark the occurrence as carried out.

        Moves every planned occurrence of the recordset to ``done``.
        Nothing is returned; the client reloads the view.
        """
        for record in self.sudo():
            record._done()

    def _done(self):
        """Set a planned occurrence to ``done``.

        :raises UserError: the occurrence is not in ``planned`` state.
        """
        self.ensure_one()
        self._check_state_before("planned", "mark as done")
        self.write({"state": "done"})

    def action_cancel(self):
        """Mark the occurrence as cancelled.

        Moves every planned occurrence of the recordset to ``cancel``.
        A cancelled occurrence is ignored when the completeness of the work
        program is evaluated. Nothing is returned.
        """
        for record in self.sudo():
            record._cancel()

    def _cancel(self):
        """Set a planned occurrence to ``cancel``.

        :raises UserError: the occurrence is not in ``planned`` state.
        """
        self.ensure_one()
        self._check_state_before("planned", "cancel")
        self.write({"state": "cancel"})

    def action_reset(self):
        """Put a done or cancelled occurrence back to planned.

        Nothing is returned; the client reloads the view.
        """
        for record in self.sudo():
            record._reset()

    def _reset(self):
        """Set a done or cancelled occurrence back to ``planned``.

        :raises UserError: the occurrence is still ``planned``.
        """
        self.ensure_one()
        if self.state == "planned":
            self._raise_state_error("reset to planned")
        self.write({"state": "planned"})

    def _check_state_before(self, expected_state, action_label):
        """Make sure the occurrence is in the state an action starts from.

        :param expected_state: state the action is allowed from.
        :param action_label: human readable action used in the message.
        :raises UserError: the occurrence is in another state.
        """
        self.ensure_one()
        if self.state != expected_state:
            self._raise_state_error(action_label)

    def _raise_state_error(self, action_label):
        """Raise the structured error of a refused state change.

        :param action_label: human readable action used in the message.
        :raises UserError: always.
        """
        self.ensure_one()
        error_message = (
            _(
                """
Context: Change work program occurrence status (%s)
Database ID: %s
Problem: The occurrence cannot be changed from status '%s'
Solution: Check the status of the occurrence before running this action
"""
            )
            % (action_label, self.id, self.state)
        )
        raise UserError(error_message)
