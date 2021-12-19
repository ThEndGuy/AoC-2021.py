#!/usr/bin/env python

def read_file(_file):
    with open(_file, 'r') as f:
       lines = [line.strip('\n') for line in f.readlines()]
       for line in lines:
           curr_line = line.split(' ')

class Cell:
    def __init__(self, state=0):
        self.state = state

    def __repr__(self):
        return str(self.state) if self.state else '.'

    def add_cross(self, crosses=1):
        self.state += crosses

class Grid:
    def __init__(self, w:int, h:int):
        self.w = w
        self.h = h
        self.grid = [[Cell() for _ in range(w)].copy() for _ in range(h)]

    def draw_line(self, spt:tuple, ept:tuple) -> None:
        if spt[0] == ept[0]:
            col = spt[0]
            strt = spt[1] if spt[1] > ept[1] else ept[1]
            end = ept[1] if spt[1] > ept[1] else spt[1]
            for i in range(end, strt):
                self.grid[col][i].add_cross()
        elif spt[1] == ept[1]:
            row = spt[1]
            strt = spt[0] if spt[0] > ept[0] else ept[0]
            end = ept[0] if spt[0] > ept[0] else spt[0]
            for i in range(end, strt):
                self.grid[i][row].add_cross()


    def find_above(self, num):
        count = 0
        for i, row in self.grid:
            for j, col in row:
               if col.state >= num:
                   count += 1
        return count
