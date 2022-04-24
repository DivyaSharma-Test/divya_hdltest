Feature: Login
  Background:
    Given user is on the company home page

 @Login @raga
  Scenario: User successfully logs into the application
    When user clicks the login link on home page
    And enters correct username
    And enters correct password
    Then user is successfully logged into the application.


  @Login
   Scenario: User gets an error when trying to logon with invalid username
    When user clicks the login link on home page
    And enters invalid credentials for username
    And enters correct password
    Then user gets an error message.

  @Login
   Scenario: User gets an error when trying to logon with invalid username
    When user clicks the login link on home page
    And enters correct username
    And enters invalid credentials for password
    Then user gets an error message.