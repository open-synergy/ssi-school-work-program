# Cancel Work Program Evaluation

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_evaluation`\
> **Menu:** School > Work Program > Evaluations\
> **Actor:** user in group `Work Program Evaluation — Validator`\
> **State:** `draft` | `confirm` | `done` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Waiting for Approval**, or **Done**.
- **Config:** An active `policy.template` for this model grants `cancel_ok` for state
  `draft` to the actor's group (`Work Program Evaluation — Validator`).
- **Config:** At least one cancellation reason exists and is available for use.
- **Access:** User is in group `Work Program Evaluation — Validator`.

## Flow

1. Open the **School > Work Program > Evaluations** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- A cancelled final evaluation no longer counts: another final evaluation can be made
  for the same work program, and it no longer lets the program be finished.
