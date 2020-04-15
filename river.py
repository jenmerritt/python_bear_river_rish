class River:
    def __init__(self, name, fishes):
        self.name = name
        self.fishes = fishes

    def get_name(self):
        return self.name
    
    def get_number_of_fish(self):
        return len(self.fishes)
    
    def add_fish(self, fish):
        self.fishes.append(fish)
    
    def yield_fish(self):
        if len(self.fishes) > 0:
            return self.fishes.pop()
        else:
            pass