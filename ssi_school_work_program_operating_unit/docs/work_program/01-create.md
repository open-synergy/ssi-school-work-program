# Create Work Program

> **Module:** `ssi_school_work_program_operating_unit`\
> **Extends:** ssi_school_work_program — model `work_program`, aksi `01-create`

## Additional Fields

When this module is installed, the create form gains one field:

- **Operating Unit**: The operating unit this work program belongs to. Defaults to the
  current user's default operating unit and can be changed while the program is in
  **Draft**; it is read-only in every other status. The occurrences and the evaluations
  of the program always carry the same operating unit as the program and follow it when
  it changes. The field is only shown to users who belong to the **Multiple Operating
  Unit** group.

## Modified — Record Visibility

- The Work Program, Work Program Occurrence and Work Program Evaluation lists are now
  filtered by operating unit for users in the `Operating Unit` data ownership groups
  (implied by the `Company` data ownership group of each document). A user only sees
  records whose Operating Unit is one of their own assigned operating units. This is not
  a Flow step.
- The analytic account created by **Create Analytic Account** is not given an operating
  unit.
