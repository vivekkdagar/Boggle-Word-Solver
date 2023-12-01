# Boggle-Word-Solver
> A Python Boggle game solver that finds valid words on a 4x4 grid using a custom word database.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Components](#components)
   - [Main Program (main.py)](#main-program-mainpy)
   - [Word Tree (WordTree.py)](#word-tree-wordtreepy)
   - [Boggle Game (BoggleGame.py)](#boggle-game-bogglegamepy)
4. [How the Game Works](#how-the-game-works)
   - [Boggle Board](#boggle-board)
   - [Word Validation](#word-validation)
   - [Algorithm Overview](#algorithm-overview)
5. [Usage Guide](#usage-guide)
   - [Installation](#installation)
   - [Running the Game](#running-the-game)
   - [Entering the Boggle Board](#entering-the-boggle-board)
   - [Viewing Valid Words](#viewing-valid-words)
   - [Adding a Word to the Database](#adding-a-word-to-the-database)
6. [Conclusion](#conclusion)

## 1. Introduction<a name="introduction"></a>
Boggle is a word game where players search for words on a 4x4 grid of letters. This project implements a Boggle Game solver that takes a Boggle board as input and finds all valid words that can be formed on that board based on a provided word database.

![Example](https://www.cs.oberlin.edu/~rhoyle/19s-cs151/lab10/Boggle1.png)

## 2. Project Structure<a name="project-structure"></a>

The project is organized into three main components:

- `main.py`: The main program responsible for user interaction and running the Boggle game.
- `WordTree.py`: The WordTree class, which is used to store a dictionary of valid words and find words on the Boggle board.
- `BoggleGame.py`: The BoggleGame class, which handles the game logic, including loading the word database and solving the Boggle board.

## 3. Components<a name="components"></a>

### Main Program (main.py)<a name="main-program-mainpy"></a>

The `main.py` file serves as the entry point of the program. It allows users to input a Boggle board, loads a word database, and then finds and displays valid words on the board.

### Word Tree (WordTree.py)<a name="word-tree-wordtreepy"></a>

The `WordTree` class in `WordTree.py` is responsible for storing a dictionary of valid words and finding words on the Boggle board. It uses a tree-like data structure to efficiently search for words.

### Boggle Game (BoggleGame.py)<a name="boggle-game-bogglegamepy"></a>

The `BoggleGame` class in `BoggleGame.py` manages the core logic of the Boggle game. It loads the word database, solves the Boggle board, and prints the board and valid words.

## 4. How the Game Works<a name="how-the-game-works"></a>

### Boggle Board<a name="boggle-board"></a>

The Boggle board is a 4x4 grid of letters. Users input this grid as a list of lists, where each inner list represents a row of letters. The game board is displayed to the user.

### Word Validation<a name="word-validation"></a>

The program validates words against a word database. If a sequence of letters on the Boggle board forms a valid word in the dictionary, it is considered a valid word.

### Algorithm Overview<a name="algorithm-overview"></a>

1. The Boggle board is represented as a 4x4 grid of letters.
2. The program uses a recursive depth-first search (DFS) algorithm to explore all possible paths on the board.
3. During the DFS traversal, it checks if the current path forms a valid word by consulting the WordTree, which stores the valid words.
4. Valid words are added to the list of validated words.
5. The program returns a sorted list of validated words to be displayed to the user.

## 5. Usage Guide<a name="usage-guide"></a>

### Installation<a name="installation"></a>

Before running the Boggle game, ensure you have the required dependencies installed. You can use `pip` or `conda` for installation.

#### Using Pip
```bash
pip install prettytable
```

#### Using Conda
```bash
conda install prettytable
```

### Running the Game<a name="running-the-game"></a>

To run the Boggle game, execute the `main.py` script:

```bash
python3 main.py
```

### Entering the Boggle Board<a name="entering-the-boggle-board"></a>

1. When prompted, enter the Boggle board as a 4x4 grid of letters. Each row should be entered on a separate line.
2. Ensure that each row contains exactly four letters.
3. The board will be displayed to you.

### Viewing Valid Words<a name="viewing-valid-words"></a>

After entering the Boggle board, the program will display the valid words found on the board.

### Adding a Word to the Database<a name="adding-a-word-to-the-database"></a>

To add a word

 to the word database (`word_database.txt`), follow these steps:

1. Open the `word_database.txt` file in a text editor.
2. Add the new word to the file, ensuring it is in uppercase and follows the format of one word per line.
3. Save the file.

## 6. Conclusion<a name="conclusion"></a>

This documentation has provided a thorough understanding of the Boggle Game project, including its structure, components, how it works, and how to use it. Have fun playing Boggle and finding words on the board! If you have any questions or need further assistance, please don't hesitate to ask.
