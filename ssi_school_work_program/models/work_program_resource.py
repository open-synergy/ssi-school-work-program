# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramResource(models.Model):  # pylint: disable=too-few-public-methods
    """
    Detail line of a work program naming one human resource that takes
    part in the program without being a committee member, for example a
    guest speaker or an external coach.
    """

    _name = "work_program_resource"
    _description = "Work Program Resource"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this resource person belongs to.",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        help="Person or organization providing the resource.",
    )
    role_description = fields.Char(
        string="Role Description",
        help="What this resource person does in the program.",
    )
