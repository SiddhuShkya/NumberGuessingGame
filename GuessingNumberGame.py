import random

def welcome():
    print("----------> WELCOME TO THE NUMBER GUESSING GAME <----------")
    difficulty()

def difficulty():
    print("1.Easy\n2.Normal\n3.Hard")
    a = input("Choose the Difficulty of the game : ")
    if a == "1":
        generate_random_num(1,10, 4)
    elif a == "2":
        generate_random_num(1, 100, 5)
    elif a == "3":
        generate_random_num(1, 1000, 7)
    else:
        print("------> Invalid Input! please try again <------")
        difficulty()


def generate_random_num(a,b,c):
    print(f"The program has generated a random number from range {a} to {b}.")
    num = random.randint(a,b)
    #print(num)
    print(f"NOTE : You will only get {c} chances to guess the number.")
    userInput(num,c)

def userInput(n,c):
    guess = int(input("Your Guess? : "))
    if guess!=n:
        c = c-1
        guessCheck(guess,n,c)
    else:
        end(n)

def end(n):
    print(f"-------> Congrats! You have guessed the number {n} correctly <-------")
    again()

def again():
    again = input("Would you like to play again?(y/n): ").lower()
    if again=="y":
        welcome()
    else:
        print("-------> THANK YOU FOR PLAYING THIS GAME <-------")
        quit()

def guessCheck(g,n,c):
    while g!=n:
        if c!=0:
            if g>n:
                guess = int(input(f"Chance {c} | The number is lower than {g} : "))
                c = c-1
                guessCheck(guess, n, c)
            else:
                guess = int(input(f"Chance {c} | The number is greater than {g} : "))
                c = c-1
                guessCheck(guess, n, c)
        else:
            gameOver(n)
    if g==n:
        end(n)

def gameOver(n):
    print(f"-------> Game Over! The number was {n} <-------")
    again()

def main():
    welcome()

if __name__=="__main__":
    main()