# Assignment 4

#####Question 1####
print("ques-1")


def Towerofhanoi(n, Start, Extra, End):
    if n > 0:
        Towerofhanoi(n - 1, Start, End, Extra)
        print("Transfer disk from", Start, "to", End)
        Towerofhanoi(n - 1, Extra, Start, End)


Towerofhanoi(3, "A", "B", "C")
print("Done")






########questuon  no.2######
print("ques-2")
# Pascal's triangle using iteration
print("With  iteration:")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# making ncr function
def ncr(n, r):
    x = factorial(n) / (factorial(n - r) * factorial(r))
    return int(x)


row = int(input("Enter the nunber of rows:"))
i = 1
while i <= row:
    print(" " * (row - i), end="")
    j = 0
    while j < i:
        print(ncr(i - 1, j), " ", end="")
        j += 1
    print("\n")
    i += 1

# pascal's triangle using recurssion

print("With recursion:")


def pascal_triangle(n, s, m):
    if n == 0:
        print(" " * (s - 1), 1, "\n")
        return pascal_triangle(n + 1, s, m)
    elif n == m:
        print("Done!")
        n = -1
    else:
        print(" " * (s - n), end="")
        x = 0
        while x <= n:
            print(ncr(n, x), "", end="")
            x += 1
        print("\n")
        if n == m:
            n = -2
        return pascal_triangle(n + 1, s, m)


m = int(input("Enter the no. of rows:"))
n = m - m
s = m + m
pascal_triangle(n, s, m)
print("Done")








######question no.3#######

print("ques-3")
print("part(a)")


def fun(a, b):
    quotient = a // b
    remainder = a % b
    print("The quotient is:", quotient)
    print("The remainder is", remainder)
    result = [quotient, remainder]
    return result


a = int(input("Enter your first number:"))
b = int(input("Enter your second number-"))
result = fun(a, b)
print(result)
print("Callable:", callable(fun))

print("part(b)")
print("a is zero:", a == 0)
print("b is zero:", b == 0)
print("quotient is zero:", result[0] == 0)
print("remainder is zero:", result[1] == 0)
if (a == 0):
    print("a is zero")

print("part(c)")
alist = []
for i in result:
    if i > 4:
        alist.append(i)
print("The values greater than 4 are:", alist)

print("part(d)")
aset = set(alist)
print(aset)

print("part(e)")
immutable_set = frozenset(aset)
print("The required immutable set", immutable_set)

print("part(f)")
maxval = 0
for i in immutable_set:
    if i > maxval:
        maxval = i
print("The required max value is:", maxval)
print("The required hash value is:", hash(maxval))
print("Done")








#####question no.4######
print("ques-4")


class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def __del__(self):
        print("Object has been destroyed")


obj_1 = Student("Gourav", 21104066)
print(obj_1.name)
print(obj_1.rollnumber)
print("Done")








#######question no.5#######
print("ques-5")


class EmployeeDetails:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def func(self):
        print("Name of employee is:", self.name, "and salary is:", self.salary)


Emp_1 = EmployeeDetails("Mehak", 40000)
Emp_2 = EmployeeDetails("Ashok", 50000)
Emp_3 = EmployeeDetails("Viren", 60000)
Emp_1.func()
Emp_2.func()
Emp_3.func()

print("part(a)")
# updating salary of Mehak
Emp_1.salary = 70000
print("The updated salary of Mehak is:", Emp_1.salary)

print("part(b)")
# deleting the record of Viren
del Emp_3
print("The record of Viren has been successfully deleted")
print("Done")







#####question no.6######
print("ques-6")


# we will use the concept of anagrams

def anagram(word):
    if len(word) == 1:
        return [word];
    partial_words = anagram(word[1:])
    char = word[0]
    mylist = []
    for perm in partial_words:
        for i in range(len(perm) + 1):
            mylist.append(perm[:i] + char + perm[i:])
    return mylist


George_word = input("Enter the word by George:")
Possible_words = anagram(George_word)
Barbie_word = input("Enter word by Barbie:")
print("Possible Words are:", Possible_words)
print("If Barbie's word is present in the list , then their friendship is real.")

if Barbie_word in Possible_words:
    print("Your Friendship is real.")
else:
    print("Your Friendship is fake.")
print("Done")