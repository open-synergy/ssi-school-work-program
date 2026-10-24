# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramOccurrence(models.Model):
    # Extension of the work program occurrence with the Operating Unit of
    # its program.
    #
    # The occurrence is a detail line whose Operating Unit is fully decided
    # by its parent program, so it is a stored related field instead of a
    # ``mixin.single_operating_unit``. This also covers the occurrences made
    # by ``action_generate_occurrence``: they need no override to be
    # propagated.

    _name = "work_program_occurrence"
    _inherit = "work_program_occurrence"

    operating_unit_id = fields.Many2one(
        string="Operating Unit",
        comodel_name="operating.unit",
        related="work_program_id.operating_unit_id",
        store=True,
        readonly=True,
        help="Operating unit of the work program this occurrence belongs to.",
    )
