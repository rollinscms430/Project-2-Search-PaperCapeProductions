"""Holds information for each state including the frontier and returns the next element in the frontier"""
class State(object):
    def __init__(self, name):
        self.name = name
        self.list = []
        self.count = 0
    
    def get_name(self):
        return self.name
        
    def add_to_frontier(self, word):
        self.list.append(word)
    
    def get_next_element(self):
        index = self.count
        self.count += 1
        length = len(self.get_frontier())
        if length > index:
            return self.list[index]
    
    def get_frontier(self):
        return self.list

"""Implements a Stack with the usual methods"""
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def build_state(state, possible_words):
    for word in possible_words:
        if is_valid(word, state.get_name()):
            state.add_to_frontier(word)
    return state

    
def is_valid(word, state_name):
    count = 0
    if word == state_name:
        return False
    for index in range(len(state_name)):
        if word[index] != state_name[index]:
            count += 1
        if count > 1:
            return False
    return True
    
def create_dict(state, dict, goal):
    new_dict = {}
    state = build_state(state, dict)

    stack = Stack()
    visited = [] 
    stack.push(state)
    while not stack.isEmpty():
        current = stack.pop()
        new_dict[current.get_name()] = current.get_frontier()
        if current.get_name() in visited:
            continue
        else:
            visited.append(current.get_name())
            for node in current.get_frontier():
                state = State(node)
                new_state = build_state(state, dict)
                stack.push(new_state)

    return new_dict
    
def bfs(states, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in states.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

          
def main():
    dictionary = {}
    start = 'snakes'
    goal = 'brains'
    file = open('words.txt')
    for word in file:
        dictionary[word.split()[0]] = word.split()
        
    possible_words = {}
    for word in dictionary:
        if len(word) == len(goal):
            possible_words[word] = word
    state = State(start)
    states = create_dict(state, possible_words, goal) 
    print 'Shortest path', bfs(states, start, goal)
    

main()
        
