# Word Guessing Game 🕹️

This is a simple word guessing game written in Python. The player must guess a randomly chosen English word from a list, with up to **7 attempts** allowed. After each guess, the program shows which letters are correct and in the correct position.

## 🧠 How the Game Works

- A random word is selected from a list of 1000 lowercase English words (stored in `words.txt`).
- The player has 7 attempts to guess the correct word.
- For each guess, the game shows:
  - Letters that are correct and in the correct position.
  - Underscores (`_`) for incorrect letters or positions.
- The game ends when:
  - The word is guessed correctly, or
  - The player runs out of attempts.
