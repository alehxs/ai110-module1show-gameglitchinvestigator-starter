# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - A number guessing game where the player tries to guess a secret number within a number of attempts. The game has three difficulty levels (Easy, Normal, Hard) with different ranges and attempt limits, and tracks a score across guesses.

- [x] Detail which bugs you found.
  - The secret number kept changing on every guess because it was not stored in session state — Streamlit reruns the script on every interaction, so a new random number was picked each time.
  - The hints were backwards — "Too High" told the player to go higher and "Too Low" told them to go lower, which is the opposite of correct.
  - The New Game button was resetting the secret using a hardcoded range of 1–100 instead of respecting the selected difficulty.

- [x] Explain what fixes you applied.
  - Wrapped the secret generation in a `st.session_state` check so it only picks a number once per game.
  - Fixed the hint messages in `check_guess` so "Too High" says go lower and "Too Low" says go higher.
  - Extracted `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py` and wrote pytest tests for each.

## 📸 Demo

- [x] ![alt text](<CleanShot 2026-03-13 at 14.40.55@2x.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
