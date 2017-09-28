import os
import sys

currentKey = "12345"
checkForKey = "yes"
while checkForKey == "yes":
    accessKey = input("Enter acess key:")
    if accessKey == currentKey:
        currentV = "2.2"
        currentInput = ""
        personName = "user"
        systemRunning = "yes"
        print("")
        print("starting MaxShell V" + currentV)
        print("")
        print("Welcome!")
        print("To get started, type 'help' to learn some commands")
        print("--")
        while systemRunning == "yes":
            currentInput = input(personName + ": ")

            if currentInput == "help":
                print("")
                print("help center:")
                print("showInput | A simple command to show the input")
                print("shutdown | Shuts down program")
                print("logout | Logs out to access mode.")
                print("--v | Displays current version")
                print("--s | Support Max")
                print("--i | Info")
                print("physCalc | Calculations that are useful for physics")
                print("geoCalc | Calculations that are useful for Geometry")
                print("avgCalc | Calculates averages like mean, mode, and median")
                print("showSource | Opens source code for MaxShell")
                print("changeKey | Changes current access key.")
                print("count | Counts to a certain number from one.")
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
                    settingsInput = input(personName + "/settings:")
                    if settingsInput == "close":
                        settingsOn = "false"
                    else:
                        print()
                        print("ERROR: '" + settingsInput + "' is not an input, type help for commands.")
            elif currentInput == "logout":
                print("logging out")
                logout = "yes"


            elif currentInput == "avgCalc":
                print()
                print("AverageCalc has started")
                print("Type help to get started.")
                print()
                avgRunning = "yes"
                while avgRunning == "yes":
                    avgInput = input(personName + "/avg:")

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

                    countNumber = input(personName + "/count: ")
                    if countNumber == "close":
                        countRunning = "no"

                    else:
                        os.system("jot - 1 " + countNumber)
                        countRunning = "no"


            elif currentInput == "showSource":
                print()
                print("WARNING: This will open the source code, anything edited will be changed.")
                print("Please note, it is still not allowed to distribute MaxShell, and remains my intelectual property.")
                print("If you would like to continue, please type 'I Agree'")
                openCheck = input(personName + "/open:")
                if openCheck == "I Agree":
                    os.system("nano MaxShell.py")
                    print()
                else:
                    print()
                    print("Sorry, that was invalid.")
                    print()

            elif currentInput == "--s":
                print("")
                print("go to maxsimon.io to support Max")
                print("--")
            elif currentInput == "hello":
                print("Hi!")
            elif currentInput == "shutdown":
                print("Are you sure you would like to to shut down the system? (y/n)")
                shutdownConfirm = input(personName + "/shutdown: ")
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

            elif currentInput == "--i":
                print()
                print("Info:")
                print()
                print("Version: " + currentV)
                print("About:")
                print("This is set of tools that makes modern tools simplified to be used in a terminal.")
            elif currentInput == "":
                spaceholder = ""
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
#Created By Max Simon
