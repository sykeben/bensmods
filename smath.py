# Ben's Mods "smath" Module
# (C)2018 - Ben Sykes

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num, exp):
    return pow(num, exp)

def squareroot(num):
    return sqrt(num)

def demoterm():
    smath_quitdemo = False
    smath_demofirst = True
    while not(smath_quitdemo):

        if not(smath_demofirst):
            print("")

        smath_demofirst = False
        smath_democommand = input("CMD~> ").lower()

        if smath_democommand == "":
            smath_demofirst = True

        elif smath_democommand == "quit":
            smath_quitdemo = True

        elif smath_democommand == "add":
            smath_demonum1ok = True
            try:
                smath_demonum1 = float(input("NUM1? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                smath_demonum2ok = True
                try:
                    smath_demonum2 = float(input("NUM2? "))
                except TypeError:
                    smath_demonum2ok = False
                    print("Invalid type.")
                except ValueError:
                    smath_demonum2ok = False
                    print("Invalid value.")
            if smath_demonum1ok and smath_demonum2ok:
                print("= ", end='')
                print(str(add(smath_demonum1,smath_demonum2)))

        elif smath_democommand == "subtract":
            smath_demonum1ok = True
            try:
                smath_demonum1 = float(input("NUM1? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                smath_demonum2ok = True
                try:
                    smath_demonum2 = float(input("NUM2? "))
                except TypeError:
                    smath_demonum2ok = False
                    print("Invalid type.")
                except ValueError:
                    smath_demonum2ok = False
                    print("Invalid value.")
            if smath_demonum1ok and smath_demonum2ok:
                print("= ", end='')
                print(str(subtract(smath_demonum1,smath_demonum2)))

        elif smath_democommand == "multiply":
            smath_demonum1ok = True
            try:
                smath_demonum1 = float(input("NUM1? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                smath_demonum2ok = True
                try:
                    smath_demonum2 = float(input("NUM2? "))
                except TypeError:
                    smath_demonum2ok = False
                    print("Invalid type.")
                except ValueError:
                    smath_demonum2ok = False
                    print("Invalid value.")
            if smath_demonum1ok and smath_demonum2ok:
                print("= ", end='')
                print(str(multiply(smath_demonum1,smath_demonum2)))

        elif smath_democommand == "divide":
            smath_demonum1ok = True
            try:
                smath_demonum1 = float(input("NUM1? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                smath_demonum2ok = True
                try:
                    smath_demonum2 = float(input("NUM2? "))
                except TypeError:
                    smath_demonum2ok = False
                    print("Invalid type.")
                except ValueError:
                    smath_demonum2ok = False
                    print("Invalid value.")
            if smath_demonum1ok and smath_demonum2ok:
                print("= ", end='')
                print(str(divide(smath_demonum1,smath_demonum2)))

        elif smath_democommand == "power":
            smath_demonum1ok = True
            try:
                smath_demonum1 = int(input("NUM~? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                smath_demonum2ok = True
                try:
                    smath_demonum2 = int(input("EXP? "))
                except TypeError:
                    smath_demonum2ok = False
                    print("Invalid type.")
                except ValueError:
                    smath_demonum2ok = False
                    print("Invalid value.")
            if smath_demonum1ok and smath_demonum2ok:
                print("= ", end='')
                print(str(power(smath_demonum1,smath_demonum2)))

        elif smath_democommand == "sqrt":
            smath_demonum1ok = True
            try:
                smath_demonum1 = float(input("NUM~? "))
            except TypeError:
                smath_demonum1ok = False
                print("Invalid type.")
            except ValueError:
                smath_demonum1ok = False
                print("Invalid value.")
            if smath_demonum1ok:
                print("= ", end='')
                print(str(squareroot(smath_demonum1)))

        else:
            print("Invalid command.")