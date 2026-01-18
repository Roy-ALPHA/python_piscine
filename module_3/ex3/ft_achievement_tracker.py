#!/usr/bin/env python3
print("== Achievement Tracker System ===\n")
alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
           'perfectionist'}
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}\n")

print("=== Achievement Analytics ===")
print(f"All unique achievements: {alice.union(bob, charlie)}")
print(f"Total unique achievements: {len(alice.union(bob, charlie))}\n")
print(f"Common to all players: {alice.intersection(bob, charlie)}")
rare = charlie.difference(bob | alice) | bob.difference(charlie | alice)
print(f"Rare achievements (1 player): {rare}\n")
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
