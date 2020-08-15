# import os
#
# current_directory = os.getcwd()
# current_folder = current_directory + "/Part 1/Introduction to Python (2)"
# directory_files = os.listdir(current_folder)
# exception_stats = os.stat(current_folder + "/handling_exceptions.py")
#
# filepath = os.path.join(current_folder, "for_loops.py")
#
# print("My working directory is:", current_directory)
# print("Current folder is:", current_folder)
# print("Folder Files:", current_folder)
# print("Exceptions Stats:", exception_stats)
#
# print("File Path:", filepath)
#
# os.chdir("Part 1/Introduction to Python (2)/")

from datetime import datetime, timedelta

today = datetime.now()

first_of_the_year = datetime(2020, 1, 1)
how_many_days = first_of_the_year - today

day_increment = timedelta(days=1, seconds=300)

tomorrow = today + day_increment

print(tomorrow)

# print(how_many_days)
