# Based on example given by Barbara in class
# TODO: learn from, use and rewrite
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
from numpy.random import choice
import random
import pickle

from sklearn.model_selection import KFold

from machinelearning.featurizers.featurizer import Featurizer


def perform_classification(X_train, X_test, y_train, y_test):

    # Choose label for majority baseline (at random, equal class sizes)
    # TODO: re-evaluate
    majority_label = choice([0, 1], 1, p=[0.5, 0.5])
    majority_prediction = [majority_label for label in y_test]

    print("Vectorization of data…")
    vectorizer = DictVectorizer()
    featurizer = Featurizer(word_ngrams="1-2", binary=True)
    classifier = LogisticRegression()

    # first extract the features (as dictionaries)
    X_train_dict = featurizer.fit_transform(X_train)
    X_test_dict = featurizer.transform(X_test)

    # then convert them to the internal representation (maps each feature to an id)
    X_train = vectorizer.fit_transform(X_train_dict)
    X_test = vectorizer.transform(X_test_dict)

    print("Training model…")
    classifier.fit(X_train, y_train)

    print("Predicting…\n")
    y_predicted = classifier.predict(X_test)

    print("=== RESULTS ===\n- Accuracy: {}\n- Majority baseline: {}\n- Most predictive features:\n"
          .format(accuracy_score(y_test, y_predicted),
                  accuracy_score(y_test, majority_prediction)))

    # Printing most informative features and confusion matrix
    print(classification_report(y_test, y_predicted, [0,1], ["low", "high"]))
    show_most_informative_features(vectorizer, classifier)
    cnf_matrix = confusion_matrix(y_test, y_predicted)
    print("\n- Confusion matrix:")
    for line in cnf_matrix:
        print("\t" + str(line))
    print("\n===== CLASSIFIER END =====")
    return y_predicted.tolist()

    # you can access the vectorizer (feature to feature number mapping) this way
    # print(vectorizer.vocabulary_.get('the'))


def load_user_data(userfile="../supportdata/output_files/sentenced_tokenized_users.pickle"):
    """
    Loads user data from pretokenized dict.
    """
    with open(userfile, "rb") as inputfile:
        userdata = pickle.load(inputfile)

    high_income_users = userdata["high"]
    low_income_users = userdata["low"]

    high_labels = [1 for user in high_income_users]
    low_labels = [0 for user in low_income_users]

    users = np.concatenate([high_income_users, low_income_users], axis=0)
    labels = np.concatenate([high_labels, low_labels], axis=0)

    # make sure we have a label for every data instance
    assert (len(users) == len(labels))

    data = list(zip(users, labels))

    # Use a seed number to ensure reproducibility
    random.seed(42)
    random.shuffle(data)

    # return the data (instances + labels)
    return data


def show_most_informative_features(vectorizer, clf, n=5):
    feature_names = vectorizer.get_feature_names()
    for i in range(0, len(clf.coef_)):
        coefs_with_fns = sorted(zip(clf.coef_[i], feature_names))
        top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
        print("\tClass", i)
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))


def classify(method="single", k=10):
    print("===== CLASSIFIER START =====\n")
    print("Loading data…")
    data = load_user_data()
    print("- Total # of instances:", len(data))

    users = np.array([users for users, label in data])
    labels = np.array([label for sentence, label in data])

    if method == "single":

        print("\nSplitting data…")
        split_point = int(0.75 * len(data))
        X_train, X_test = users[:split_point], users[split_point:]
        y_train, y_test = labels[:split_point], labels[split_point:]

        # Check that our train and test instances have both data and labels
        assert (len(X_train) == len(y_train))
        assert (len(X_test) == len(y_test))

        print("- # of train instances: {}\n- # of test instances: {}\n".format(len(X_train), len(X_test)))
        assert (len(X_train) == len(y_train))
        assert (len(X_test) == len(y_test))

        perform_classification(X_train, X_test, y_train, y_test)

    else:
        y_test_total, y_predicted_total = [], []
        kf = KFold(n_splits=k)
        for train, test in kf.split(users):
            X_train, X_test, y_train, y_test = users[train], users[test], labels[train], labels[test]
            print(type(y_test_total), type(y_test))
            y_test_total = y_test_total + y_test.tolist()
            y_predicted_total = y_predicted_total + perform_classification(X_train, X_test, y_train, y_test)

        print(classification_report(y_test_total, y_predicted_total, [0, 1], ["low", "high"]))


if __name__ == '__main__':
    classify("multi", 10)
    #perform_classification()
    #load_user_data()
