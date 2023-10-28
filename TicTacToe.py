import random

def main():
  # Create the board.
  board = [['' for x in range(3)] for y in range(3)]

  # Choose who goes first.
  turn = random.randint(0, 1)

  # Play the game.
  while not is_game_over(board):
    # Get the player's move.
    move = get_player_move(board, turn)

    # Make the move.
    make_move(board, move, turn)

    # Check if the game is over.
    if is_game_over(board):
      break

    # Switch turns.
    turn = 1 - turn

  # Determine the winner.
  winner = determine_winner(board)

  # Print the winner.
  if winner is not None:
    print(f"The winner is {winner}!")
  else:
    print("The game is a tie!")

def is_game_over(board):
  # Check for a winner.
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != '':
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] != '':
      return board[0][i]
    if board[i][0] == board[1][1] == board[2][2] != '':
      return board[i][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
      return board[0][2]

  # Check for a tie.
  for i in range(3):
    for j in range(3):
      if board[i][j] == '':
        return False

  return True

def get_player_move(board, turn):
  # Get the player's move.
  while True:
    move = input("Enter your move (1-9): ")
    move = int(move) - 1
    if 0 <= move < 9 and board[move][0] == '':
      break

  return move

def make_move(board, move, turn):
  # Make the move.
  board[move][0] = 'X' if turn == 0 else 'O'

def determine_winner(board):
  # Determine the winner.
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != '':
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] != '':
      return board[0][i]
    if board[i][0] == board[1][1] == board[2][2] != '':
      return board[i][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
      return board[0][2]

  return None

if __name__ == "__main__":
  main()
