# Approve Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** approver on the pending approval level\
> **State:** `confirm` → `open`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `approve_ok` to the actor's group.
- **Access:** User is registered as an approver on the approval level that is currently
  **pending**. When the template uses sequential approval, only the first unapproved
  level is pending.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If all approval levels are fulfilled, status changes automatically to **On Progress**
  (there is no separate Start step), the document number is generated, and the analytic
  account is created when the program does not have one yet.
- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.

> **Note:** `work_program` inherits `mixin.transaction_open`, but the Start button is
> not rendered. The transition to **On Progress** always happens automatically as soon
> as the last approval level is fulfilled — there is no `Start` instruction for this
> model.
