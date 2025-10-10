My Kisah - A Simple Story Game
Hey there! This is My Kisah, a small text-based game I built in C. I’m still new to programming, so it’s pretty simple, but I had fun making it! In the game, you make choices in a story about meeting someone special at a café, and your decisions lead to different endings. There are 5 endings to find!
What’s Cool About It

Pick Your Path: Choose options to change the story and see how it ends.
Your Own Name: Add your character’s name to make it feel like you’re in the story.
Friendship Points: Your choices affect how much Silvia (the other character) likes you (I called this “affinity” in the code).
Ending Tracker: Check which endings you’ve unlocked in the “Riwayat Ending” menu.
Text-Only Game: No fancy graphics, just text in the console and your imagination!

What You Need
To play, you’ll need:

A C compiler like GCC (if you want to compile the code yourself).
A terminal or command prompt.
I included the .exe file in the repo, so Windows users can just run it!
I made this on Windows (it uses cls to clear the screen). If you’re on Linux or Mac and compiling the code, change system("cls") to system("clear") in the clearScreen() function.

How to Run It
Since I already added the .exe file, it’s super easy for Windows users. Here’s how to get started:

Get the Code:
git clone https://github.com/your-username/my-kisah.git
cd my-kisah


Run the Game (Windows):Just double-click My_Kisah.exe in the repo folder, or run it from the terminal:
My_Kisah.exe


If You Want to Compile It Yourself:If you prefer to build it from the source code:
gcc My_Kisah.c -o My_Kisah

Then run it:
./My_Kisah   # Linux/Mac
My_Kisah.exe # Windows



How to Play

Start the game (either with the .exe or by compiling).
You’ll see a main menu with these options:
1: Start the story and type your character’s name.
2: See the endings you’ve unlocked.
3: Exit the game.


In the story:
Read the text and pick a number (like 1, 2, 3, etc.) to make choices.
Press Enter to move to the next part.
Your choices affect how close you get to Silvia, which changes the ending.
You can go back to the main menu anytime by picking the “back” option.



Files in the Repo

My_Kisah.c: The C code with all the story and game logic.
My_Kisah.exe: The executable for Windows users (no need to compile!).
README.md: This file you’re reading.

Endings
There are 5 endings (I tried to make each one feel different):

Heart Connected: A happy ending if you make great choices!
Unspoken Feelings: You stay friends because you didn’t confess your feelings.
Friendzone: You confess, but Silvia just wants to be friends.
Broken Bonds: A sad ending after a big fight.
Faded Away: You leave the café and lose touch.

Things to Watch Out For

The .exe is for Windows. If you’re on Linux or Mac, you’ll need to compile the code yourself.
If you compile and you’re not on Windows, change system("cls") to system("clear") in the clearScreen() function.
The game is in Indonesian because that’s what I know best, and it’s got a casual, emotional vibe.
I tested it on DevC++ and it works fine, but some online compilers (like Programiz) might not like the system() calls.

Want to Help?
I’m still learning, so if you have ideas to make this better, I’d love to hear them! Here’s how you can help:

Fork my repo (make your own copy on GitHub).
Create a new branch (git checkout -b my-fix-or-feature).
Make your changes and commit (git commit -m "Added something cool").
Push it (git push origin my-fix-or-feature).
Open a pull request, and I’ll take a look!

Thanks

I got inspired by visual novel games and wanted to try making one in C.
Thanks for checking out my game! I hope you enjoy it, and sorry if there are any bugs—I’m still getting the hang of this!
