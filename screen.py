import game_value
import main_game
import math
import framework
SIZE_X, SIZE_Y = 8400, 8400

PIXEL_PER_KILOMETER = 5
SCREEN_MOVE_SPEED = 300
WINDOW_SIZE = (960, 540)
MIDDLE = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
LOCK, LOCK_TO_UNLOCK, UNLOCK = range(3)

class LockedState:
    @staticmethod
    def enter(screen, event):
        pass

    @staticmethod
    def exit(screen, event):
        pass

    @staticmethod
    def do(screen):
        pass

    @staticmethod
    def draw(one, screen):
        pass


class FromLockedToUnlock:
    @staticmethod
    def enter(screen, event):
        pass

    @staticmethod
    def exit(screen, event):
        pass

    @staticmethod
    def do(screen):
        player = main_game.get_player()
        middle_screen_y = (screen.y + game_value.middle[1])
        middle_screen_x = (screen.x + game_value.middle[0])
        direc = math.atan2(player.y - middle_screen_y, player.x - middle_screen_x)
        screen.x += SCREEN_MOVE_SPEED * math.cos(direc) * framework.frame_time
        screen.y += SCREEN_MOVE_SPEED * math.sin(direc) * framework.frame_time
        distance = (player.y - middle_screen_y) ** 2 + (player.x - middle_screen_x) ** 2
        if distance < (PIXEL_PER_KILOMETER * (SCREEN_MOVE_SPEED / 100))**2:
            screen.event_que.append(UNLOCK)

    @staticmethod
    def draw(one, screen):
        pass


class UnlockedState:
    @staticmethod
    def enter(screen, event):
        pass

    @staticmethod
    def exit(screen, event):
        pass

    @staticmethod
    def do(screen):
        screen.x = int(screen.player.x - MIDDLE[0])
        screen.y = int(screen.player.y - MIDDLE[1])

    @staticmethod
    def draw(one, screen):
        pass

next_state_table = {
    LOCK: LockedState,
    LOCK_TO_UNLOCK: FromLockedToUnlock,
    UNLOCK: UnlockedState
}

class Screen:
    player = None

    def __init__(self, player):
        if Screen.player is None:
            Screen.player = player
        self.x = player.x - game_value.middle[0]
        self.y = player.y - game_value.middle[1]
        self.event_que = []
        self.locked = False
        self.cur_state = UnlockedState
        self.cur_state.enter(self, None)

    def get_bb(self):
        pass

    def lock_screen(self):
        self.event_que.append(LOCK)

    def unlock_screen(self):
        self.event_que.append(LOCK_TO_UNLOCK)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[event]
            self.cur_state.enter(self, event)


    def draw(self, screen):
        self.cur_state.draw(self, None)












