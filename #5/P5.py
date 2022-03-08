#!/usr/bin/env python


def read_file(_file: str) -> list:
    with open(_file, "r") as f:
        lines = [line.strip("\n").split(" ") for line in f.readlines()]
    coord_lines = [[].copy() for _ in lines]
    for i, line in enumerate(lines):
        for word in line:
            if word == "->":
                continue
            word = tuple(int(x) for x in word.split(","))
            coord_lines[i].append(word)
    return coord_lines


class Cell:
    def __init__(self, state=0):
        self.state = state

    def __repr__(self):
        return str(self.state) if self.state else "."

    def add_cross(self, crosses=1):
        self.state += crosses


class Grid:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.grid = [[Cell() for _ in range(w)].copy() for _ in range(h)]

    def __repr__(self):
        strr = ""
        for item in self.grid:
            strr += f"{item}\n"
        return strr

    def output_to_file(self, _file):
        with open(_file, "w") as f:
            for item in self.grid:
                f.write(f"{item}\n")
        print(f"'{_file}' written.")

    def draw_line(self, spt: tuple, ept: tuple, diag=True) -> None:
        r_strt = max(spt[1], ept[1])
        r_end = min(spt[1], ept[1])
        c_strt = max(spt[0], ept[0])
        c_end = min(spt[0], ept[0])

        if spt[0] - ept[0] == spt[1] - ept[1] and diag is True:
            for i, j in zip(range(r_end, r_strt + 1), range(c_end, c_strt + 1)):
                self.grid[i][j].add_cross()
        elif spt[0] - ept[0] == ept[1] - spt[1] and diag is True:
            if spt[0] > ept[0]:
                for i, j in zip(range(r_strt, r_end - 1, -1), range(c_end, c_strt + 1)):
                    self.grid[i][j].add_cross()
            else:
                for i, j in zip(range(r_end, r_strt + 1), range(c_strt, c_end - 1, -1)):
                    self.grid[i][j].add_cross()
        elif spt[0] == ept[0]:
            col = spt[0]
            for i in range(r_end, r_strt + 1):
                self.grid[i][col].add_cross()
        elif spt[1] == ept[1]:
            row = spt[1]
            for i in range(c_end, c_strt + 1):
                self.grid[row][i].add_cross()

    def find_above(self, num):
        count = 0
        for row in self.grid:
            for col in row:
                if col.state >= num:
                    count += 1
        return count

    def draw_lines(self, _file: str, diag=True) -> None:
        coords = read_file(_file)
        for coord in coords:
            self.draw_line(coord[0], coord[1], diag)


G = Grid(1000, 1000)
G.draw_lines("input.txt", diag=True)  # diag=False for the first problem
print(G.find_above(2))
