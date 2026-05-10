# Clinic Appointment and Prescription Management System

## Project Overview
This project defines the static architecture of a **Clinic Management System** using UML Class Diagrams. It captures the full patient lifecycle, from the initial appointment booking and registration fee payment to the medical consultation and eventual prescription fulfillment.

## Class Diagram Description
1. This UML class diagram illustrates the static structure of a clinic management system, covering the entire workflow from booking to prescription fulfillment.
2. The **Patient** class acts as the service initiator, maintaining a one-to-many ($1:*$) relationship with the **Appointment** class.
3. The **Clinic** class serves as the administrative authority, managing available slots and coordinating the scheduling of all **Appointments**.
4. A **Doctor** class is included, representing medical staff who hold a one-to-many ($1:n$) relationship with the **Clinic**.
5. Every **Appointment** is assigned to a specific doctor and eventually results in a single **Consultation** session.
6. During the **Consultation**, the doctor records key diagnosis details and exam notes by executing the `conductExam()` method.
7. The $0..1$ multiplicity between **Consultation** and **MedicationOrder** accurately reflects that a prescription is an optional outcome of a diagnosis.
8. The **Payment** class utilizes dual associations to support the two distinct settlement points in the process: booking fees and medication fees.
9. This design ensures financial accountability by linking each transaction to a specific business entity, such as an appointment or an order.
10. The entire architecture achieves a functional loop through clearly defined methods like `processOrder()`, `confirmSlot()`, and `updateStatus()`.

## Key Features
- **Dual-Checkpoint Payment**: Supports both booking fee (registration) and medication fee processing.
- **Conditional Workflow**: Handles consultations that may or may not result in a prescription ($0..1$ multiplicity).
- **Role-Based Design**: Clearly separates the responsibilities of Patients, Doctors, and Clinic Administration.

## Artifacts
- `Class_Diagram.png`: The visual representation of the system structure.
- `Activity_Diagram.png`: (Reference) The behavioral flow matching this class structure.

---
*Generated based on system design specifications for the Clinic Management System.*
