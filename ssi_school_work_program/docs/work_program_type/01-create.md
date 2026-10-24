# Create Work Program Type

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_type`\
> **Menu:** School > Configuration > Work Program > Types\
> **Actor:** user in group `Work Program Type`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Access:** User is in group `Work Program Type`.

## Flow

1. Open the **School > Configuration > Work Program > Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name.
   - **Code** _(required)_: Enter a unique code, or leave it as **/** to assign it later
     using **Generate Code**.
   - **Analytic** tab, **Analytic Group**: Optional. The analytic group given to the
     analytic account of the work programs of this type.
   - **Planning Requirements** tab: eight checkboxes (Require Occurrence, Target,
     Objective, Committee, Material, Resource, Need, Rundown), all checked by default.
     Uncheck the sections that are not mandatory for this type of program.
4. Optional: click **Generate Code** in the header to automatically assign a code from
   the `sequence.template` configured for `work_program_type`. This requires an active
   `sequence.template` for this model; without one the action fails with an error. You
   may also leave the Code field as **/** or type a code manually instead.
5. Click **Save**.

## Post-Condition

- Work Program Type record is created and active.
- It becomes selectable in the **Type** field of a Work Program.
