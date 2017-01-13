#!/usr/bin/python
from machinelearning import prefeaturizer


def main():
    """
    Generates the neccesary dictionary files with all the different feature compositions for our evaluation script.

    :return: None
    """
    print("Generating...")
    # 2: Surface
    prefeaturizer.main(filename="12", feature_set=("surface"))

    # 3: Readability
    prefeaturizer.main(filename="8", feature_set=("readability"))

    # 4: N-grams (n=1)
    prefeaturizer.main(filename="15", ngrams="1", feature_set=("ngrams"))

    # 5: N-grams (n=2)
    prefeaturizer.main(filename="28", ngrams="2", feature_set=("ngrams"))

    # 6: N-grams (n=3)
    prefeaturizer.main(filename="30", ngrams="3", feature_set=("ngrams"))

    # 7: N-grams (n=1-2)
    prefeaturizer.main(filename="14", ngrams="1-2", feature_set=("ngrams"))

    # 8: N-grams (n=1-3)
    prefeaturizer.main(filename="31", ngrams="1-3", feature_set=("ngrams"))

    # 9: N-grams (n=2-3)
    prefeaturizer.main(filename="29", ngrams="2-3", feature_set=("ngrams"))

    # 10: N-grams (n=1-2-3)
    prefeaturizer.main(filename="13", ngrams="1-2-3", feature_set=("ngrams"))

    # 11: Surface + Readability
    prefeaturizer.main(filename="4", feature_set=("surface", "readability"))

    # 12: Surface + N-grams (n=1)
    prefeaturizer.main(filename="11", ngrams="1", feature_set=("ngrams", "surface"))

    # 13: Surface + N-grams (n=2)
    prefeaturizer.main(filename="20", ngrams="2", feature_set=("ngrams", "surface"))

    # 14: Surface + N-grams (n=3)
    prefeaturizer.main(filename="22", ngrams="3", feature_set=("ngrams", "surface"))

    # 15: Readability + N-grams (n=1)
    prefeaturizer.main(filename="7", ngrams="1", feature_set=("ngrams", "readability"))

    # 16: Readability + N-grams (n=2)
    prefeaturizer.main(filename="16", ngrams="2", feature_set=("ngrams", "readability"))

    # 17: Readability + N-grams (n=3)
    prefeaturizer.main(filename="18", ngrams="3", feature_set=("ngrams", "readability"))

    # 18: Surface + N-grams (n=1-2)
    prefeaturizer.main(filename="10", ngrams="1-2", feature_set=("ngrams", "surface"))

    # 19: Surface + N-grams (n=1-3)
    prefeaturizer.main(filename="23", ngrams="1-3", feature_set=("ngrams", "surface"))

    # 20: Surface + N-grams (n=2-3)
    prefeaturizer.main(filename="21", ngrams="2-3", feature_set=("ngrams", "surface"))

    # 21: Surface + N-grams (n=1-2-3)
    prefeaturizer.main(filename="9", ngrams="1-2-3", feature_set=("ngrams", "surface"))

    # 22: Readability + N-grams (n=1-2)
    prefeaturizer.main(filename="6", ngrams="1-2", feature_set=("ngrams", "readability"))

    # 23: Readability + N-grams (n=1-3)
    prefeaturizer.main(filename="19", ngrams="1-3", feature_set=("ngrams", "readability"))

    # 24: Readability + N-grams (n=2-3)
    prefeaturizer.main(filename="17", ngrams="2-3", feature_set=("ngrams", "readability"))

    # 25: Readability + N-grams (n=1-2-3)
    prefeaturizer.main(filename="5", ngrams="1-2-3", feature_set=("ngrams", "readability"))

    # 26: Surface + Readability + N-grams (n=1)
    prefeaturizer.main(filename="3", ngrams="1", feature_set=("ngrams", "surface", "readability"))

    # 27: Surface + Readability + N-grams (n=2)
    prefeaturizer.main(filename="24", ngrams="2", feature_set=("ngrams", "surface", "readability"))

    # 28: Surface + Readability + N-grams (n=3)
    prefeaturizer.main(filename="26", ngrams="3", feature_set=("ngrams", "surface", "readability"))

    # 29: Surface + Readability + N-grams (n=1-2)
    prefeaturizer.main(filename="2", ngrams="1-2", feature_set=("ngrams", "surface", "readability"))

    # 30: Surface + Readability + N-grams (n=1-3)
    prefeaturizer.main(filename="27", ngrams="1-3", feature_set=("ngrams", "surface", "readability"))

    # 31: Surface + Readability + N-grams (n=2-3)
    prefeaturizer.main(filename="25", ngrams="2-3", feature_set=("ngrams", "surface", "readability"))

    # 32: Surface + Readability + N-grams (n=1-2-3)
    prefeaturizer.main(filename="1", ngrams="1-2-3", feature_set=("ngrams", "surface", "readability"))

    print("Done!")

if __name__ == '__main__':
    main()
