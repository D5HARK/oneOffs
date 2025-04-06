Factorial Checker – README

WHAT IS THIS?
-------------
This Python script checks whether a number is a factorial of some integer. 
It repeatedly prompts the user for input, checks if it’s a factorial, 
and offers to check another number afterward — with some spicy commentary if you mess up.

HOW TO USE IT
-------------
1. Run the script.
2. Enter an integer when prompted.
3. The program will tell you if it’s a factorial or not.
4. You can continue checking more numbers, or gracefully bow out.

FEATURES
--------
- Handles non-integer inputs with a friendly (and progressively annoyed) retry loop.
- Uses recursion and a global `badinputcount` to track how often you fail at step 2.
- Checks whether a number is a factorial using clean floor division and a `while` loop.
- Offers to continue the game with a Y/N prompt.
- Gives attitude if you press its buttons too many times.

FILE STRUCTURE
--------------
- `factorialCheck.py` : The main script.
- All functions are defined separately, and the script starts via `main()`.

NOTES FROM THE CREATOR
----------------------
- Yes, I'm aware not everything is "best practice." I'm cooking in the kitchen my way for now.
- `if __name__ == "__main__":` is used so this script can be imported elsewhere without auto-running. 
  (Pay up on that beer and burger.)
- `global badinputcount` lets the error count persist across recursive calls to `inputFunction()`. Neat, huh?

TODO
----
- Consider replacing recursion with a `while True:` loop to avoid stack overflows.
- Expand functionality to find the nearest factorial.
- Add GUI? Maybe. Maybe not.

CREDITS
-------
Made with frustration, recursion, and good old-fashioned print statements.

-- D5HARK
