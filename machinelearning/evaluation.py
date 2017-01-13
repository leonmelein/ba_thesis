#!/usr/bin/python
from machinelearning import classifier


def main():
    reports = []

    # 2: Surface
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 16 S
                                                   userfile="../supportdata/output_files/prefeaturized_users_12.pickle"))

    # 3: Readability
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 24 R
                                                   userfile="../supportdata/output_files/prefeaturized_users_8.pickle"))

    # 4: N-grams (n=1)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 31 1
                                                   userfile="../supportdata/output_files/prefeaturized_users_15.pickle"))

    # 5: N-grams (n=2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 30 2
                                                   userfile="../supportdata/output_files/prefeaturized_users_28.pickle"))

    # 6: N-grams (n=3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 29 3
                                                   userfile="../supportdata/output_files/prefeaturized_users_30.pickle"))

    # 7: N-grams (n=1-2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 28 1+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_14.pickle"))

    # 8: N-grams (n=1-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 27 1+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_31.pickle"))

    # 9: N-grams (n=2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 26 2+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_29.pickle"))

    # 10: N-grams (n=1-2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 25 1+2+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_13.pickle"))

    # 11: Surface + Readability
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 8 S+R
                                                   userfile="../supportdata/output_files/prefeaturized_users_4.pickle"))

    # 12: Surface + N-grams (n=1)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 15 S+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_11.pickle"))

    # 13: Surface + N-grams (n=2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 14 S+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_20.pickle"))

    # 14: Surface + N-grams (n=3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 13 S+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_22.pickle"))

    # 15: Readability + N-grams (n=1)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 23 R+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_7.pickle"))

    # 16: Readability + N-grams (n=2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 22 R+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_16.pickle"))

    # 17: Readability + N-grams (n=3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 21 R+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_18.pickle"))

    # 18: Surface + N-grams (n=1-2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 12 S+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_10.pickle"))

    # 19: Surface + N-grams (n=1-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 11 S+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_23.pickle"))

    # 20: Surface + N-grams (n=2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 10 S+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_21.pickle"))

    # 21: Surface + N-grams (n=1-2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 9 S+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_9.pickle"))

    # 22: Readability + N-grams (n=1-2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 20 R+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_6.pickle"))

    # 23: Readability + N-grams (n=1-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 3 S+R+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_27.pickle"))

    # 24: Readability + N-grams (n=2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 2 S+R+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_25.pickle"))

    # 25: Readability + N-grams (n=1-2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1 S+R+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_1.pickle"))

    # 26: Surface + Readability + N-grams (n=1)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 7 S+R+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_3.pickle"))

    # 27: Surface + Readability + N-grams (n=2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 6 S+R+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_24.pickle"))

    # 28: Surface + Readability + N-grams (n=3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 5 S+R+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_26.pickle"))

    # 29: Surface + Readability + N-grams (n=1-2)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 4 S+R+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_2.pickle"))

    # 30: Surface + Readability + N-grams (n=1-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 19 R+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_19.pickle"))

    # 31: Surface + Readability + N-grams (n=2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 18 R+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_17.pickle"))

    # 32: Surface + Readability + N-grams (n=1-2-3)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 17 R+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_5.pickle"))

    print("\n=================================\n\n")
    i = 1
    for report in reports:
        print("Test", i)
        print(report)
        i += 1

if __name__ == '__main__':
    main()
