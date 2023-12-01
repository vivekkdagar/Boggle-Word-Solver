#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:33:32 2023

@author: vivekdagar
"""

class WordTree:
    def __init__(self):
        # Initialize the word tree with an empty root node and an empty set for validated words
        self.root = {}
        self.validated = set()

    def add_word(self, word):
        node = self.root
        # Iterate through each letter in the word
        for letter in word:
            # Create a new node if the letter is not already present
            node = node.setdefault(letter, {})
        # Mark the end of a word with '*'
        node['*'] = True

    def find_words(self, board):
        def dfs(row, col, path, node, word):
            # Helper function for depth-first search to find words on the board
            if not (0 <= row < 4) or not (0 <= col < 4) or (row, col) in path:
                return
            letter = board[row][col]
            if letter in node:
                path.append((row, col))
                node = node[letter]
                word += letter
                if '*' in node and len(word) > 2:
                    self.validated.add(word)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        dfs(row + dr, col + dc, path, node, word)
                path.pop()

        # Iterate through the entire board to find words
        for r in range(4):
            for c in range(4):
                dfs(r, c, [], self.root, '')
