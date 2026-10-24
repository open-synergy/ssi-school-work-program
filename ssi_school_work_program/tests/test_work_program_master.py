# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestWorkProgramMaster(YamlTransactionCase):
    """YAML scenario tests for the work program master data models."""

    def test_work_program_master(self):
        """Run the work program master data CRUD YAML scenarios."""
        self.run_yaml_scenario("test_data_work_program_master.yaml")
