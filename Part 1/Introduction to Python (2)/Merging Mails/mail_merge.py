winners_path = "/media/kevinapetrei/KEVIN USB/Files/Programming/MTA Python Course Work/Part 1/Introdution to Python (2)/Merging Mails/winners.txt"
message_path = "/media/kevinapetrei/KEVIN USB/Files/Programming/MTA Python Course Work/Part 1/Introdution to Python (2)/Merging Mails/message.txt"

mail_path = "/media/kevinapetrei/KEVIN USB/Files/Programming/MTA Python Course Work/Part 1/Introdution to Python (2)/Merging Mails/Mails/"

with open(message_path, "r") as message_file, open(winners_path, "r") as winners_file:
    winners = winners_file.readlines()
    message = message_file.read()

for winner in winners:
    filename = winner.strip("\n") + ".txt"
    with open(mail_path + filename, "w") as f:
        f.write("Dear " + winner.strip("\n") + ",\n")
        f.write(message)
