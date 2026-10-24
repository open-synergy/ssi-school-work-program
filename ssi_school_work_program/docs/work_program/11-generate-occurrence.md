# Generate Occurrence of Work Program

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program`\
> **Menu:** School > Work Program > Work Programs\
> **Actor:** user in group `Work Program — User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft** or **On Progress**.
- **Record:** **Frequency Set** is filled in, and **Date Start** and **Date End** are
  set.
- **Data:** The Frequency Set has at least one frequency rule.
- **Config:** An active `policy.template` for this model grants `generate_occurrence_ok`
  for state `draft` to the actor's group (`Work Program — User`).
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Work Programs** menu.
2. Open the record.
3. Click the **Generate Occurrence** button.
4. Click **OK** on the confirmation dialog.
5. Open the **Occurrences** tab to see the generated dates.

## Post-Condition

- One occurrence is created for each date given by the Frequency Set between **Date
  Start** and **Date End**, starting and ending on that date, in **Planned** status.
- Dates that already have an occurrence are skipped and existing occurrences are never
  deleted, so the action can be run again safely.
