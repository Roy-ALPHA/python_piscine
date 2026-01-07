#!/usr/bin/env python3
def tracker_system():
    print("== Achievement Tracker System ===\n")
    players = {
    "alice": {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
    "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
    "charlie": {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    }
    for player in players:
        print(f"Player {player} achievements: {players[player]}")
    return players
players = tracker_system()
print("=== Achievement Analytics ===\n")
unique_ach = set()
for player in players:
    unique_ach = unique_ach.union(players[player])
print(f"All unique achievements: {unique_ach}")
print(f"Total unique achievements: {len(unique_ach)}\n")
for player in players:
    common = set(players[player])
    break
for player in players[1:]:
    common = common.intersection(players[player])
print(f"Common to all players: {common}")
# print(f"Rare achievements (1 player): {dif}\n")