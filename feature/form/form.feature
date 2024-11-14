# Created by a00586601 at 10-11-2024
Feature: Form Submission

  # User enters the form details and on successful registration,
  # "Form successfully submitted" message will appear.

  Scenario: Successful form submission
    Given the user is on the form page
    When the user enters valid form details and submits the form
    Then a "Form successfully submitted" message should appear
