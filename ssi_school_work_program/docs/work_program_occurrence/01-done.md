# Mark Work Program Occurrence as Done

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_occurrence`\
> **Menu:** School > Work Program > Occurrences\
> **Actor:** user in group `Work Program — User`\
> **State:** `planned` → `done`

## Pre-Condition

- **Record:** Status is **Planned**.
- **Data:** The work program of the occurrence exists.
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Occurrences** menu.
2. Open the occurrence to mark.
3. Click the **Done** button.

## Post-Condition

- Status changes to **Done**.
