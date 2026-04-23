# Unbeatable Tic Tac Toe Engine

An implementation of a **deterministic Tic Tac Toe AI** where the user can never win.  
The system guarantees either a **win for the AI** or a **draw**, depending on the game state.

---


## 🎯 Objective

- The user should never be able to win — the system either forces a win or guarantees a draw.

---

## 🧠 Approach

The system uses **two separate strategies** based on turn order:

### 1. X (First Move – Attacking Engine)
- Uses hardcoded strategic patterns  
- Plays aggressively to create forced win paths  
- Switches to defensive mode when required  

### 2. O (Second Move – Defensive Engine)
- Uses advanced defensive patterns  
- Blocks all possible winning opportunities  
- Transitions into counter-attacks when possible  

---

## ⚙️ Core Concept

Instead of a single generalized algorithm, the logic is split into:

- **Attacking strategy (X)**
- **Defensive strategy (O)**

This provides tighter control over outcomes and simplifies decision-making.

Each move is:
- Deterministic  
- Based on current board state  
- Pre-optimized using known game strategies  

---

## 🔍 Key Features

- No randomness involved  
- Handles all possible game states  
- Hardcoded optimal strategies  
- Guarantees no user victory  

---

## 📊 Result

| Outcome | Possibility |
|--------|------------|
| AI Wins | ✅ |
| Draw    | ✅ |
| User Wins | ❌ |

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. run main.py
