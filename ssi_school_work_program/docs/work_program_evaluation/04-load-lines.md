# Load Lines of Work Program Evaluation

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_evaluation`\
> **Menu:** School > Work Program > Evaluations\
> **Actor:** user in group `Work Program Evaluation — User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Data:** The Work Program has participant targets, objectives or occurrences that are
  not yet reported in the evaluation.
- **Config:** An active `policy.template` for this model grants `load_lines_ok` for
  state `draft` to the actor's group (`Work Program Evaluation — User`).
- **Access:** User is in group `Work Program Evaluation — User`.

## Flow

1. Open the **School > Work Program > Evaluations** menu.
2. Open the record in Draft status.
3. Click the **Load Lines** button.
4. Click **OK** on the confirmation dialog.
5. Open the **Participants**, **Objectives** and **Occurrences** tabs to see the lines.

## Post-Condition

- One participant line is created for each participant target of the work program, one
  objective line for each objective, and one occurrence line for each occurrence that is
  not cancelled.
- Targets, objectives and occurrences that already have a line are skipped and existing
  lines are never changed or deleted, so the action can be run again safely.
- Status remains **Draft**.
