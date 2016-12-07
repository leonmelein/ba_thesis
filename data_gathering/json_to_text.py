import json
import os

def main():
    os.chdir("corpus")
    labels = [name for name in os.listdir(".") if os.path.isdir(name)]
    print(labels)

    for label in labels:
        print(label)
        search_directory = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/corpus/" + label)
        write_directory = os.path.expanduser("~/Desktop/Thesis/ba_thesis/data_gathering/corpus_txt/" + label)
        if not os.path.exists(write_directory):
            os.makedirs(write_directory)

        # files = [name for name in os.listdir(".") if os.path.isfile(name)]
        # print(files)
        # for file in files:
        os.chdir(search_directory)
        print([name for name in os.listdir(".")])
        for name in os.listdir("."):
            os.chdir(search_directory)
            print(os.getcwd())
            if name[-4:] == "json":
                with(open(name, 'r')) as inputfile:
                    userfile = json.load(inputfile)

                os.chdir(write_directory)
                with open("{}.txt".format(name[:-5]), 'w+') as file_handler:
                    for tweet in userfile:
                        file_handler.write(tweet['text'].replace("\n", " ") + "\n")

if __name__ == '__main__':
    main()