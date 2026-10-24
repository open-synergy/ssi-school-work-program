# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestWorkProgramEvaluation(YamlTransactionCase):
    """Scenario tests for the work program evaluation document."""

    def test_work_program_evaluation(self):
        """Run the work program evaluation YAML scenarios."""
        self.run_yaml_scenario("test_data_work_program_evaluation.yaml")

    def test_action_open_evaluation_returns_program_domain(self):
        """Assert the window action returned by ``action_open_evaluation``.

        Pure Python - trigger P1 (L-01: the ``call`` action discards the
        return value, so YAML cannot assert the action dict at all).
        """
        grade_type = self.env["school_grade_type"].create(
            {"name": "Eval Action Grade Type", "code": "/"}
        )
        school = self.env["school"].create(
            {"name": "Eval Action School", "code": "/", "grade_type_id": grade_type.id}
        )
        year = self.env["school_academic_year"].create(
            {
                "name": "Eval Action Year",
                "code": "/",
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        program = self.env["work_program"].create(
            {
                "title": "Eval Action Program",
                "school_id": school.id,
                "academic_year_id": year.id,
                "type_id": self.env["work_program_type"]
                .create({"name": "Eval Action Type", "code": "/"})
                .id,
                "category_id": self.env["work_program_category"]
                .create({"name": "Eval Action Category", "code": "/"})
                .id,
                "pic_id": self.env["hr.employee"]
                .create({"name": "Eval Action PIC"})
                .id,
                "date_start": "2026-01-01",
                "date_end": "2026-01-28",
            }
        )
        action = program.action_open_evaluation()
        self.assertEqual(action["type"], "ir.actions.act_window")
        self.assertEqual(action["res_model"], "work_program_evaluation")
        self.assertEqual(action["domain"], [("work_program_id", "=", program.id)])
        self.assertEqual(action["context"], {"default_work_program_id": program.id})
