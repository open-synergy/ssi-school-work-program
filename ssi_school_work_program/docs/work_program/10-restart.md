# Restart Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — Validator`\
> **State:** `cancel` | `reject` → `draft`\
> **Requires:** `09-cancel`

## Pre-Condition

- **Record:** Status is **Cancelled** or **Rejected**.
- **Config:** An active `policy.template` for this model grants `restart_ok` for state
  `cancel` to the actor's group (`Work Program — Validator`).
- **Access:** User is in group `Work Program — Validator`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status returns to **Draft**.
- All approval records are removed and the approval template is cleared. A later Confirm
  starts the approval process from the beginning.
