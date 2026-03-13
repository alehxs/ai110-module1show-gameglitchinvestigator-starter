# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  - It looked bad. Guesses were not going down, some guesses were not counting, and then new game didn't reset game right. It was a mess.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Strings are counted in the history array
  2. Attempts go lower than 0
  3. New Game does not start a new game. State stays as game over.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  - I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  - Claude suggested difficult range function logic was set up incorrectly, so I told him to fix it and then he did. I tried to the difficulties before fixing, then tried again after fixing it. And then, it worked as intended.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  - Claude suggested we continued to build upon the boilerplate tests, which compared check_guess results directly to strings like "Win" or "Too High". This was misleading bc check_guess actually returns a tuple (outcome, message), so the tes

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - If the game worked as it was intended to. When you guess wrong, attempts is decremented. When you restart game, the game is supposed to restart. Then also by writing tests bc my professor always emphasized TDD.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran all the tests using pytest. I also created some of my own such as canary test, etc. It showed my code was working as intended and the bug was addressed.
- Did AI help you design or understand any tests? How?

  - Yes, my professor always taught me that we should always have a canary test to first see if the testing is even working, then we create a test first before we write any code. Then keep making them for all the things a fn is supposed to handle (edge cases, etc.)

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - Streamlit reruns its entire script from top to bottom on every interaction. In the original app, the secret was just
  ```python
    - secret = random.randint(low,high)
  ```
  - With no session_state protection, everytime a guess was submitted, Streamlit would rerun its script and pick a brand new number. The player was essentially guessing against a moving target.

  The fix was wrapping it inside a session_state check:
  ```python
  if "secret" not in st.session_state:
      st.session_state.secret = random.randint(low,high)
  ```
  - This only generates a secret once and keeps it constant across reruns until a new game is started.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - So a rerun is straightforward, every time a user does anything in a Streamlit app (clicks a button, types somehting), Streamlit reruns the entire program. It's basically like going on a page and after every interaction you just refresh the page. That's what Streamlit is doing, just rerunning the program every time you do something.

  - Session state is basically a way to say "hey, remmeber this." It's like a sticky note that survives each restart. So instead you ssay. "only pick a new secret if you don't already have one saved" and it stays the same the whole game.
- What change did you make that finally gave the game a stable secret number?
  - Like my one of previous answer says, we wrapped the secret generation in a session state check:
  ```python
  if "secret" not in st.session_state:
    st.session_state = random.randInt(low, high)
  ```
  Instead of the old version, which would pick a new secret number at every interaction, making the number a moving target.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
  - I would say explore the codebase. I didn't even know there were tests until they were mentioned. There was a canary test missing as well. 
  - Another thing I would say is to commit after fixing stuff or implementing stuff. I tried to commit stuff at the end I had to commit 1 file and couldn't commit bug fixes and implementation separately since I didn't commit changes before.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Give me a rundown of the codebase, I would like to have a brief overview of what I'm working with and what each file does. Before looking into it myself.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It taught me that I should also still be in control. Control being that I see things for myself (exploring original codebase, reviewing proposed changes, etc.) – I shouldn't be just taking Claude Code's word for it. I still have to remember that at the end of the day a human is going to still read the codebase.
