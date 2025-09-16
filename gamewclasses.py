import random

# ------------------------------
# Class 1: Creature
# ------------------------------
class Creature:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health

    def attack(self, other):
        """Attack another Creature and reduce their health"""
        damage = random.randint(1, 10) + self.level
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        if other.health <= 0:
            other.health = 0
            print(f"{other.name} has been defeated!")

    def heal(self):
        """Heal this creature"""
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} points! Current health: {self.health}")

    def is_alive(self):
        """Check if the creature is alive"""
        return self.health > 0

    def __repr__(self):
        return f"{self.name} (Level {self.level}) - HP: {self.health}/{self.max_health}"

# ------------------------------
# Class 2: Trainer
# ------------------------------
class Trainer:
    def __init__(self, name, creatures):
        self.name = name
        self.creatures = creatures  # list of Creature objects
        self.active_creature = creatures[0]

    def choose_creature(self, index):
        """Switch to a different creature"""
        if 0 <= index < len(self.creatures):
            self.active_creature = self.creatures[index]
            print(f"{self.name} switched to {self.active_creature.name}")
        else:
            print("Invalid creature index!")

    def attack_trainer(self, other_trainer):
        """Attack another trainer's active creature"""
        if self.active_creature.is_alive():
            self.active_creature.attack(other_trainer.active_creature)
        else:
            print(f"{self.active_creature.name} is unable to fight!")

    def __repr__(self):
        return f"Trainer {self.name} with creatures: {self.creatures}"

# ------------------------------
# Create Creature Instances
# ------------------------------
creature1 = Creature("Flareon", 5, 50)
creature2 = Creature("Aquata", 4, 45)
creature3 = Creature("Leafy", 3, 40)
creature4 = Creature("Rocko", 6, 55)

# ------------------------------
# Create Trainer Instances
# ------------------------------
trainer1 = Trainer("Ash", [creature1, creature2])
trainer2 = Trainer("Misty", [creature3, creature4])

# ------------------------------
# Testing __repr__ methods
# ------------------------------
print(creature1)
print(trainer1)

# ------------------------------
# Test interactions
# ------------------------------
trainer1.attack_trainer(trainer2)
trainer2.attack_trainer(trainer1)
creature1.heal()
trainer2.choose_creature(1)
trainer2.attack_trainer(trainer1)
