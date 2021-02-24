# tictactoe
A simple tic tac toe game created at a higher level.

I started the project based on a reddit comment. It gave me new perceptions to learn programming as I used to be stuck in the tutorial purgatory. I am using this platform to showcase my skills and remind me what I have created thus far to keep me motivated always.

reddit post: https://www.reddit.com/r/learnprogramming/comments/li3jxh/what_are_some_good_projects_to_do_as_an/?utm_medium=android_app&utm_source=share
reddit comment:

"""
You can take almost any idea and expand it to include 95% of programming topics. For example the simple game of tic-tac-toe. Past the base game try these:

1. Have the user define X for an x by x board. Meaning support anything from 3x3 to 10x10 boards dynamically based on user input. (done)

2. Have the user define how many in a row you need to win - checking for 3 in a row on a 5x5 is very different than checking for 5 in a row on 5x5. (done)

3. Create a UI/graphics instead of printing text out to display the board. Or make it web based.

4. Make it 3 player. Or X players. Have the players choose what symbol/letter to use.

5. Make a computer player that can play the game. Make easy,average,hard versions of the ai. The mini-max algorithm is commonly used. Make a version of the AI that uses machine learning. (mini-max in progress)

6. Ruin all your previous logic by supporting non-perfect square boards. 3x5 or 6x2 boards. Go crazy and remove a random square from the middle of a generated board (this really screws all your previous logic.)

7. Have a database of users and keep their win/loss records. Make an elo system for them.

8. Write unit tests for your program.

9. Support network games (non-hotseat.)

What these will teach you:

1, 2, 4, 6 - These will push you towards single responsibility methods and separation of concerns. Relying on input parameters rather than global values. Should stop most of your hardcoding hacks. Many of these will cause you to do large refactoring if not entire rewrites if you don't plan ahead for them. After you are forced to rewrite for the 3rd time, you will learn why requirements are valuable to know ahead of time.

3 - Basics of UI implementation. Varies a lot based on which UI library you pick.

5 - Various algorithms and the basic of AI. Tic-Tac-Toe is a relatively simple algorithm. In a normal 3x3 board, you can brute force it and not worry too much about the math. You will get introduced into culling branches and mini-max once you go into larger boards or force timing constraints (easy vs hard) on the AI decision time.

7 - Database skills. Learning how to persist data after program shuts down, how to load data on startup.

8 - Unit tests really really enforce not using globals and having each method do only the small piece it is required to do. Forces you to think about potential non-happy paths. Knowing how to write unit-testable code is a big plus in a professional environment. That kind of code tends to be very easy to read and maintain.

9 - Networking, you can go as far as you want in this. Anywhere from basic LAN to hosting a server for leaderboards. You can go overboard and make a minecraft like setup where you need both a client and server to play the game; this really enforces separation of UI/frontend and backend.
"""
