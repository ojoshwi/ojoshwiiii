import random
import time
import pickle
import os

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.turns_above_80 = 0

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
        print(f"{self.name} is being fed. Hunger is now {self.hunger}.")

    def play(self):
        if self.energy >= 10:
            self.happiness += 10
            self.energy -= 10
            print(f"{self.name} played! Happiness is now {self.happiness} and Energy is {self.energy}.")
        else:
            print(f"{self.name} is too tired to play!")

    def rest(self):
        self.energy += 10
        self.hunger = max(0, self.hunger - 5)
        print(f"{self.name} is resting. Energy is now {self.energy} and Hunger is {self.hunger}.")

    def check_status(self):
        print(f"\n{self.name}'s current status: Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}\n")
        
    def random_event(self):
        event = random.choice(['toy', 'rainy_day', 'nothing'])
        if event == 'toy':
            self.happiness += 20
            print(f"{self.name} found a toy! Happiness increased by 20.")
        elif event == 'rainy_day':
            self.energy -= 10
            print(f"A rainy day makes {self.name} tired. Energy decreased by 10.")
        else:
            print(f"{self.name} encountered nothing special today.")

    def is_sick(self):
        return self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0

    def check_win(self):
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.turns_above_80 += 1
        else:
            self.turns_above_80 = 0

        if self.turns_above_80 >= 3:
            print(f"\nCongratulations! {self.name} has become super happy and energetic!")
            return True
        return False

def save_game(pet):
    with open('pet_game_save.pkl', 'wb') as f:
        pickle.dump(pet, f)
    print("\nGame saved successfully.")

def load_game():
    if os.path.exists('pet_game_save.pkl'):
        with open('pet_game_save.pkl', 'rb') as f:
            pet = pickle.load(f)
        print("\nGame loaded successfully.")
        return pet
    else:
        print("\nNo saved game found.")
        return None

def game():
    print("Welcome to the Pet Game!")
    name = input("What will you name your pet? ")

    pet = Pet(name)
    print(f"\nWelcome, {pet.name}!\n")

    while True:
        pet.check_status()

        if pet.is_sick():
            print(f"{pet.name} is sick! Game Over!")
            break

        if pet.check_win():
            break

        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Check Stats")
        print("5. Random Event")
        print("6. Save Game")
        print("7. Load Game")
        print("8. Quit")

        try:
            action = int(input("\nChoose an action (1-8): "))
            if action == 1:
                pet.feed()
            elif action == 2:
                pet.play()
            elif action == 3:
                pet.rest()
            elif action == 4:
                pet.check_status()
            elif action == 5:
                pet.random_event()
            elif action == 6:
                save_game(pet)
            elif action == 7:
                loaded_pet = load_game()
                if loaded_pet:
                    pet = loaded_pet
            elif action == 8:
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")

        print("You have 10 seconds to make your next move...")
        time.sleep(10)

game()
                   