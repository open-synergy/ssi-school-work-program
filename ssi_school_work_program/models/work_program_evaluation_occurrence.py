# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramEvaluationOccurrence(models.Model):
    """
    Detail line of a work program evaluation holding what happened on one
    planned occurrence date of the program: the number of participants
    who attended, the actual date when it differs from the plan, a note
    and the evidence attached.
    """

    _name = "work_program_evaluation_occurrence"
    _description = "Work Program Evaluation Occurrence"
    _order = "evaluation_id, id"

    evaluation_id = fields.Many2one(
        string="# Evaluation",
        comodel_name="work_program_evaluation",
        required=True,
        ondelete="cascade",
        help="Work program evaluation this occurrence line belongs to.",
    )
    occurrence_id = fields.Many2one(
        string="Occurrence",
        comodel_name="work_program_occurrence",
        required=True,
        ondelete="restrict",
        help=("Occurrence of the evaluated work program that this line " "reports on."),
    )
    date_start = fields.Date(
        string="Planned Date",
        related="occurrence_id.date_start",
        readonly=True,
        help="First day of the occurrence as planned.",
    )
    actual_participant = fields.Integer(
        string="Actual Participant",
        default=0,
        help="Number of participants who attended the occurrence.",
    )
    date_actual = fields.Date(
        string="Actual Date",
        help=(
            "Day the occurrence really took place. Leave empty when it "
            "took place on the planned date."
        ),
    )
    note = fields.Text(
        string="Note",
        help="Remarks about how this occurrence went.",
    )
    attachment_ids = fields.Many2many(
        string="Evidence",
        comodel_name="ir.attachment",
        relation="work_program_evaluation_occurrence_attachment_rel",
        column1="occurrence_line_id",
        column2="attachment_id",
        help="Files that prove the occurrence took place.",
    )

    @api.constrains("evaluation_id", "occurrence_id")
    def _check_occurrence_program(self):
        """Require the occurrence to belong to the evaluated program.

        :raises ValidationError: the occurrence is a line of another
            program.
        """
        for record in self.sudo():
            if not record._check_occurrence_program_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation occurrence
Database ID: %s
Problem: The occurrence does not belong to the evaluated work program
Solution: Select an occurrence of the work program being evaluated
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_occurrence_program_condition(self):
        """Tell whether the occurrence is a line of the evaluated program.

        Extension point of ``_check_occurrence_program``.

        :return: ``True`` when the occurrence belongs to the work
            program of the evaluation.
        """
        self.ensure_one()
        program = self.evaluation_id.work_program_id
        return self.occurrence_id.work_program_id == program

    @api.constrains("evaluation_id", "occurrence_id")
    def _check_unique_occurrence(self):
        """Reject two lines for the same occurrence in one evaluation.

        :raises ValidationError: the occurrence is already reported.
        """
        for record in self.sudo():
            if not record._check_unique_occurrence_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation occurrence
Database ID: %s
Problem: The occurrence is already reported in this evaluation
Solution: Edit the existing line instead of adding a duplicate
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_unique_occurrence_condition(self):
        """Tell whether the occurrence is reported only once.

        Extension point of ``_check_unique_occurrence``.

        :return: ``True`` when no other line of the same evaluation
            reports the same occurrence.
        """
        self.ensure_one()
        criteria = [
            ("id", "!=", self.id),
            ("evaluation_id", "=", self.evaluation_id.id),
            ("occurrence_id", "=", self.occurrence_id.id),
        ]
        return not self.search_count(criteria)

    @api.constrains("actual_participant")
    def _check_actual_participant(self):
        """Reject a negative number of participants.

        :raises ValidationError: ``actual_participant`` is below zero.
        """
        for record in self.sudo():
            if not record._check_actual_participant_condition():
                error_message = (
                    _(
                        """
Context: Set work program evaluation occurrence participants
Database ID: %s
Problem: Actual participant must not be negative
Solution: Enter zero or a positive number of participants
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_actual_participant_condition(self):
        """Tell whether the number of participants is not negative.

        Extension point of ``_check_actual_participant``.

        :return: ``True`` when ``actual_participant`` is zero or greater.
        """
        self.ensure_one()
        return self.actual_participant >= 0
