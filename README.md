# stonks
Web App to predict stock prices using Social Media Sentiment.

<center><h1>Stonks</h1></center>
<hr>
 <br>
  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/thecoderenroute/stonks/blob/main/LICENSE)
[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=Naereen&theme=blue-green)](https://github.com/anuraghazra/github-readme-stats)

The name of our app is "Stonks" named after a popular internet catchphrase associated with financial gain and popularized during the Gamestop event.

The main purpose of our app is to scan through social media feeds (currently we are just going through Twitter but plan to including Reddit as well) and determine the future stock performance based on the financial sentiment surrounding a certain stock/ company.

We implemented this App in Python using the Django framework to deploy it. We used HTML, CSS, JavaScript, and some of their frameworks (Bootstrap, AOS, etc.) for the front-end. We implemented the backend in pure python using the MVT approach. The main components of the back-end were the Twitter data retrieval, Stock Market Data retrieval and processing of received data using Machine Learning (Natural Language Processing). 

The Sentiment determination is done using two libraries: nltk to format our data and flair to determine the sentiment of individual tweets. We are using DataFrames from the pandas library to handle our data with ease. The final score determination depends not only on the social media sentiment but also on the relation between social media sentiment and stock market performance of previous days. This helps us predict the data for the next day. Our data's authenticity lies in the fact that our multiplying factors depend on the social media sentiment as well as the performance of the said stock on the particular day for which we are deriving the social media sentiment.
