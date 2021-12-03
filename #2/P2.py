#!/usr/bin/env python

def text_interpreter(_file):
    with open(_file, 'r') as f:
        text = f.readlines()
        text = [word.strip("\n") for word in text]
    return text



class Submarine():
    def __init__(self, h=0, d=0):
        self.h = h
        self.d = d

    def execute(self, param:str):
        com = param.split(" ")
        units = int(com[1])
        if com[0] == 'forward':
            self.h += units
        elif com[0] == 'down':
            self.d += units
        elif com[0] == 'up':
            self.d -= units
        else:
            raise ValueError(f"{com[0]} is not a valid command")

    def get_pos(self):
        print(f"(horizontal = {self.h}, depth = {self.d})")


sub = Submarine()
text = text_interpreter("input.txt")
for command in text:
    sub.execute(command)
sub.get_pos()

class BetterSubmarine(Submarine):
    def __init__(self, h=0, d=0):
        super().__init__(h, d)
        self.aim = 0
    def execute(self, param: str):
        com = param.split(" ")
        units = int(com[1])
        if com[0] == 'forward':
            self.h += units
            self.d += self.aim*units
        elif com[0] == 'down':
            self.aim += units
        elif com[0] == 'up':
            self.aim -= units
        else:
            raise ValueError(f"{com[0]} is not a valid command")

sub = BetterSubmarine()
for command in text:
    sub.execute(command)
sub.get_pos()
