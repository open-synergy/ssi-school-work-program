# Create Work Program Strategic Objective

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_strategic_objective`\
> **Menu:** School > Configuration > Work Program > Strategic Objectives\
> **Actor:** user in group `Work Program Strategic Objective`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Access:** User is in group `Work Program Strategic Objective`.

## Flow

1. Open the **School > Configuration > Work Program > Strategic Objectives** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name.
   - **Code** _(required)_: Enter a unique code, or leave it as **/** to assign it later
     using **Generate Code**.
4. Optional: click **Generate Code** in the header to automatically assign a code from
   the `sequence.template` configured for `work_program_strategic_objective`. This
   requires an active `sequence.template` for this model; without one the action fails
   with an error. You may also leave the Code field as **/** or type a code manually
   instead.
5. Click **Save**.

## Post-Condition

- Work Program Strategic Objective record is created and active.
- It becomes selectable in the **Strategic Objective** field of a Work Program.
