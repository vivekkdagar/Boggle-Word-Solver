#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:34:47 2023

@author: vivekdagar
"""

from prettytable import PrettyTable
from WordTree import WordTree

class BoggleGame:
    def __init__(self, board):
        self.board = board
        self.word_tree = WordTree()

    def load_word_database(self, filename):
        # Load words from a file into the word tree
        with open(filename, 'r') as dict_file:
            for line in dict_file:
                self.word_tree.add_word(line.strip().upper())

    def solve(self):
        # Find and return the sorted list of validated words
        self.word_tree.find_words(self.board)
        return sorted(self.word_tree.validated)

    def print_board(self):
        # Print the Boggle board
        for row in self.board:
            print(' '.join(row))

    def print_valid_words(self):
        valid_words = self.solve()
        if valid_words:
            # Create a table for valid words using PrettyTable
            table = PrettyTable(["Valid Words"])
            for word in valid_words:
                table.add_row([word])
            print(table)
        else:
            print("No valid words found.")
