class Room:
    # Constructor
    def __init__(self, name: str):
        self.name = name
        self.exit_directions: list[str] = []  # north, south, east, ...
        self.exit_destinations: list['Room'] = []
        self.items: list[str] = []
        self.item_descriptions: list[str] = []
        self.lootables = []
        self.openables = []
        self.openables_descriptions = []
        self.usables = []
        self.usables_descriptions = []

    # Getters/Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Room name must be a string")

    @property
    def exit_directions(self):
        return self._exit_directions

    @exit_directions.setter
    def exit_directions(self, value: list[str]):
        self._exit_directions = value

    @property
    def exit_destinations(self):
        return self._exit_destinations

    @exit_destinations.setter
    def exit_destinations(self, value: list['Room']):
        self._exit_destinations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value: list[str]):
        self._items = value

    @property
    def item_descriptions(self):
        return self._item_descriptions

    @item_descriptions.setter
    def item_descriptions(self, value: list[str]):
        self._item_descriptions = value

    @property
    def lootables(self):
        return self._lootables

    @lootables.setter
    def lootables(self, value: list[str]):
        self._lootables = value

    @property
    def openables(self):
        return self._openables

    @openables.setter
    def openables(self, value: list[str]):
        self._openables = value

    @property
    def usables(self):
        return self._usables

    @usables.setter
    def usables(self, value: list[str]):
        self._usables = value

    # Additional Methods
    def add_exit(self, exit_direction: str, exit_destination: 'Room'):
        self.exit_directions.append(exit_direction)
        self.exit_destinations.append(exit_destination)

    def add_item(self, item_name: str, item_description: str):
        self.items.append(item_name)
        self.item_descriptions.append(item_description)  # Correctly appends

    def add_lootable(self, new_lootable: str):
        self.lootables.append(new_lootable)

    def delete_lootable(self, existing_lootable: str):
        if existing_lootable in self.lootables:
            self.lootables.remove(existing_lootable)

    def open_openable(self, new_openable: str):
        self.openables.append(new_openable)

    def delete_openable(self, existing_openable: str):
        if existing_openable in self.openables:
            self.openables.remove(existing_openable)

    def use_usable(self, new_usable: str):
        self.usables.append(new_usable)

    def delete_usable(self, existing_usable: str):
        if existing_usable in self.usables:
            self.usables.remove(existing_usable)

    def add_usable(self, usable_name: str, usable_description: str):
        self.usables.append(usable_name)
        self.usables_descriptions.append(usable_description)

    # String representation
    def __str__(self):
        result = []

        # Where we are
        result.append(f"Location: {self.name}")

        # What we see
        if self.items:
            result.append("You see:")
            for item in self.items:
                result.append(f"  - {item}")

        # Exits
        if self.exit_directions:
            result.append("Exits:")
            for direction in self.exit_directions:
                result.append(f"  - {direction}")

        return "\n".join(result)


# Test the Room class
if __name__ == "__main__":
    r1 = Room("Room 1")
    r2 = Room("Room 2")

    r1.add_exit("East", r2)
    r1.add_item("chair", "It is made of wicker")
    r1.add_lootable("key")
    r1.delete_lootable("key")

    print(r1)
