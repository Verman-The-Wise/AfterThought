from datetime import date
print("MENU\n 1 : Create new Period of time\n 2 : Show the logs\n 3 : Exit")

file_path = "tracker.txt"

def option1():
    subject = input("Choose subject for the time period like Science, etc: ")
    duration = input("Duration of your task: ")
    today  = date.today().strftime("%Y-%m-%d")
    print(f"Creating new Period of time for {subject}.")
    with open(file_path, "a") as file:
        file.write(f"SUBJ: {subject} \nTIME: {duration} \nDATE: {today}\n\n")

def option2():
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

while True:
    x = int(input("Choose your option: "))
    if x == 1:
        option1()
    elif x == 2:
        option2()
    elif x == 3:
        break
    else:
        print("The only available options are 1,2 and 3.")

