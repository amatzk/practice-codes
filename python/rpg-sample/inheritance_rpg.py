class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} の攻撃: {other.name} へ {self.attack_power} のダメージ!")

    def is_alive(self):
        return self.health > 0


class Player(Character):
    def __init__(self, name, health, attack_power, potions):
        super().__init__(name, health, attack_power)
        self.potions = potions

    def drink_potion(self):
        if self.potions > 0:
            self.health += 10
            self.potions -= 1
            print(f"{self.name} はポーションを飲み、HPが10回復した!")
        else:
            print(f"{self.name} は、もうポーションを持っていない")


class Enemy(Character):
    pass


player = Player("Hero", 50, 20, 1)
enemy = Enemy("Goblin", 30, 10)

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
