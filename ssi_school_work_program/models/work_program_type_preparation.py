# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramTypePreparation(models.Model):
    """
    Detail line of a work program type describing one standard
    preparation task. The lines form the template checklist that can be
    loaded into the occurrences of the work programs of the type, each
    task being due a number of days before the occurrence starts.
    """

    _name = "work_program_type_preparation"
    _description = "Work Program Type Preparation"
    _order = "type_id, sequence, id"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="work_program_type",
        required=True,
        ondelete="cascade",
        help="Work program type this preparation task belongs to.",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
        help="Order of the task in the checklist.",
    )
    name = fields.Char(
        string="Task",
        required=True,
        help="What has to be prepared.",
    )
    lead_days = fields.Integer(
        string="Lead Days",
        required=True,
        default=0,
        help=(
            "Number of days before the start date of the occurrence on "
            "which the task is due."
        ),
    )
    description = fields.Text(
        string="Description",
        help="Further explanation of the task.",
    )

    @api.constrains("lead_days")
    def _check_lead_days(self):
        """Reject a negative number of lead days.

        :raises ValidationError: ``lead_days`` is lower than zero.
        """
        for record in self.sudo():
            if not record._check_lead_days_condition():
                error_message = (
                    _(
                        """
Context: Set work program type preparation lead days
Database ID: %s
Problem: Lead Days cannot be negative
Solution: Enter zero or a positive number of days
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_lead_days_condition(self):
        """Tell whether the lead days are zero or more.

        Extension point of ``_check_lead_days``.

        :return: ``True`` when ``lead_days`` is not negative.
        """
        self.ensure_one()
        return self.lead_days >= 0
