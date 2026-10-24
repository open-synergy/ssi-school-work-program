# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramRundown(models.Model):
    """
    Detail line of an occurrence of a work program describing one slot of
    the day schedule: what happens, when, and who is responsible for it.
    """

    _name = "work_program_rundown"
    _description = "Work Program Rundown"
    _order = "occurrence_id, date, time_start, id"

    occurrence_id = fields.Many2one(
        string="Occurrence",
        comodel_name="work_program_occurrence",
        required=True,
        ondelete="cascade",
        help="Occurrence of the work program this rundown line belongs to.",
    )
    date = fields.Date(
        string="Date",
        compute="_compute_date",
        store=True,
        compute_sudo=True,
        readonly=False,
        required=True,
        help=(
            "Day of the rundown line. It starts equal to the start date of "
            "the occurrence and can be moved inside the occurrence period."
        ),
    )
    time_start = fields.Float(
        string="Time Start",
        required=True,
        help="Start time of day of the rundown line.",
    )
    time_end = fields.Float(
        string="Time End",
        required=True,
        help="End time of day of the rundown line.",
    )
    name = fields.Char(
        string="Activity",
        required=True,
        help="What takes place during this slot.",
    )
    pic_id = fields.Many2one(
        string="Person in Charge",
        comodel_name="hr.employee",
        help="Employee responsible for this slot.",
    )

    @api.depends("occurrence_id.date_start")
    def _compute_date(self):
        """Propose the occurrence start date as the day of the line.

        The value stays editable, so a date typed by the user is kept until
        the occurrence start date changes again.
        """
        for record in self:
            result = record.occurrence_id.date_start
            record.date = result

    @api.model_create_multi
    def create(self, vals_list):
        """Fill a missing day with the occurrence start date before insert.

        ``date`` is a required stored computed field; the database row is
        inserted before computed values exist, so the value has to be
        given up front or the NOT NULL constraint would reject the row.

        :param vals_list: list of value dicts of the records to create.
        :return: the created records.
        """
        occurrence_model = self.env["work_program_occurrence"]
        for vals in vals_list:
            if not vals.get("date") and vals.get("occurrence_id"):
                occurrence = occurrence_model.browse(vals["occurrence_id"])
                vals["date"] = occurrence.date_start
        return super().create(vals_list)

    @api.constrains("occurrence_id", "date")
    def _check_date_within_occurrence(self):
        """Reject a rundown day outside the period of its occurrence.

        :raises ValidationError: ``date`` is before the occurrence start or
            after the occurrence end.
        """
        for record in self.sudo():
            if not record._check_date_within_occurrence_condition():
                error_message = (
                    _(
                        """
Context: Set work program rundown date
Database ID: %s
Problem: The date is outside the period of the occurrence
Solution: Choose a date between %s and %s
"""
                    )
                    % (
                        record.id,
                        record.occurrence_id.date_start,
                        record.occurrence_id.date_end,
                    )
                )
                raise ValidationError(error_message)

    def _check_date_within_occurrence_condition(self):
        """Tell whether the rundown day lies inside its occurrence.

        Extension point of ``_check_date_within_occurrence``.

        :return: ``True`` when ``date`` is between the start and end date
            of the occurrence, or when a date needed for the test is
            missing.
        """
        self.ensure_one()
        occurrence = self.occurrence_id
        if not (self.date and occurrence.date_start and occurrence.date_end):
            return True
        return occurrence.date_start <= self.date <= occurrence.date_end

    @api.constrains("time_start", "time_end")
    def _check_time_order(self):
        """Reject a rundown slot that ends before it starts.

        :raises ValidationError: ``time_end`` is not later than
            ``time_start``.
        """
        for record in self.sudo():
            if not record._check_time_order_condition():
                error_message = (
                    _(
                        """
Context: Set work program rundown time
Database ID: %s
Problem: Time End must be later than Time Start
Solution: Enter an end time later than the start time
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_time_order_condition(self):
        """Tell whether the slot ends after it starts.

        Extension point of ``_check_time_order``.

        :return: ``True`` when ``time_end`` is later than ``time_start``.
        """
        self.ensure_one()
        return self.time_end > self.time_start
