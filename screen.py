import game_value
SIZE_X, SIZE_Y = 8400, 8400


class Screen:
    player = None
    def __init__(self, player):
        if Screen.player == None:
            Screen.player = player
        self.x = player.x - game_value.middle[0]
        self.y = player.y - game_value.middle[1]
        self.locked = 0

    def update(self):
        if not self.locked:
            self.x = self.player.x - game_value.middle[0]
            self.y = self.player.y - game_value.middle[1]

    def draw(self, screen):
        pass












