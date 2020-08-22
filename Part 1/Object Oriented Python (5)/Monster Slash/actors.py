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


class Enemy:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level

    def __repr__(self):
        return ("<Enemy {}>"
                    .format(
                        self.kind
                    ))


if __name__ == "__main__":
    player = Player(name="Hercules", level=1)
    print(player)
