#!/usr/bin/env python3
import sys


def args_to_list(args):
    lis = []
    i = 1
    try:
        while i < len(args):
            lis += [int(args[i])]
            i += 1
    except ValueError:
        return False
    return lis


print("=== Player Score Analytics ===")
scores = args_to_list(sys.argv)
if len(sys.argv) > 1 and scores is not False:
    print(f"Scores processed:  {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
elif scores is False:
    print("Invalid score detected")
    print("Scores must be integers")
else:
    print(
        "No scores provided. Usage: python3 "
        "ft_score_analytics.py <score1> <score2> ...")
