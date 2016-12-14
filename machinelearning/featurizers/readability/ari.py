#!/usr/bin/python
import readability

def main():
    high_income_users = open("../../../data/income.high").readlines()
    print(high_income_users[0].split(" . "))

    # for user in high_income_users:
    #     print(user)
    #     #print(readability.getmeasures(user, lang="nl", merge=True))

if __name__ == '__main__':
    main()
