import random  # Import the random module to generate random numbers

# Function to roll two dice and return their values
def roll_dice():
    # Generate and return two random integers between 1 and 6
    # This simulates the rolling of two dice
    return random.randint(1, 6), random.randint(1, 6)

# Function to check if the chosen move is valid
def is_valid_move(board, choice):
    # Check if all numbers in the chosen move are available on the board
    # A move is valid if all chosen numbers are still available (represented by 1 on the board)
    return all(board[num-1] == 1 for num in choice)

# Function to make a move by "shutting" the chosen numbers
def make_move(board, choice):
    # Mark the chosen numbers as shut (set to 0)
    # This updates the board to reflect the chosen numbers have been used
    for num in choice:
        board[num-1] = 0 

# Function to get all possible moves that sum to the given total
def get_possible_moves(board, total):
    moves = [] # List to store all valid moves
    
    # Recursive function to find all possible moves
    def find_moves(start, path):
        # If the current path sums to the total, add it to the list of moves
        if sum(path) == total:
            moves.append(path)
            return
        # Try to add each number to the current path and check if it forms a valid move
        # Continue this process until all possible moves are found
        for i in range(start, len(board)):
            # Check if the current number is available on the board and if adding it doesn't exceed the total
            if board[i] == 1 and sum(path) + (i+1) <= total:
                find_moves(i+1, path + [i+1])  # Recur with the next number added to the path
    
    # Start finding moves from the beginning of the board
    # This ensures all combinations are checked
    find_moves(0, [])
    return moves

# Main function to play the game "Shut the Box"
def play_shut_the_box():
    while True:  # Loop to allow replaying the game
        # Initialize the board with numbers 1 to 9 (all available), all numbers are open at the start of the game. 
        board = [1] * 9 # It is set to 1, which means that the number is open (0 if it is closed). 
        while sum(board) > 0:  # Continue playing when there are open tiles
            # Display the current state of the board
            print("\nBoard:", [i+1 if board[i] else "X" for i in range(9)]) # Shows the numbers 1 to 9 for open tiles and "X" for closed tiles.
            # Get the roll_dice function to roll dice. dice1 and dice2 is the return values in the roll_dice function.
            dice1, dice2 = roll_dice()
            print(f"Rolled: {dice1} and {dice2}") # Print the number of each dice. 
            # Calculates the total of the dice roll and prints it.
            total = dice1 + dice2
            print(f"Total: {total}")

            # Get all possible moves for the current total
            possible_moves = get_possible_moves(board, total) # Determines possible moves that sum up to the dice total and checks if there are any.
            if not possible_moves:  # If there are no possible moves, the game is over
                print("No possible moves. Game over!")
                break

            # Display all possible moves
            print("Possible moves:")
            for move in possible_moves:
                print(move)

            while True:  # Begins an inner loop to handle user input for making moves.
                try:
                    # Prompts the user for input to choose numbers to shut or to quit the game. 
                    user_input = input("\nChoose numbers to shut (space-separated or type 'Q' to quit): ")
                    # The option to quit the game is to gracefully exit the game. 
                    if user_input.strip().lower() == 'q':
                        # If the user chooses to quit, end the game
                        print("Thanks for playing!")
                        return
                    
                    # Filter out any non-digit characters before converting them to integers and convert to a list of integers. 
                    # "xyz23 4---" --> [2,3,4]
                    choice = [int(char) for char in user_input if char.isdigit()]                     
                                         
                    # Check if the chosen move is valid: All numbers are from 1 to 9; Move is valid (according to is_valid_move function); Numbers closed = total (dice roll).
                    if all(1 <= num <= 9 for num in choice) and is_valid_move(board, choice) and sum(choice) == total:
                        # If valid, make the move and shut the chosen numbers
                        make_move(board, choice) # Goes from 1 to 0
                        break
                    else:
                        # If the move is invalid, prompt the user to try again
                        print("\nInvalid move. Please try again.")
                
                except ValueError:
                    # Handle invalid input
                    print("\nInvalid input. Enter numbers only.")
                
                # Display the board and possible moves again if the input was invalid (makes it easier to view; same code as above)
                print("\nBoard:", [i+1 if board[i] else "X" for i in range(9)]) 
                print("Possible moves:")
                for move in possible_moves:
                    print(move)
        
        # Display the final state of the board and calculate the score
        print("Final board:", [i+1 if board[i] else "X" for i in range(9)])
        score = sum(i+1 for i in range(9) if board[i]) # Sum of total tiles left open
        print(f"Your score: {score}")
        
        # Congratulate the player if they shut all the numbers
        if score == 0:
            print("\nCongratulations! You've shut the box!")
        
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

        # The while loop checks if play_again is not in the tuple ('y', 'n'). 
        while play_again not in ('y', 'n'):
            print("\nInvalid input. Please enter 'y' to play again or 'n' to stop playing.")
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower() # If the input is invalid, it prompts the user to enter a valid response.
        # Section above is added to improve the code. Initially, users could continue the game if they type anything aside from 'n'. 
        
        # Stops the game
        if play_again == 'n': 
            print("\nThanks for playing!")
            break
        
# Start the game when the script is run directly
if __name__ == "__main__":
    play_shut_the_box()  # Call the main function to start the game
