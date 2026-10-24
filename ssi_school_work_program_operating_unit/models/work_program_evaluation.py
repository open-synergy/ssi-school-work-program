# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramEvaluation(models.Model):
    # Extension of the work program evaluation with the Operating Unit of
    # its program.
    #
    # The evaluation is a document, but the exception for details whose
    # Operating Unit is decided by the parent applies: an evaluation always
    # belongs to exactly one work program, so it is a stored related field
    # instead of a ``mixin.single_operating_unit``.

    _name = "work_program_evaluation"
    _inherit = "work_program_evaluation"

    operating_unit_id = fields.Many2one(
        string="Operating Unit",
        comodel_name="operating.unit",
        related="work_program_id.operating_unit_id",
        store=True,
        readonly=True,
        help="Operating unit of the work program this evaluation belongs to.",
    )
