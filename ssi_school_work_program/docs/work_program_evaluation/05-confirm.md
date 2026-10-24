# Confirm Work Program Evaluation

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_evaluation`\
> **Menu:** School > Work Program > Evaluations\
> **Actor:** user in group `Work Program Evaluation — User`\
> **State:** `draft` → `confirm`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group (`Work Program Evaluation — User`).
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Access:** User is in group `Work Program Evaluation — User`.

## Flow

1. Open the **School > Work Program > Evaluations** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
