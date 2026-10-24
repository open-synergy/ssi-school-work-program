# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. 14.0's HttpCase does not set up
# cls.env in setUpClass (see odoo-development-ui-test skill).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiWorkProgramOccurrence(HttpSavepointCase):
    """Tour tests for the ``work_program_occurrence`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create one program with an occurrence per tour.

        Each tour acts on its own planned occurrence; the occurrence of the
        reset tour is moved to ``done`` first because Reset starts from
        a finished or cancelled occurrence.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        grade_type = cls.env["school_grade_type"].create(
            {"name": "Tour WPO Grade Type", "code": "/"}
        )
        school = cls.env["school"].create(
            {"name": "Tour WPO School", "code": "/", "grade_type_id": grade_type.id}
        )
        year = cls.env["school_academic_year"].create(
            {
                "name": "Tour WPO Year",
                "code": "/",
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        wp_type = cls.env["work_program_type"].create(
            {"name": "Tour WPO Type", "code": "/"}
        )
        category = cls.env["work_program_category"].create(
            {"name": "Tour WPO Category", "code": "/"}
        )
        employee = cls.env["hr.employee"].create({"name": "Tour WPO Employee"})
        program = cls.env["work_program"].create(
            {
                "title": "Tour WPO Program",
                "school_id": school.id,
                "academic_year_id": year.id,
                "type_id": wp_type.id,
                "category_id": category.id,
                "pic_id": employee.id,
                "date_start": "2026-01-01",
                "date_end": "2026-01-28",
                "user_id": admin.id,
            }
        )
        occurrence_model = cls.env["work_program_occurrence"]
        for name in ("Tour Occ Done", "Tour Occ Cancel", "Tour Occ Reset"):
            occurrence_model.create(
                {
                    "work_program_id": program.id,
                    "name": name,
                    "date_start": "2026-01-10",
                }
            )
        occurrence_model.search([("name", "=", "Tour Occ Reset")]).action_done()

    def test_done(self):
        """Run the done tour for ``work_program_occurrence``.

        IK: docs/work_program_occurrence/01-done.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_occurrence_done",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``work_program_occurrence``.

        IK: docs/work_program_occurrence/02-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_occurrence_cancel",
            login="admin",
        )

    def test_reset(self):
        """Run the reset tour for ``work_program_occurrence``.

        IK: docs/work_program_occurrence/03-reset.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_occurrence_reset",
            login="admin",
        )
