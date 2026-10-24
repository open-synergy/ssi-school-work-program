# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgram(models.Model):
    # Extension of the work program with a single Operating Unit.
    #
    # The work program is the root document of the Operating Unit scope:
    # its Operating Unit is chosen here, not derived from anything else.
    # The occurrences and the evaluations of the program follow it through
    # a stored related field (see the sibling models of this module).
    #
    # The analytic account created by ``action_create_analytic_account``
    # is deliberately NOT given an Operating Unit: ``account.analytic.account``
    # has no Operating Unit field in the allowed stack (only the OCA module
    # ``analytic_operating_unit`` adds one, and OCA Operating Unit modules
    # other than ``operating_unit`` must not be depended on).

    _name = "work_program"
    _inherit = [
        "work_program",
        "mixin.single_operating_unit",
    ]

    operating_unit_id = fields.Many2one(
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
