


# 🛡️ COMP 163 – Project 2: Character Abilities Showcase  
### **By: [Chris Baring]**  
*(Replace with your actual name)*

---

# 🎯 Project Overview  
This project demonstrates core object-oriented programming principles using a simple character combat system. The main goals are:

- ✔ **Inheritance** (3-level chain: `Character → Player → Warrior/Mage/Rogue`)  
- ✔ **Method Overriding & Polymorphism** (`attack()` behaves differently per subclass)  
- ✔ **Composition** (`Weapon` is a separate class that characters *have*)  
- ✔ **Special Abilities** unique to each character class  
- ✔ Clean, well-commented code suitable for interview discussion  

This project does **not** attempt to be a full game—just a structured OOP demo.

---

# 🏗️ Class Structure (6 Classes Total)

Character        (Base Class)
↓
Player           (Inherits from Character)
↓
Warrior, Mage, Rogue   (Inherit from Player)

Weapon          (Composition)

---

# 📊 Character Stats (Required)

| Class   | Health | Strength | Magic | Special Ability   |
|---------|--------|----------|-------|--------------------|
| **Warrior** | 120 | 15 | 5 | Power Strike |
| **Mage**    | 80  | 8  | 20 | Fireball |
| **Rogue**   | 90  | 12 | 10 | Sneak Attack |

All classes implement:

- `attack(target)`  
- `take_damage(damage)`  
- `display_stats()`  

`Player` additionally includes:

- `character_class`  
- `level`  
- `experience`  
- overridden `display_stats()` showing expanded information  

---

# 🔥 Special Abilities (Required)

| Class | Method | Description |
|-------|---------|--------------|
| **Warrior** | `power_strike(target)` | Heavy physical attack |
| **Mage** | `fireball(target)` | High-damage magic attack |
| **Rogue** | `sneak_attack(target)` | Critical backstab attack |

---

# 🗡️ Weapons (Composition)

### `Weapon(name, damage_bonus)`  
Characters *have* a weapon. Weapons do not inherit from anything.

Each weapon can:

- Add bonus damage to attacks  
- Show info using `display_info()`  

---

# 🧪 Running & Testing the Project

## Run your program
```bash
python project2_starter.py

Run all unit tests

python -m pytest tests/ -v

Run specific categories:

Inheritance:

python -m pytest tests/test_inheritance.py -v

Method Overriding:

python -m pytest tests/test_method_overriding.py -v

Special Abilities:

python -m pytest tests/test_special_abilities.py -v


⸻

🎮 Example Usage

warrior = Warrior("Marcus")
mage = Mage("Aria")  
rogue = Rogue("Shadow")

# Polymorphism
for character in [warrior, mage, rogue]:
    character.attack(enemy)

# Special abilities
warrior.power_strike(enemy)
mage.fireball(enemy)
rogue.sneak_attack(enemy)

# Composition
sword = Weapon("Iron Sword", 15)
sword.display_info()

SimpleBattle is provided and should not be modified.

⸻

🎨 Bonus Creative Elements

(Not required, but can boost your score)
	•	Extra character subclasses
	•	Additional weapon types
	•	More complex abilities
	•	Visual output or UI formatting

(If you added anything extra, describe it here.)

⸻

🤖 AI Usage Statement (Required)

AI Usage: Used ChatGPT to clarify assignment instructions and provide guidance on class structure and inheritance. All code and testing were completed and verified by me.

⸻

👨‍💻 What I Learned
	•	How inheritance creates reusable class structures
	•	How method overriding enables polymorphism
	•	How composition lets objects contain other objects
	•	How to test code using pytest
	•	How to push code using GitHub

---

