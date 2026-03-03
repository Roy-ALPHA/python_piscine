from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validator(self: "SpaceMission") -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        ranks = [c.rank for c in self.crew]
        if Rank.COMMANDER not in ranks and Rank.CAPTAIN not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        experienced = [
            c for c in self.crew if c.years_experience >= 5
        ]
        exp = len(experienced) / len(self.crew) * 100 < 50
        print(experienced)
        if self.duration_days > 365 and exp:
            raise ValueError(
                "Long missions require at least 50% experienced crew"
            )
        deactive = [1 for c in self.crew if not c.is_active]
        if deactive:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    crew = [
        CrewMember(
            member_id="1234_GOGO",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=25,
            specialization="Mission Command",
            years_experience=2,
        ),
        CrewMember(
            member_id="1543_GOGO",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=45,
            specialization="Navigation",
            years_experience=22,
        ),
        CrewMember(
            member_id="6543_GOGO",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=30,
            specialization="Engineering",
            years_experience=10,
        )
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-03-04T12:43:00",
        duration_days=900,
        crew=crew,
        budget_millions=2500.0
    )

    print(
        f"Mission: {mission.mission_name}",
        f"ID: {mission.mission_id}",
        f"Destination: {mission.destination}",
        f"Duration: {mission.duration_days} days",
        f"Budget: ${mission.budget_millions}M",
        f"Crew size: {len(mission.crew)}",
        "Crew members: ", sep="\n"
    )

    for c in mission.crew:
        print(f"- {c.name} ({c.rank.value}) - {c.specialization}")

    print("\n=========================================")
    print("Expected validation error:")
    crew[0].rank = Rank.LIEUTENANT
    try:
        _ = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-03-04T12:43:00",
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0].get("ctx").get("error"))


if __name__ == "__main__":
    main()
