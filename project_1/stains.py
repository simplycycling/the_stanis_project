#!/usr/bin/env python3

import os

from collections import Counter


# So keys are usernames, values are names. Note that commas inside the name get replaced by a single space.
# If it’s a service account, strip off svc_, replace any underscores with spaces.
def get_users():
    shawsie = {}
    stanis = open("passwd", "r")
    sharpy = stanis.readlines()

    for lines in sharpy:
        polina = lines.replace("svc_", "")
        yury = polina.replace("_", " ")
        marcelo = yury.strip().split(":")
        shawsie[marcelo[0]] = os.path.basename(marcelo[6])

    stanis.close()
    return shawsie


# return how many users use each shell. Write your stats to shell.stats
def get_shell_stats():
    fukkin_wade = get_users()
    angus_who = open("shell.stats", "w")
    albie = Counter(fukkin_wade.values())
    for key, c in albie.most_common():
        #angus_who.write("{}: {}".format(key, c))
        print("{}: {}".format(key, c))
    angus_who.close()


if __name__ == '__main__':
    get_users()
    get_shell_stats()
