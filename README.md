# My Kisah - A Simple Story Game 🎮

Hey there! This is **My Kisah**, a small text-based game I built in C. I'm still new to programming, so it's pretty simple, but I had fun making it! You get to make choices in a story about meeting someone special at a café, and your decisions lead to 5 different endings. What's cool? Let's dive in! 😄

---

## What's Cool About It? ✨
- **Pick Your Path**: Choose options to change the story and see how it ends.
- **Your Own Name**: Add your character's name to make it personal.
- **Friendship Points**: Your choices affect how close you get to Silvia (called "affinity" in the code).
- **Ending Tracker**: Check which endings you've unlocked in the menu.
- **Text-Only Fun**: No graphics, just text and your imagination!

---

## What You Need to Play 🛠️
- A C compiler like GCC (if you want to compile it yourself).
- A terminal or command prompt.
- The `.exe` file works for Windows users (no need to compile!).

---

## How to Run It 🚀

Since I added the `.exe` file, it’s super easy for Windows users. Here’s how to get started:

### 1. Get the Code
```bash
git clone https://github.com/Jofadlan/My-Kisah.git
cd My-Kisah
```

### 2. Run the Game (Windows)
- Double-click `My_Kisah.exe` in the repo folder, or run from terminal:
```bash
My_Kisah.exe
```

### 3. Compile It Yourself (Optional)
If you prefer to build from source:
```bash
gcc My_Kisah.c -o My_Kisah
```
Then run it:
- Linux/Mac: `./My_Kisah`
- Windows: `My_Kisah.exe`

---

## How to Play 🎯
1. **Start the Game**: Type your character’s name.
2. **See the Endings**: Check which ones you’ve unlocked.
3. **Exit**: Leave the game anytime.

In the story:
- Read the text and pick a number (like 1, 2, 3, etc.) to make choices.
- Press Enter to move to the next part.
- Your choices affect how close you get to Silvia, which changes the ending. You can go back to the main menu anytime!

---

## Files in the Repo 📂
- `My_Kisah.c`: The C code with the story and game logic.
- `My_Kisah.exe`: The executable for Windows users.
- `README.md`: This file you’re reading!

---

## Endings 🌟
There are 5 endings (I tried to make each one feel different):
- **Heart Connected**: A happy ending if you make great choices!
- **Unspoken Feelings**: Stay friends because you didn’t confess.
- **Friendzone**: Confess, but Silvia just wants to be friends.
- **Broken Bonds**: A sad ending after a big fight.
- **Faded Away**: Leave the café and lose touch.

---

## Things to Watch Out For ⚠️
- The `.exe` is for Windows. For Linux/Mac, compile the code yourself.
- I tested it on Dev-C++ and it works, but some online compilers (like Programiz) might not like `system()` calls.

---

## Want to Help? 🤝
I’m still learning, so if you have ideas to make this better, I’d love to hear them! Here’s how you can help:
1. Fork my repo (make your own copy on GitHub).
2. Create a new branch (`git checkout -b my-fix`).
3. Make changes and commit (`git commit -m "Added something cool"`).
4. Push it (`git push origin my-fix`).
5. Open a pull request, and I’ll take a look!

---

## Thanks! 🙌
I got inspired by visual novel games and wanted to try making one in C. The ending "Heart Connected" is a nod to an animation on YouTube by ReeKu: [link](https://www.youtube.com/watch?v=Td3xOjORMsi). Thanks for checking out my game! I hope you enjoy it, and sorry if there are bugs—I’m still getting the hang of this! 😅