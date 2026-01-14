"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Kankrlík
email: kankrlik.jakub@gmail.com
discord: jakancz
"""

def print_rules():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark")
    print("per turn on the 3x3 grid. The WINNER is the one")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal")
    print("row")
    print("========================================")
    print("Let's start the game")

def print_board(board):
    print("--------------------------------------------")
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")
    print("============================================")

def check_win(board, player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    
    for a, b, c in win_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def main():
    board = [' ' for _ in range(9)]
    
    current_player = 'O' 
    
    print_rules()
    print_board(board)
    
    game_running = True
    
    while game_running:
        print(f"Player {current_player} | Please enter your move number:")
        
        user_input = input()
        
        if not user_input.isdigit():
            print("Please enter a number.")
            continue
        
        move = int(user_input)
        
        if move < 1 or move > 9:
            print("Please enter a number between 1 and 9.")
            continue
        
        index = move - 1
        
        if board[index] != ' ':
            print("This spot is already taken.")
            continue
            
        board[index] = current_player
        
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Congratulations, the player {current_player} WON!")
            game_running = False
        elif check_draw(board):
            print("Game over! It's a draw.")
            game_running = False
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'


if __name__ == "__main__":
    main()