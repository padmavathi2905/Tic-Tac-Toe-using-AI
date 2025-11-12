# Tic-Tac-Toe using AI

This project implements an **unbeatable Tic-Tac-Toe AI** using the **Minimax algorithm** — a fundamental concept in artificial intelligence and game theory.  
The AI always plays optimally, ensuring that the human player can never win if both play perfectly.

---

## Features

-  **Optimal AI** using the **Minimax algorithm** (with optional alpha–beta pruning for efficiency)
-  **Automatic turn management** – X always starts and turns alternate
-  **Smart move validation** – no illegal or duplicate moves
-  **Game state detection** – identifies wins, losses, and ties
-  **Graphical user interface (GUI)** built with **Pygame**

---

## Project Structure

| File | Description |
|------|--------------|
| `tictactoe.py` | Core game logic and AI implementation |
| `runner.py` | GUI interface for human vs. AI gameplay (provided by CS50) |
| `requirements.txt` | Python dependencies (includes Pygame) |

---

## ⚙️ How It Works

1. The board is represented as a 3×3 list of lists.
2. `player()` determines whose turn it is (X or O).
3. `actions()` lists all available moves.
4. `result()` returns the board state after a move.
5. `winner()` checks if there’s a winner.
6. `terminal()` checks if the game has ended.
7. `utility()` assigns scores:
   - **+1** → X wins  
   - **−1** → O wins  
   - **0** → Tie  
8. `minimax()` explores all possible future states to choose the optimal move.

---

## How to Run

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
2. **Install dependencies and run the code:**
```bash
pip install -r requirements.txt
python runner.py
