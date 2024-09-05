## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skills = ["python", "java", "programming"]
levels = ["beginner", "veteran", "semiprofessional"]
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old\n")
print("my skills are")
for x in range(len(skills)):
    print("- ", skills[x], " (" + levels[x] + ")")
print("\nI am looking for a job with a salary of", str(lower) + "-" + str(upper), "dollars per month")





## Problem 2 ##
print()
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")

print(x,"+", y, "=", int(x) + int(y))
print(x,"-", y, "=", int(x) - int(y))
print(x,"*", y, "=", int(x) * int(y))
print(x,"/", y, "=", int(x) / int(y))
