# format a letter
import os
def mainFunc():
    date = input("Enter the date(MM/DD/YY): ")
    nameOfTxt = input("Please enter the name of the txt file the letter will be written to: ")
    for x in os.listdir():
        # iterate through current directory in case the txt file already
        if x == f"{nameOfTxt}.txt": 
         v = input("the txt name entered already has an instance within the folder, would you like to overwrite it? y/n")
         if v == "y": 
               continue
         elif v == "n":
             print("setting name of txt to Default")
             nameOfTxt = "Default"
             break 
    opener = ""
    begin = input("Please choose your opener: Input 1 for Dear Sir/Madam Input 2 for Hello, Sir/Madam Input 3 for Greetings Sir/Madam ")
    if begin == "1":
        opener = opener + "Dear Sir/Madam, "
    elif begin == "2":
        opener = opener + "Hello Sir/Madam, "
    elif begin == "3":
      opener = opener + "Greetings Sir/Madam"
    else:
        print("None of the choices presented have been selected, setting it to default value..")
        endGreeting = "Default"
    text = input("Please type in your text: ")
    endGreeting = ""
    endGret = input("Please choose your end greeting: Input 1 for Sincerely, Input 2 for Yours truly, Input 3 for Lovingly, ")
    if endGret == "1":
        endGreeting = endGreeting + "Sincerely, "
    elif endGret == "2": 
        endGreeting = endGreeting + "Yours truly, "
    elif endGret == "3": 
        endGreeting = endGreeting + "Lovingly, "
    else:
        print("None of the choices presented have been selected, setting it to default value..")
        endGreeting = "Default"

    name_Names = input("Please input your name: ")
    coolstring = f"""{date}


{opener} 

{text} 


{endGreeting}


{name_Names}"""
    f = open(f"{nameOfTxt}.txt", "w")
    f.write(coolstring)
    f.close()
    print("Enjoy your formatted letter!")

mainFunc()
