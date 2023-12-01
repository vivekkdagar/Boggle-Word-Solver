from BoggleGame import BoggleGame

def main():
    print("Enter the Boggle Game Board (4x4 grid):")
    board = [input().strip().upper().split() for _ in range(4)]
    
    if not all(len(row) == 4 for row in board):
        print("Invalid input. Please enter 4 letters for each row.")
        return

    # Initialize the Boggle game and load the word database
    game = BoggleGame(board)
    game.load_word_database('word_database.txt')
    
    # Print the Boggle board and valid words
    print("\nBoggle Game Board:")
    game.print_board()
    print("\nValid Words:")
    game.print_valid_words()

if __name__ == "__main__":
    main()
