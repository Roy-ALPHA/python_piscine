#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0}

    max_power = max(mages, key=lambda mage: mage["power"])
    min_power = min(mages, key=lambda mage: mage["power"])
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power["power"],
        "min_power": min_power["power"],
        "avg_power": avg_power
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    crystal = {
        "name": "Crystal Orb", "power": 85, "type": "artifact"
    }

    fire = {
        "name": "Fire Staff", "power": 92, "type": "artifact"
    }
    power_sort = artifact_sorter([crystal, fire])
    print(
        f'{power_sort[0]["name"]} ({power_sort[0]["power"]} power) comes'
        f' before {power_sort[1]["name"]} ({power_sort[1]["power"]} power)'
    )

    print("\nTesting spell transformer...")
    spl_trans = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(spl_trans))


if __name__ == "__main__":
    main()
