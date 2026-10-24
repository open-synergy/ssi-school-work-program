# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. 14.0's HttpCase does not set up
# cls.env in setUpClass (see odoo-development-ui-test skill).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiWorkProgram(HttpSavepointCase):
    """Tour tests for the ``work_program`` work instructions."""

    @classmethod
    def _create_program(cls, title, **extra):
        """Create a draft work program owned by the admin user.

        ``user_id`` is explicit: ``cls.env`` runs as SUPERUSER and the
        internal user record rule would otherwise hide the fixture from the
        admin browser session of the tour.

        :param title: title of the work program.
        :param extra: additional field values.
        :return: the created ``work_program`` record.
        """
        values = {
            "title": title,
            "school_id": cls.school.id,
            "academic_year_id": cls.year.id,
            "type_id": cls.wp_type.id,
            "category_id": cls.category.id,
            "pic_id": cls.employee.id,
            "date_start": "2026-01-01",
            "date_end": "2026-01-28",
            "user_id": cls.admin.id,
        }
        values.update(extra)
        return cls.env["work_program"].create(values)

    @classmethod
    def _confirm_program(cls, program):
        """Move a draft program to ``confirm`` through its action.

        :param program: draft ``work_program`` record.
        """
        program.action_confirm()
        program.invalidate_cache()

    @classmethod
    def setUpClass(cls):
        """Create the master data and the programs the tours act on.

        The create tour builds its program through the UI, so only the
        master data it picks from exists for it. Every other tour gets a
        program already in the state its Pre-Condition requires, reached
        through the action methods rather than by writing ``state``.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        grade_type = cls.env["school_grade_type"].create(
            {"name": "Tour WP Grade Type", "code": "/"}
        )
        cls.school = cls.env["school"].create(
            {"name": "Tour WP School", "code": "/", "grade_type_id": grade_type.id}
        )
        cls.year = cls.env["school_academic_year"].create(
            {
                "name": "Tour WP Year",
                "code": "/",
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        cls.wp_type = cls.env["work_program_type"].create(
            {"name": "Tour WP Type", "code": "/"}
        )
        cls.category = cls.env["work_program_category"].create(
            {"name": "Tour WP Category", "code": "/"}
        )
        cls.employee = cls.env["hr.employee"].create({"name": "Tour WP Employee"})
        cls.reason = cls.env["base.cancel_reason"].create(
            {"name": "Tour WP Reason", "code": "TOURWPR", "global_use": True}
        )
        monday = cls.env["frequency"].create(
            {
                "name": "Tour WP Monday",
                "code": "/",
                "interval": 1,
                "interval_type": "weekly",
                "use_byweekday": True,
                "mo": True,
            }
        )
        cls.frequency_set = cls.env["frequency_set"].create(
            {
                "name": "Tour WP Mondays",
                "code": "/",
                "fsm_frequency_ids": [(6, 0, monday.ids)],
            }
        )

        # 02-edit, 03-delete, 04-confirm, 09-cancel, 12-create-analytic-account
        # start from a plain draft program.
        cls._create_program("Tour WP Edit")
        cls._create_program("Tour WP Delete")
        cls._create_program("Tour WP Confirm")
        cls._create_program("Tour WP Cancel")
        cls._create_program("Tour WP Analytic")
        cls._create_program("Tour WP Generate", frequency_set_id=cls.frequency_set.id)

        # 05-approve: program waiting for approval.
        cls._confirm_program(cls._create_program("Tour WP Approve"))

        # 06-reject: program waiting for approval, rejected by the approver.
        cls._confirm_program(cls._create_program("Tour WP Reject"))

        # 07-restart-approval: program stuck in confirm without an approval
        # template. The button is only visible in that situation.
        stuck = cls._create_program("Tour WP Stuck")
        cls._confirm_program(stuck)
        stuck.sudo().write({"approval_template_id": False})
        stuck.invalidate_cache()

        # 08-done: program already approved, therefore on progress.
        done = cls._create_program("Tour WP Done")
        cls._confirm_program(done)
        done.with_user(cls.admin).action_approve_approval()
        done.invalidate_cache()

        # 10-restart: cancelled program.
        restart = cls._create_program("Tour WP Restart")
        restart.action_cancel()
        restart.invalidate_cache()

        # 13-open-evaluation: program that already has one evaluation.
        evaluated = cls._create_program("Tour WP Evaluated")
        cls.env["work_program_evaluation"].create(
            {
                "work_program_id": evaluated.id,
                "evaluation_type": "mid",
                "date": "2026-02-01",
                "user_id": cls.admin.id,
            }
        )

        # Approve tour fixture approves in the tour itself.

    def test_create(self):
        """Run the create tour for ``work_program``.

        IK: docs/work_program/01-create.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``work_program``.

        IK: docs/work_program/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``work_program``.

        IK: docs/work_program/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_delete", login="admin"
        )

    def test_confirm(self):
        """Run the confirm tour for ``work_program``.

        IK: docs/work_program/04-confirm.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_confirm", login="admin"
        )

    def test_approve(self):
        """Run the approve tour for ``work_program``.

        IK: docs/work_program/05-approve.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_approve", login="admin"
        )

    def test_reject(self):
        """Run the reject tour for ``work_program``.

        IK: docs/work_program/06-reject.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_reject", login="admin"
        )

    def test_restart_approval(self):
        """Run the restart approval tour for ``work_program``.

        IK: docs/work_program/07-restart-approval.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_restart_approval",
            login="admin",
        )

    def test_done(self):
        """Run the finish tour for ``work_program``.

        IK: docs/work_program/08-done.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_done", login="admin"
        )

    def test_cancel(self):
        """Run the cancel tour for ``work_program``.

        IK: docs/work_program/09-cancel.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_cancel", login="admin"
        )

    def test_restart(self):
        """Run the restart tour for ``work_program``.

        IK: docs/work_program/10-restart.md
        """
        self.start_tour(
            "/web", "ssi_school_work_program_work_program_restart", login="admin"
        )

    def test_generate_occurrence(self):
        """Run the generate occurrence tour for ``work_program``.

        IK: docs/work_program/11-generate-occurrence.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_generate_occurrence",
            login="admin",
        )

    def test_create_analytic_account(self):
        """Run the create analytic account tour for ``work_program``.

        IK: docs/work_program/12-create-analytic-account.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_create_analytic_account",
            login="admin",
        )

    def test_open_evaluation(self):
        """Run the open evaluation tour for ``work_program``.

        IK: docs/work_program/13-open-evaluation.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_open_evaluation",
            login="admin",
        )
