class State(object):
    def __init__(self, name):
        self.name = name
        self.list = []
        self.is_parent = False
        self.count = 0
        self.parent = self
        self.complete = False
        self.next = ''

    def makeParent(self):
        self.is_parent = True
    
    def addParent(self, parent):
        self.parent = parent
        
    def getParent(self):
        return self.parent
        
    def isComplete(self):
        return self.complete
        
    def addWord(self, word):
        self.list.append(word)
    
    def setIncrement(self, count):
        self.count = count
    
    def getIncrement(self):
        return self.count
    
    def getNext(self):
        if len(self.getList()) > self.getIncrement():
            self.next = self.getList()[self.count]
            print self.getIncrement()
            return self.next
        else: 
            self.complete = True
            return None
            
    def getList(self):
        return self.list
        
    # toString
    def __str__(self):
        s = 'State ' + self.name + '\n'
        return s

def buildState(state, possible_words):
    for word in possible_words:
        if isValid(word, state.name):
            state.addWord(word)
    return state

        
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


def isValid(word, state_name):
    count = 0
    if word == state_name:
        return False
    for index in range(len(state_name)):
        if word[index] != state_name[index]:
            count += 1
        if count > 1:
            return False
    return True

def createDictionary(possible_words, start, goal):
    state = State(start)
    dict = {}
    state.makeParent()
    new_state = buildState(state, possible_words)
    dict[new_state.name] = new_state.getList()
    next = new_state.getNext()
    
    print 'next', next

    while not new_state.getParent().isComplete() or not next != goal:
        if not new_state.getParent().isComplete():
            state = State(next)
            state.addParent(new_state);
            parent = new_state
            new_state = buildState(state, possible_words)
            dict[new_state.name] = new_state.getList() 
            next = parent.getNext()
            
            print 'next2', next
            print dict
        else:
            next_child = new_state.getParent().getList()[0]
            next_child.addParent(new_state)
            next_child = buildState(state, possible_words)
            dict[next_child.name] = next_child.getList()
            new_state = next_child
            break

    print dict.keys()
    return dict

    
def main():
    dictionary = {}
    start = 'egg'
    goal = 'eng'
    file = open('words.txt')
    for word in file:
        dictionary[word.split()[0]] = word.split()
        
    possible_words = {}
    for word in dictionary:
        if len(word) == len(goal):
            possible_words[word] = word
    
    dict = createDictionary(possible_words, start, goal)
    
    #print bfs(dict, start, goal)
        
main()
        

    
    
    

