/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_school_work_program.work_program_role_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/work_program_role/01-create.md
    tour.register(
        "ssi_school_work_program_work_program_role_create",
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
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school.menu_school_configuration"]',
            },
            {
                content: "Open the Work Program Roles menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_role_menu"]',
            },
            {
                content: "Work Program Roles list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Roles)",
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
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Role Create",
            },
            {
                content: "Ensure Code is /",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
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
                content: "Name is shown",
                trigger:
                    ".o_form_view.o_form_readonly .o_field_widget[name='name']:contains(Tour Role Create)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_role/02-edit.md
    tour.register(
        "ssi_school_work_program_work_program_role_edit",
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
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school.menu_school_configuration"]',
            },
            {
                content: "Open the Work Program Roles menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_role_menu"]',
            },
            {
                content: "Work Program Roles list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Roles)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the record to edit",
                trigger: ".o_data_row:contains(Tour Role Edit) .o_data_cell:first",
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
                content: "Change the Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Role Edited",
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
                content: "Name shows the new value",
                trigger:
                    ".o_form_view.o_form_readonly .o_field_widget[name='name']:contains(Tour Role Edited)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );

    // IK: docs/work_program_role/03-delete.md
    tour.register(
        "ssi_school_work_program_work_program_role_delete",
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
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school.menu_school_configuration"]',
            },
            {
                content: "Open the Work Program Roles menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_school_work_program.work_program_role_menu"]',
            },
            {
                content: "Work Program Roles list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Work Program Roles)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Open the record to delete",
                trigger: ".o_data_row:contains(Tour Role Delete) .o_data_cell:first",
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
                    ".breadcrumb-item.o_back_button a:contains(Work Program Roles)",
            },
            {
                content: "Tour Role Delete no longer appears in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(Tour Role Delete)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
