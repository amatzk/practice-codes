from abc import ABC, abstractmethod


class Health:
    def __init__(self, value: int):
        self.value = value

    def decrease(self, amount: int):
        self.value -= amount

    def increase(self, amount: int):
        self.value += amount

    def is_positive(self):
        return self.value > 0


class AttackPower:
    def __init__(self, value: int):
        self.value = value


class Potions:
    def __init__(self, stock: int):
        self.stock = stock

    def use(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        else:
            return False


class Character(ABC):
    def __init__(self, name: str, health: Health, attack_power: AttackPower):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return self.health.is_positive()


class Player(Character):
    def __init__(
        self,
        name: str,
        health: Health,
        attack_power: AttackPower,
        potions: Potions,
    ):
        super().__init__(name, health, attack_power)
        self.potions = potions

    def attack(self, other: Character):
        other.health.decrease(self.attack_power.value)
        print(
            f"{self.name} の攻撃: {other.name} へ",
            f"{self.attack_power.value} のダメージ!",
        )

    def drink_potion(self):
        if self.potions.use():
            self.health.increase(10)
            print(f"{self.name} はポーションを飲み、HPが10回復した!")
        else:
            print(f"{self.name} は、もうポーションを持っていない")


class Enemy(Character):
    def attack(self, other: Character):
        other.health.decrease(self.attack_power.value)
        print(
            f"{self.name} の攻撃: {other.name} へ",
            f"{self.attack_power.value} のダメージ!",
        )


player = Player("Hero", Health(50), AttackPower(20), Potions(1))
enemy = Enemy("Goblin", Health(30), AttackPower(10))

print("\n+++++ 戦闘 +++++")
while player.is_alive() and enemy.is_alive():
    player.attack(enemy)
    if enemy.is_alive():
        enemy.attack(player)
    else:
        print(f"{enemy.name} は倒れた!")

    player.drink_potion()
    print()

if player.is_alive():
    print(f"{player.name} は勝利した!")
else:
    print(f"{player.name} は負けた!")
