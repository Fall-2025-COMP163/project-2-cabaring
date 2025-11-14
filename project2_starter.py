"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: Used ChatGPT to clarify assignment instructions and provide guidance on class structure and inheritance. All code and testing were completed and verified by me.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

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
# YOUR CLASSES TO IMPLEMENT
# ============================================================================

class Character:
    """Base class for all characters"""
    
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
    
    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    def display_stats(self):
        print(f"{self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


class Player(Character):
    """Base class for player characters"""
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
    
    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | Experience: {self.experience}")


class Warrior(Player):
    """Warrior class - strong physical fighter"""
    
    def __init__(self, name, weapon=None):
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        self.weapon = weapon
    
    def attack(self, target):
        damage = self.strength + 5  # warrior bonus
        if self.weapon:
            damage += self.weapon.damage_bonus
        print(f"{self.name} swings sword at {target.name} for {damage} damage.")
        target.take_damage(damage)
    
    def power_strike(self, target):
        damage = self.strength * 2
        if self.weapon:
            damage += self.weapon.damage_bonus
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """Mage class - magical spellcaster"""
    
    def __init__(self, name, weapon=None):
        super().__init__(name, "Mage", health=80, strength=8, magic=20)
        self.weapon = weapon
    
    def attack(self, target):
        damage = self.magic
        if self.weapon:
            damage += self.weapon.damage_bonus
        print(f"{self.name} casts a spell on {target.name} for {damage} damage.")
        target.take_damage(damage)
    
    def fireball(self, target):
        damage = self.magic * 2
        if self.weapon:
            damage += self.weapon.damage_bonus
        print(f"{self.name} casts FIREBALL on {target.name} for {damage} damage!")
        target.take_damage(damage)


import random

class Rogue(Player):
    """Rogue class - quick and sneaky fighter"""
    
    def __init__(self, name, weapon=None):
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)
        self.weapon = weapon
    
    def attack(self, target):
        crit = random.randint(1, 10) <= 3
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus
        if crit:
            damage *= 2
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)
    
    def sneak_attack(self, target):
        damage = self.strength * 2
        if self.weapon:
            damage += self.weapon.damage_bonus
        print(f"{self.name} performs SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """Weapon class for composition"""
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
    
    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    
    # Create weapons
    sword = Weapon("Iron Sword", 15)
    staff = Weapon("Oak Staff", 10)
    dagger = Weapon("Shadow Dagger", 12)

    # Create characters
    warrior = Warrior("Marcus", sword)
    mage = Mage("Aria", staff)
    rogue = Rogue("Shadow", dagger)

    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test special abilities
    print("\n✨ Special Abilities:")
    warrior.power_strike(rogue)
    mage.fireball(warrior)
    rogue.sneak_attack(mage)

    # Test weapons
    print("\n🗡️ Weapons Info:")
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Test battle system
    print("\n⚔️ Battle System Test:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
