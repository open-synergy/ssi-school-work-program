# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class WorkProgramStrategicObjective(models.Model):
    """
    Represents a strategic objective of the school that work programs
    can contribute to. It is a plain reference list: a work program may
    optionally point to one objective to show which long-term goal it
    supports.
    """

    _name = "work_program_strategic_objective"
    _inherit = ["mixin.master_data"]
    _description = "Work Program Strategic Objective"
