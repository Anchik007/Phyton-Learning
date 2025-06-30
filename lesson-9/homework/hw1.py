1. Circle Class

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius
2.  Person Class

from datetime import date

class Person:
    def __init__(self, name, country, dob):  # dob format: YYYY-MM-DD
        self.name = name
        self.country = country
        self.dob = date.fromisoformat(dob)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
3.  Calculator Class

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
4.  Shape and Subclasses

import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius**2
    def perimeter(self): return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side**2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c, height=None): self.a, self.b, self.c, self.height = a, b, c, height
    def area(self): return 0.5 * self.a * self.height if self.height else "Height required"
    def perimeter(self): return self.a + self.b + self.c
5.  Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node: return Node(value)
            if value < node.value: node.left = _insert(node.left, value)
            else: node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node: return False
            if node.value == value: return True
            return _search(node.left, value) if value < node.value else _search(node.right, value)
        return _search(self.root, value)
6.  Stack Data Structure

class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else "Stack is empty"
    def is_empty(self): return len(self.items) == 0
7.  Linked List

class Node:
    def __init__(self, data): self.data, self.next = data, None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
8. Shopping Cart

class ShoppingCart:
    def __init__(self): self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items: del self.items[name]

    def total(self):
        return sum(self.items.values())
9.  Stack with Display

class Stack:
    def __init__(self): self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else "Stack is empty"
    def display(self): print("Stack:", self.items)
10.  Queue Data Structure

class Queue:
    def __init__(self): self.items = []

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else "Queue is empty"
    def display(self): print("Queue:", self.items)
11.  Bank Class

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def show_balance(self): print(f"{self.name}'s balance: ${self.balance}")
