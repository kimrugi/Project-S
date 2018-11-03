import time

running = None
stack = None
frame_time = 0


def run(start):
    global running, stack
    running = True
    stack = [start]
    start.init()
    current_time = time.time()
    global frame_time
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        frame_time = time.time() - current_time
        current_time += frame_time

    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()

def delete_all_and_change(state):
    global stack
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    stack.enter()


def change(state):
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    state.enter()


def push_state(state):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(state)
    state.enter()


def pop_state(state):
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    if len(stack) > 0:
        stack[-1].resume()


def quit():
    global running
    running = False


