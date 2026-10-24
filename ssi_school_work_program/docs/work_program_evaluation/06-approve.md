# Approve Work Program Evaluation

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_evaluation`\
> **Menu:** School > Work Program > Evaluations\
> **Actor:** approver on the pending approval level\
> **State:** `confirm` → `done`\
> **Requires:** `05-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `approve_ok` to the actor's group.
- **Access:** User is registered as an approver on the approval level that is currently
  **pending**. When the template uses sequential approval, only the first unapproved
  level is pending.

## Flow

1. Open the **School > Work Program > Evaluations** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If all approval levels are fulfilled, status changes automatically to **Done** and the
  document number is generated. There is no separate Start or Done button: the
  evaluation moves from Waiting for Approval straight to Done.
- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.
- A final evaluation that is **Done** lets the work program be finished when its type
  requires a final evaluation (see `work_program` `08-done`).
