# Imports used for time sleep and the date
import time
import datetime

#Scores (All scores start at zero and progressively add up if the user answers questions correctly)
score = 0
soccerscore = 0
tennisscore = 0
basketballscore = 0
baseballscore = 0

#More Suggestions (Function)
# This allow users to input questions they want to the quiz
# Their requested questin will be transfered to the suggestions.txt file
def suggestions():
    i = 1
    while i>0:
        d = open("more_question.txt", "w+")
        ask = raw_input("Do you have any questions for me to add to my quiz?")
        if ask == "yes":
                question1 = raw_input("Please input any questions")
                for i in range(1):
                    d.write("__________________\n")
                    d.write("Questions: %s \r" % question1)
                    d.write("__________________\n")
                break
        else:
            break


#print_score (Function)
# Shows your scores in each section out of 5 and the overall score out of 20
# gives a message according to the score
def print_score():
    global score
    global soccerscore
    global tenniscore
    global basketballscore
    global baseballscore
    print("Soccer: %d/5 Tennis: %d/5 BasketBall: %d/5 Baseball: %d/5 Overall: %d/20 " %(soccerscore,tennisscore,basketballscore,baseballscore,score))
    if score <= 3:
        print("Do you even play any sports? Or are you just dumb")
    elif score <= 5 and score > 3:
        print("You are the mere definition of a jock")
    elif score <= 10 and score > 5:
        print("You are probably guessing most of them. You are pretty lucky to get this score")
    elif score <= 15 and score > 10:
        print("You are getting there, but you are not a nerd yet")
    elif score <= 20 and score > 15:
        print("Congratulaions, you are officially a Nerdy Jock!")



#check_answer (Function)
# The input parameters are the user's answer, the correct answer, and the category.
# If the user's answer is correct, the category score is incremented. The overall score is also incremented.
def check_answer(ans,correct,category):
    global score
    global soccerscore
    global tennisscore
    global basketballscore
    global baseballscore

    if ans == correct:
        if category == "soccer":
            soccerscore = soccerscore + 1
        elif category == "basketball":
            basketballscore = basketballscore + 1
        elif category == "tennis":
            tennisscore = tennisscore + 1
        elif category == "baseball":
            baseballscore = baseballscore + 1
        score = score + 1
        print("You got this correct")
    else:
        print("You are wrong")


#Soccer category (Function)
# The soccer list starts off with an empty list
# Questions will be added (appeneded) to the list throught the parameters
# ques[0] is the question, ques[1], [2], [3], [4] are the options, ques[5] is the answer
# (ques[0], correct answer, soccer)

def soccer_category():
    soccerlist = []
    print("""
     .oooo.o  .ooooo.   .ooooo.   .ooooo.   .ooooo.  oooo d8b
    d88(  "8 d88' `88b d88' `"Y8 d88' `"Y8 d88' `88b `888""8P
    `"Y88b.  888   888 888       888       888ooo888  888
    o.  )88b 888   888 888   .o8 888   .o8 888    .o  888
    8""888P' `Y8bod8P' `Y8bod8P' `Y8bod8P' `Y8bod8P' d888b

    """)
    soccerlist.append(("Question 1: When did the Premier League start?", "1990", "1992", "1994", "2000", "b"))
    soccerlist.append(("Question 2: How many goals did Ronaldo score during 2016 - 2017?", "42", "50", "46", "47", "a"))
    soccerlist.append(("Question 3: What is the fastest time a player received a red card?", "5 seconds", "5 minutes", "1 minute", "2 seconds", "d"))
    soccerlist.append(("Question 4: On average, how far does a soccer play run per match?", "500 meters", "6.8 miles", "9.5 miles", "12 miles", "c"))
    soccerlist.append(("Question 5: IN 2013, who opened a museum dedicated to himself?", "Wayne Rooney", "Neymar Jr", "Cristiano Ronaldo", "Zlatan Ibrahimovic", "c"))

    for ques in soccerlist:
       print(ques[0])
       print("a. %s" %ques[1])
       print("b. %s" %ques[2])
       print("c. %s" %ques[3])
       print("d. %s" %ques[4])
       answer = raw_input()
       check_answer(answer, ques[5],"soccer")
    print("You have finished the soccer section.")
    time.sleep(2)

#Tennis category (Function)
# The tennis list starts off with an empty list
# Questions will be added (appeneded) to the list throught the parameters
# ques[0] is the question, ques[1], [2], [3], [4] are the options, ques[5] is the answer
# (ques[0], correct answer, tennis)

def tennis_category():
    tennislist = []
    print("""
     .                                      o8o
  .o8                                      `"'
.o888oo  .ooooo.  ooo. .oo.   ooo. .oo.   oooo   .oooo.o
  888   d88' `88b `888P"Y88b  `888P"Y88b  `888  d88(  "8
  888   888ooo888  888   888   888   888   888  `"Y88b.
  888 . 888    .o  888   888   888   888   888  o.  )88b
  "888" `Y8bod8P' o888o o888o o888o o888o o888o 8""888P'
    
    """)
    print("Moving on to the tennis section")
    tennislist.append(("Question 1: Who is officially the No.1 player in 2017?", "Rafael Nadal", "Roger Federrer", "Andy Murray", "Novak Djokovic", "a"))
    tennislist.append(("Question 2: Which Grand Slam is the oldest?", "Australian Open", "Roland Garros", "Wimbledon", "US Open", "c"))
    tennislist.append(("Question 3: Who won Wimbledon in 2017?", "Rafael Nadal", "Roger Federrer", "Andy Murray", "Novak Djokovic", "b"))
    tennislist.append(("Question 4: When was the first Wimbledon played?", "1892", "1930", "1877", "1850", "c"))
    tennislist.append(("Question 5: How long was the longest tennis match?", "3 hours 24 minutes", "13 hours 53 minutes", "11 hours 5 minutes", "9 hours 32 minutes", "c"))

    for ques in tennislist:
       print(ques[0])
       print("a. %s" % ques[1])
       print("b. %s" % ques[2])
       print("c. %s" % ques[3])
       print("d. %s" % ques[4])
       answer = raw_input()
       check_answer(answer, ques[5],"tennis")
    print("You have finished the tennis section.")
    time.sleep(2)

#Basketball category (Function)
# The basketball list starts off with an empty list
# Questions will be added (appeneded) to the list throught the parameters
# ques[0] is the question, ques[1], [2], [3], [4] are the options, ques[5] is the answer
# (ques[0], correct answer, basketball)
def basketball_category():
    basketballlist = []
    print("""
    .o8                          oooo                      .    .o8                 oooo  oooo
    "888                          `888                    .o8   "888                 `888  `888
    888oooo.   .oooo.    .oooo.o  888  oooo   .ooooo.  .o888oo  888oooo.   .oooo.    888   888
    d88' `88b `P  )88b  d88(  "8  888 .8P'   d88' `88b   888    d88' `88b `P  )88b   888   888
    888   888  .oP"888  `"Y88b.   888888.    888ooo888   888    888   888  .oP"888   888   888
    888   888 d8(  888  o.  )88b  888 `88b.  888    .o   888 .  888   888 d8(  888   888   888
    `Y8bod8P' `Y888""8o 8""888P' o888o o888o `Y8bod8P'   "888"  `Y8bod8P' `Y888""8o o888o o888o
    """)
    print("Moving on to the basketball section")
    basketballlist.append(("Question 1: Where was Lebron James born?", "Michigan", "New York", "Florida", "Ohio", "d"))
    basketballlist.append(("Question 2: Which year was Lebron born in?", "1982", "1993", "1989", "1984", "d"))
    basketballlist.append(("Question 3: Who was once starred in a Burger King commercial as a kid?", "Kevin Durant", "Stephen Curry", "Lebron James", "Tim Duncan", "b"))
    basketballlist.append(("Question 4: When did Stephen Curry started to play basketball", "9 years old", "6 years old", "4 years old", "14 years old", "b"))
    basketballlist.append(("Question 5: Who eats and writes with their left hand? ", "Kevin Durant", "Stephen Curry", "Lebron James", "Tim Duncan", "c"))

    for ques in basketballlist:
       print(ques[0])
       print("a. %s" % ques[1])
       print("b. %s" % ques[2])
       print("c. %s" % ques[3])
       print("d. %s" % ques[4])
       answer = raw_input()
       check_answer(answer, ques[5],"basketball")
    print("You have finished the basketball section.")
    time.sleep(2)

#Baseball category (Function)
# The baseball list starts off with an empty list
# Questions will be added (appeneded) to the list throught the parameters
# ques[0] is the question, ques[1], [2], [3], [4] are the options, ques[5] is the answer
# (ques[0], correct answer, baseball)
def baseball_category():
    baseballlist= []
    print("""
     .o8                                     .o8                 oooo  oooo
    "888                                    "888                 `888  `888
     888oooo.   .oooo.    .oooo.o  .ooooo.   888oooo.   .oooo.    888   888
    d88' `88b `P  )88b  d88(  "8 d88' `88b  d88' `88b `P  )88b   888   888
    888   888  .oP"888  `"Y88b.  888ooo888  888   888  .oP"888   888   888
    888   888 d8(  888  o.  )88b 888    .o  888   888 d8(  888   888   888
    `Y8bod8P' `Y888""8o 8""888P' `Y8bod8P'  `Y8bod8P' `Y888""8o o888o o888o
    """)
    print("Moving on to the baseball section")
    baseballlist.append(("Question 1: Which baseball team have the won the most world series?", "Chicago Cubs", "LA Dodgers", "Boston Red Sox", "New York Yankees", "d"))
    baseballlist.append(("Question 2: When was the first pro baseball game aired on TV?", "1939", "1943", "1967", "1921", "a"))
    baseballlist.append(("Question 3: Which team have the most players in the Hall of Fame?", "Chicago Cubs", "Sanfrancisco Giants", "New York Yankees", "Los Angeles Angels", "b"))
    baseballlist.append(("Question 4: How many inning were made in the most innings in the world?", "15", "26", "29", "32", "b"))
    baseballlist.append(("Question 5: Which team was the first team to wear numbers on their backs?", "Chicago Cubs", "LA Dodgers", "Boston Red Sox", "New York Yankees", "d" ))

    for ques in baseballlist:
       print(ques[0])

       print("a. %s" % ques[1])
       print("b. %s" % ques[2])
       print("c. %s" % ques[3])
       print("d. %s" % ques[4])
       answer = raw_input()
       check_answer(answer, ques[5],"baseball")
    print("You have finished the baseball section.")
    time.sleep(2)



#Main Program - This is the main program . It displays the welcome message and rules of the game
# It calls functions to display questions of each category
# It calls a function to display the scores at the end
# There is a while loop in the function so that players can play again after the quiz. If yes then the scores are reset for the next round

def main_program():
    global score
    global soccerscore
    global tennisscore
    global basketballscore
    global baseballscore
    print("""
    db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b 
    88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'     
    88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo 
    Y8   I8I   88 88~~~~~ 88      8b      88    88 88  88  88 88~~~~~ 
    `8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.     
    `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P 
    """)
    time.sleep(1)
    print("""
    ___________      
    \__    ___/___   
      |    | /  _ \  
      |    |(  <_> ) 
      |____| \____/  
                 """)
    time.sleep(1)
    print("""
                 |    |   ____|\    \     ___|\    \  |    |  |    ||\    \    /    /|      |\    \ |\     \   ___|\     \   ___|\    \   ___|\    \           ___|\     \  |    | |    ||    |  /    /|___     
       |    |  /     /\    \   /    /\    \ |    |  |    || \    \  /    / |       \\    \| \     \ |     \     \ |    |\    \ |    |\    \         /    /\     \ |    | |    ||    | /    /|    |    
       |    | /     /  \    \ |    |  |    ||    | /    //|  \____\/    /  /        \|    \  \     ||     ,_____/||    | |    ||    | |    |       /    /  |     ||    | |    ||    ||\____\|    |    
 ____  |    ||     |    |    ||    |  |____||    |/ _ _//  \ |    /    /  /          |     \  |    ||     \--'\_|/|    |/____/ |    | |    |      |    |   |     ||    | |    ||    || |   |/    |___ 
|    | |    ||     |    |    ||    |   ____ |    |\    \'   \|___/    /  /           |      \ |    ||     /___/|  |    |\    \ |    | |    |      |\    \  |__   ||    | |    ||    | \|___/    /    |
|    | |    ||\     \  /    /||    |  |    ||    | \    \       /    /  /            |    |\ \|    ||     \____|\ |    | |    ||    | |    |      | \    \\`  \ /||    | |    ||    |    /     /|    |
|\____\|____|| \_____\/____/ ||\ ___\/    /||____|  \____\     /____/  /             |____||\_____/||____ '     /||____| |____||____|/____/|       \ \ ___\\   \ ||\___\_|____||____|   |_____|/____/|
| |    |    | \ |    ||    | /| |   /____/ ||    |   |    |   |`    | /              |    |/ \|   |||    /_____/ ||    | |    ||    /    | |        \ |    ||___|/| |    |    ||    |   |     |    | |
 \|____|____|  \|____||____|/  \|___|    | /|____|   |____|   |_____|/               |____|   |___|/|____|     | /|____| |____||____|____|/          \|____||   |  \|____|____||____|   |_____|____|/ 
    \(   )/       \(    )/       \( |____|/   \(       )/        )/                    \(       )/    \( |_____|/   \(     )/    \(    )/               \(  |___|     \(   )/    \(       \(    )/    
     '   '         '    '         '   )/       '       '         '                      '       '      '    )/       '     '      '    '                 '    )/       '   '      '        '    '     
                                      '                                                                     '                                                 '                                                                                                        '                                                      '                                       
    """)
    fname = raw_input("What is your name?")
    print("Hello %s" % fname)
    print("You are about to take the Jocky Nerd Quiz. This quiz gives you a series of questions about facts of famous sports. Are you a Nerdy Jock?")
    print("________________________________________________________________________________________________________________________________________")
    print("The rules of this quiz are: 1) No searching information up or asking a friend 2) Only input letters from a - d")
    print("________________________________________________________________________________________________________________________________________")

    while True:
        global score
        print("The first section of the quiz is soccer. Get Ready...")
        time.sleep(2) # this allows the program to be paused for 2 seconds
        soccer_category()
        tennis_category()
        basketball_category()
        baseball_category()
        print("You have finished this quiz. Here are your scores:")
        print_score()
        print("Your score will be appended to a file")

        time.sleep(1)

        # This asks for the date
        year = int(raw_input("Enter a today's year"))
        month = int(raw_input("Enter today's a month (In numbers)"))
        day = int(raw_input("Enter today's a day"))
        date1 = datetime.date(year, month, day)

        # This information (Name, score, date) will be stored into the leaderboard.txt file
        z = open("leaderboard.txt", "a+")
        for i in range(1):
            z.write("________________________ \n")
            z.write("Player's Name: %s \r \n" % (fname))
            z.write("Score: %d\r\n" % (score))
            z.write("Date %s\n" %date1)
            z.write("________________________ \n")


        again = raw_input("Would you like to play again (y/n)")
        if again == "n":
            suggestions()
            break
        else:
            score = 0
            soccerscore = 0
            tennisscore = 0
            basketballscore = 0
            baseballscore = 0


main_program()