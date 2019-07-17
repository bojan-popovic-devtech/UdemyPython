age = int(input("How old are you "))

#if (age >=16) and (age <=66):
# if 15 < age < 66 :
#     print("Have a good day at work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# if (some_condition) or (some_weird_function_that does_stuff()):
#     #do something

# x = "false"
# if x:
#      print("x is true")


# x = input("Please enter some text ")
# if x:
#         print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

if not(age < 18):
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))