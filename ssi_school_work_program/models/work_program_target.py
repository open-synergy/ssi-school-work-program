# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramTarget(models.Model):
    """
    Detail line of a work program describing one group of intended
    participants, such as the students of one grade, the teachers, the
    staff, or the parents. It only holds the planned head count; the
    actual attendance is not recorded in the work program.
    """

    _name = "work_program_target"
    _description = "Work Program Target"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this participant target belongs to.",
    )
    participant_type = fields.Selection(
        string="Participant Type",
        selection=[
            ("student", "Student"),
            ("teacher", "Teacher"),
            ("staff", "Staff"),
            ("parent", "Parent"),
            ("other", "Other"),
        ],
        required=True,
        default="student",
        help="Kind of participants this line targets.",
    )
    grade_id = fields.Many2one(
        string="Grade",
        comodel_name="school_grade",
        help=(
            "Grade of the targeted students. Required when the participant "
            "type is Student, optional otherwise."
        ),
    )
    description = fields.Char(
        string="Description",
        help="Free text clarifying who exactly is targeted by this line.",
    )
    quantity = fields.Integer(
        string="Quantity",
        required=True,
        default=1,
        help="Planned number of participants for this line. Must be positive.",
    )

    @api.onchange("participant_type")
    def onchange_grade_id(self):
        """Clear the grade when the participant type is not Student."""
        if self.participant_type != "student":
            self.grade_id = False

    @api.constrains("participant_type", "grade_id")
    def _check_grade_required(self):
        """Require a grade on every student target line.

        :raises ValidationError: a Student line has no grade.
        """
        for record in self.sudo():
            if not record._check_grade_required_condition():
                error_message = (
                    _(
                        """
Context: Set work program target
Database ID: %s
Problem: Grade is required when the participant type is Student
Solution: Select the grade of the targeted students
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_grade_required_condition(self):
        """Tell whether a student line carries its grade.

        Extension point of ``_check_grade_required``.

        :return: ``True`` unless the type is Student without a grade.
        """
        self.ensure_one()
        if self.participant_type != "student":
            return True
        return bool(self.grade_id)

    @api.constrains("quantity")
    def _check_quantity(self):
        """Require a positive planned quantity.

        :raises ValidationError: ``quantity`` is zero or negative.
        """
        for record in self.sudo():
            if not record._check_quantity_condition():
                error_message = (
                    _(
                        """
Context: Set work program target quantity
Database ID: %s
Problem: Quantity must be greater than zero
Solution: Enter the planned number of participants
"""
                    )
                    % (record.id,)
                )
                raise ValidationError(error_message)

    def _check_quantity_condition(self):
        """Tell whether the planned quantity is positive.

        Extension point of ``_check_quantity``.

        :return: ``True`` when ``quantity`` is greater than zero.
        """
        self.ensure_one()
        return self.quantity > 0

    @api.constrains("work_program_id", "participant_type", "grade_id")
    def _check_unique_participant(self):
        """Reject two lines with the same type and grade in one program.

        :raises ValidationError: the combination is already used.
        """
        for record in self.sudo():
            if not record._check_unique_participant_condition():
                error_message = (
                    _(
                        """
Context: Set work program target
Database ID: %s
Problem: Participant type '%s' with grade '%s' is already targeted
Solution: Edit the existing line instead of adding a duplicate
"""
                    )
                    % (
                        record.id,
                        record.participant_type,
                        record.grade_id.name or "-",
                    )
                )
                raise ValidationError(error_message)

    def _check_unique_participant_condition(self):
        """Tell whether the type and grade pair is unique in its program.

        Extension point of ``_check_unique_participant``.

        :return: ``True`` when no other line of the same work program has
            the same ``participant_type`` and ``grade_id``.
        """
        self.ensure_one()
        criteria = [
            ("id", "!=", self.id),
            ("work_program_id", "=", self.work_program_id.id),
            ("participant_type", "=", self.participant_type),
            ("grade_id", "=", self.grade_id.id or False),
        ]
        return not self.search_count(criteria)
