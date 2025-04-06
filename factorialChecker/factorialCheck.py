#this function requests a response and calls factorialchecker() if the user inputs an integer,
# if they input anything except for an integer the function fails
# but this try/except format catches the error and starts inputFunction over again
badinputcount = 0
def inputFunction():
    #most variables are local, as in only seen by the function they're in.
    #if I declare a variable outside of function(s) and then use the global tag like this, you can pull variables from elsewhere
    global badinputcount
    try:
        x=int(input("Pick an integer to test. "))
        print(str(x)+" is an excellent choice!")
        factorialchecker(x)
    except ValueError:
        print("....I said integer....\nTry again.")
        # badinputcount +=1 is the same as badinput = badinput + 1, just concise
        badinputcount +=1
        if badinputcount >= 5:
            print("Really busting my balls huh?")
        inputFunction()
#this function checks if number is a factorial
#x%n checks if the remainder of x divided by n is 0
#this is a quick way of checking for "perfect division"
#I used x//n instead of x/n because it does something called floor division, read into this.
#this also runs another() after a y/n response to see if the user wants to keep going (knowhatimsaaaayyyn)
def factorialchecker(x):
    y=x
    n=1
    while x%n == 0:
        x=x//n
        n+=1
    if x ==1:
        #I convert y to str so I can print it with my text, maybe not necessary, but it's how I'm rolling today
        print(str(y)+" is a factorial. It's "+ str(n-1)+"!")
        another()
    else:
        print(str(y)+" is not a factorial.")
        another()
#this function prompts the user for a "Y" or a "N" input, then starts this bad chicken from the top or ends the program
#if they do not answer Y or N it asks for a valid Y or N response
def another():
    anotherresponse = input("GIVE US ANOTHER ONE?!?! (Y/N)")
    if anotherresponse == "Y":
        inputFunction()
    if anotherresponse == "N":
        print("Coward.")
    else:
        print("not a valid answer homie, try again")
        another()
#this is best practice
#you write individual functions that do things
#then you write a main() function that actually calls your functions
#I nested the entire process into inputfunction() so I only call inputfunction()
#I don't know and I don't care if it's best practice this is how I roll (for now)
def main():
    inputFunction()

#I don't fully understand why this is here, my buddy told me to put this at the bottom of all my scripts (more or less)
#if you can explain why this is here I'll buy you a beer and burger
if __name__ == "__main__":
    main()



