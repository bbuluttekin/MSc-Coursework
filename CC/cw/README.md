# Word count and Pagerank exercise in AWS

This is a programming project that designed using [MrJob](http://mrjob.readthedocs.org/en/stable/) library and Python 3.6+.

## Word Count
This part implements word count algorithm for calculating conditional probability of word w` that occurs immediately after another word w, ie.

P[w`|w] = count(w, w`) / count(w)

Calculations applied to all bigrams of [short jokes](https://www.kaggle.com/abhinavmoudgil95/short-jokes) dataset (200 000 short jokes) from Kaggle and returns top ten results for any given word.

## PageRank 

Writing a MapReduce program to calculate pagerank for each user in Epinions who-trust-whom online social network dataset. This program will return top 10 user with their associated pagerank score with the damping factor of 0.85.