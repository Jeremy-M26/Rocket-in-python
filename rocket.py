#Rocket launch Jeremy M.
import time
rocket = """
      /\\
     /  \\
    /    \\
   /      \\
  /________\\
  |   /\\   |
  |  /  \\  |
  | /    \\ |
  |/______\\|
  |   ||   |
  |   ||   |
  |   ||   |
  |   ||   |
 /|   ||   |\\
| |   ||   | |
| |   ||   | |
| |   ||   | |
|_|___||___|_|
"""
rocket_on = """
      /\\
     /  \\
    /    \\
   /      \\
  /________\\
  |   /\\   |
  |  /  \\  |
  | /    \\ |
  |/______\\|
  |   ||   |
  |   ||   |
  |   ||   |
  |   ||   |
 /|   ||   |\\
| |   ||   | |
| |   ||   | |
| |   ||   | |
|_|___||___|_|
vvvvvvvvvvvvvv
  vvvvvvvvvv
    vvvvvv
      vv
"""

def home():
    print("Welcome to Cabo Cañaveral")
    confirm = input("Do you want to launch a rocket [Y] or [N]?")
    ignition = False

    if confirm.upper() == "Y":
        ignition = True
        if ignition:
            for i in range(3):
                time.sleep(3)
                print("\n" * 25)
                print("Placing platform...")
                if i == 2:
                    print("\n" * 25)
                    time.sleep(2)
                    break
            print("Rocket ready!")
            print(rocket)
            time.sleep(4)
            print("\n" * 50)

            launch = input("Start engines [Y] or [N]?")
            if launch.upper() == "Y":
                for j in reversed(range(0,11)):
                    print(j)
                    time.sleep(1)
                    print("\n" * 100)
                    if j <= 0:
                        print("\n" * 100)
                        print("Lift off!")
                        print(rocket_on)
                        time.sleep(15)
            elif launch.upper() == "N":
                time.sleep(1)
                print("\n" * 50)
                time.sleep(5)
                print("Shutting down...")
                print("\n" * 50)
                home()

    elif confirm.upper() == "N":
        ignition = False
    else:
        print("Wrong choice! Reloading...")
        print("\n" * 50)
        home()

home()