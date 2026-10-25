# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WorkProgramOccurrencePreparation(models.Model):
    """
    Detail line of an occurrence of a work program holding one task of
    its preparation checklist: who is in charge, when it is due, when it
    was actually finished, and the files proving it. A line is either
    loaded from the preparation template of the work program type or
    added by hand.
    """

    _name = "work_program_occurrence_preparation"
    _description = "Work Program Occurrence Preparation"
    _order = "occurrence_id, sequence, id"

    occurrence_id = fields.Many2one(
        string="Occurrence",
        comodel_name="work_program_occurrence",
        required=True,
        ondelete="cascade",
        help="Occurrence of the work program this task belongs to.",
    )
    template_id = fields.Many2one(
        string="Template",
        comodel_name="work_program_type_preparation",
        ondelete="set null",
        copy=False,
        help=(
            "Preparation task of the work program type this line was "
            "loaded from. Empty for a line added by hand."
        ),
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
    pic_id = fields.Many2one(
        string="Person in Charge",
        comodel_name="hr.employee",
        help="Employee responsible for this task.",
    )
    date_deadline = fields.Date(
        string="Deadline",
        help="Day on which the task has to be finished.",
    )
    date_done = fields.Date(
        string="Date Done",
        help="Day on which the task was actually finished.",
    )
    is_done = fields.Boolean(
        string="Done",
        compute="_compute_is_done",
        store=True,
        compute_sudo=True,
        help="Checked once the actual finish date is filled in.",
    )
    attachment_ids = fields.Many2many(
        string="Evidence",
        comodel_name="ir.attachment",
        relation="work_program_occurrence_preparation_attachment_rel",
        column1="preparation_id",
        column2="attachment_id",
        help="Files proving that the task has been carried out.",
    )
    note = fields.Text(
        string="Note",
        help="Free remark about the task.",
    )

    @api.depends("date_done")
    def _compute_is_done(self):
        """Mark the line as done when its finish date is filled in."""
        for record in self:
            result = bool(record.date_done)
            record.is_done = result

    @api.constrains(
        "occurrence_id",
        "name",
        "pic_id",
        "date_deadline",
        "date_done",
        "attachment_ids",
        "note",
    )
    def _check_occurrence_planned(self):
        """Reject a checklist line change on a finished occurrence.

        :raises ValidationError: the occurrence is not ``planned``.
        """
        for record in self.sudo():
            if not record._check_occurrence_planned_condition():
                error_message = (
                    _(
                        """
Context: Change work program occurrence preparation
Database ID: %s
Problem: The occurrence is '%s', so its preparation can no longer change
Solution: Reset the occurrence to planned before changing its preparation
"""
                    )
                    % (record.id, record.occurrence_id.state)
                )
                raise ValidationError(error_message)

    def _check_occurrence_planned_condition(self):
        """Tell whether the occurrence still accepts checklist changes.

        Extension point of ``_check_occurrence_planned``.

        :return: ``True`` when the occurrence is ``planned``.
        """
        self.ensure_one()
        return self.occurrence_id.state == "planned"
