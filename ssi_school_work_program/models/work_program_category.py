# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class WorkProgramCategory(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a category used to classify school work programs by theme,
    for example one of the national education standards. A work program
    always belongs to exactly one category, which is used for filtering
    and grouping in the planning reports.
    """

    _name = "work_program_category"
    _inherit = ["mixin.master_data"]
    _description = "Work Program Category"
