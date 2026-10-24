# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class WorkProgramRole(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a role that an employee can hold in the committee of a
    work program, such as chairperson, secretary, or treasurer. It is
    selected on each committee member line of the work program.
    """

    _name = "work_program_role"
    _inherit = ["mixin.master_data"]
    _description = "Work Program Committee Role"
