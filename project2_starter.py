"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Chris Baring]
Date: [11/14/25]

AI Usage: Used ChatGPT to clarify assignment instructions and guide class design, inheritance structure, and method overriding. All code was written, tested, and verified by me.


class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================
# ----------------------------
# Weapon Class (Composition)
# ----------------------------
class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        return f"Weapon: {self.name} | Bonus Damage: {self.damage_bonus}"

# ----------------------------
# Character Class (Base)
# ----------------------------
class Character:
    def __init__(self, name, health, strength, magic, weapon=None):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = weapon

    def attack(self, target):
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {damage} damage!"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"{self.name} takes {damage} damage. New health: {self.health}"

    def display_stats(self):
        weapon_info = self.weapon.display_info() if self.weapon else "No weapon"
        return f"{self.name} | HP: {self.health} | STR: {self.strength} | MAG: {self.magic} | {weapon_info}"

# ----------------------------
# Player Class
# ----------------------------
class Player(Character):
    def __init__(self, name, character_class, health, strength, magic, weapon=None):
        super().__init__(name, health, strength, magic, weapon)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        base_stats = super().display_stats()
        return base_stats + f" | Class: {self.character_class} | Level: {self.level} | XP: {self.experience}"

# ----------------------------
# Warrior Class
# ----------------------------
class Warrior(Player):
    def __init__(self, name, weapon=None):
        super().__init__(name, "Warrior", 120, 15, 5, weapon)

    def attack(self, target):
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} slashes {target.name} for {damage} damage!"

    def power_strike(self, target):
        damage = self.strength * 2 + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!"

# ----------------------------
# Mage Class
# ----------------------------
class Mage(Player):
    def __init__(self, name, weapon=None):
        super().__init__(name, "Mage", 80, 8, 20, weapon)

    def attack(self, target):
        damage = self.magic + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} casts a spell on {target.name} for {damage} damage!"

    def fireball(self, target):
        damage = self.magic * 3 + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} hurls a FIREBALL at {target.name} for {damage} damage!"

# ----------------------------
# Rogue Class
# ----------------------------
class Rogue(Player):
    def __init__(self, name, weapon=None):
        super().__init__(name, "Rogue", 90, 12, 10, weapon)

    def attack(self, target):
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} swiftly strikes {target.name} for {damage} damage!"

    def sneak_attack(self, target):
        damage = int(self.strength * 2.5) + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)
        return f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!"

# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================
if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    sword = Weapon("Iron Sword", 15)
    staff = Weapon("Oak Staff", 10)
    dagger = Weapon("Shadow Dagger", 12)

    warrior = Warrior("Marcus", sword)
    mage = Mage("Aria", staff)
    rogue = Rogue("Shadow", dagger)

    print(warrior.display_stats())
    print(mage.display_stats())
    print(rogue.display_stats())
