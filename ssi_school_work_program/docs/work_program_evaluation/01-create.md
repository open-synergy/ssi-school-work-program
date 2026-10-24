# Create Work Program Evaluation

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_evaluation`\
> **Menu:** School > Work Program > Evaluations\
> **Actor:** user in group `Work Program Evaluation — User`\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** The Work Program to evaluate already exists and is **On Progress** or
  **Done**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group (needed later by `05-confirm`).
- **Config:** An active `sequence.template` exists for this model (the document number
  is assigned when the evaluation is done).
- **Access:** User is in group `Work Program Evaluation — User`.

## Flow

1. Open the **School > Work Program > Evaluations** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Work Program** _(required)_: Select the work program to evaluate. Only programs
     that are On Progress or Done can be selected. The **School** and **Academic Year**
     are filled in from the program.
   - **Evaluation Type** _(required)_: **Final** (default) or **Mid-term**. A work
     program can have only one final evaluation that is not cancelled.
   - **Date** _(required)_: Enter the date of the evaluation. It must not be earlier
     than the **Date Start** of the work program.
4. On the **Participants**, **Objectives** and **Occurrences** tabs, click **Add a
   line** and report the actual result of each line, or use `04-load-lines` to create
   the lines from the work program.
5. On the **Conclusion** tab, enter the evaluation note, the lesson learned and the
   recommendation.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- The document number is still **/**; it is assigned when the evaluation is done.
