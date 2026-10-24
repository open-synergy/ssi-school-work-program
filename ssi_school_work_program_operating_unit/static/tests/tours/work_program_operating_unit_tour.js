/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_school_work_program_operating_unit.work_program_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/work_program/01-create.md
    // Extension tour (E1): creates a program like the base module's create
    // tour and additionally picks the Operating Unit added by this module.
    tour.register(
        "ssi_school_work_program_operating_unit_work_program_create",
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
                content: "Operating Unit field is present on the create form",
                trigger: ".o_field_many2one[name='operating_unit_id']:visible",
                extra_trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Title",
                trigger: ".o_field_widget[name='title']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Create",
            },
            {
                content: "Select the School",
                trigger: ".o_field_many2one[name='school_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU School",
            },
            {
                content: "Pick Tour WPOU School from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU School)",
                in_modal: false,
            },
            {
                content: "Select the Academic Year",
                trigger: ".o_field_many2one[name='academic_year_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Year",
            },
            {
                content: "Pick Tour WPOU Year from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU Year)",
                in_modal: false,
            },
            {
                content: "Select the Type",
                trigger: ".o_field_many2one[name='type_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Type",
            },
            {
                content: "Pick Tour WPOU Type from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU Type)",
                in_modal: false,
            },
            {
                content: "Select the Category",
                trigger: ".o_field_many2one[name='category_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Category",
            },
            {
                content: "Pick Tour WPOU Category from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU Category)",
                in_modal: false,
            },
            {
                content: "Select the Person in Charge",
                trigger: ".o_field_many2one[name='pic_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Employee",
            },
            {
                content: "Pick Tour WPOU Employee from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU Employee)",
                in_modal: false,
            },
            {
                content: "Select the Operating Unit",
                trigger: ".o_field_many2one[name='operating_unit_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour WPOU Unit B",
            },
            {
                content: "Pick Tour WPOU Unit B from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour WPOU Unit B)",
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
                content: "Operating Unit is the selected one",
                trigger:
                    ".o_form_view.o_form_readonly .o_field_widget[name='operating_unit_id']:contains(Tour WPOU Unit B)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
