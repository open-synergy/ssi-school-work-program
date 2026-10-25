/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_school_work_program.work_program_occurrence_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    /**
     * Click the primary button of the topmost dialog.
     *
     * An existing line opens with "Save", a new one with "Save & Close".
     *
     * @param {String} content Step description.
     * @returns {Object} Tour step.
     */
    function clickDialogSaveStep(content) {
        return {
            content: content,
            trigger: ".modal-footer button.btn-primary",
            run: function () {
                var $btn = $(".modal:visible")
                    .last()
                    .find(".modal-footer button.btn-primary")
                    .filter(function () {
                        var t = $(this).text().trim();
                        return t === "Save & Close" || t === "Save";
                    });
                $btn[0].click();
            },
        };
    }

    // IK: docs/work_program_occurrence/01-done.md
    tour.register(
        "ssi_school_work_program_work_program_occurrence_done",
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
                content: "Open the Work Program Occurrences menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_occurrence_menu"]',
            },
            {
                content: "Work Program Occurrences list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Occurrences)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the occurrence to mark",
                trigger: ".o_data_row:contains(Tour Occ Done) .o_data_cell:first",
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
                content: "Status is Done",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_occurrence/02-cancel.md
    tour.register(
        "ssi_school_work_program_work_program_occurrence_cancel",
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
                content: "Open the Work Program Occurrences menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_occurrence_menu"]',
            },
            {
                content: "Work Program Occurrences list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Occurrences)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the occurrence to cancel",
                trigger: ".o_data_row:contains(Tour Occ Cancel) .o_data_cell:first",
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
                trigger: ".o_statusbar_buttons button[name='action_cancel']",
                extra_trigger: ".o_form_view",
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

    // IK: docs/work_program_occurrence/03-reset.md
    tour.register(
        "ssi_school_work_program_work_program_occurrence_reset",
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
                content: "Open the Work Program Occurrences menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_occurrence_menu"]',
            },
            {
                content: "Work Program Occurrences list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Occurrences)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the occurrence to reset",
                trigger: ".o_data_row:contains(Tour Occ Reset) .o_data_cell:first",
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
                content: "Click the Reset to Planned button",
                trigger: ".o_statusbar_buttons button[name='action_reset']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Status is Planned",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='planned'].btn-primary",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_occurrence/04-load-preparation.md
    tour.register(
        "ssi_school_work_program_work_program_occurrence_load_preparation",
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
                content: "Open the Work Program Occurrences menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_occurrence_menu"]',
            },
            {
                content: "Work Program Occurrences list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Occurrences)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the occurrence to prepare",
                trigger: ".o_data_row:contains(Tour Occ Prepare) .o_data_cell:first",
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
                content: "Click the Load Preparation button",
                trigger: ".o_statusbar_buttons button[name='action_load_preparation']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Load Preparation finished",
                trigger:
                    ".o_statusbar_buttons button[name='action_load_preparation']:enabled",
                extra_trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit:enabled",
                extra_trigger: ".o_form_view.o_form_readonly",
            },
            {
                content: "Open the Preparation tab",
                trigger: ".o_notebook .nav-link:contains(Preparation)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Open the loaded task line",
                trigger:
                    ".o_field_widget[name='preparation_ids'] .o_data_row:contains(Tour Prepare Venue) .o_data_cell:first",
            },
            {
                content: "Fill in Date Done",
                trigger: ".o_field_widget[name='date_done'] input",
                run: "text 01/05/2026",
            },
            clickDialogSaveStep("Save the task line"),
            {
                content: "Task line is listed",
                trigger: ".o_field_widget[name='preparation_ids'] .o_data_row",
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
        ]
    );
});
