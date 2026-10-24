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
});
