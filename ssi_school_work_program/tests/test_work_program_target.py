# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestWorkProgramTarget(YamlTransactionCase):
    """YAML scenario tests for the work program target lines."""

    def test_work_program_target(self):
        """Run the work program target YAML scenarios."""
        self.run_yaml_scenario("test_data_work_program_target.yaml")
