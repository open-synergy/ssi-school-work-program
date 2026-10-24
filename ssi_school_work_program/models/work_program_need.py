# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramNeed(models.Model):  # pylint: disable=too-few-public-methods
    """
    Detail line of a work program listing one thing the program needs,
    such as equipment, a venue, or supplies, optionally tied to the
    occurrence date on which it is needed.
    """

    _name = "work_program_need"
    _description = "Work Program Need"
    _order = "work_program_id, id"

    work_program_id = fields.Many2one(
        string="# Work Program",
        comodel_name="work_program",
        required=True,
        ondelete="cascade",
        help="Work program this need belongs to.",
    )
    name = fields.Char(
        string="Need",
        required=True,
        help="Short name of the equipment, venue or supply that is needed.",
    )
    quantity = fields.Float(
        string="Quantity",
        default=1.0,
        help="Planned quantity of the need.",
    )
    occurrence_id = fields.Many2one(
        string="Occurrence",
        comodel_name="work_program_occurrence",
        help=(
            "Occurrence of the same work program on which this need is "
            "used. Leave empty if it applies to the whole program."
        ),
    )
