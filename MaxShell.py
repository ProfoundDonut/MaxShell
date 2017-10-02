import os
import sys
import random
def guessing_game():
    print()
    print()
    print("Welcome to guessing_game!")
    print("type help to begin")
    print()
    print()
    running = "yes"
    while running == "yes":
        guessingInput = input(userName + "/game: ")

        if guessingInput == "start":
            print()
            print("Starting Game:")
            gameRunning = "yes"
            print()
            print()
            pickedNumber = random.randint(1, 1000)
            while gameRunning == "yes":
                gameInput = int(input("Please guess a number: "))
                if gameInput == pickedNumber:
                    print()
                    print("Your Right!!!")
                    gameRunning = "no"
                    print()
                elif gameInput > pickedNumber:
                    print()
                    print("Sorry, close but too high.")
                    print()
                elif gameInput < pickedNumber:
                    print()
                    print("Sorry, close but too low.")
                    print()
                else:
                    print("ERROR: That is not a number")
        elif guessingInput == "close":
            print()
            print("Shutting down.")
            print()
            running = "no"
        elif guessingInput == "help":
            print()
            print("start | Starts game.")
            print("help | options menu")
            print("close| Closes guessing_game")
            print("randA | Random Array (NOT WORKING)")

        else:
            print()
            print("ERROR: '" + guessingInput + "' is not an input.'")

currentKey = "12345"
checkForKey = "yes"
while checkForKey == "yes":
    accessKey = input("Enter acess key:")
    keyTryAmmount = 1
    if accessKey == currentKey:
        userName = "user"
        currentV = "2.5"
        currentInput = ""
        systemRunning = "yes"
        logout = "no"
        print("")
        print("starting MaxShell V" + currentV)
        print("")
        print("Welcome " + userName)
        print("To get started, type 'help' to learn some commands")
        print("--")
        while systemRunning == "yes":
            currentInput = input(userName + ": ")

            if currentInput == "help":
                print("")
                print("help center:")
                print("showInput | A simple command to show the input")
                print("settings")
                print("shutdown | Shuts down program")
                print("logout | Logs out to access mode.")
                print("cancelLogout | Cancles logout mode.")
                print("--v | Displays current version")
                print("--s | Support Max")
                print("--i | Info")
                print("physCalc | Calculations that are useful for physics")
                print("geoCalc | Calculations that are useful for Geometry")
                print("avgCalc | Calculates averages like mean, mode, and median")
                print("showSource | Opens source code for MaxShell")
                print("changeKey | Changes current access key.")
                print("count | Counts to a certain number from one.")
                print("guessingGame | A simple numeric guessing game.")
                print("kittens | Emergency shutdown after 5 seconds")
                print("--")

            elif currentInput == "showInput":
                showInputV1 = input("Input:")
                print("")
                print("your input is '" + showInputV1 + "'")
                print("--")
            elif currentInput == "--v":
                print("")
                print("current version of MaxShell: '" + currentV + "'")
                print("--")

            elif currentInput == "settings":
                settingsOn = "true"
                print("Sorry, settings is not available.")
                while settingsOn == "errorCode3000":
                    print()
                    print("Settings:")
                    print()
                    print("Options: ")
                    print("name | changes name for shell")
                    print("password | changes password")
                    print("close")
                    settingsInput = input(userName + "/settings:")
                    if settingsInput == "close":
                        settingsOn = "false"
                    else:
                        print()
                        print("ERROR: '" + settingsInput + "' is not an input, type help for commands.")
            elif currentInput == "logout":
                print()
                print("The system in now in logout mode, type 'shutdown' to logout.")
                logout = "yes"
                print()
                currentInput = "shutdown"

            elif currentInput == "cancelLogout":
                logout = "no"
                print()
                print("Logout mode canceled.  Typing shutdown will shutdown the system normally")


            elif currentInput == "avgCalc":
                print()
                print("AverageCalc has started")
                print("Type help to get started.")
                print()
                avgRunning = "yes"
                while avgRunning == "yes":
                    avgInput = input(userName + "/avg:")

                    if avgInput == "help":
                        print()
                        print("calcMean | Calculates mean from up to 10 numbers.")
                        print("calcMedian | Calculates median from up to 10 numbers.")
                        print("calcMode | Calculates mode from up to 10 numbers.")
                        print("close | Closes AverageCalc")
                        print()
                    elif avgInput == "close":
                        print("AverageCalc Clsoing")
                        avgInput = "no"
                    elif avgInput == "calcMean":
                        avgInputMeanNumber = int(input("How many numbers would you like to calculate?"))
                        if avgInputMeanNumber >= 10:
                            print("ERROR: The number cannot be above 10")
            elif currentInput == "count":
                countRunning = "yes"
                while countRunning == "yes":
                    print("What number would you like to count to?")

                    countNumber = input(userName + "/count: ")
                    if countNumber == "close":
                        countRunning = "no"

                    else:
                        os.system("jot - 1 " + countNumber)
                        print()
                        countRunning = "no"


            elif currentInput == "showSource":
                print()
                print("WARNING: This will open the source code, anything edited will be changed.")
                print("Please note, it is still not allowed to distribute MaxShell, and remains my intelectual property.")
                print("If you would like to continue, please type 'I Agree'")
                openCheck = input(userName + "/open:")
                if openCheck == "I Agree":
                    os.system("open -a atom MaxShell.py")
                    print()
                else:
                    print()
                    print("Sorry, that was invalid.")
                    print()

            elif currentInput == "--s":
                print("")
                print("Would you like to go to maxsimon.io(y/n)")
                print()
                supportCheck = input(userName + "/support: ")
                if supportCheck == "y":
                    os.system("open -a safari http://maxsimon.io")
                elif supportCheck == "n":
                    print("Cacnled")


            elif currentInput == "hello":
                print("Hi!")
            elif currentInput == "shutdown":
                print("Are you sure you would like to to shut down the system? (y/n)")
                shutdownConfirm = input(userName + "/shutdown: ")
                if shutdownConfirm == "y":
                    print("")
                    print("shutting down")
                    systemRunning = "no"
                    if logout == "yes":
                        checkForKey = "yes"
                    else:
                        checkForKey = "no"
                    print("")
                elif shutdownConfirm == "n":
                    print("")
                    print("shutdown cancled")
                    print("")
                elif currentInput == "eShutdown":
                    print("shutting down")
                    systemRunning = "no"
                else:
                    print("")
                    print("ERROR: Input invalid, canceling shutdown")
                    print("")

            elif currentInput == "physCalc":
                print()
                print("PhysCalc is running")
                print("Type 'help' for information.")
                print("")
                physInput = ""
                while physInput != "close":
                    physInput = input("user/phys:")
                    if physInput == "help":
                        print("")
                        print("close | Closees PhysCalc")
                        print("calcKE | Calculates Kinetic Energy in Joules")
                        print("calcGPE | Calculates Gravitation Potensial Energy in Joules")
                        print("")
                    elif physInput == "close":
                        print("PhysCalc closed")
                        print("")
                    elif physInput == "calcKE":
                        print()
                        calcKEMassInpt = int(input("mass in Kg:"))
                        calcKEVelInpt = int(input("velocity in m/s:"))
                        KEPrpMass = calcKEMassInpt
                        KEPrpVel = calcKEVelInpt*calcKEVelInpt
                        print("")
                        print("Kinetic Energy in Joules")
                        print(KEPrpMass * KEPrpVel * 0.5)
                    elif physInput == "calcGPE":
                        print("")
                        GPEmass = int(input("Mass in Kg:"))
                        GPEheight = int(input("Height in Meters:"))
                        print("Gravitational Potensial Energy is Joules:")
                        print(9.8 * GPEmass * GPEheight)
                        print("--")

                    else:
                        print("")
                        print("ERROR: '" + physInput + "' is not an input, type help for commands.")
                        print("--")
            elif currentInput == "kittens":
                print()
                print()
                print()
                print("Kitten Power Activated")
                print()
                print()
                os.system("jot - 1 500000")
                runCancelProtocol()


            elif currentInput == "--i":
                print()
                print("Info:")
                print()
                print("Version: " + currentV)
                print("About:")
                print("This is set of tools that makes modern tools simplified to be used in a terminal.")
            elif currentInput == "":
                spaceholder = ""
            elif currentInput == "guessingGame":
                guessing_game()
            elif currentInput == "geoCalc":
                geoInput = ""
                print()
                print("GeoCalc Started")
                print("Type 'help' for commands.")
                while geoInput != "close":
                    print()
                    geoInput = input(currentInput + "/geo:")
                    if geoInput == "help":
                        print()
                        print("calcPythag")
                        print()
                    elif geoInput == "calcPythag":
                        print("")
                        print("Insert A")
                        geoInputA = int(input(currentInput + "/geo:"))
                        print()
                        print("Insert B")
                        geoInputB = int(input(currentInput + "/geo:"))
                        geoAPrp = geoInputA**2
                        geoBPrp = geoInputB**2
                        geoC = geoAPrp + geoBPrp
                        geoCprp = geoC**0.5
                        print()
                        print("C =")
                        print(geoCprp)


                else:
                    print("ERROR: '" + geoInput + "' is not an input, type help for commands'")

            else:
                print("")
                print("ERROR: '" + currentInput + "' is not an input, type help for commands.")
                print("--")
    elif accessKey == "close":
        checkForKey = "no"
    else:
        print("ERROR: Acess Key Invalid")
        keyTryAmmount = keyTryAmmount + 1
if keyTryAmmount == 5:
    checkForKey = "no"

#Created By Max Simon
