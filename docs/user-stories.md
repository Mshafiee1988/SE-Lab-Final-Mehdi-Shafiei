User Stories – University Registration System

User Story 1

As a student, I want to view available courses with their schedules so that I can choose courses that fit my timetable.

INVEST Analysis

Criteria| Status| Explanation
Independent| Yes| Can be implemented without other features
Negotiable| Yes| UI and display format can vary
Valuable| Yes| Helps students choose correct courses
Estimable| Yes| Effort can be estimated clearly
Small| Yes| Focuses only on course listing
Testable| Yes| Can be verified by checking course list

---

User Story 2

As a student, I want to register for a course so that I can enroll in my desired class.

INVEST Analysis

Criteria| Status| Explanation
Independent| Yes| Works independently from reporting modules
Negotiable| Yes| Registration process can be designed differently
Valuable| Yes| Core functionality of the system
Estimable| Yes| Implementation is straightforward
Small| Yes| Focused on single action (enroll)
Testable| Yes| Can verify enrollment success

---

User Story 3

As an administrator, I want to manage course capacity so that no course exceeds its maximum number of students.

INVEST Analysis

Criteria| Status| Explanation
Independent| Yes| Separate from student actions
Negotiable| Yes| Capacity rules can vary
Valuable| Yes| Prevents system overload
Estimable| Yes| Clear logic for capacity control
Small| Yes| Focused only on capacity management
Testable| Yes| Can test max enrollment limit |

---



Acceptance Criteria (Gherkin)


Scenario 1 – Successful Course Registration


Given the student is logged into the system

And the course has available seats

When the student selects the course and clicks "Register"

Then the system should successfully enroll the student in the course

And the available seats should decrease by one



Scenario 2 – Failed Registration (No Capacity)


Given the student is logged into the system

And the course has no available seats

When the student attempts to register for the course

Then the system should reject the registration request

And an error message "Course is full" should be displayed

