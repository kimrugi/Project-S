
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
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    state.enter()


def push_state(state):
    pass

def pop_state(state):
    pass


