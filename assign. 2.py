#Question 1
print("\nThe solution of Question 1 is :\n")
input_str = "Python is a case sensitive language"
print("(a)\tThe length of the given string is : %s" % len(input_str))                                       #Printing the length of the string
reversed_str = input_str[ : : -1 ]                                                                          #Creating reversed string
print("(b)\tThe string in reverse would be : %s" % reversed_str)
new_str = input_str[10:26]                                                                                  #Creating a new string              
print("(c)\tThe new string becomes : %s" % new_str)
dup_input_str = input_str.replace("a case sensitive", "object oriented")                                    #Creating a duplicate input string for replaced value
print("(d)\tThe replaced substring will be : %s" % dup_input_str)
substr = "a"
indx = input_str.find(substr)                                                                               #Finding the index value of the given substring
if indx == -1:
    print("(e)\tThe given substring was not found in the inputted string")
else:
    print("(e)\tThe first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))   #Printing the index value
no_white_spaces_str=input_str.replace(" ","")                                                               #Removing white spaces
print("(f)\tThe inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)

#Question 2
print("\nThe solution of Question 2 is :\n")
#inputs
name = input("Enter your name : ")
sid = int(input("Enter your SID : "))
dept_name = input("Enter the name of your department : ").upper()
cgpa=float(input("Enter your CGPA : "))
#output
print("\nHey, \033[1m%s\033[0m Here!\nMy SID is \033[1m%d\033[0m\nI am from \033[1m%s\033[0m department and my CGPA is \033[1m%0.1f\033[0m\n" % (name, sid, dept_name, cgpa))

#Question 3
print("\nThe solution of Question 3 is :\n")
a=56
b=10
print("a.\ta & b = %d" % (a & b))
print("b.\ta | b = %d" % (a | b))
print("c.\ta ^ b = %d" % (a ^ b))
print("d.\tLeft shift both a and b with 2 bits : a = %d, b = %d" % (a << 2,b << 2))
print("e.\tRight shift a with 2 bits and b with 4 bits : a = %d, b = %d\n" % (a >> 2,b >> 4))

#Question 4
print("\nThe solution of Question 4 is :\n")
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))
if first_number >= second_number:
    if first_number >= third_number:
        print("The greatest number is %s\n" % first_number)
    else:
        print("The greatest number is %s\n" % third_number)
else:
    if second_number >= third_number:
        print("The greatest number is %s\n" % second_number)
    else:
        print("The greatest number is %s\n" % third_number)

#Question 5
print("\nThe solution of Question 5 is :\n")
if "name" in input("Enter the string : "):
    print("Yes\n")
else:
    print("No\n")

#Question 6
print("\nThe solution of Question 6 is :\n")
while True:
    sides = sorted(input("Enter the dimensions to check whether triangle possible or not : ").split())  #Sorting the inputted values in a list
    if len(sides) == 3:                                                                                 #Making sure only 3 values are entered
        break
    else:
        print("\nA triangle has only 3 sides!\nPlease enter only 3 values")
if int(sides[2]) > (int(sides[0]) + int(sides[1])):
    print("No\n")
else:
    print("Yes\n")
