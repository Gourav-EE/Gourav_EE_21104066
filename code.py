
# 1st program

#average of three number of student taken from user.
print("solving Q1 " ,"\n")
num1=int(input("enter no 1 "))
num2=int(input("enter no 2 "))
num3=int(input("enter no 3 "))

Sum = num1 + num2 + num3        # sum of given number of student.
avg  = Sum / 3                     # average of given nos

print("sum of given nos is ", Sum,)
print("average of given nos is ", avg ,'\n')


# 2nd program

# calculating tax in dollars.

print("solving Q2 ",'\n')
print(" All values are to be entered in dollars.")
gross_income = float(input("enter your gross income $"))
dependents = int(input("enter no of dependents "))

tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = (gross_income - standard_deduction - (dependent_deduction*dependents))
tax = taxable_income*tax_rate
print("the tax comes out to be $", tax,'\n') 


# 3rd program.

# data entry of student.

print("solving Q3 ",'\n')
print("Student = [sid, name, gender, course, cgpa]")
sid = int(input("enter your SID "))
name = input("enter your name ")
gender = input("enter your gender 'M', 'F', 'U' for male, female, unknown respectively.")
course = input("enter your course name ")
cgpa = float(input("enter your cgpa "))
student = [sid, name, gender, course, cgpa]   # converting data provided by user into list.
print("student info ", student, '\n')


# 4th program

# Marks of 5 student in a shorted manner

print("solving Q4",'\n')
# taking input from user
a = int(input("enter marks of student 1 "))
b = int(input("enter marks of student 2 "))
c = int(input("enter marks of student 3 "))
d = int(input("enter marks of student 4 "))
e = int(input("enter marks of student 5 "))
# converting input data into list.
marks = [a,b,c,d,e]
print("marks of 5 students are ", marks)
# sorting the list in asecending and descending order.
asc = marks.sort()
print("marks in ascending order ", marks)

desc = marks.sort(reverse = True)
print("marks in descending order ", marks, '\n')


# 5th program

# removing the elements of a given list.
print("solving Q5", '\n')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

# removing the 4th term and returning modified list
color.pop(3)
print(" The modified list  is color 1 =", color)

# replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list is color 2 =", color2)
