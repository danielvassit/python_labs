
# ======================================================================================
# 1. Create a function add_numbers that takes two integers and adds them together.
# ======================================================================================


def add_numbers(a, b):
    return a + b


# result should be 3
print(add_numbers(1, 2))

# ==================================================================================================
# 2. Update function add_numbers so that it takes third optional parameter and sum them all together.
# ==================================================================================================


def add_numbers(x, y, z=None):
    if (z is None):
        return x+y
    else:
        return x+y+z

# result should be 3 and 6
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

# ======================================================================================
# 3. Assign function add_numbers to variable and run it.
# ======================================================================================


a = add_numbers
a(1, 2)


# ======================================================================================
# 4. Check type of all variables
# ======================================================================================

a = 1
b = '1'
c = None
d = 1.0
e = add_numbers

type(a)
type(b)
type(c)
type(d)
type(e)

# ======================================================================================
# 5. Create list, tuple, dictionary with values 1, 2, 3
# ======================================================================================


l = [1, 2, 3]
t = (1, 2, 3)
d = {"key1": 1, "key2": 2, "key3": 3}


# ======================================================================================
# 6. Iterate through list l and print all values
# ======================================================================================

for item in l:
    print(item)


# ======================================================================================
# 7. Dictionaries
#       a) Iterate through dictionary d and print all values
#       b) Iterate through dictionary d through values and print them
#       c) Iterate through dictionary d and print all keys and values
# ======================================================================================

for key in d:
    print(d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key)
    print(value)

# ======================================================================================
# 8. Add new element to list l and print it's value - element 4
# ======================================================================================

l.append(4)
print(l)

# ======================================================================================
# 9. Concatenate list a and b
# ======================================================================================

a = [1, 2]
b = [3, 4]
print(a + b)


# ======================================================================================
# 10. Multiply list l 3 times
# ======================================================================================

l = [1, 2]
print(l * 3)

# ======================================================================================
# 11. Check if list l contains number 1
# ======================================================================================

print(1 in l)


# ======================================================================================
# 12. Slice string x
#       a) get first character
#       b) first two characters
#       c) last character
#       d) 4 character from end to 2 character from the end ('ri')
#       e) first 3 characters without specifying first
#       f) from 3 character to end
# ======================================================================================

x = 'This is a string'
print(x[0])
print(x[0:2])
print(x[-1])
print(x[-4:-2])
print(x[:3])
print(x[3:])


# ======================================================================================
# 13. Working with strings
#       a) print firstname and lastname together
#       b) repeat firstname 3 times
#       c) check if firstname contains word "Chris"
# ======================================================================================


firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)


# ======================================================================================
# 14. Concatenate word "Chris" to number 1
# ======================================================================================

'Chris' + str(2)


# ======================================================================================
# 15. Assign all elements of tuple to different variables
# ======================================================================================

x = ("a", "b", "c")
first, second, third = x


# ======================================================================================
# 16. Print length of tuple x
# ======================================================================================

print(len(x))


# ======================================================================================
# 17. Print string sales_statement replacing empty brackets with words from dictionary,
#     last empty bracket should be filled with num_items * price
# ======================================================================================

sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


# ======================================================================================
# 18. Print current time in epoch
# ======================================================================================

import time as tm

print(tm.time())


# ======================================================================================
# 19. Convert epoch to datetime
# ======================================================================================

import datetime as dt

dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)


# ======================================================================================
# 20. Print year, month, day, hour, minute and seconds for datetime
# ======================================================================================

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second


# ======================================================================================
# 21. Create time delta of 100 days and subtract it from today
# ======================================================================================

today = dt.date.today()
delta = dt.timedelta(days=100)

today - delta


# ======================================================================================
# 22. Create class Pearson with attribute department set to "School" and two methods, one
#     for setting name and one for setting location
# ======================================================================================

class Person:
    department = 'School '

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

# ======================================================================================
# 23. Instantiate class Person and print it's department and name
# ======================================================================================

p = Person()
p.set_name("Tom")
p.set_location("London")

print(p.department + " " + p.location)


# ======================================================================================
# 24. Create map m from two lists that contains minimum values
# ======================================================================================

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
m = map(min, store1, store2)


# ======================================================================================
# 25. Iterate through map m
# ======================================================================================

for item in m:
    print(item)


# ======================================================================================
# 26. Create lambda that takes 3 parameters and adds first two of them
# ======================================================================================

my_function = lambda a, b, c: a + b


# ======================================================================================
# 27. Iterate from 0 to 999 and add even numbers to my_list
# ======================================================================================

my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

print(my_list)


# ======================================================================================
# 28. Iterate from 0 to 999 and return the even numbers with comprehension list
# ======================================================================================

my_list = [number for number in range(0, 1000) if number % 2 == 0]
print(my_list)

