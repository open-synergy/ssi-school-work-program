# Create Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — User`\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** The School, the Academic Year, a Work Program Type, a Work Program Category,
  and the Employee who is the person in charge already exist.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group (needed later by `04-confirm`).
- **Config:** An active `sequence.template` exists for this model (the document number
  is assigned when the program is opened).
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Title** _(required)_: Enter the short name of the activity.
   - **School** _(required)_: Select the school that carries out the program.
   - **Academic Year** _(required)_: Select the academic year the program is planned
     for.
   - **Type** _(required)_ and **Category** _(required)_: Select the type and the
     category of the program.
   - **Strategic Objective**: Optional. Select the strategic objective the program
     supports.
   - **Person in Charge** _(required)_: Select the employee responsible for the program.
   - **Date Start** _(required)_ and **Date End** _(required)_: Enter the period of the
     program. The end date must not be earlier than the start date.
   - **Planning Cycle** _(required)_: Automatically filled with **Regular** or
     **Additional** from the planning deadline of the academic year. Change if needed.
   - **Budget Ceiling**: Optional. Enter the maximum budget of the program.
   - **Frequency Set**: Optional. Select the recurrence rules used later by
     `11-generate-occurrence`.
4. On the **Background** tab, enter the need, the context and the participant criteria.
5. On the **Participant Targets**, **Objectives**, **Committee**, **Materials**,
   **Resource Persons**, **Needs** and **Occurrences** tabs, click **Add a line** and
   fill in the lines. The **Completeness** tab and the **Planning Complete** field show
   which sections are filled in; they are informative and do not block `04-confirm`.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number is still **/**; it is assigned when the program is opened.
