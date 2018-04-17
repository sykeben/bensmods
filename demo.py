# Ben's Mods Demo Script
# (C)2018 - Benjamin Sykes

print("Ben's Mods Demo")
print("(C)2018 - Ben Sykes")
print("")

print("Setting variables . . . ", end='')
quitall = False
menu = "main"
print("Done.")
print("")

print("Importing custom modules . . . ")
print("- fibo")
import fibo
print("- smath")
import smath
print("")

while not(quitall):

    while menu == "main":
        print("MAIN MENU")
        print("[0] Quit")
        print("[1] \"fibo\" Demo")
        print("[2] \"smath\" Terminal")
        option = input("(0-2)> ")
        print("")
        if option == "0":
            quitall = True
            menu = "quit"
        elif option == "1":
            menu = "fibodemo"
        elif option == "2":
            menu = "smathterm"
        else:
            print("Invalid option.")
            print("")

    while menu == "fibodemo":
        print("\"FIBO\" DEMO")
        print(str(fibo.genfib(1000)))
        print("")
        menu = "main"

    while menu == "smathterm":
        print("\"SMATH\" TERMINAL")
        print("")
        smath.demoterm()
        print("")
        menu = "main"