import random
import AWSTerms 

AWSTerms = AWSTerms.AWSTerms

def AWSFlash(seed=None):
  random.seed(seed)                         # Set random seed if desired
  terms = list(AWSTerms.keys())             # Create a list of AWS terms from dictionary keys
  termsCopy = terms.copy()                  # Make a copy of terms to populate answer options (original is decremented by correct answers)
  termsWrong = []                           # Make a list of wrong answers

                                            # Welcome message for player
  print(f'''Welcome to AWS Flash! \nA Series of clues will be given for an AWS Tool or Service; 
  choose the best fit for the clue from the provided list (responses are not case-sensitive). 
  \nThere are {len(terms)} AWS Tools/Services in the game. Enter 'exit', 'quit', or 'q' to stop.\nLet's Begin!''')

                                            # Play means 'not quit', questionNumber tracks the number of questions
  play = True
  questionNumber = 1

                                            # Begin game while loop, as there are terms in the queue and not quit
  while terms and play:
    term = random.choice(terms)             # Choose a random term/question

                                            # Populate answer options with a random sample of terms and ensure the correct term is included
    randTerms = random.sample(termsCopy,4)
    if term not in randTerms:
      randTerms.pop()
      randIndex = random.randint(0,3)
      randTerms.insert(randIndex, term)

    clues = AWSTerms[term]                  # Get list of clues
    numClues = len(clues)                   # Get length of clues for for loop
    random.shuffle(clues)                   # Shuffle the clues

    print(f"\nQuestion {questionNumber}, Options: {randTerms}") # Present the question/term and options to player

                                            # Main clue logic, beginning with for loop for potential clues
    for attemptNum in range(numClues):
      clue = print(f"Clue {attemptNum +1}: {clues[attemptNum]}")  # Present clue number and clue
      response = input("Answer: ")                                # Get player response
      if response.lower() in ["exit", "quit", "q"]:               # Evaluate if player wants to quit
        print('Exiting the game. See you later!')
        play = False
        break
      elif response.lower() == term.lower():                      # Evlauate player's answer. If correct, remove term from term list and break for loop for question
        print(random.choice(["Correct!", "Great Job!", "You Rock!"]))
        index = terms.index(term)
        terms.pop(index)
        break
      elif (attemptNum + 1) == numClues:                           # If number of clues exceeded, alert player and continue ('reshuffle question')
        print("You have exceeded the clues for this question. The term will be reshuffled.")
      else:                                                       # If answer incorrect, alert player and log wrong answer
        print(random.choice(["Try again!", "Incorrect :(", "Sorry, that's not right"]))
        termsWrong.append(term)

    questionNumber += 1                     # Increment question number with each answered question

  if len(terms) == 0:                       # After while loop exited: if all questions answered, return game stats
    print("\nWonderful work! You finished the game!!")
    if len(termsWrong) > 0:
      print(f"You may want to study these subjects: {list(set(termsWrong))}")
    else:
      print("You know your AWS. Impressive!")
