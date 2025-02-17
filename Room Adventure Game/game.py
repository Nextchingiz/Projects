# Import libraries
from room import Room 
from time import sleep

class Game:
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.response = ""
        self.running = True
        self.create_rooms()

    def create_rooms(self):
        """Create the rooms that exist in the game."""
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")

        # Adding exits to the rooms
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)

        # Adding items
        r1.add_item("chair", "It only has 3 legs, so I'm not going to sit on it.")
        r1.add_item("table", "It has a key on it. Maybe we should take it.")

        r2.add_item("couch", "It looks soft. But I'm not going to sit on it.")
        r2.add_item("empty-pizza-box", "It looks greasy. Maybe I can take it. There is a wire coming out of it.")

        r3.add_item("fridge-lamp", "It looks like a lamp, but it's cold inside and there's cheese.")
        r3.add_item("frog", "It's noisy and pretty. I don't want to sit on it. Although, it has something shiny inside.")

        r4.add_item("hand", "Yes, a human hand. It doesn't want to sit on me.")
        r4.add_item("pokeball", "Maybe I can take it to capture the frog. It has a button, maybe I can use it.")

        # Adding lootables
        r1.add_lootable("key")
        r2.add_lootable("empty-pizza-box")
        r3.add_lootable("cheese")
        r4.add_lootable("pokeball")

        # Adding objects that can be opened
        r2.open_openable("empty-pizza-box")
        r3.open_openable("frog")
        r4.open_openable("pokeball")

        # Objects you can use
        r2.use_usable("headphones")
        r3.use_usable("battery")
        r4.use_usable("mp3")

        # Adding objects you can use
        r2.add_usable("headphones", "It has a number 3 written on it, weird.")
        r3.add_usable("battery", "It has a sticker with a number 2.")
        r4.add_usable("mp3", "There is a number 1 on the backside.")

        # Set the current room
        self.current_room = r1

    def play(self):
        while self.running:
            if self.current_room is None:
                self.death()
                break

            # Display current game status
            status = f"\n{self.current_room}"
            if self.inventory:
                status += f"\nYou are carrying: {', '.join(self.inventory)}"
            else:
                status += "\nYou have no items in your inventory."
            print(status)

            # Default response
            self.response = "I only understand the verbs 'go', 'look', 'take', 'open', and 'use'."
            self.response += "\nType 'quit' to exit the game."

            # Prompt the user
            action = input("What would you like to do? ").lower().strip()

            # Does the user want to quit?
            if action in ["quit", "q", "exit", "bye", "see ya", "ciao"]:
                self.running = False
                break

            # Rickroll Easter Egg
            if action == "use mp3 battery headphones":
                if all(item in self.inventory for item in ["mp3", "battery", "headphones"]):
                    self.response = "🎵 Never gonna give you up, never gonna let you down... 🎵\nYOU GOT RICKROLLED"
                    for item in ["mp3", "battery", "headphones"]:
                        self.inventory.remove(item)
                else:
                    self.response = "You don't have all the required items to use them together."
            else:
                # Interpret the input
                words = action.split()
                if len(words) == 2:
                    verb, noun = words
                    if verb == "go":
                        self.handle_go(noun)
                    elif verb == "look":
                        self.handle_look(noun)
                    elif verb == "take":
                        self.handle_take(noun)
                    elif verb == "open":
                        self.handle_open(noun)
                    elif verb == "use":
                        self.handle_use(noun)
                    else:
                        self.response = "Invalid verb. Try 'go', 'look', 'take', 'open', or 'use'."
                else:
                    self.response = "Invalid input. Use the format '[verb] [noun]'."

            print(self.response)
            sleep(1)


    def handle_go(self, noun):
        if noun in self.current_room.exit_directions:
            index = self.current_room.exit_directions.index(noun)
            self.current_room = self.current_room.exit_destinations[index]
            self.response = "You moved to a new room."
        else:
            self.response = "Invalid exit."

    def handle_look(self, noun):
        if noun in self.current_room.items:
            index = self.current_room.items.index(noun)
            self.response = self.current_room.item_descriptions[index]
        else:
            self.response = "That item does not exist here."

    def handle_take(self, noun):
        if noun in self.current_room.lootables:
            self.inventory.append(noun)
            self.current_room.delete_lootable(noun)
            self.response = f"Grabbed {noun}."
        elif noun in self.current_room.items:
            self.inventory.append(noun)
            self.current_room.items.remove(noun)
            self.response = f"Picked up {noun}."
        else:
            self.response = "That is not something you can take."

    def handle_open(self, noun):
        if noun in self.current_room.openables:
            self.response = f"You opened the {noun}.\n"
            if noun == "frog":
                self.response += "Inside, you find a battery. It has a sticker with a number 2 on the back."
                self.current_room.add_item("battery", "A small rectangular battery. It has a sticker with a number 2 on the back.")
            elif noun == "pokeball":
                self.response += "Inside, you find an mp3. It has a number 1 written on the back."
                self.current_room.add_item("mp3", "An mp3 with some music probably. It has a number 1 written on the back.")
            elif noun == "empty-pizza-box":
                self.response += "Inside, you find some headphones. It has 3 lines on the side."
                self.current_room.add_item("headphones", "A pair of purple headphones. It has 3 lines on the side.")
            else:
                self.response += "There's nothing inside."
        else:
            self.response = "That is not something you can open."

    def handle_use(self, noun):
        if noun in ["mp3", "battery", "headphones"]:
            if noun in self.inventory:
                self.response = f"You are holding {noun}, but it cannot be used by itself."
            else:
                self.response = "You cannot use this object as it is not in your inventory."
        else:
            self.response = "That is not something you can use."

    def death(self):
        print("You fell out a window and died. 💀💀")

if __name__ == "__main__":
    g = Game()
    g.play()

