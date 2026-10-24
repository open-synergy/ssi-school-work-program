# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase -- NOT HttpCase. 14.0's HttpCase does not set up
# cls.env in setUpClass (see odoo-development-ui-test skill).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiWorkProgramEvaluation(HttpSavepointCase):
    """Tour tests for the ``work_program_evaluation`` work instructions."""

    @classmethod
    def _create_evaluation(cls, date, **extra):
        """Create a draft mid-term evaluation owned by the admin user.

        ``user_id`` is explicit: ``cls.env`` runs as SUPERUSER and the
        internal user record rule would otherwise hide the fixture from the
        admin browser session of the tour. The date is unique for each
        fixture, because the list row of a tour is found by its date.

        :param date: evaluation date, ``YYYY-MM-DD``.
        :param extra: additional field values.
        :return: the created ``work_program_evaluation`` record.
        """
        values = {
            "work_program_id": cls.program.id,
            "evaluation_type": "mid",
            "date": date,
            "user_id": cls.admin.id,
        }
        values.update(extra)
        return cls.env["work_program_evaluation"].create(values)

    @classmethod
    def _confirm_evaluation(cls, evaluation):
        """Move a draft evaluation to ``confirm`` through its action.

        :param evaluation: draft ``work_program_evaluation`` record.
        """
        evaluation.action_confirm()
        evaluation.invalidate_cache()

    @classmethod
    def setUpClass(cls):
        """Create the work program and the evaluations the tours act on.

        The program is brought to ``on progress`` through its action
        methods and owns one target, one objective and one occurrence, so
        that ``04-load-lines`` has something to load. Every other tour gets
        an evaluation already in the state its Pre-Condition requires.
        The create tour builds its evaluation through the UI.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        grade_type = cls.env["school_grade_type"].create(
            {"name": "Tour WPE Grade Type", "code": "/"}
        )
        grade = cls.env["school_grade"].create(
            {
                "name": "Tour WPE Grade",
                "code": "/",
                "sequence": 10,
                "type_id": grade_type.id,
            }
        )
        school = cls.env["school"].create(
            {"name": "Tour WPE School", "code": "/", "grade_type_id": grade_type.id}
        )
        year = cls.env["school_academic_year"].create(
            {
                "name": "Tour WPE Year",
                "code": "/",
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        wp_type = cls.env["work_program_type"].create(
            {"name": "Tour WPE Type", "code": "/"}
        )
        category = cls.env["work_program_category"].create(
            {"name": "Tour WPE Category", "code": "/"}
        )
        employee = cls.env["hr.employee"].create({"name": "Tour WPE Employee"})
        cls.reason = cls.env["base.cancel_reason"].create(
            {"name": "Tour WPE Reason", "code": "TOURWPER", "global_use": True}
        )
        cls.program = cls.env["work_program"].create(
            {
                "title": "Tour WPE Program",
                "school_id": school.id,
                "academic_year_id": year.id,
                "type_id": wp_type.id,
                "category_id": category.id,
                "pic_id": employee.id,
                "date_start": "2026-01-01",
                "date_end": "2026-01-28",
                "user_id": cls.admin.id,
            }
        )
        cls.env["work_program_target"].create(
            {
                "work_program_id": cls.program.id,
                "participant_type": "student",
                "grade_id": grade.id,
                "quantity": 40,
            }
        )
        cls.env["work_program_objective"].create(
            {
                "work_program_id": cls.program.id,
                "name": "Tour WPE Objective",
                "indicator": "Tour WPE Indicator",
                "measurement_type": "numeric",
                "target_value": 4,
            }
        )
        cls.env["work_program_occurrence"].create(
            {
                "work_program_id": cls.program.id,
                "name": "Tour WPE Day",
                "date_start": "2026-01-05",
            }
        )
        cls.program.action_confirm()
        cls.program.invalidate_cache()
        cls.program.with_user(cls.admin).action_approve_approval()
        cls.program.invalidate_cache()

        # 02-edit, 03-delete, 04-load-lines, 05-confirm, 09-cancel start from
        # a plain draft evaluation without lines.
        cls._create_evaluation("2026-02-02")
        cls._create_evaluation("2026-02-03")
        cls._create_evaluation("2026-02-04")
        cls._create_evaluation("2026-02-05")
        cls._create_evaluation("2026-02-09")

        # 06-approve: evaluation waiting for approval.
        cls._confirm_evaluation(cls._create_evaluation("2026-02-06"))

        # 07-reject: evaluation waiting for approval, rejected in the tour.
        cls._confirm_evaluation(cls._create_evaluation("2026-02-07"))

        # 08-restart-approval: evaluation stuck in confirm without an
        # approval template. The button is only visible in that situation.
        stuck = cls._create_evaluation("2026-02-08")
        cls._confirm_evaluation(stuck)
        stuck.sudo().write({"approval_template_id": False})
        stuck.invalidate_cache()

        # 10-restart: cancelled evaluation.
        restart = cls._create_evaluation("2026-02-10")
        restart.action_cancel()
        restart.invalidate_cache()

    def test_create(self):
        """Run the create tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_delete",
            login="admin",
        )

    def test_load_lines(self):
        """Run the load lines tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/04-load-lines.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_load_lines",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/05-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/06-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_approve",
            login="admin",
        )

    def test_reject(self):
        """Run the reject tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/07-reject.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_reject",
            login="admin",
        )

    def test_restart_approval(self):
        """Run the restart approval tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/08-restart-approval.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_restart_approval",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/09-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_cancel",
            login="admin",
        )

    def test_restart(self):
        """Run the restart tour for ``work_program_evaluation``.

        IK: docs/work_program_evaluation/10-restart.md
        """
        self.start_tour(
            "/web",
            "ssi_school_work_program_work_program_evaluation_restart",
            login="admin",
        )
