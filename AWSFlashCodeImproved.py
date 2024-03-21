import random
import AWSTerms 

AWSTerms = AWSTerms.AWSTerms


# Define functions to be used in AWSFlash game
def printWelcome(terms):
   '''Prints a welcome message and brief description of how to play AWSFlash'''

   print(f'''Welcome to AWS Flash! \nA Series of clues will be given for an AWS Tool or Service; 
  choose the best fit for the clue from the provided list (responses are not case-sensitive). 
  \nThere are {len(terms)} AWS Tools/Services in the game. Enter 'exit', 'quit', or 'q' to stop.\nLet's Begin!''')


def getAnswerList(term, termsCopy):
  '''Generates a list of _ potential answers and ensures the correct term is included in the list'''

  answerList = random.sample(termsCopy,4)
  if term not in answerList:
    answerList.pop()
    randIndex = random.randint(0,3)
    answerList.insert(randIndex, term)
  return answerList


def askQuestion(termsList, term, termsWrong):
    '''The game kernel, this code generates a round of clue based questions based on term while accounting for quitting and incorrect answers'''

    clues = AWSTerms[term]                  # Get list of clues
    numClues = len(clues)                   # Get length of clues for for loop
    random.shuffle(clues)                   # Shuffle the clues

                                            # Main clue logic, beginning with for loop for potential clues
    for attemptNum in range(numClues):
      clue = print(f"Clue {attemptNum +1}: {clues[attemptNum]}")  # Present clue number and clue
      response = input("Answer: ")                                # Get player response
      if response.lower() in ["exit", "quit", "q"]:               # Evaluate if player wants to quit
        print('Exiting the game. See you later!')
        global play 
        play = False
        break
      elif response.lower() == term.lower():                      # Evlauate player's answer. If correct, remove term from term list and break for loop for question
        print(random.choice(["Correct!", "Great Job!", "You Rock!"]))
        index = termsList.index(term)
        termsList.pop(index)
        break
      elif (attemptNum + 1) == numClues:                           # If number of clues exceeded, alert player and continue ('reshuffle question')
        print("You have exceeded the clues for this question. The term will be reshuffled.")
      else:                                                       # If answer incorrect, alert player and log wrong answer
        print(random.choice(["Try again!", "Incorrect :(", "Sorry, that's not right"]))
        termsWrong.append(term)


def endGame(termsWrong):
    '''Prints a goodbye message and game stats'''

    print("\nWonderful work! You finished the game!!")
    if len(termsWrong) > 0:
        print(f"You may want to study these subjects: {list(set(termsWrong))}")
    else:
        print("You know your AWS. Impressive!")



# Begin master function AWSFlash

play = True                                 # Set global while loop condition 'play' as True
def AWSFlash(seed=None):
  random.seed(seed)                         # Set random seed if desired
  termsList = list(AWSTerms.keys())             # Create a list of AWS terms from dictionary keys
  termsCopy = termsList.copy()                  # Make a copy of terms to populate answer options (original is decremented by correct answers)
  termsWrong = []                           # Make a list of wrong answers

  printWelcome(termsList)                   # Welcome message for player

  questionNumber = 1                        # Track the while loop question number                    
  while termsList and play:                 # Begin game while loop, as there are terms in the queue and condition play

    term = random.choice(termsList)                     # Choose a random term/question
    answerList = getAnswerList(term, termsCopy)         # Populate answer options with a random sample of terms and ensure the correct term is included 
    print(f"\nQuestion {questionNumber}, Options: {answerList}") # Present the question/term and options to player
    askQuestion(termsList, term, termsWrong)            # Ask a question and handle case logic
    questionNumber += 1                                 # Increment question number with each answered question

  if len(termsList) == 0:                   # After while loop exited: if all questions answered, return game stats
    endGame(termsWrong)
