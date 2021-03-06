__TOPIC: Cryptocurrencies__
==============================================

__Entities: News - Quotation__
-------------------

This will allow us to know both the latest related news such as the price of different currency pairs as well as possible future changes or purchase opportunities.

Obtaining data: through the api of coinmarketcap.com and the news through the research website or similar

The API will use the KEY of [coinmarketcap.com](https://coinmarketcap.com/) that allows us to obtain 5 pairs of currencies free of charge and to make 10k consultation calls per month.

__Requirements__
-------------------
To run this application you need to have installed file Requirements.txt.
You can do it by doing this in the terminal 

__How to use__
-------------------
In our web we find 2 sections often the most important coins and their quotes and on the other hand we find the most relevant news in the world of cryptocurrencies.

__Deliverable 2.0__
-------------------

In this second deliverable, the option has been implemented that allows registered users to add news, modify it and eliminate it. For now, all users can modify and delete all news without restriction. The best option would be that each one can only modify and eliminate the news that were created by him, but this option has not been implemented yet.

In addition to all this, small unit tests have been carried out to verify that the attributes of the database of each news item correspond to those expected.

Finally, the [coinmarketcap.com](https://coinmarketcap.com/) API has been added, and in this way we can see the crypto-currencies. A filter has been applied, which only shows the first 25 coins, because if the first 100 were shown, the page took a long time to load.

__Deliverable 3.0__
-------------------
In this version, we have imrpoved the news section by making it with a more structured design. The news database model has been modified to make a more accurate representation of the RDFa mark.

More visual styles have been added to the cryptocurrency part that makes it possible to differentiate them.

RDFa has been included in HTML, that allows the machines to better recognize the structured data, in our case we have used it in the news and currencies fields, although the Google tool does not recognize the latter.

To carry out all this activity, the following tools have been used to perform the marking correctly and to verify it:
* [schema.org](https://schema.org/)
* [Google Structured Data Testing tool](https://search.google.com/structured-data/testing-tool)
* [Tool to test the generated RDFa](http://rdfa.info/play/)

__Credits__
-------------------
* [Xavi Berga](https://github.com/xaps97)
* [Jose Almunia](https://github.com/jokerarm96)
* [Marc Castellnou](https://github.com/MarCastellnou) 
* [Saber Tiguer](https://github.com/stiguer)

