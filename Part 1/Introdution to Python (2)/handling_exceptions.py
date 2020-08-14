total = 4
count = 0

try:
    average = total / count
    print("Average is: {}".format(average))
except ZeroDivisionError as e:
    print("Cannot divide by zero! ({})".format(e))
except Exception as e:
    print("Unexpected Exception: ({})".format(e))
finally:
    print("Save my progress.")
