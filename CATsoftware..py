import csv
#FILE INPUT MODE NOT WORKING AS OF NOW

inputType = input("Enter a input type, 'manual' or 'file'")

if(inputType == "file"):
    file = open('test.txt', "r")
    while True:
        line = file.readline()
        if not line:
            break

    stsIndicator = False
    command = "";
    for x in line:
      if stsIndicator == False:
        if ((x == 0) and (command != "001")):
            print("Invalid first command")
            quit()
        if (command == "001"):
            print("ACK")
        elif (command == "010"):
            print("STS")
            stsIndicator = True;
        elif (command == "000"):
            print("request of status")
        elif (command == "011"):
            print("request for fuel level")
        elif (command == "100"):
            print("end")
        if(x != ' '):
            command = command+x
      else:
        if (command == "001"):
            print("Feul System Component = 1")
        elif (command == "010"):
            print("Feul System Component = 2")

        elif (command == "011"):
            print("Feul System Component = 3")

        elif (command == "100"):
            print("Feul System Component = 4")

        elif (command == "101"):
            print("Feul System Component = 5")

        elif (command == "110"):
            print("Feul System Component = 6")

        elif (command == "111"):
            print("Feul System Component = 7")
        stsIndicator = False

elif(inputType == "manual"):
    manualInput = input("Enter Input Manually: ")
    stsIndicator = False
    command = "";
    counter = 0;
    for x in manualInput:
     if stsIndicator == False:
        if (x != ' '):
            command = command + x
        if ((x == 0) and (command != "001")):
            print("Invalid first command")
            quit()
        if (command == "001"):
            print("ACK")
            if stsIndicator == False:
             command = "";
        elif (command == "010"):
            print("STS")
            if stsIndicator == False:
             command = "";
            stsIndicator = True;
            command = manualInput[counter:counter+3]
        elif (command == "000"):
            print("request of status")
            if stsIndicator == False:
             command = "";
        elif (command == "011"):
            print("request for fuel level")
            if stsIndicator == False:
             command = "";
        elif (command == "100"):
            print("end")
            if stsIndicator == False:
             command = "";
     else:
        if (command == "001"):
            print("Feul System Component = 1")
            command = "";
        elif (command == "010"):
            print("Feul System Component = 2")
            command = "";
        elif (command == "011"):
            print("Feul System Component = 3")
            command = "";
        elif (command == "100"):
            print("Feul System Component = 4")
            command = "";
        elif (command == "101"):
            print("Feul System Component = 5")
            command = "";
        elif (command == "110"):
            print("Feul System Component = 6")
            command = "";
        elif (command == "111"):
            print("Feul System Component = 7")
            command = "";
        stsIndicator = False
        counter+=1
        command = ""

else:
    print("You entered an invalid file input")












