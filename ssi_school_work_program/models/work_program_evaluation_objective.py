# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramEvaluationObjective(models.Model):
    """
    Detail line of a work program evaluation holding the realization of
    one planned objective of the program: the achieved value of its
    indicator, a note and the evidence attached. For a numeric indicator
    the achievement percentage is computed from the actual and target
    values; for a qualitative indicator the user enters it.
    """

    _name = "work_program_evaluation_objective"
    _description = "Work Program Evaluation Objective"
    _order = "evaluation_id, id"

    evaluation_id = fields.Many2one(
        string="# Evaluation",
        comodel_name="work_program_evaluation",
        required=True,
        ondelete="cascade",
        help="Work program evaluation this objective line belongs to.",
    )
    objective_id = fields.Many2one(
        string="Objective",
        comodel_name="work_program_objective",
        required=True,
        ondelete="restrict",
        help=("Objective of the evaluated work program that this line " "reports on."),
    )
    measurement_type = fields.Selection(
        string="Measurement Type",
        related="objective_id.measurement_type",
        readonly=True,
        help="Numeric or qualitative indicator, copied from the plan.",
    )
    baseline_value = fields.Float(
        string="Baseline Value",
        related="objective_id.baseline_value",
        readonly=True,
        help="Value of the indicator before the program, from the plan.",
    )
    target_value = fields.Float(
        string="Target Value",
        related="objective_id.target_value",
        readonly=True,
        help="Value of the indicator the program aimed at, from the plan.",
    )
    target_description = fields.Char(
        string="Target Description",
        related="objective_id.target_description",
        readonly=True,
        help="Expected result of a qualitative indicator, from the plan.",
    )
    actual_value = fields.Float(
        string="Actual Value",
        help="Value of the numeric indicator that was actually reached.",
    )
    actual_note = fields.Text(
        string="Actual Note",
        help="Description of the result that was actually reached.",
    )
    attachment_ids = fields.Many2many(
        string="Evidence",
        comodel_name="ir.attachment",
        relation="work_program_evaluation_objective_attachment_rel",
        column1="objective_line_id",
        column2="attachment_id",
        help="Files that prove the result reported on this line.",
    )
    achievement_percent = fields.Float(
        string="Achievement (%)",
        compute="_compute_achievement_percent",
        store=True,
        compute_sudo=True,
        readonly=False,
        help=(
            "Numeric indicator: actual value as a percentage of the target "
            "value, zero when the target is zero. Qualitative indicator: "
            "the percentage entered by the user, which is kept as is."
        ),
    )

    @api.depends(
        "actual_value",
        "objective_id.target_value",
        "objective_id.measurement_type",
    )
    def _compute_achievement_percent(self):
        """Compute the achievement of a numeric indicator.

        A numeric indicator gets actual value over target value, as a
        percentage, or zero when the target is zero. A qualitative
        indicator keeps the stored value that the user entered.
        """
        for record in self:
            result = record.achievement_percent
            if record.objective_id.measurement_type == "numeric":
                result = 0.0
                target = record.objective_id.target_value
                if target:
                    result = record.actual_value * 100.0 / target
            record.achievement_percent = result

    @api.constrains("evaluation_id", "objective_id")
    def _check_objective_program(self):
        """Require the objective to belong to the evaluated work program.

        :raises ValidationError: the objective is a line of another
            program.
        """
        for record in self.sudo():
            if not record._check_objective_program_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation objective
Database ID: %s
Problem: The objective does not belong to the evaluated work program
Solution: Select an objective of the work program being evaluated
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_objective_program_condition(self):
        """Tell whether the objective is a line of the evaluated program.

        Extension point of ``_check_objective_program``.

        :return: ``True`` when the objective belongs to the work program
            of the evaluation.
        """
        self.ensure_one()
        program = self.evaluation_id.work_program_id
        return self.objective_id.work_program_id == program

    @api.constrains("evaluation_id", "objective_id")
    def _check_unique_objective(self):
        """Reject two lines for the same objective in one evaluation.

        :raises ValidationError: the objective is already reported.
        """
        for record in self.sudo():
            if not record._check_unique_objective_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation objective
Database ID: %s
Problem: The objective is already reported in this evaluation
Solution: Edit the existing line instead of adding a duplicate
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_unique_objective_condition(self):
        """Tell whether the objective is reported only once.

        Extension point of ``_check_unique_objective``.

        :return: ``True`` when no other line of the same evaluation
            reports the same objective.
        """
        self.ensure_one()
        criteria = [
            ("id", "!=", self.id),
            ("evaluation_id", "=", self.evaluation_id.id),
            ("objective_id", "=", self.objective_id.id),
        ]
        return not self.search_count(criteria)
