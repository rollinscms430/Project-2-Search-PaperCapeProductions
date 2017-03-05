"""Holds information for each state including the 
state name and frontier.
"""
class State(object):
    def __init__(self, name):
        self.name = name
        self.list = []
        self.count = 0
    
    def get_name(self):
        return self.name
        
    def add_to_frontier(self, word):
        """Adds a word the the frontier of
        the state."""
        self.list.append(word)
    
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
    """Builds each state."""
    for word in possible_words:
        if is_valid(word, state.get_name()):
            state.add_to_frontier(word)
    return state

    
def is_valid(word, state_name):
    """Checks to see if a word is one letter away
    fromt the given word."""
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
    """Creates the dictionary of states. 
    It achieves this by using a depth first search
    strategy by creating a new state and its frontier and then
    adds it to the dictionary for each new word found.
    """
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
    """Finds the shortest path by using a 
    breadth first search. The queue in this case holds
    and entire list of words. Each time it checks to see if
    the next list in the queue holds the target word and then
    returns that path."""
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
    """Creates the dictionary of states and returns the shortest path."""
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
    print 'Shortest path:', bfs(states, start, goal)
    

main()
        
