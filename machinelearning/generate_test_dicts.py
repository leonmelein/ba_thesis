#!/usr/bin/python
#   generate_test_dicts.py - Léon Melein, s2580861
#   <DESCRIPTION>
from machinelearning import prefeaturizer


def main():
    print("All...")
    prefeaturizer.main(filename="1", ngrams="1-2-3", feature_set=("ngrams", "surface", "readability"))
    prefeaturizer.main(filename="2", ngrams="1-2", feature_set=("ngrams", "surface", "readability"))
    prefeaturizer.main(filename="3", ngrams="1", feature_set=("ngrams", "surface", "readability"))
    prefeaturizer.main(filename="4", feature_set=("surface", "readability"))

    print("Readability...")
    prefeaturizer.main(filename="5", ngrams="1-2-3", feature_set=("ngrams", "readability"))
    prefeaturizer.main(filename="6", ngrams="1-2", feature_set=("ngrams", "readability"))
    prefeaturizer.main(filename="7", ngrams="1", feature_set=("ngrams", "readability"))
    prefeaturizer.main(filename="8", feature_set=("readability"))

    print("Surface...")
    prefeaturizer.main(filename="9", ngrams="1-2-3", feature_set=("ngrams", "surface"))
    prefeaturizer.main(filename="10", ngrams="1-2", feature_set=("ngrams", "surface"))
    prefeaturizer.main(filename="11", ngrams="1", feature_set=("ngrams", "surface"))
    prefeaturizer.main(filename="12", feature_set=("surface"))

    print("NGrams...")
    prefeaturizer.main(filename="13", ngrams="1-2-3", feature_set=("ngrams"))
    prefeaturizer.main(filename="14", ngrams="1-2", feature_set=("ngrams"))
    prefeaturizer.main(filename="15", ngrams="1", feature_set=("ngrams"))

    print("Done!")

if __name__ == '__main__':
    main()
