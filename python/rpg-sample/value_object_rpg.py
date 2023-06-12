from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from typing import Self


@dataclass(frozen=True, slots=True)
class Health:
    value: int

    def decrease(self, amount: int) -> Self:
        return replace(self, value=self.value - amount)

    def increase(self, amount: int) -> Self:
        return replace(self, value=self.value + amount)

    def is_positive(self) -> bool:
        return self.value > 0


@dataclass(frozen=True, slots=True)
class AttackPower:
    value: int


@dataclass(frozen=True, slots=True)
class Potions:
    stock: int

    def use(self) -> tuple[Self, bool]:
        if self.stock > 0:
            return (replace(self, stock=self.stock - 1), True)
        else:
            return (self, False)


class Character(ABC):
    def __init__(self, name: str, health: Health, attack_power: AttackPower):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self) -> bool:
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

    def attack(self, other: Character) -> None:
        other.health = other.health.decrease(self.attack_power.value)
        print(
            f"{self.name} の攻撃: {other.name} へ",
            f"{self.attack_power.value} のダメージ!",
        )

    def drink_potion(self) -> None:
        self.potions, used = self.potions.use()
        if used:
            self.health = self.health.increase(10)
            print(f"{self.name} はポーションを飲み、HPが10回復した!")
        else:
            print(f"{self.name} は、もうポーションを持っていない")


class Enemy(Character):
    def attack(self, other: Character) -> None:
        other.health = other.health.decrease(self.attack_power.value)
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
