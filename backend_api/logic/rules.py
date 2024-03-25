from enum import Enum

from django.core.exceptions import ValidationError


class Race:
    traits_choices = [
        "Versatile", "Extra Language", "Night Vision", "Keen Senses", "Darkvision", "Dwarven Resilience",
        "Dwarven Combat Training",
        "Tool Proficiency", "Fleet of Foot", "Lucky", "Brave", "Halfling Nimbleness", "Naturally Stealthy",
        "Artificer's Lore"]

    choices = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Elf", "Half-Orc", "Tiefling", "Dragonborn"]
    proficiencies_choices = ["Light Armor", "Medium Armor", "Heavy Armor", "Simple Weapons", "Martial Weapons",
                             "Shields", "Saving Throws", "Skills"]

    def __init__(self, name: str, traits: list[str], proficiencies: list[str]):
        if name.capitalize() not in self.choices:
            raise ValueError("Invalid race name")
        self.name = name

        for trait in traits:
            if trait not in self.traits_choices:
                raise ValueError("Invalid trait")

        self.traits = traits

        for proficiency in proficiencies:
            if proficiency not in self.proficiencies_choices:
                raise ValueError("Invalid proficiency")

        self.proficiencies = proficiencies


class DndClass:
    def __init__(self, name: str, features: list[str]):
        self.name = name
        self.features = features  # A list of class features


class Subclass(DndClass):
    def __init__(self, name: str, features: list[str], parent_class: DndClass):
        super().__init__(name, features)
        self.parent_class = parent_class


# Example races and classes
human = Race("Human", ["Versatile", "Extra Language"])
elf = Race("Elf", ["Night Vision", "Keen Senses"])

wizard = DndClass("Wizard", ["Spell Casting", "Arcane Recovery"])
fighter = DndClass("Fighter", ["Fighting Style", "Second Wind"])
