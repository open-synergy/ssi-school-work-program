# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Migration: 14.0.1.1.1 -> 14.0.1.1.2
#
# Changes: ``work_program`` no longer inherits ``mixin.status_check``.
#          This script deletes the ``status_check`` rows that belong to
#          ``work_program`` and drops the ``status_check_template_id``
#          column from the ``work_program`` table. ``status_check_template``
#          records are left untouched.

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    """Remove the status check data left behind on work programs.

    :param env: the migration environment
    :param version: the version being migrated to (unused)
    :return: nothing; deletes ``status_check`` rows and drops a column
    """
    if openupgrade.table_exists(env.cr, "status_check"):
        rows = openupgrade.logged_query(
            env.cr,
            """
            DELETE FROM status_check
            WHERE model = %s
            """,
            ("work_program",),
        )
        _logger.info("Deleted %s status_check row(s) of work_program.", rows)
    if openupgrade.column_exists(env.cr, "work_program", "status_check_template_id"):
        openupgrade.logged_query(
            env.cr,
            """
            ALTER TABLE work_program
            DROP COLUMN status_check_template_id
            """,
        )
