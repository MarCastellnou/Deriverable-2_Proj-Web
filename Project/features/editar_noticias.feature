Feature: Edit news
  In order to keep the cryptocurrency news updated all the time.
  As a user
  I want to edit and modify the outdated news

  Background: There are registered users and news created.
    Given Exists a user "user1" with password "123456"
    And There is news created by user "user1"
      | title | body | user |
      | Bitcoin approaches USD 7,000 | Most of the top 20 cryptocurrencies report significant gains on the day, while Bitcoin exceeds USD 6,900 | user1 |

    Scenario: Edit the body of the news
      Given login as user "username" with password "password"
      When I see the body for the news "news"
      And I edit the body of the news.
        | title | body | user |
      | Bitcoin approaches USD 7,000 | Most of the top 20 cryptocurrencies report significant gains on the day, while Bitcoin exceeds USD 6,900 | user1 |
      Then I'll see the book's details page.
        | title | body | user |
      | Bitcoin approaches USD 7,000 | Most of the top 20 cryptocurrencies report significant gains on the day, while Bitcoin exceeds USD 6,900 | user1 |

    Scenario: Try to edit the body but you have not logged in
      Given I'm not connected
      When I see the news
      Then There is no "edit" link available

    Scenario: Try to edit the body but not the title
      Given Login as user "username" with password "password"
      When I see the title and the body of the news
      Then there is no "edit" link available

    Scenario: Remove a news item
      Then I can delete notica

