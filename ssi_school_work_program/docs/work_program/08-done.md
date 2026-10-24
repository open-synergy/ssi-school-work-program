# Finish Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — User`\
> **State:** `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for this model grants `done_ok` for state
  `open` to the actor's group (`Work Program — User`).
- **Config:** When the **Work Program Type** has **Require Final Evaluation** checked,
  the work program has a **Final** evaluation in status **Done** (see
  `work_program_evaluation` `06-approve`); without it the **Done** button is rejected
  with an error. A type without that flag does not need an evaluation.
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
