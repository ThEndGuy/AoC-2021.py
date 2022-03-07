#!/usr/bin/env python

def file_read(_file):
    with open(_file, 'r') as f:
        lines = f.readlines()
        return [int(x) for x in lines[0] if x not in (',', '\n')]

class LFish:


    def __init__(self, current_age, just_created=True, default_age=6):
        self.current_age = current_age
        self.default_age = default_age
        self.make_fish = False

    def advance_one_day(self):
        if self.current_age > 0:
            self.current_age -= 1
            return False
        elif self.current_age == 0:
            self.current_age = self.default_age
            return True
        else:
            raise ValueError(f'{self} should not have a negative age')

    def __repr__(self):
        return f"Fish({(self.current_age)})"

    def get_age(self):
        return self.current_age

    def create_fish(self):
        if self.make_fish:
            self.make_fish = False
            return True


starting_age = file_read('input.txt')
# starting_age = [3,4,3,1,2]
starting_fishes = [LFish(fish, False) for fish in starting_age]
for _ in range(256):
    new_fishes = []
    for fish in starting_fishes:
        if fish.advance_one_day():
            new_fishes.append(LFish(8))
    starting_fishes += new_fishes

print(len(starting_fishes))
#print(sum([fish.get_age() for fish in starting_fishes]))
