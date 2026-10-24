# Restart Approval Process of Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — Validator`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**, and the document has no approval
  template attached (the approval is stuck because no approver was assigned).
- **Config:** An active `policy.template` grants `restart_approval_ok` for state
  `confirm` to the actor's group (`Work Program — Validator`). By default the grant is
  guarded: the **Restart Approval Process** button is visible only while the document
  has no approval template, so it does not appear on a document whose approval is
  running normally.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Access:** User is in group `Work Program — Validator`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the stuck record.
3. Click the **Restart Approval Process** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The old approval records are removed and the approval is requested again from the
  beginning, using the approval template that matches the record now.
- Status remains **Waiting for Approval**.
