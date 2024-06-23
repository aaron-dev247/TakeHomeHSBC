# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

# Issue: When using a mutable object (like list) as a default argument, it retain its state across multiple function calls
# Example:

list1 = add_to_list(10)
print(list1)  # Output: [10]

list2 = add_to_list(20)
print(list2)  # Output: [10, 20]

# Fix: Use `None` as the default argument, create the list inside the function if argument is none

def add_to_list(value, my_list=None):

    if my_list is None:
        my_list = [] # Create a new list

    my_list.append(value)

    return my_list


# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."

# Issue: Placeholders {name} and {age} won't be replace by the value of `name` and `age`

# Fix 1: Use f-string

def format_greeting(name, age):

    return f"Hello, my name is {name} and I am {age} years old."

# Fix 2: Use .format()

def format_greeting(name, age):

    return "Hello, my name is {} and I am {} years old.".format(name, age)


# Review 3

class Counter:

    count = 0

    def __init__(self):

        self.count += 1

    def get_count(self):

        return self.count

# Issue 1: `self.count` is not pointing to `count` in the Counter because it's a class variable
# Issue 2: `__init__` usually use for declare and initialize attributes

# Fix: Declare `count` in `__init__`, change it's value in another method

class Counter:

    def __init__(self):
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def increment(self):
        self.count += 1


# Review 4

import threading

class SafeCounter:

    def __init__(self):

        self.count = 0

    def increment(self):

        self.count += 1


def worker(counter):

    for _ in range(1000):

        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)
 

for t in threads:

    t.join()

# Issue: Multiple threads can access and modify `self.count`, leading to race conditions

# Fix: Using lock to prevent other threads access `self.count`

class SafeCounter:

    def __init__(self):

        self.count = 0
        self.lock = threading.Lock() # Thread lock

    def increment(self):

        with self.lock:
            self.count += 1

# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts

# Issues: Should be `counts[item] += 1` not `counts[item] =+ 1`

# Fix:

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1

        else:

            counts[item] = 1

    return counts
