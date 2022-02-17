
class Character:
    def __init__(self, name):
        self.name = name
        # Starter, Beginner, Amateur, Ace, Professional
        self.rank = None
        # Kid, Teen (Default), Adult, Senior
        self.age = None
        # Strength, Vitality, Dexterity, Insight
        self.core_attributes = None
        # Tough, Beauty, Cool, Cute, Clever
        self.social_attributes = None
        # The skills that are in the game.
        self.skills = None
        # Always 150,000
        self.money = 150_000
        self.nature = None
        self.confidence = None
        # Initial max HP is equal to Vitality
        self.current_hp = None
        self.max_hp = None
        # Initial Will is equal to (Insight + 2)
        self.will = None
        # Can carry up to 6 of the critters with you at once. Just there names here.
        self.pokemon = []
        


