# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "School Work Program + Operating Unit",
    "version": "14.0.1.0.1",
    "website": "https://simetri-sinergi.id",
    # pylint: disable=line-too-long
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia, Odoo Community Association (OCA)",  # noqa: B950
    # pylint: enable=line-too-long
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_school_work_program",
        "ssi_school_operating_unit",
        "ssi_operating_unit_mixin",
        "web_tour",
    ],
    "data": [
        "security/res_groups/work_program.xml",
        "security/res_groups/work_program_evaluation.xml",
        "security/ir_rule/work_program.xml",
        "security/ir_rule/work_program_evaluation.xml",
        "views/work_program.xml",
        "views/work_program_occurrence.xml",
        "views/work_program_evaluation.xml",
        "views/assets.xml",
    ],
}
