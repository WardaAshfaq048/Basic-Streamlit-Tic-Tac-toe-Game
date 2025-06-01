import streamlit as st
import random

def reset_board():
    return [[0] * 3 for _ in range(3)]

def check_win(board):
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)):
            return 1
        if all(board[i][j] == 2 for j in range(3)):
            return 2
    for j in range(3):
        if all(board[i][j] == 1 for i in range(3)):
            return 1
        if all(board[i][j] == 2 for i in range(3)):
            return 2
    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(board[i][i] == 2 for i in range(3)) or all(board[i][2 - i] == 2 for i in range(3)):
        return 2
    if all(board[i][j] != 0 for i in range(3) for j in range(3)):
        return -1
    return 0

def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2

def main():
    st.title("Tic-Tac-Toe")
    
    if "board" not in st.session_state:
        st.session_state.board = reset_board()
        st.session_state.turn = 1
        st.session_state.game_over = False
        st.session_state.winner = None
    
    board = st.session_state.board
    game_over = st.session_state.game_over
    winner = st.session_state.winner
    
    st.write("Player 1 is X and Player 2 is O")
    
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            label = "X" if board[i][j] == 1 else "O" if board[i][j] == 2 else " "
            if cols[j].button(label, key=f"{i}-{j}") and not game_over and board[i][j] == 0:
                board[i][j] = 1
                winner = check_win(board)
                if winner == 0:
                    ai_move(board)
                    winner = check_win(board)
                
                if winner != 0:
                    st.session_state.game_over = True
                    st.session_state.winner = winner
    
    if game_over:
        if winner == 1:
            st.success("Player 1 wins!")
        elif winner == 2:
            st.error("PLayer 2 wins!")
        else:
            st.warning("It's a tie!")
        if st.button("Restart Game"):
            st.session_state.board = reset_board()
            st.session_state.game_over = False
            st.session_state.winner = None

if __name__ == "__main__":
    main()
