# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class WorkProgramType(models.Model):  # pylint: disable=too-few-public-methods
    """
    Represents a type of school work program, for example an event, an
    extracurricular, achievement coaching, HR development, or an
    investment. Besides classifying programs, a type decides which of the
    eight planning sections are mandatory (the ``require_*`` flags) and
    which analytic account group the analytic account of its programs is
    placed in.
    """

    _name = "work_program_type"
    _inherit = ["mixin.master_data"]
    _description = "Work Program Type"

    analytic_group_id = fields.Many2one(
        string="Analytic Group",
        comodel_name="account.analytic.group",
        help=(
            "Analytic account group assigned to the analytic account that "
            "is created for the work programs of this type. Leave empty "
            "to create the analytic account without a group."
        ),
    )
    require_occurrence = fields.Boolean(
        string="Require Occurrence",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its occurrence dates section is filled in."
        ),
    )
    require_target = fields.Boolean(
        string="Require Target",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its participant targets section is filled in."
        ),
    )
    require_objective = fields.Boolean(
        string="Require Objective",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its objectives and indicators section is filled in."
        ),
    )
    require_committee = fields.Boolean(
        string="Require Committee",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its committee members section is filled in."
        ),
    )
    require_material = fields.Boolean(
        string="Require Material",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its materials section is filled in."
        ),
    )
    require_resource = fields.Boolean(
        string="Require Resource",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its non-committee resource persons section is filled in."
        ),
    )
    require_need = fields.Boolean(
        string="Require Need",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its needs section is filled in."
        ),
    )
    require_rundown = fields.Boolean(
        string="Require Rundown",
        default=True,
        help=(
            "If checked, a work program of this type is only considered "
            "complete when its rundown (schedule of activities) section is filled in."
        ),
    )
    require_final_evaluation = fields.Boolean(
        string="Require Final Evaluation",
        default=False,
        help=(
            "If checked, a work program of this type can only be finished "
            "after one of its final evaluations has been approved and is "
            "done."
        ),
    )
