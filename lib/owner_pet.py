class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __str__(self):
        return f"{self.name} the {self.pet_type}"


Pet.all = []


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def pets(self):
        if not isinstance(self.pets, list):
            raise Exception("Expected list of pets")
        return self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Expected Pet object")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        if not isinstance(self.pets, list):
            raise Exception("Expected list of pets")
        return sorted(self.pets, key=lambda x: x.name)


if __name__ == "__main__":
    try:
        poodle = Pet("Fido", "dog")
        snake = Pet("Scales", "reptile")
        # Cat with no owner
        whiskers = Pet("Whiskers", "cat")
        joseph = Owner("Joseph")
        joseph.add_pet(poodle)
        joseph.add_pet(snake)
        print(joseph.pets())
        for pet in joseph.get_sorted_pets():
            print(pet)
    except Exception as e:
        print(f"Error: {e}")
