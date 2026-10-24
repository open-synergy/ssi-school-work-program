# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramObjective(models.Model):
    """
    Detail line of a work program holding one planned objective with its
    indicator. The line only records the plan: baseline, target and the
    way to verify it. The achieved value is recorded elsewhere, in the
    evaluation of the work program.
    """

    _name = "work_program_objective"
    _description = "Work Program Objective"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this objective belongs to.",
    )
    kind = fields.Selection(
        string="Kind",
        selection=[
            ("outcome", "Outcome"),
            ("output", "Output"),
        ],
        required=True,
        default="outcome",
        help=(
            "Outcome is the change the program is meant to bring about; "
            "output is the direct product it delivers."
        ),
    )
    name = fields.Char(
        string="Objective",
        required=True,
        help="Statement of what the program intends to achieve.",
    )
    indicator = fields.Char(
        string="Indicator",
        required=True,
        help="Measure used to tell whether the objective has been achieved.",
    )
    measurement_type = fields.Selection(
        string="Measurement Type",
        selection=[
            ("numeric", "Numeric"),
            ("qualitative", "Qualitative"),
        ],
        required=True,
        default="numeric",
        help=(
            "Numeric indicators use the baseline and target values; "
            "qualitative indicators use the target description."
        ),
    )
    baseline_value = fields.Float(
        string="Baseline Value",
        help="Value of the indicator before the program starts.",
    )
    target_value = fields.Float(
        string="Target Value",
        help="Value of the indicator the program aims to reach.",
    )
    uom_name = fields.Char(
        string="Unit",
        help="Free text unit of measure of the baseline and target values.",
    )
    target_description = fields.Char(
        string="Target Description",
        help="Description of the expected result of a qualitative indicator.",
    )
    verification = fields.Char(
        string="Verification",
        help="Method or source used to verify the indicator.",
    )

    @api.constrains("baseline_value", "target_value")
    def _check_values(self):
        """Reject negative baseline or target values.

        :raises ValidationError: a value is lower than zero.
        """
        for record in self.sudo():
            if not record._check_values_condition():
                error_message = (
                    _(
                        """
Context: Set work program objective values
Database ID: %s
Problem: Baseline value and target value must not be negative
Solution: Enter zero or a positive value
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_values_condition(self):
        """Tell whether baseline and target values are not negative.

        Extension point of ``_check_values``.

        :return: ``True`` when both values are zero or greater.
        """
        self.ensure_one()
        return self.baseline_value >= 0 and self.target_value >= 0
