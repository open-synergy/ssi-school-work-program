/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_school_work_program.work_program_evaluation_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/work_program_evaluation/01-create.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_create",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
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
                content: "Select the Work Program",
                trigger: ".o_field_many2one[name='work_program_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text WP/2026",
            },
            {
                content: "Pick the work program from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(WP/2026)",
                in_modal: false,
            },
            {
                content: "Fill in Date",
                trigger: ".o_field_widget[name='date'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 02/01/2026",
            },
            {
                content: "Open the Participants tab",
                trigger: ".o_notebook .nav-link:contains(Participants)",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Add a line to Participants",
                trigger:
                    ".o_field_widget[name='participant_ids'] .o_field_x2many_list_row_add a",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Participant dialog is open",
                trigger: ".o_field_widget[name='actual_quantity']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Target",
                trigger: ".o_field_many2one[name='target_id'] input",
                run: "click",
            },
            {
                content: "Pick work_program_target from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(work_program_target)",
                in_modal: false,
            },
            {
                content: "Fill in Actual Quantity",
                trigger: ".o_field_widget[name='actual_quantity']",
                run: "text 35",
            },
            {
                content: "Save & Close the Participant line",
                trigger: ".modal-footer .btn-primary:contains(Save & Close)",
            },
            {
                content: "Participant line is listed",
                trigger: ".o_field_widget[name='participant_ids'] .o_data_row",
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
                trigger: ".o_field_widget[name='actual_value']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Objective",
                trigger: ".o_field_many2one[name='objective_id'] input",
                run: "click",
            },
            {
                content: "Pick Tour WPE Objective from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour WPE Objective)",
                in_modal: false,
            },
            {
                content: "Fill in Actual Value",
                trigger: ".o_field_widget[name='actual_value']",
                run: "text 4",
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
                trigger: ".o_field_widget[name='actual_participant']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Occurrence",
                trigger: ".o_field_many2one[name='occurrence_id'] input",
                run: "click",
            },
            {
                content: "Pick Tour WPE Day from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WPE Day)",
                in_modal: false,
            },
            {
                content: "Fill in Actual Participant",
                trigger: ".o_field_widget[name='actual_participant']",
                run: "text 35",
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
                content: "Open the Conclusion tab",
                trigger: ".o_notebook .nav-link:contains(Conclusion)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Fill in the Evaluation Note",
                trigger: ".o_field_widget[name='evaluation_note']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPE Created note",
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
                extra_trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_evaluation/02-edit.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_edit",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to edit",
                trigger: ".o_data_row:contains(02/02/2026) .o_data_cell:first",
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
                content: "Open the Conclusion tab",
                trigger: ".o_notebook .nav-link:contains(Conclusion)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Change the Evaluation Note",
                trigger: ".o_field_widget[name='evaluation_note']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPE Edited note",
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
                content: "Evaluation Note shows the new value",
                trigger:
                    ".o_form_view.o_form_readonly .o_field_widget[name='evaluation_note']:contains(Tour WPE Edited note)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_evaluation/03-delete.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_delete",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to delete",
                trigger: ".o_data_row:contains(02/03/2026) .o_data_cell:first",
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
                trigger:
                    ".breadcrumb-item.o_back_button a:contains(Work Program Evaluations)",
            },
            {
                content: "The evaluation no longer appears in the list",
                trigger: ".o_list_view:not(:has(.o_data_row:contains(02/03/2026)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_evaluation/04-load-lines.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_load_lines",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to load lines for",
                trigger: ".o_data_row:contains(02/04/2026) .o_data_cell:first",
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
                content: "Click the Load Lines button",
                trigger: ".o_statusbar_buttons button[name='action_load_lines']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Participant lines are listed",
                trigger: ".o_field_widget[name='participant_ids'] .o_data_row",
                extra_trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_evaluation/05-confirm.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_confirm",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to confirm",
                trigger: ".o_data_row:contains(02/05/2026) .o_data_cell:first",
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

    // IK: docs/work_program_evaluation/06-approve.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_approve",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to approve",
                trigger: ".o_data_row:contains(02/06/2026) .o_data_cell:first",
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

    // IK: docs/work_program_evaluation/07-reject.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_reject",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to reject",
                trigger: ".o_data_row:contains(02/07/2026) .o_data_cell:first",
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

    // IK: docs/work_program_evaluation/08-restart-approval.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_restart_approval",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the stuck evaluation",
                trigger: ".o_data_row:contains(02/08/2026) .o_data_cell:first",
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

    // IK: docs/work_program_evaluation/09-cancel.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_cancel",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to cancel",
                trigger: ".o_data_row:contains(02/09/2026) .o_data_cell:first",
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
                    ".o_field_widget[name='cancel_reason_id'] .o_radio_item:contains(Tour WPE Reason) input",
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

    // IK: docs/work_program_evaluation/10-restart.md
    tour.register(
        "ssi_school_work_program_work_program_evaluation_restart",
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
                content: "Open the Evaluations menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_evaluation_menu"]',
            },
            {
                content: "Work Program Evaluations list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Evaluations)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the evaluation to restart",
                trigger: ".o_data_row:contains(02/10/2026) .o_data_cell:first",
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
});
