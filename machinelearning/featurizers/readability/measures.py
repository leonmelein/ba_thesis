#!/usr/bin/python
#   Readability measures - Léon Melein, s2580861
#   Generates a number of popular readability measures for a given user's tweets
#   Relies on the readability library <https://pypi.python.org/pypi/readability> for measure calculation

import readability


def generate(text, debug=False):
    """
    Generates the following readability scores for a user's tweets:

    -   Automated Readability Index (R_ARI)
    -   Coleman-Liau Index          (R_COL)
    -   Flesch Reading Ease         (R_FRE)
    -   Gunning-Fog Index           (R_GUN)
    -   Kincaid Grade Level         (R_KIN)
    -   LIX                         (R_LIX)
    -   SMOG Grade                  (R_SMOG)

    :param text: a String containing all tokenized sentences of a user, divided by newline characters (\n).
    :param debug: a Bool indicating if debugging information should be printed (default: False).
    :return: a Dict containing the feature names as keys and calculated lengths as values.
    """

    measures = readability.getmeasures(text, lang='nl', merge=True)
    if debug:
        for key, value in measures.items():
            print(key, ": ", value)

    return {"R_ARI": measures["ARI"],
            "R_COL": measures["Coleman-Liau"],
            "R_FRE": measures["FleschReadingEase"],
            "R_GUN": measures["GunningFogIndex"],
            "R_KIN": measures["Kincaid"],
            "R_LIX": measures["LIX"],
            "R_SMOG": measures["SMOGIndex"]}