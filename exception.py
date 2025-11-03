try:
    num = int(input("Enter number:"))
    print(50 / num)
except ZeroDivisionError:
    print("You cant divide by Zero")
except ValueError:
    print("You didn't enter a number")
except Exception as e:
    print(e)

""" output :-

ZeroDivisionError---
Enter number:0
You cant divide by Zero

ValueError---------
Enter number:df
You didn't enter a number

Exception--------
Enter number:#not entering value enter ,enter button
You didn't enter a number
"""
