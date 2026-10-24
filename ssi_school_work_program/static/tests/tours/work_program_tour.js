/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_school_work_program.work_program_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/work_program/01-create.md
    tour.register(
        "ssi_school_work_program_work_program_create",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Title",
                trigger: ".o_field_widget[name='title']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Create",
            },
            {
                content: "Select the School",
                trigger: ".o_field_many2one[name='school_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP School",
            },
            {
                content: "Pick Tour WP School from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP School)",
                in_modal: false,
            },
            {
                content: "Select the Academic Year",
                trigger: ".o_field_many2one[name='academic_year_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Year",
            },
            {
                content: "Pick Tour WP Year from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Year)",
                in_modal: false,
            },
            {
                content: "Select the Type",
                trigger: ".o_field_many2one[name='type_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Type",
            },
            {
                content: "Pick Tour WP Type from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Type)",
                in_modal: false,
            },
            {
                content: "Select the Category",
                trigger: ".o_field_many2one[name='category_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Category",
            },
            {
                content: "Pick Tour WP Category from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Category)",
                in_modal: false,
            },
            {
                content: "Select the Person in Charge",
                trigger: ".o_field_many2one[name='pic_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Employee",
            },
            {
                content: "Pick Tour WP Employee from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Employee)",
                in_modal: false,
            },
            {
                content: "Fill in Date Start",
                trigger: ".o_field_widget[name='date_start'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 01/05/2026",
            },
            {
                content: "Fill in Date End",
                trigger: ".o_field_widget[name='date_end'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 01/30/2026",
            },
            {
                content: "Open the Participant Targets tab",
                trigger: ".o_notebook .nav-link:contains(Participant Targets)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Participant Targets",
                trigger:
                    ".o_field_widget[name='target_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Grade is required for a Student line",
                trigger: ".o_field_many2one[name='grade_id'].o_required_modifier",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Grade",
                trigger: ".o_field_many2one[name='grade_id'] input",
                run: "text Tour WP Grade",
            },
            {
                content: "Pick Tour WP Grade from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Grade)",
                in_modal: false,
            },
            {
                content: "Fill in Quantity",
                trigger: ".o_field_widget[name='quantity']",
                run: "text 30",
            },
            {
                content: "Save & Close the Participant Target line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Participant Target line is listed",
                trigger: ".o_field_widget[name='target_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Objectives tab",
                trigger: ".o_notebook .nav-link:contains(Objectives)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Objectives",
                trigger:
                    ".o_field_widget[name='objective_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Objective dialog is open",
                trigger: ".o_field_widget[name='indicator']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Objective",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour WP Objective",
            },
            {
                content: "Fill in Indicator",
                trigger: ".o_field_widget[name='indicator']",
                run: "text Tour WP Indicator",
            },
            {
                content: "Save & Close the Objective line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Objective line is listed",
                trigger: ".o_field_widget[name='objective_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Committee tab",
                trigger: ".o_notebook .nav-link:contains(Committee)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Committee",
                trigger:
                    ".o_field_widget[name='committee_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Committee dialog is open",
                trigger: ".o_field_many2one[name='role_id']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Employee",
                trigger: ".o_field_many2one[name='employee_id'] input",
                run: "text Tour WP Employee",
            },
            {
                content: "Pick Tour WP Employee from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Employee)",
                in_modal: false,
            },
            {
                content: "Select the Role",
                trigger: ".o_field_many2one[name='role_id'] input",
                run: "text Tour WP Role",
            },
            {
                content: "Pick Tour WP Role from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Role)",
                in_modal: false,
            },
            {
                content: "Save & Close the Committee line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Committee line is listed",
                trigger: ".o_field_widget[name='committee_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Materials tab",
                trigger: ".o_notebook .nav-link:contains(Materials)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Materials",
                trigger:
                    ".o_field_widget[name='material_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Material dialog is open",
                trigger: ".o_field_widget[name='description']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Material",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour WP Material",
            },
            {
                content: "Save & Close the Material line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Material line is listed",
                trigger: ".o_field_widget[name='material_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Resource Persons tab",
                trigger: ".o_notebook .nav-link:contains(Resource Persons)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Resource Persons",
                trigger:
                    ".o_field_widget[name='resource_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Resource person dialog is open",
                trigger: ".o_field_widget[name='role_description']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Partner",
                trigger: ".o_field_many2one[name='partner_id'] input",
                run: "text Tour WP Resource",
            },
            {
                content: "Pick Tour WP Resource from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WP Resource)",
                in_modal: false,
            },
            {
                content: "Save & Close the Resource Person line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Resource Person line is listed",
                trigger: ".o_field_widget[name='resource_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Needs tab",
                trigger: ".o_notebook .nav-link:contains(Needs)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Needs",
                trigger:
                    ".o_field_widget[name='need_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Need dialog is open",
                trigger: ".o_field_many2one[name='occurrence_id']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Need",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour WP Need",
            },
            {
                content: "Save & Close the Need line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Need line is listed",
                trigger: ".o_field_widget[name='need_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Occurrences tab",
                trigger: ".o_notebook .nav-link:contains(Occurrences)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Occurrences",
                trigger:
                    ".o_field_widget[name='occurrence_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Occurrence dialog is open",
                trigger: ".o_field_widget[name='location']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour WP Occurrence",
            },
            {
                content: "Fill in the occurrence Date Start",
                trigger: ".o_field_widget[name='date_start'] input",
                run: "text 01/10/2026",
            },
            {
                content: "Save & Close the Occurrence line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Occurrence line is listed",
                trigger: ".o_field_widget[name='occurrence_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Status is Draft",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/02-edit.md
    tour.register(
        "ssi_school_work_program_work_program_edit",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to edit",
                trigger: ".o_data_row:contains(Tour WP Edit) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click Edit",
                trigger: ".o_form_button_edit",
                extra_trigger: ".o_form_view.o_form_readonly",
            },
            {
                content: "Change the Title",
                trigger: ".o_field_widget[name='title']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WP Edited",
            },
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Title shows the new value",
                trigger:
                    ".o_form_view.o_form_readonly .o_field_widget[name='title']:contains(Tour WP Edited)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/03-delete.md
    tour.register(
        "ssi_school_work_program_work_program_delete",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to delete",
                trigger: ".o_data_row:contains(Tour WP Delete) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Click Delete",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $delete[0].click();
                },
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Click the list breadcrumb to return to the list",
                trigger: ".breadcrumb-item.o_back_button a:contains(Work Programs)",
            },
            {
                content: "Tour WP Delete no longer appears in the list",
                trigger: ".o_list_view:not(:has(.o_data_row:contains(Tour WP Delete)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/04-confirm.md
    tour.register(
        "ssi_school_work_program_work_program_confirm",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to confirm",
                trigger: ".o_data_row:contains(Tour WP Confirm) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Confirm button",
                trigger: ".o_statusbar_buttons button[name='action_confirm']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Waiting for Approval",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/05-approve.md
    tour.register(
        "ssi_school_work_program_work_program_approve",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to approve",
                trigger: ".o_data_row:contains(Tour WP Approve) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Approve button",
                trigger: ".o_statusbar_buttons button[name='action_approve_approval']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is On Progress",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='open'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/06-reject.md
    tour.register(
        "ssi_school_work_program_work_program_reject",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to reject",
                trigger: ".o_data_row:contains(Tour WP Reject) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Reject button",
                trigger: ".o_statusbar_buttons button[name='action_reject_approval']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Rejected",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='reject'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/07-restart-approval.md
    tour.register(
        "ssi_school_work_program_work_program_restart_approval",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the stuck program",
                trigger: ".o_data_row:contains(Tour WP Stuck) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Restart Approval Process button",
                trigger:
                    ".o_statusbar_buttons button[name='action_reload_approval_template']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Waiting for Approval",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/08-done.md
    tour.register(
        "ssi_school_work_program_work_program_done",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to finish",
                trigger: ".o_data_row:contains(Tour WP Done) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Done button",
                trigger: ".o_statusbar_buttons button[name='action_done']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Done",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/09-cancel.md
    tour.register(
        "ssi_school_work_program_work_program_cancel",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to cancel",
                trigger: ".o_data_row:contains(Tour WP Cancel) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Cancel button",
                trigger: ".o_statusbar_buttons button:enabled:contains('Cancel')",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Wizard is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the cancellation reason",
                trigger:
                    ".o_field_widget[name='cancel_reason_id'] .o_radio_item:contains(Tour WP Reason) input",
            },
            {
                content: "Confirm the wizard",
                trigger: ".modal-footer button[name='action_confirm']",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Cancelled",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/10-restart.md
    tour.register(
        "ssi_school_work_program_work_program_restart",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to restart",
                trigger: ".o_data_row:contains(Tour WP Restart) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Restart button",
                trigger: ".o_statusbar_buttons button[name='action_restart']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Status is Draft",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/11-generate-occurrence.md
    tour.register(
        "ssi_school_work_program_work_program_generate_occurrence",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to generate occurrence for",
                trigger: ".o_data_row:contains(Tour WP Generate) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Generate Occurrence button",
                trigger:
                    ".o_statusbar_buttons button[name='action_generate_occurrence']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Open the Occurrences tab",
                trigger: ".o_notebook .nav-link:contains(Occurrences)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Occurrence lines are listed",
                trigger: ".o_field_widget[name='occurrence_ids'] .o_data_row",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/12-create-analytic-account.md
    tour.register(
        "ssi_school_work_program_work_program_create_analytic_account",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program to create the analytic account for",
                trigger: ".o_data_row:contains(Tour WP Analytic) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Create Analytic Account button",
                trigger:
                    ".o_statusbar_buttons button[name='action_create_analytic_account']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Analytic account is linked",
                trigger:
                    ".o_form_view .o_field_widget[name='analytic_account_id']:contains(Tour WP Analytic)",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "The button is gone",
                trigger:
                    ".o_statusbar_buttons:not(:has(button[name='action_create_analytic_account']:visible))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program/13-open-evaluation.md
    tour.register(
        "ssi_school_work_program_work_program_open_evaluation",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the School app",
                trigger: '.o_app[data-menu-xmlid="ssi_school.menu_school_root"]',
            },
            {
                content: "Open the Work Program menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.menu_work_program_root"]',
            },
            {
                content: "Open the Work Programs menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_menu"]',
            },
            {
                content: "Work Programs list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Programs)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the program with an evaluation",
                trigger: ".o_data_row:contains(Tour WP Evaluated) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Evaluations smart button",
                trigger: ".oe_button_box button[name='action_open_evaluation']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "The evaluations list of the program is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "The evaluation of the program is listed",
                trigger: ".o_list_view .o_data_row",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
