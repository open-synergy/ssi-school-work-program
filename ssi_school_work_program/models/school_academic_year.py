# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


# Extends ``school_academic_year`` with the work program planning
# deadline. The deadline only marks whether a work program was planned in
# the regular cycle or as an additional one; it is not a parent document.
class SchoolAcademicYear(models.Model):
    _name = "school_academic_year"
    _inherit = ["school_academic_year"]

    work_program_planning_deadline = fields.Date(
        string="Work Program Planning Deadline",
        help=(
            "Last date on which work programs of this academic year are "
            "still planned in the regular cycle. Work programs created "
            "after this date are flagged as additional. Leave empty if the "
            "regular cycle has no deadline."
        ),
    )
