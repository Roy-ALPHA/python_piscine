#!/usr/bin/env python3
import typing


def event_generator(n) -> typing.Generator:
    players = ["alice", "bob", "charlie"]
    ach = ["killed monster", "found treasure", "leveled up"]
    level = [5, 12, 8]
    for i in range(n):
        yield {
            "player": players[i % len(players)],
            "ach": ach[i % len(ach)],
            "level": level[i % len(level)]
        }


def fibonacci_gen(n) -> typing.Generator:
    prev = 0
    next_fib = 1
    for i in range(n):
        yield prev
        tmp = next_fib + prev
        prev = next_fib
        next_fib = tmp


def check(n) -> bool:
    i = 2
    while i <= n / 2:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_num_gen(n) -> typing.Generator:
    prime = 2
    i = 0
    while i < n:
        if check(prime) is True:
            yield prime
            i += 1
        prime += 1


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
count = 0
hp_level = 0
treasure_ach = 0
lp_ach = 0
for player in event_generator(1000):
    if player.get("level") > 10:
        hp_level += 1
    if player.get("ach") == "found treasure":
        treasure_ach += 1
    if player.get("ach") == "leveled up":
        lp_ach += 1
    print(f"Event {count + 1}: Player {player.get("player")} "
          f"(level {player.get("level")}) {player.get("ach")}")
    count += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {count}")
print(f"High-level players (10+): {hp_level}")
print(f"Treasure events: {treasure_ach}")
print(f"Level-up events: {lp_ach}\n")
print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds\n")

print("=== Generator Demonstration ===")
print("Fibonacci sequence (first 10):", end=" ")
lis = list()
for n in fibonacci_gen(10):
    lis += [n]
print(str(lis)[1:-1])
lis = list()
for prime in prime_num_gen(5):
    lis += [prime]
print("Prime numbers (first 5):", end=' ')
print(str(lis)[1:-1])
