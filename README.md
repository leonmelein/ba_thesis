# Detecting Income Level of Dutch Twitter Users using Stylometric Features
Léon Melein (S2580861), University of Groningen, l.r.melein@student.rug.nl

### Abstract
Income prediction is a relatively undiscovered aspect of author profiling. Early research on English (Flekova et al., 2016) linking Twitter users to occupations and their respective average incomes, obtained promising results. There is no comparable research for Dutch speakers yet. In this thesis, we explore to what extent author profiling can predict the income level of Dutch users.

We do so by creating a dataset of 2000 Twitter users. These are divided into two income classes as there currently is no complete income data available for individual occupations in The Netherlands. We use _distant supervision_ to annotate users with their occupational class and their income. We then extract a number of surface, readability and n-gram features from the users' posts. Using logistic regression, we try to classify the users on their income class with those features.

After testing various feature groupings, the classifier proved to be the most robust with uni-, bi- and trigram features, reaching an F1-score of 0.72. Although this indicates that profiling can predict a user's income class to a very large extent, this can only be seen as a first indication as the scope of this study is limited. With clear directions for future improvement, we hope that this study may be a stepping stone towards the prediction of individual incomes for Dutch authors.


### Python packages
* datagathering: tools used to download data from Twitter for our users and make a random selection of users.
* preprocessing: tools used to process the downloaded data into a suitable format for use with our classifier
* machinelearning: tools used to build the classifier that will predict income class for a given user.