# Based on example given by Barbara in class
# TODO: learn from, use and rewrite
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
from numpy.random import choice
import random


def classify():
    print("===== CLASSIFIER START =====\n")

    print("Loading data…")
    data = load_sentiment_sentences_and_labels()
    print("- Total # of instances:", len(data))

    print("\nSplitting data…")
    split_point = int(0.75 * len(data))
    sentences = [sentence for sentence, label in data]
    labels = [label for sentence, label in data]
    X_train, X_test = sentences[:split_point], sentences[split_point:]
    y_train, y_test = labels[:split_point], labels[split_point:]

    print("- # of train instances: {}\n- # of test instances: {}\n".format(len(X_train), len(X_test)))
    assert (len(X_train) == len(y_train))
    assert (len(X_test) == len(y_test))

    # Choose label for majority baseline (at random, equal class sizes)
    majority_label = choice([0, 1], 1, replace=False)
    majority_prediction = [majority_label for label in y_test]

    print("Vectorization of data…")
    vectorizer = CountVectorizer()
    clf = LogisticRegression()
    classifier = Pipeline(
        [
            ('vec', vectorizer),
            ('clf', clf)
        ]
    )

    print("Training model…")
    classifier.fit(X_train, y_train)

    print("Predicting…\n")
    y_predicted = classifier.predict(X_test)

    print("=== RESULTS ===\n- Accuracy: {}\n- Majority baseline: {}\n- Most predictive features:\n"
          .format(accuracy_score(y_test, y_predicted),
                  accuracy_score(y_test, majority_prediction)))

    # Printing most informative features and confusion matrix
    show_most_informative_features(vectorizer, clf)
    cnf_matrix = confusion_matrix(y_test, y_predicted)
    print("\n- Confusion matrix:")
    for line in cnf_matrix:
        print("\t" + str(line))
    print("\n===== CLASSIFIER END =====")

    # you can access the vectorizer (feature to feature number mapping) this way
    # print(vectorizer.vocabulary_.get('the'))


def load_sentiment_sentences_and_labels():
    """
    loads the movie review data
    """
    # Q1: What are the features used? Q4: How could you improve the representation of the data?
    high_income_users = open("../data/income.high").readlines()
    low_income_users = open("../data/income.low").readlines()

    # Q2: What is the label distribution?
    high_labels = [1 for user in high_income_users]
    low_labels = [0 for user in low_income_users]

    sentences = np.concatenate([high_income_users, low_income_users], axis=0)
    labels = np.concatenate([high_labels, low_labels], axis=0)

    # make sure we have a label for every data instance
    assert (len(sentences) == len(labels))

    data = list(zip(sentences, labels))
    random.shuffle(data)

    # return the data (instances + labels)
    return data


def show_most_informative_features(vectorizer, clf, n=10):
    feature_names = vectorizer.get_feature_names()
    for i in range(0, len(clf.coef_)):
        coefs_with_fns = sorted(zip(clf.coef_[i], feature_names))
        top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
        print("\tClass", i)
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))

if __name__ == '__main__':
    classify()