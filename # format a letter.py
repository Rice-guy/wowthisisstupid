# format a letter
import time 
import json
def DoubleEnter():
    print("")
    print("")
def mainFunc():
    date = input("Enter the date(MM/DD/YY): ")
    opener = ""
    begin = input("Please choose your opener: Input 1 for Dear Sir/Madam Input 2 for Hello, Sir/Madam Input 3 for Greetings Sir/Madam")
    if begin == "1":
        opener = opener + "Dear Sir/Madam, "
    elif begin == "2":
        opener = opener + "Hello Sir/Madam, "
    elif begin == "3":
      opener = opener + "Greetings Sir/Madam"
    text = input("Please type in your text: ")
    endGreeting = ""
    endGret = input("Please choose your opener: Input 1 for Sincerely, Input 2 for Your + (your choice) Input 3 for Lovingly, ")
    if endGret == "1":
        endGreeting = endGreeting + "Sincerely, "
    elif endGret == "2": 
        endGreeting = endGreeting + "Yours truly, "
    elif endGret == "3": 
        endGreeting = endGreeting + "Lovingly, "
    name_Names = input("Please input your name: ")
    print(date)
    DoubleEnter()
    print(opener)
    print("")
    print(text)
    DoubleEnter()
    print(endGreeting)
    DoubleEnter()
    print("")
    print(name_Names)
    DoubleEnter()
    print("")

mainFunc()