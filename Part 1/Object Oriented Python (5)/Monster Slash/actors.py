from random import randint


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return ("<Player: {} at Level {}>"
                    .format(
                        self.name,
                        self.level
                    ))

    def get_attack_power(self):
        return randint(1, 100) * self.level

    def attacks(self, enemy):
        power = self.get_attack_power()
        enemy_power = enemy.get_attack_power()

        print("You summon {} power units!".format(power))
        print("{} summons {} power units!".format(enemy.kind, enemy_power))

        if power >= enemy_power:
            print("You slay the {}.".format(enemy.kind))
            return True
        else:
            print("You were defeated!")
            return False
            

class Enemy:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level

    def __repr__(self):
        return ("<Enemy: {}>"
                    .format(
                        self.kind
                    ))

    def get_attack_power(self):
        return randint(1, 100) * self.level


if __name__ == "__main__":
    # player = Player(name="Hercules", level=1)
    # print(player)
    # print(player.get_attack_power())

    enemy = Enemy(kind="Ogre", level=1)
    print(enemy)
    print(enemy.get_attack_power())
