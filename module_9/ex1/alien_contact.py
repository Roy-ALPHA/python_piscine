from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate(self: "AlienContact") -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (not self.is_verified and
           self.contact_type == ContactType.PHYSICAL):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a received message"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-03-03T05:52:00",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received='Greetings from Zeta Reticuli',
        is_verified=True
    )

    print(
        f"ID: {valid_contact.contact_id}",
        f"Type: {valid_contact.contact_type.value}",
        f"Location: {valid_contact.location}",
        f"Signal: {valid_contact.signal_strength}/10",
        f"Duration: {valid_contact.duration_minutes} minutes",
        f"Witnesses: {valid_contact.witness_count}",
        f"Message: '{valid_contact.message_received}'", sep="\n"
    )

    print("\n======================================")
    print("Expected validation error:")
    try:
        _ = AlienContact(
            is_verified=True,
            contact_id="AC_2024_001",
            timestamp="2026-03-03T05:52:00",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli'
        )
    except ValidationError as e:
        print(e.errors()[0].get("ctx").get("error"))


if __name__ == "__main__":
    main()
