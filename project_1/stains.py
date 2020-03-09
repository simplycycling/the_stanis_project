#!/usr/bin/env python3

import os

from collections import Counter


# So keys are usernames, values are names. Note that commas inside the name get replaced by a single space.
# If it’s a service account, strip off svc_, replace any underscores with spaces.
def get_users():
    usernames = {}
    handle = open("project_1/passwd", "r")
    handle_lines = handle.readlines()

    for lines in handle_lines:
        remove_svc = lines.replace("svc_", "")
        remove_underscores = remove_svc.replace("_", " ")
        cleanup = remove_underscores.strip().split(":")
        user = cleanup[0]
        shells = os.path.basename(cleanup[6])
        usernames[user] = shells

    handle.close()
    return usernames


# return how many users use each shell. Write your stats to shell.stats
def get_shell_stats():
    all_users = get_users()
    handle = open("shell.stats", "w")
    get_count = Counter(all_users.values())
    for key, c in get_count.most_common():
        print("{}: {}".format(key, c), file=handle)
        print("{}: {}".format(key, c))
    handle.close()


if __name__ == '__main__':
    get_users()
    get_shell_stats()
