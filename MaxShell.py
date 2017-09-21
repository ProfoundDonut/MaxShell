currentKey = "12345"
checkForKey = "yes"
while checkForKey == "yes":
    accessKey = input("Enter acess key:")
    if accessKey == currentKey:
        currentV = "1.5.1"
        currentInput = ""
        personName = "user"
        systemRunning = "yes"

        print("")
        print("")
        print("running var tests:")
        print("currentV = " + currentV)
        print("currentInput = null")
        print("personName = " + personName)
        print("systemRunning = " + systemRunning)
        print("")
        print("tests completed")
        print("")
        print("starting Max MaxShell V" + currentV)
        print("")
        print("Welcome!")
        print("To get started, type 'help' to learn some commands")
        print("--")
        while systemRunning == "yes":
            currentInput = input(personName + ":")

            if currentInput == "help":
                print("")
                print("help center:")
                print("showInput | A simple command to show the input")
                print("shutdown | Shuts down program")
                print("--v | Displays current version")
                print("--s | Support Max")
                print("--i | Info")
                print("physCalc | Calculations that are useful for physics")
                print("geoCalc | Calculations that are useful for Geometry")
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
                while geoInput != close:
                    print()
                    print("GeoCalc Started")
                    print("Type 'help' for commands.")
                    print()
                    geoInput = input(currentInput + "/geo:")
                    if geoInput == "help":
                        print()
                        print("calcPythag")
                        print()
                    elif geoInput == "calcPythag":
                        print("")
                        print("Insert A")
                        geoInputA = int(input(currentUser + "/geo:"))
                        print()
                        print("Insert B")
                        geoInputB = int(input(currentUser + "/geo:"))
                        geoAPrp = geoInputA**2
                        geoBPrp = geoInputB**2
                        geoC = geoAPrp + geoBPrp
                        geoCprp = sqrt(geoC)
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
    elif accessKey == "change":
        testKey = input("Insert current Acess Key:")
        if testKey == accessKey:
            newKey = input("Type in new key:")
            acessKey = newKey

    else:
        print("ERROR: Acess Key Invalid")
