# Cancel Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — Validator`\
> **State:** `draft` | `confirm` | `open` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Waiting for Approval**, or **On Progress**.
- **Config:** An active `policy.template` for this model grants `cancel_ok` for state
  `draft` to the actor's group (`Work Program — Validator`).
- **Config:** At least one cancellation reason exists and is available for use.
- **Access:** User is in group `Work Program — Validator`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- The analytic account of the program, if any, is kept.
