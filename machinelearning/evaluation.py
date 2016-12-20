#!/usr/bin/python
#   Evaluation - Léon Melein, s2580861
#   Running evaluation scenarios with classifier
from machinelearning import classifier
ngrams, surface, readability = "ngrams", "surface", "readability"
unigram, bigram, trigram = "1", "1-2", "1-2-3"

ngrams_list = ["3W:", "2W:", "1W:"]
surface_list = ["S_5CH", "S_TLW", "S_TLCH", "S_RWL", "S_TTR"]
readability_list = ["R_ARI", "R_COL", "R_FRE", "R_GUN", "R_KIN", "R_LIX", "R_SMOG"]


def main():
    reports = []

    ## STRATKFOLD ##
    ################
    # Surface + Readability (1-4)
    print("S+R+N")
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1 S+R+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_1.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 2 S+R+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_25.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 3 S+R+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_27.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 4 S+R+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_2.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 5 S+R+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_26.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 6 S+R+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_24.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 7 S+R+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_3.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 8 S+R
                                                   userfile="../supportdata/output_files/prefeaturized_users_4.pickle"))
    print("S+N")
    # Surface (9-12)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_9.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_21.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_23.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_10.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_22.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_20.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_11.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # S
                                                   userfile="../supportdata/output_files/prefeaturized_users_12.pickle"))

    print("R+N")
    # Readability (5-8)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+1-2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_5.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+2-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_17.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+1-3
                                                   userfile="../supportdata/output_files/prefeaturized_users_19.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+1-2
                                                   userfile="../supportdata/output_files/prefeaturized_users_6.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_18.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_16.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R+1
                                                   userfile="../supportdata/output_files/prefeaturized_users_7.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # R
                                                   userfile="../supportdata/output_files/prefeaturized_users_8.pickle"))

    print("N")
    # NGrams (13-15)
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1+2+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_13.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 2+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_29.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1+3
                                                   userfile="../supportdata/output_files/prefeaturized_users_31.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1+2
                                                   userfile="../supportdata/output_files/prefeaturized_users_14.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 3
                                                   userfile="../supportdata/output_files/prefeaturized_users_30.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 2
                                                   userfile="../supportdata/output_files/prefeaturized_users_28.pickle"))
    reports.append(classifier.strat_kfold_validate(k=10, prefeaturized=True,  # 1
                                                   userfile="../supportdata/output_files/prefeaturized_users_15.pickle"))


    print("\n=================================\n\n")
    i = 1
    for report in reports:
        print("Test", i)
        print(report)
        i += 1

if __name__ == '__main__':
    main()
