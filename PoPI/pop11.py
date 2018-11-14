# Linked Lists and Stacks


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # top stores a Node

    def push(self, x):
        # implement this: adds a new Node, makes top point to it,
        # old top is "saved in" the new Node's next
        if self.top == None:
            self.init_node = Node(x)
            self.top = self.init_node
        else:
            self.new_node = Node(x)
            self.new_node.next = self.init_node
            self.init_node = self.new_node
            self.top = self.init_node

    def pop(self):
        # implement this: makes top point to the next of the Node pointed to by top
        self.init_node = self.init_node.next
        self.top = self.init_node

    def peek(self):
        # implement this: returns the data of the Node pointed to by top
        return self.init_node.data

    def is_empty(self):
        # implement this: returns True if there are no Nodes in
        # Stack, otherwise False
        return self.top == None


# NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input:
    exec(line)

# Balanced Parentheses


class Stack:
    def __init__(self):
        self.content = []

    def push(self, item):
        self.content.append(item)

    def is_empty(self):
        return self.content == []

    def peek(self):
        return self.content[-1]     # same as [len(self.content)-1]

    def pop(self):
        del self.content[-1]


strs = [i for i in input()]
stk = Stack()
error = False

for sym in strs:
    if sym == '(' or sym == '[' or sym == '<' or sym == '{':
        stk.push(sym)
    else:  # so sym == ')' or sym == ‘]'
        if stk.is_empty():
            error = True
        elif stk.peek() == '(' and sym == ')' or stk.peek() == '[' and sym == ']' or stk.peek() == '<' and sym == '>' or stk.peek() == '{' and sym == '}':
            stk.pop()
        else:
            error = True

if stk.is_empty() and not error:
    print("True")
else:
    print("False")

# Doubly Linked Lists and Queue


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, x):
        # implements this: adds a new Node with x to back, so back points to this node,
        # while the previous of the old back's Node must point to the this new node and
        # this new Node's next must point to the old back
        if self.front == None:
            init_node = Node(x)
            self.front = init_node
        else:
            new_node = Node(x)
            if self.back == None:
                self.front.previous = new_node
                new_node.next = self.front
                self.back = new_node
            else:
                self.back.previous = new_node
                new_node.next = self.back
                self.back = new_node

    def dequeue(self):
        # implement this: returns the data of the Node pointed to by front and
        # makes new front point to the previous of the Node pointed to by old front
        node_needed = self.front
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.previous
        return node_needed.data

    def is_empty(self):
        # implement this
        return self.front == None and self.back == None


# NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input:
    exec(line)
