# Create Analytic Account of Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Waiting for Approval**, or **On Progress**.
- **Record:** The **Analytic Account** field is still empty.
- **Config:** An active `policy.template` for this model grants
  `create_analytic_account_ok` for state `draft` to the actor's group
  (`Work Program — User`).
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record.
3. Click the **Create Analytic Account** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- An analytic account named after the program title is created and shown in the
  **Analytic Account** field. It is placed in the analytic group of the program type and
  linked to the partner of the company.
- The button disappears once the account exists; no second account is ever created.
- When the program is opened without an analytic account, the system creates it
  automatically.
