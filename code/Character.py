from code.Entity import Entity


class Character(Entity):
    def __init__(self, name: str, position, dirname):
        super().__init__(name, position, dirname)
        self.idle = None
        self.run = None
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.shot_attack = None
        self.shot = None
        self.jump = None
        self.dead = None

    def update(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass

    def shot(self):
        pass