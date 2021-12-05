#!/usr/bin/env python

import numpy as np


class BingoBoard:
    def __init__(self, board: np.array):
        self.board = board
        self.h, self.w = len(self.board), len(self.board[0])
        self.bool_board = np.array([[False for _ in board[0]].copy() for _ in board])

    def __repr__(self):
        return str(self.board)

    def mark_number(self, num: int):
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i, j] == num:
                    self.bool_board[i, j] = True
                    return i, j
        return None

    def check_bingo(self, posx, posy):
        return all(self.bool_board[posx, :]) or all(self.bool_board[:, posy])

    def mark_and_check(self, num):
        result = self.mark_number(num)
        if result is None:
            return None
        posx, posy = result
        return self.check_bingo(posx, posy)

    def sum_not_marked(self):
        summ = 0
        for i in range(self.h):
            for j in range(self.w):
                if not self.bool_board[i, j]:
                    summ += self.board[i, j]
        return summ


def interpret_boards(_file: str):
    with open(_file, "r") as f:
        lines = f.readlines()
        call_nums = lines.pop(0).split(",")
        call_nums = [int(x) for x in call_nums]
        boards = []
        for i, line in enumerate(lines):
            if line == "\n":
                boards.append([])
            else:
                line = line.strip("\n")
                sline = line.split(" ")
                sline = [int(x) for x in sline if x != ""]
                boards[i // 6].append(sline)
        boards = [BingoBoard(np.array(board)) for board in boards]
    return call_nums, boards


def calculate_first_bingo(call_nums, boards):
    for num in call_nums:
        for board in boards:
            if board.mark_and_check(num):
                return board.sum_not_marked() * num
    assert False, "No board was completed (Impossible)"


call_nums, boards = interpret_boards("input.txt")
# Uncomment for first part
# print(calculate_first_bingo(call_nums, boards))

## PART 2 ##
# THIS PART CURRENTLY DOES NOT WORK
# TODO: Fix part 2


def calculate_last_bingo(call_nums, boards):
    for num in call_nums:
        for board in boards:
            if board.mark_and_check(num):
                boards.remove(board)
    return last_board_score


print(calculate_last_bingo(call_nums, boards))
