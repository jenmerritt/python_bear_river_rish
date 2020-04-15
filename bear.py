class Bear:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.stomach = []

    def get_name(self):
        return self.name
    
    def get_breed(self):
        return self.breed
    
    def get_number_of_fish_in_stomach(self):
        return len(self.stomach)

    def roar(self):
        return "ROAR!"
    
    def take_fish(self, river):
        if len(river.fishes) > 0:
            fish = river.yield_fish()
            self.stomach.append(fish)
    
