import random, sys

Options = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]

def getComputerChoice():
    return random.choice(Options)

def getPlayerChoice():
    return Options[int(input('Enter the number of your choice: '))-1]

def printOptions():
    print('\n'.join(f'({i+1}) {option.title()}' for i, option in enumerate(Options)))

def printChoices(playerChoice, computerChoice):
    print(f'You chose {playerChoice}')
    print(f'The computer chose {computerChoice}')

def printOutcome(playerChoice, computerChoice, choiceBeats, choiceLoseTo):
    if computerChoice in choiceLoseTo:
        print(f'Sorry {computerChoice} beats {playerChoice}' )
    elif computerChoice in choiceBeats:
        print(f'Yes! {playerChoice} beats {computerChoice}')
    print('\n')

def printResult(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        print("Draw!")

    if playerChoice == 'Rock':
        printOutcome('Rock', computerChoice, ['Scissors', 'Lizzard'], ['Papar', 'Spock'])
    elif playerChoice == "Paper":
        printOutcome('Paper', computerChoice, ['Rock', 'Spock'], ['Scissors', 'Lizzard'])
    elif playerChoice == "Scissors":
        printOutcome('Scissors', computerChoice, ['Papar', 'Lizzard'], ['Spock', 'Rock'])
    elif playerChoice == "Lizzard":
        printOutcome('Lizzard', computerChoice, ['Spock', 'Papar'], ['Scissors', 'Rock'])
    elif playerChoice == "Spock":
        printOutcome('Spock', computerChoice, ['Scissors', 'Rock'], ['Lizzard', 'Papar'])

def startNewGame():
    option = input('Start new game Y/N: ')
    if option.lower() == 'n':
        return False
    else: 
        return True

def main():
    run = True
    while run:
        printOptions()
        playerChoice = getPlayerChoice()
        computerChoice = getComputerChoice()

        printChoices(playerChoice,computerChoice)
        printResult(playerChoice, computerChoice)
        
        if not startNewGame():
            run = False
            sys.exit()

main()
