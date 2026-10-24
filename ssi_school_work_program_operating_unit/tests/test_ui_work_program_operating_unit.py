# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. In 14.0 plain HttpCase does not set
# up ``cls.env`` in ``setUpClass``, so any fixture would fail before the
# browser even starts.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiWorkProgramOperatingUnit(HttpSavepointCase):
    """Tour test for the Operating Unit delta of the work program."""

    @classmethod
    def setUpClass(cls):
        """Create the master data and the Operating Unit the tour picks.

        The tour builds its program through the UI, so only the records it
        picks from exist. The Operating Unit is assigned to the admin user
        explicitly: the Operating Unit record rule hides every unit that
        is not assigned to the user running the browser session.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        partner = cls.env["res.partner"].create({"name": "Tour WPOU Unit B Partner"})
        unit = cls.env["operating.unit"].create(
            {
                "name": "Tour WPOU Unit B",
                "code": "TWPOUB",
                "company_id": admin.company_id.id,
                "partner_id": partner.id,
            }
        )
        admin.write({"assigned_operating_unit_ids": [(4, unit.id)]})
        grade_type = cls.env["school_grade_type"].create(
            {"name": "Tour WPOU Grade Type", "code": "/"}
        )
        cls.env["school"].create(
            {
                "name": "Tour WPOU School",
                "code": "/",
                "grade_type_id": grade_type.id,
            }
        )
        cls.env["school_academic_year"].create(
            {
                "name": "Tour WPOU Year",
                "code": "/",
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        cls.env["work_program_type"].create({"name": "Tour WPOU Type", "code": "/"})
        cls.env["work_program_category"].create(
            {"name": "Tour WPOU Category", "code": "/"}
        )
        cls.env["hr.employee"].create({"name": "Tour WPOU Employee"})

    def test_create(self):
        """Run the extension create tour for ``work_program``.

        IK: docs/work_program/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_operating_unit_work_program_create",
            login="admin",
        )
