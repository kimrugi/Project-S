import time

running = None
stack = None
frame_time = 0
delete_list = None

def run(start):
    global running, stack, delete_list
    running = True
    stack = [start]
    delete_list = []
    start.enter()
    current_time = time.time()
    global frame_time
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        frame_time = time.time() - current_time
        current_time += frame_time
        if len(delete_list) > 0:
            manage_delete_list()

    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()


def manage_delete_list():
    global delete_list
    i = delete_list.pop()
    if i[1] == "delete_all_and_change":
        DAAC(i[0])
    elif i[1] == "change":
        C(i[0])
    elif i[1] == "push_state":
        PS(i[0])
    elif i[1] == "pop_state":
        POPS()


def delete_all_and_change(state):
    global delete_list
    delete_list.append((state, "delete_all_and_change"))


def change(state):
    global delete_list
    delete_list.append((state, "change"))


def push_state(state):
    global delete_list
    delete_list.append((state, "push_state"))


def pop_state():
    global delete_list
    delete_list.append((None, "pop_state"))

def DAAC(state):
    global stack
    while len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    stack.enter()


def C(state):
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    state.enter()


def PS(state):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(state)
    state.enter()


def POPS():
    global stack
    if len(stack) > 0:
        stack[-1].exit()
        stack.pop()
    if len(stack) > 0:
        stack[-1].resume()


def quit():
    global running
    running = False


