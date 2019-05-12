Feature: Create news
  Given Exists is a user "user1" with password "123456"

Scenario: Register some news
  Given I login as user "user1" with password "123456"
  When I register news
    | title | body | user |
    | Bitcoin approaches USD 7,000 | Most of the top 20 cryptocurrencies report significant gains on the day, while Bitcoin exceeds USD 6,900 | user1 |
    | Ethereum Foundation | The Ethereum Foundation plans to spend USD 30 million on different projects | user1 |
  Then There is 2 news