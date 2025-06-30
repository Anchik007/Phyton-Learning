Homework 1: ToDo List Application
 Task and ToDoList Classes + CLI

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Due: {self.due_date}) - {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def show_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}. {task}")

# ==== CLI ====
def todo_cli():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Task Complete\n3. List All Tasks\n4. Show Incomplete Tasks\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(title, desc, due)
        elif choice == "2":
            idx = int(input("Task number to mark complete: "))
            todo.mark_complete(idx)
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.show_incomplete_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

# Run with:
# todo_cli()
Homework 2: Simple Blog System
 Post and Blog Classes + CLI

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nBy: {self.author}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        self.posts.append(Post(title, content, author))

    def list_all_posts(self):
        for i, post in enumerate(self.posts):
            print(f"\nPost {i}:\n{post}\n")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content

    def latest_posts(self, count=3):
        for post in self.posts[-count:]:
            print(post)

# ==== CLI ====
def blog_cli():
    blog = Blog()
    while True:
        print("\n1. Add Post\n2. List All Posts\n3. Posts by Author\n4. Delete Post\n5. Edit Post\n6. Show Latest Posts\n7. Exit")
        choice = input("Choose: ")
        if choice == "1":
            t = input("Title: ")
            c = input("Content: ")
            a = input("Author: ")
            blog.add_post(t, c, a)
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            a = input("Author name: ")
            blog.posts_by_author(a)
        elif choice == "4":
            idx = int(input("Post number to delete: "))
            blog.delete_post(idx)
        elif choice == "5":
            idx = int(input("Post number to edit: "))
            new_t = input("New title: ")
            new_c = input("New content: ")
            blog.edit_post(idx, new_t, new_c)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

# Run with:
# blog_cli()
Homework 3: Simple Banking System
 Account and Bank Classes + CLI

class Account:
    def __init__(self, number, name, balance=0.0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Overdraft! Transaction failed.")
        else:
            self.balance -= amount

    def display(self):
        print(f"Account: {self.number} | Name: {self.name} | Balance: ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, number, name):
        self.accounts[number] = Account(number, name)

    def get_account(self, number):
        return self.accounts.get(number)

    def transfer(self, from_acc, to_acc, amount):
        src = self.get_account(from_acc)
        dst = self.get_account(to_acc)
        if src and dst and src.balance >= amount:
            src.withdraw(amount)
            dst.deposit(amount)
        else:
            print("Transfer failed.")

# ==== CLI ====
def bank_cli():
    bank = Bank()
    while True:
        print("\n1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Display Account\n7. Exit")
        choice = input("Choose: ")
        if choice == "1":
            num = input("Account Number: ")
            name = input("Name: ")
            bank.add_account(num, name)
        elif choice == "2":
            num = input("Account Number: ")
            acc = bank.get_account(num)
            if acc: print(f"Balance: ${acc.balance:.2f}")
        elif choice == "3":
            num = input("Account Number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc: acc.deposit(amt)
        elif choice == "4":
            num = input("Account Number: ")
            amt = float(input("Amount: "))
            acc = bank.get_account(num)
            if acc: acc.withdraw(amt)
        elif choice == "5":
            f = input("From Account: ")
            t = input("To Account: ")
            amt = float(input("Amount: "))
            bank.transfer(f, t, amt)
        elif choice == "6":
            num = input("Account Number: ")
            acc = bank.get_account(num)
            if acc: acc.display()
        elif choice == "7":
            break
        else:
            print("Invalid option.")

# Run with:
# bank_cli()
