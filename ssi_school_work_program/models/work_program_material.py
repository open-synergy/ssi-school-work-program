# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramMaterial(models.Model):  # pylint: disable=too-few-public-methods
    """
    Detail line of a work program describing one learning or activity
    material that is prepared for the program.
    """

    _name = "work_program_material"
    _description = "Work Program Material"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this material belongs to.",
    )
    name = fields.Char(
        string="Material",
        required=True,
        help="Short name of the material.",
    )
    description = fields.Text(
        string="Description",
        help="Longer description of the material and how it is used.",
    )
