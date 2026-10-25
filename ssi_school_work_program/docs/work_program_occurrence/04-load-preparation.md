# Load Preparation of Work Program Occurrence

> **Module:** `ssi_school_work_program`\
> **Model:** `work_program_occurrence`\
> **Menu:** School > Work Program > Occurrences\
> **Actor:** user in group `Work Program — User`\
> **State:** `planned` → `planned`

## Pre-Condition

- **Record:** Status is **Planned**.
- **Data:** The **Type** of the work program has at least one line in its
  **Preparation** tab (**School > Configuration > Work Program > Types**).
- **Access:** User is in group `Work Program — User`.

## Flow

1. Open the **School > Work Program > Occurrences** menu.
2. Open the occurrence in Planned status.
3. Click the **Load Preparation** button.
4. Click **Edit**.
5. Open the **Preparation** tab to see the loaded tasks.
6. Click a task line to open it.
7. Fill in the actual finish date:
   - **Date Done**: Enter the day the task was finished.
8. Click **Save & Close**.
9. Click **Save**.

## Post-Condition

- One task line is created for each preparation template of the work program type, with
  the **Deadline** set to the start date of the occurrence minus the template **Lead
  Days**, and the **Person in Charge** set to the one of the work program.
- Templates that already have a line are skipped and existing lines are never changed or
  deleted, so the action can be run again safely.
- The task line is marked **Done** and the **Preparation Progress** and **Preparation
  Status** of the occurrence follow the finished tasks.
- Status of the occurrence remains **Planned**.
