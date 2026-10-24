# Reset Work Program Occurrence to Planned

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_occurrence`\
> **Menu:** School > Work Program > Occurrences\
> **Actor:** user in group `Work Program — User`\
> **State:** `done` | `cancel` → `planned`\
> **Requires:** `01-done`

## Pre-Condition

- **Record:** Status is **Done** or **Cancelled**.
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Occurrences** menu.
2. Open the occurrence to reset.
3. Click the **Reset to Planned** button.

## Post-Condition

- Status returns to **Planned**.
