#!/usr/bin/python
# Classifier (in development)
# Léon Melein, s2580861

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import KFold
import numpy as np
import random
import pickle

from sklearn.model_selection import StratifiedKFold

from machinelearning.featurizers.Featurizer import Featurizer


def perform_classification(X_train, X_test, y_train, y_test, featureset=("ngrams", "surface", "readability"),
                           ngrams="1-2", prefeaturized=False):
    """
    Performs a single classification using a Logistic Regression model and prints the resulting statistics to screen.

    Partly based on an example by B. Plank <https://github.com/bplank/BA-scriptie/blob/master/Text_analytics.ipynb>

    :param X_train: the training set of users as a numpy array, containing a tuple with tokenized tweets and tokenized
    sentences from tweets for each user.
    :param X_test:  the test set of users as a numpy array, containing a tuple with tokenized tweets and tokenized
    sentences from tweets for each user.
    :param y_train: the training set of labels as a numpy array.
    :param y_test: the test set of labels as a numpy array.
    :return: the labels predicted by the classifier as a list.
    """

    # Choose label for majority baseline (at random, equal class sizes)
    # TODO: re-evaluate
    majority_label = np.random.choice([0, 1], 1, p=[0.5, 0.5])
    majority_prediction = [majority_label for label in y_test]

    print("(Re)vectorization of data…")
    vectorizer = DictVectorizer()
    classifier = LogisticRegression()

    # Extract features to feature dictionaries
    if not prefeaturized:
        featurizer = Featurizer(word_ngrams=ngrams, feature_set=featureset, binary=True)
        X_train_dict = featurizer.fit_transform(X_train)
        X_test_dict = featurizer.transform(X_test)

        # Convert dicts to internal representation of sklearn
        X_train = vectorizer.fit_transform(X_train_dict)
        X_test = vectorizer.transform(X_test_dict)

    else:
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)

    print("Training model…")
    classifier.fit(X_train, y_train)

    print("Predicting…\n")
    y_predicted = classifier.predict(X_test)

    # Print a result of the classification run
    print("=== RESULTS ===\n- Accuracy: {}\n- Majority baseline: {}\n- Most predictive features:\n"
          .format(accuracy_score(y_test, y_predicted),
                  accuracy_score(y_test, majority_prediction))
          )

    # Printing most informative features and confusion matrix
    print(classification_report(y_test, y_predicted, [0, 1], ["low", "high"]))
    show_most_informative_features(vectorizer, classifier)
    cnf_matrix = confusion_matrix(y_test, y_predicted)
    print("\n- Confusion matrix:")
    for line in cnf_matrix:
        print("\t" + str(line))
    return y_predicted.tolist()


def load_user_data(userfile="../supportdata/output_files/sentenced_tokenized_users.pickle"):

    """
    Loads user data from dictionary with pretokenized user information.

    Partly based on an example by B. Plank <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>

    :param userfile: A pickled dictionary containing:
        -   Two income classes as keys: "low" and "high"
        -   Tokenized tweets and sentence splitted tokenized tweets for user in that class as value
    :return: a shuffled list of tuples, containing the user data and the labels.
    """

    # Load income classes from dict
    with open(userfile, "rb") as inputfile:
        userdata = pickle.load(inputfile)

    high_income_users = userdata["high"]
    low_income_users = userdata["low"]

    # Assign users for each class their respective label
    high_labels = [1 for user in high_income_users]
    low_labels = [0 for user in low_income_users]

    # Combine the data and labels for each class into two lists containing all users and labels
    users = np.concatenate([high_income_users, low_income_users], axis=0)
    labels = np.concatenate([high_labels, low_labels], axis=0)

    # Assure that there is a label for every user
    assert (len(users) == len(labels))

    # Combine user and label in a list of tuples
    data = list(zip(users, labels))

    # Shuffle the data to ensure we get a good representative sample each time
    # To make our shuffling reproducible, we set a seed number
    random.seed(42)
    random.shuffle(data)

    # Return the shuffled list of users with their respective labels
    return data


def show_most_informative_features(vectorizer, clf, n=5):
    """
    Prints the most informative features for each class included in the classification to screen.

    Method provided by B. Plank <https://github.com/bplank/BA-scriptie/blob/master/Combining_features.ipynb>

    :param vectorizer: an sklearn vectorizer object.
    :param clf: an sklearn classifier object.
    :param n: the amount of features to be printed as Int.
    :return: None
    """

    feature_names = vectorizer.get_feature_names()
    for i in range(0, len(clf.coef_)):
        coefs_with_fns = sorted(zip(clf.coef_[i], feature_names))
        top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
        print("\tClass", i)
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))


def kfold_validate(k=1, feature_set=("ngrams", "surface", "readability"), ngrams="1-2", prefeaturized=False,
                   ignored_features=[], userfile="../supportdata/output_files/prefeaturized_users.pickle"):
    """
    Performs a k-fold validation of the classifier and prints the outcomes to screen.

    :param k: number of validations as Int (default: 1).
    :return: None
    """

    # Using 42 as seed to ensure reproducible results
    # 42? "Answer to the Ultimate Question of Life, The Universe, and Everything" (The Hitchhiker's Guide to the Galaxy)
    seed = 42

    print("===== CLASSIFIER START =====")

    print("Loading data…")
    if prefeaturized:
        data = load_user_data(userfile=userfile)
    else:
        data = load_user_data()

    print("- Total # of instances:", len(data))

    # Unpack user data into users and labels for further use
    users = np.array([users for users, label in data])
    labels = np.array([label for sentence, label in data])

    if k == 1:
        # In case of a single run, split the dataset manually at 75% training, 25% test
        print("Splitting data…")
        split_point = int(0.75 * len(data))
        X_train, X_test = users[:split_point], users[split_point:]
        y_train, y_test = labels[:split_point], labels[split_point:]

        # Check that our train and test instances have both data and labels
        assert (len(X_train) == len(y_train))
        assert (len(X_test) == len(y_test))
        print("- # of train instances: {}\n- # of test instances: {}".format(len(X_train), len(X_test)))

        # Perform the classification task with the split data
        perform_classification(X_train, X_test, y_train, y_test, featureset=feature_set, ngrams=ngrams,
                               prefeaturized=prefeaturized)

    else:
        y_test_total, y_predicted_total = [], []

        # In case of multiple runs, calculate the needed data splits according to the number of runs requested (= k)
        print("Calculating {}-fold splits…".format(k))
        kf = KFold(n_splits=k, random_state=seed)

        # For each generated split, create the requested data split and perform the classification task
        run = 1
        for train, test in kf.split(users):

            print("\n===== RUN {} OF {} =====".format(run, k))
            print("Splitting data…")
            X_train, X_test, y_train, y_test = users[train], users[test], labels[train], labels[test]
            print("- # of train instances: {}\n- # of test instances: {}".format(len(X_train), len(X_test)))

            # Save the input and output labels of each classifier run
            y_test_total = y_test_total + y_test.tolist()
            y_predicted_total = y_predicted_total + perform_classification(X_train, X_test, y_train, y_test,
                                                                           featureset=feature_set, ngrams=ngrams,
                                                                           prefeaturized=prefeaturized)
            run += 1

        print("\n===== FINAL RESULTS =====")
        # Report the results of our k-fold validation
        report = classification_report(y_test_total, y_predicted_total, [0, 1], ["low", "high"])
        print(report)
        return report

    print("\n===== CLASSIFIER END =====")

def strat_kfold_validate(k=1, feature_set=("ngrams", "surface", "readability"), ngrams="1-2", prefeaturized=False,
                   ignored_features=[], userfile="../supportdata/output_files/prefeaturized_users.pickle"):
    """
    Performs a k-fold validation of the classifier and prints the outcomes to screen.

    :param k: number of validations as Int (default: 1).
    :return: None
    """

    # Using 42 as seed to ensure reproducible results
    # 42? "Answer to the Ultimate Question of Life, The Universe, and Everything" (The Hitchhiker's Guide to the Galaxy)
    seed = 42

    print("===== CLASSIFIER START =====")

    print("Loading data…")
    if prefeaturized:
        data = load_user_data(userfile=userfile)
    else:
        data = load_user_data()

    print("- Total # of instances:", len(data))

    # Unpack user data into users and labels for further use
    users = np.array([users for users, label in data])
    labels = np.array([label for sentence, label in data])

    if k == 1:
        # In case of a single run, split the dataset manually at 75% training, 25% test
        print("Splitting data…")
        split_point = int(0.75 * len(data))
        X_train, X_test = users[:split_point], users[split_point:]
        y_train, y_test = labels[:split_point], labels[split_point:]

        # Check that our train and test instances have both data and labels
        assert (len(X_train) == len(y_train))
        assert (len(X_test) == len(y_test))
        print("- # of train instances: {}\n- # of test instances: {}".format(len(X_train), len(X_test)))

        # Perform the classification task with the split data
        perform_classification(X_train, X_test, y_train, y_test, featureset=feature_set, ngrams=ngrams,
                               prefeaturized=prefeaturized)

    else:
        y_test_total, y_predicted_total = [], []

        # In case of multiple runs, calculate the needed data splits according to the number of runs requested (= k)
        print("Calculating {}-fold splits…".format(k))
        kf = StratifiedKFold(n_splits=k, random_state=seed)

        # For each generated split, create the requested data split and perform the classification task
        run = 1
        for train, test in kf.split(users, labels):

            print("\n===== RUN {} OF {} =====".format(run, k))
            print("Splitting data…")
            X_train, X_test, y_train, y_test = users[train], users[test], labels[train], labels[test]
            print("- # of train instances: {}\n- # of test instances: {}".format(len(X_train), len(X_test)))

            # Save the input and output labels of each classifier run
            y_test_total = y_test_total + y_test.tolist()
            y_predicted_total = y_predicted_total + perform_classification(X_train, X_test, y_train, y_test,
                                                                           featureset=feature_set, ngrams=ngrams,
                                                                           prefeaturized=prefeaturized)
            run += 1

        print("\n===== FINAL RESULTS =====")
        # Report the results of our k-fold validation
        report = classification_report(y_test_total, y_predicted_total, [0, 1], ["low", "high"])
        print(report)
        return report

    print("\n===== CLASSIFIER END =====")


if __name__ == '__main__':
    kfold_validate(k=1, prefeaturized=True)
