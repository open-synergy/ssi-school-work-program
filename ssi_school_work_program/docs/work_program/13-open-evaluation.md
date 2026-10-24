# Open Evaluations of Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — Viewer`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The work program exists in any status.
- **Access:** User is in group `Work Program — Viewer`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record.
3. Click the **Evaluations** smart button at the top of the form.

## Post-Condition

- The list of **Work Program Evaluations** opens, showing only the evaluations of this
  work program. The smart button shows how many evaluations the program has.
- Clicking **New** in that list starts an evaluation whose **Work Program** is already
  this program (see `work_program_evaluation` `01-create`).
