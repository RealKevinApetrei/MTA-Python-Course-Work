import random
from actors import Player, Enemy


class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print("""
                Monster Slash!!!


                Ready Player One?
                [Press Any Key to Continue]
        """)
        input()

    def print_linebreak(self):
        print("\n" + "*" * 30 + "\n")

    def play(self):
        while True:
            next_enemy = random.choice(self.enemies)
            cmd = input("You see a {}. [r]un, [a]ttack, [p]ass? ".format(next_enemy.kind))
            if cmd == "r":
                print("{} runs away!".format(self.player.name))
            elif cmd == "a":
                print("{} attacks the {}!".format(self.player.name, next_enemy.kind))
                if self.player.attacks(next_enemy):
                    self.enemies.remove(next_enemy)
                else:
                    print("{} hides to plan the next move.".format(self.player.name))
            elif cmd == "p":
                print("You are still thinking about your next move...")
            else:
                print("Please choose a valid option.")

            self.print_linebreak()

            if not enemies:
                print("You have won! Congratulations!")
                break


if __name__ == "__main__":
    enemies = [
        Enemy("Ogre", 1),
        Enemy("Imp", 1)

    ]

    player = Player("Hercules", 1)

    Game(player, enemies).main()
    Game(player, enemies).main()
