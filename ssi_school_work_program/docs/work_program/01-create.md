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
5. On the **Participant Targets** tab, repeat the following steps as many times as
   needed:

   - Click **Add a line**.
   - **Participant Type** _(required)_: Select **Student**, **Teacher**, **Staff**,
     **Parent** or **Other**. The default is **Student**.
   - **Grade** _(required if **Participant Type** is **Student**)_: Select the grade of
     the targeted students. The field is hidden for the other types and is cleared when
     the type is changed away from **Student**.
   - **Description**: Optional. Enter who exactly is targeted by the line.
   - **Quantity** _(required)_: Enter the planned number of participants. It must be
     greater than zero.
   - Click **Save & Close**.

   A program can have only one line for each combination of type and grade.

6. On the **Objectives** tab, repeat the following steps as many times as needed:
   - Click **Add a line**.
   - **Kind** _(required)_: Select the kind of objective. The default is **Outcome**.
   - **Objective** _(required)_: Enter the objective.
   - **Indicator** _(required)_: Enter the indicator that measures the objective.
   - **Measurement Type** _(required)_: Select how the objective is measured. The
     default is **Numeric**.
   - **Baseline Value**, **Target Value** and **Unit**: Optional. Enter the numbers the
     objective is measured against.
   - **Target Description**: Optional. Describe the target in words.
   - **Verification**: Optional. Describe how the result is verified.
   - Click **Save & Close**.
7. On the **Committee** tab, repeat the following steps as many times as needed:
   - Click **Add a line**.
   - **Employee** _(required)_: Select the committee member.
   - **Role** _(required)_: Select the role of the member in the committee.
   - Click **Save & Close**.
8. On the **Materials** tab, repeat the following steps as many times as needed:
   - Click **Add a line**.
   - **Material** _(required)_: Enter the name of the material.
   - **Description**: Optional. Enter the details of the material.
   - Click **Save & Close**.
9. On the **Resource Persons** tab, repeat the following steps as many times as needed:
   - Click **Add a line**.
   - **Partner** _(required)_: Select the resource person.
   - **Role Description**: Optional. Describe the contribution of the person.
   - Click **Save & Close**.
10. On the **Needs** tab, repeat the following steps as many times as needed:
    - Click **Add a line**.
    - **Need** _(required)_: Enter the name of the need.
    - **Quantity**: Enter the planned quantity. The default is 1.
    - **Occurrence**: Optional. Select the occurrence of this program the need belongs
      to.
    - Click **Save & Close**.
11. On the **Occurrences** tab, repeat the following steps as many times as needed. You
    can skip this tab when the occurrences are generated later by
    `11-generate-occurrence`:
    - Click **Add a line**.
    - **Name**: Optional. Enter the label of the session.
    - **Date Start** _(required)_: Enter the first day of the occurrence.
    - **Date End** _(required)_: Automatically filled from **Date Start**. Change if
      needed.
    - **Time Start** and **Time End**: Optional. Enter the time of the day.
    - **Location**: Optional. Enter where the occurrence takes place.
    - To plan the rundown, repeat the following steps as many times as needed:
      - Click **Add a line** in the rundown list.
      - **Date** _(required)_, **Time Start** _(required)_, **Time End** _(required)_
        and **Activity** _(required)_: Enter when and what happens.
      - **Person in Charge**: Optional. Select the employee in charge of the activity.
      - Click **Save & Close**.
    - Click **Save & Close**.

The **Completeness** tab and the **Planning Complete** field show which sections are
filled in; they are informative and do not block `04-confirm`. 12. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number is still **/**; it is assigned when the program is opened.
