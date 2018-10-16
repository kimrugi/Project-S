
running = None
stack = None


def run(start):
    global running, stack
    running = True
    stack = [start]
    start.init()
    while running:
        stack[-1].handel_events()
        stack[-1].update()
        stack[-1].draw()
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()


def change(state):
    pass

def push_state(state):
    pass

def pop_state(state):
    pass


