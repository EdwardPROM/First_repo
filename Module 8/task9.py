from collections import deque

MAX_LEN = 5
lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    if lifo:
        return lifo.popleft()
    else:
        print("Lifo is empty.")
        return None

# Приклад використання:
push(1)
push(2)
push(3)

print("Current Lifo:", lifo)

popped_element = pop()
print("Popped element:", popped_element)
print("Current Lifo:", lifo)
