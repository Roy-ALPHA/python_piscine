#!/usr/bin/env python
class SecurePlant:
    """
    Represents a plant with security checks to prevent invalid data.

    This class ensures that plant attributes such as height and age
    cannot be set to negative values.
    """
    def is_valid(val: int) -> bool:
        """
        Check if a given value is valid (non-negative).

        Args:
            val (int): The value to validate.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        if val < 0:
            return False
        else:
            return True

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            int: The plant height in centimeters.
        """
        return self.height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            int: The plant age in days.
        """
        return self.age

    def set_age(self, age: int) -> None:
        """
        Set the age of the plant after validation.

        Args:
            age (int): The new age value in days.
        """
        if SecurePlant.is_valid(age) is True:
            self.age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height: int) -> None:
        """
        Set the height of the plant after validation.

        Args:
            height (int): The new height value in centimeters.
        """
        if SecurePlant.is_valid(height) is True:
            self.height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a SecurePlant instance with validation.

        Args:
            name (str): The name of the plant.
            height (int): Initial height in centimeters.
            age (int): Initial age in days.
        """
        self.name = name
        if SecurePlant.is_valid(height) is True:
            self.height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("Action taken: height set to 0")
            self.height = 0
        if SecurePlant.is_valid(age) is True:
            self.age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print("Action taken: age set to 0")
            self.age = 0
        print(f"Plant created: {self.name}")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 45, 9)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(
        f"Current plant: {rose.name} ({rose.get_height()}cm, "
        f"{rose.get_age()} days)"
        )
