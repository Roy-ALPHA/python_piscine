#!/usr/bin/env python3
print("=== Game Analytics Dashboard ===\n")
players = {
    'alice': {'level': 41, 'total_score': 2824,
              'active_regions': ["north", "south", "east"],
              'favorite_mode': 'ranked', 'achievements_count': 5,
              "online": False},
    'bob': {'level': 16, 'total_score': 4657,
            'active_regions': ["north", "west", "central"],
            'favorite_mode': 'ranked', 'achievements_count': 2,
            "online": True},
    'charlie': {'level': 44, 'total_score': 9935,
                'active_regions': ["west", "south", "north"],
                'favorite_mode': 'ranked', 'achievements_count': 7,
                "online": False},
    'diana': {'level': 3, 'total_score': 1488,
              'active_regions': ["west", "east"],
              'favorite_mode': 'casual', 'achievements_count': 4,
              "online": True},
    'eve': {'level': 33, 'total_score': 1488,
            'active_regions': ["central", "north"],
            'favorite_mode': 'casual', 'achievements_count': 7,
            "online": False},
    'frank': {'level': 15, 'total_score': 8359,
              'active_regions': ["south", "east", "west"],
              'favorite_mode': 'competitive', 'achievements_count': 1,
              "online": True}
    }
print("=== List Comprehension Examples ===")
print(
    "High scorers (>2000): "
    f"{[
        player
        for player in players
        if players.get(player).get("total_score") > 2000]}"
)
print(
    f"Scores doubled: "
    f"{[players.get(player).get("total_score") * 2 for player in players]}"
)
print(
    "Active players: "
    f"{[player for player in players if players.get(player).get("online")]}\n"
)
print("=== Dict Comprehension Examples ===\n")
tmp = {player: players.get(player).get("total_score") for player in players}
print(f"Player scores: {tmp}")
tmp = {"high": sum(1 for player in tmp if tmp.get(player) > 2000)}
tmp.update({"medium": sum(
    1 for player in tmp if 1500 < tmp.get(player) < 2000)})
tmp.update({"low": sum(1 for player in tmp if tmp.get(player) < 1500)})
print(f"Score categories: {tmp}")
tmp = {
    player: players.get(player).get("achievements_count")
    for player in players
    }
print(f'Achievement counts: {tmp}\n')
print("=== Set Comprehension Examples ===")
print(f"Unique players: {set(player for player in players)}")
print(f"Unique modes: {set(
                            players.get(player).get("favorite_mode")
                            for player in players)}")
tmp = set()
tmp = {
        region
        for player in players
        for region in players.get(player).get("active_regions")
        }
print(f"Active regions: {tmp}\n")
print("=== Combined Analysis ===")
print(f"Total players: {len([player for player in players])}")
tmp = len(set([players.get(player).get("favorite_mode")for player in players]))
print(f"Total unique modes: {tmp}")
tmp = sum([players.get(player).get("total_score") for player in players]) / tmp
print(f"Average score: {tmp:.1f}")
tmp = [players.get(player).get("total_score") for player in players]
achiv = {
         player: players.get(player).get('achievements_count')
         for player in players
         if players.get(player).get('total_score') == max(tmp)}
print(f"Top performer: {str(list(achiv.keys()))[2:-2]} ({max(tmp)} "
      f"points, {str(list(achiv.values()))[1:-1]} achievements)")
