# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramEvaluationParticipant(models.Model):
    """
    Detail line of a work program evaluation holding the realization of
    one participant target of the program: how many participants of the
    targeted group actually took part, compared with the planned head
    count. The achievement percentage is computed from the two numbers.
    """

    _name = "work_program_evaluation_participant"
    _description = "Work Program Evaluation Participant"
    _order = "evaluation_id, id"

    evaluation_id = fields.Many2one(
        string="# Evaluation",
        comodel_name="work_program_evaluation",
        required=True,
        ondelete="cascade",
        help="Work program evaluation this participant line belongs to.",
    )
    target_id = fields.Many2one(
        string="Target",
        comodel_name="work_program_target",
        required=True,
        ondelete="restrict",
        help=(
            "Participant target of the evaluated work program that this "
            "line reports on."
        ),
    )
    participant_type = fields.Selection(
        string="Participant Type",
        related="target_id.participant_type",
        readonly=True,
        help="Kind of participants of the target, copied from the plan.",
    )
    grade_id = fields.Many2one(
        string="Grade",
        comodel_name="school_grade",
        related="target_id.grade_id",
        readonly=True,
        help="Grade of the targeted students, copied from the plan.",
    )
    planned_quantity = fields.Integer(
        string="Planned Quantity",
        related="target_id.quantity",
        readonly=True,
        help="Number of participants planned for the target.",
    )
    actual_quantity = fields.Integer(
        string="Actual Quantity",
        default=0,
        help="Number of participants of the target that actually took part.",
    )
    achievement_percent = fields.Float(
        string="Achievement (%)",
        compute="_compute_achievement_percent",
        store=True,
        compute_sudo=True,
        help=(
            "Actual quantity as a percentage of the planned quantity. It is "
            "zero when nothing was planned."
        ),
    )

    @api.depends("actual_quantity", "target_id.quantity")
    def _compute_achievement_percent(self):
        """Compute the actual quantity as a percentage of the plan.

        The result is zero when the planned quantity is zero.
        """
        for record in self:
            result = 0.0
            planned = record.target_id.quantity
            if planned:
                result = record.actual_quantity * 100.0 / planned
            record.achievement_percent = result

    @api.constrains("evaluation_id", "target_id")
    def _check_target_program(self):
        """Require the target to belong to the evaluated work program.

        :raises ValidationError: the target is a line of another program.
        """
        for record in self.sudo():
            if not record._check_target_program_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation participant
Database ID: %s
Problem: The target does not belong to the evaluated work program
Solution: Select a target of the work program being evaluated
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_target_program_condition(self):
        """Tell whether the target is a line of the evaluated program.

        Extension point of ``_check_target_program``.

        :return: ``True`` when the target belongs to the work program of
            the evaluation.
        """
        self.ensure_one()
        program = self.evaluation_id.work_program_id
        return self.target_id.work_program_id == program

    @api.constrains("evaluation_id", "target_id")
    def _check_unique_target(self):
        """Reject two lines for the same target in one evaluation.

        :raises ValidationError: the target is already reported.
        """
        for record in self.sudo():
            if not record._check_unique_target_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation participant
Database ID: %s
Problem: The target is already reported in this evaluation
Solution: Edit the existing line instead of adding a duplicate
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_unique_target_condition(self):
        """Tell whether the target is reported only once.

        Extension point of ``_check_unique_target``.

        :return: ``True`` when no other line of the same evaluation
            reports the same target.
        """
        self.ensure_one()
        criteria = [
            ("id", "!=", self.id),
            ("evaluation_id", "=", self.evaluation_id.id),
            ("target_id", "=", self.target_id.id),
        ]
        return not self.search_count(criteria)

    @api.constrains("actual_quantity")
    def _check_actual_quantity(self):
        """Reject a negative actual quantity.

        :raises ValidationError: ``actual_quantity`` is below zero.
        """
        for record in self.sudo():
            if not record._check_actual_quantity_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation participant quantity
Database ID: %s
Problem: Actual quantity must not be negative
Solution: Enter zero or a positive number of participants
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_actual_quantity_condition(self):
        """Tell whether the actual quantity is not negative.

        Extension point of ``_check_actual_quantity``.

        :return: ``True`` when ``actual_quantity`` is zero or greater.
        """
        self.ensure_one()
        return self.actual_quantity >= 0
