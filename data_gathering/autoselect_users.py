import pickle
import numpy


def main(users):
    autoselected_users = {}
    numpy.random.seed(42)   # Real random number?

    for key in users.keys():
        print(key)
        flattened_values = []
        values = users[key]
        for value in values:
            flattened_values.append(int(value[0]))

        random_chosen = numpy.random.choice(flattened_values, 1500, replace=False)
        autoselected_users[key] = random_chosen.tolist()

    with open('output_files/autoselected_users_CLEAN.pickle', 'wb+') as outputfile:
        pickle.dump(autoselected_users, outputfile)

with open('output_files/divided_user_class_income_CLEAN.pickle', 'rb') as inputfile:
    userdict = pickle.load(inputfile)
    main(userdict)
