# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. 14.0's HttpCase does not set up
# cls.env in setUpClass (see odoo-development-ui-test skill).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiWorkProgramStrategicObjective(HttpSavepointCase):
    """Tour tests for the strategic objective work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the records the edit and delete tours act on.

        The create tour builds its record through the UI, so only the
        records of ``02-edit`` and ``03-delete`` exist beforehand.
        """
        super().setUpClass()
        model = cls.env["work_program_strategic_objective"]
        cls.record_edit = model.create(
            {"name": "Tour Strategic Objective Edit", "code": "/"}
        )
        cls.record_delete = model.create(
            {"name": "Tour Strategic Objective Delete", "code": "/"}
        )

    def test_create(self):
        """Run the create tour for ``work_program_strategic_objective``.

        IK: docs/work_program_strategic_objective/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_strategic_objective_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``work_program_strategic_objective``.

        IK: docs/work_program_strategic_objective/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_strategic_objective_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``work_program_strategic_objective``.

        IK: docs/work_program_strategic_objective/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_strategic_objective_delete",
            login="admin",
        )
