# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramCommittee(models.Model):  # pylint: disable=too-few-public-methods
    """
    Detail line of a work program naming one committee member and the
    role this employee holds in the program.
    """

    _name = "work_program_committee"
    _description = "Work Program Committee"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this committee member belongs to.",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
        help="Employee who is a member of the committee.",
    )
    role_id = fields.Many2one(
        string="Role",
        comodel_name="work_program_role",
        required=True,
        help="Role of the employee in the committee.",
    )
