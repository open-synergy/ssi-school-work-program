# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestWorkProgramOccurrence(YamlTransactionCase):
    """YAML scenario tests for occurrence generation and states."""

    def test_work_program_occurrence(self):
        """Run the occurrence generation and states YAML scenarios."""
        self.run_yaml_scenario("test_data_work_program_occurrence.yaml")
