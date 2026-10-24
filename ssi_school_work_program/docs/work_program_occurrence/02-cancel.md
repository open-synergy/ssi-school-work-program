# Cancel Work Program Occurrence

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_occurrence`\
> **Menu:** School > Work Program > Occurrences\
> **Actor:** user in group `Work Program — User`\
> **State:** `planned` → `cancel`

## Pre-Condition

- **Record:** Status is **Planned**.
- **Data:** The work program of the occurrence exists.
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Occurrences** menu.
2. Open the occurrence to cancel.
3. Click the **Cancel** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- The occurrence is no longer counted when the completeness of the work program is
  evaluated.
