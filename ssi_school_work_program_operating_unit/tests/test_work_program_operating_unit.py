# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestWorkProgramOperatingUnit(
    YamlTransactionCase
):  # pylint: disable=too-few-public-methods
    """Cover Operating Unit handling on the work program documents.

    Includes the Operating Unit of a program, its propagation to the
    generated occurrences and to the evaluations, and the record rules
    that restrict visibility per operating unit.
    """

    def test_work_program_operating_unit(self):
        """Run every Operating Unit scenario for the work program models."""
        self.run_yaml_scenario("test_data_work_program_operating_unit.yaml")
