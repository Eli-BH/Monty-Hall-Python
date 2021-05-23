import random 

def monty_hall_switch(pick):
    wins = 0
    lose = 0
    doors = ['door1', 'door2', 'door3']
    for i in range(1, 1001):
        print("You have chosen " +  doors[pick] + "!")
        pick1 = doors[pick]
        car = random.choice(doors)
        goat1 = random.choice(doors)
        while goat1 == car:
            goat1 = random.choice(doors)
        goat2 = random.choice(doors)
        while goat2 == goat1 or goat2 == car:
            goat2 = random.choice(doors)
        monty = random.choice(doors)
        while monty == car or monty == pick1:
            monty = random.choice(doors)
        print("You will now switch doors.")
        pick2 = random.choice(doors)
        while pick2 == pick1 or pick2 == monty:
            pick2 = random.choice(doors)
        if pick2 == car:
            print("You win the car!")
            wins += 1
            i += 1
        if pick2 != car:
            print("You loose!")
            lose += 1
            i += 1
    wins = (wins * 100) / 1000
    lose = (lose * 100) / 1000
    print("\nYou won %" + str(wins) + " of the time.")
    print("You lost %" +str(lose) + " of the time.")
    return wins

def monty_hall_stay(pick):
    wins = 0
    lose = 0
    doors = ['door1', 'door2', 'door3']
    for i in range(1, 1001):
        print("You have chosen " +  doors[pick] + "!")
        pick1 = doors[pick]
        car = random.choice(doors)
        goat1 = random.choice(doors)
        while goat1 == car:
            goat1 = random.choice(doors)
        goat2 = random.choice(doors)
        while goat2 == goat1 or goat2 == car:
            goat2 = random.choice(doors)
        monty = random.choice(doors)
        while monty == car or monty == pick1:
            monty = random.choice(doors)
        print("You will now stay on your original pick.")
        pick2 = pick1
        if pick2 == car:
            print("You win the car!")
            wins += 1
            i += 1
        if pick2 != car:
            print("You loose!")
            lose += 1
            i += 1
    wins = (wins * 100) / 1000
    lose = (lose * 100) / 1000
    print("\nYou won %" + str(wins) + " of the time.")
    print("You lost %" +str(lose) + " of the time.")
    return wins

def monty_random(pick):
    wins = 0
    lose = 0
    doors = ['door1', 'door2', 'door3']
    for i in range(1, 1001):
        print("You have chosen " +  doors[pick] + "!")
        pick1 = doors[pick]
        car = random.choice(doors)
        goat1 = random.choice(doors)
        while goat1 == car:
            goat1 = random.choice(doors)
        goat2 = random.choice(doors)
        while goat2 == goat1 or goat2 == car:
            goat2 = random.choice(doors)
        monty = random.choice(doors)
        while monty == car:
            monty = random.choice(doors)
        print("You will now switch doors.")
        pick2 = random.choice(doors)
        while pick2 == monty:
            pick2 = random.choice(doors)
        if pick2 == car:
            print("You win the car!")
            wins += 1
            i += 1
        if pick2 != car:
            print("You loose!")
            lose += 1
            i += 1
    wins = (wins * 100) / 1000
    lose = (lose * 100) / 1000
    print("\nYou won %" + str(wins) + " of the time.")
    print("You lost %" +str(lose) + " of the time.")
    return wins

def monty_hall_problems(pick):
    switch = monty_hall_switch(pick)
    stay = monty_hall_stay(pick)
    rando = monty_random(pick)
    print("These are the results of the Monty Hall problem out of 3000 runs.")
    print("The results come from switching, staying and switching at random," +
    " each done 1000 times. Each tactics percentage of wins are shown below. \n")
    print("\nIf you stay, you win %" + str(stay) + " of the time out of.")
    print("If you switch, you win %" + str(switch) + " of the time out of.")
    print("If you chose randomly, you win %" + str(rando) + " of the time.")

try:
    door = int(input("Door Selection: Please Enter 0, 1, or 2"))
except ValueError:
    print("Please only select the presented doors.")

monty_hall_problems(door)

input("Enter any key to exit.")
 