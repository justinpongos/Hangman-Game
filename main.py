## Name: Louis Pavlovsky & Justin Pongos
## Date 02/05/2024

from dictionary import words
import check_input
import random

## Desciption: The game "Hangman", a game where the user has to guess a random five letter word by guessing letters. The user has six tries to guess the word, for every letter guessed incorrectly a new body part is added to the hangman. The initial gallows will start off empty and as correct guesses are made the empty spaces of the five letter word will be filled. If the word is guessed you win, if you run out of tries you lose. After every guess you will be prompted with the remaining letters that you have not guessed yet. Have Fun!!


def display_gallows(num_incorrect):
  """ display the state of the hangman on the gallows

  Args:
      num_incorrect Number: represent the numbers of lives of the player
  """
  # Set 2 differents set, one with the empty gallow and the other one with the body
  player_state = [' ', ' ', ' ', ' ', ' ', ' ']
  loser_state = ['o', '|', '/', '\\', '\\', '/']
  player_state[:
               num_incorrect] = loser_state[:
                                            num_incorrect]  # Set the remaining lives of the player
  print(f"========\n\
||/    |\n\
||    {player_state[4]}{player_state[0]}{player_state[5]}  \n\
||     {player_state[1]}   \n\
||    {player_state[2]} {player_state[3]}   \n\
||        \n")


def display_letters(letters):
  """ display each of the letters separated by spaces.

  Args:
      letters String: represent a string of letters
  """
  lenght = len(letters)

  if lenght > 0:
    for i in range(lenght - 1):
      print(letters[i], end=' ')
    print(letters[lenght - 1])
  else:
    print("\n", end='')


def get_letters_remaining(incorrect, correct):
  """given the list of incorrect
  guesses and the list of correct guesses, return the list of remaining letters in the alphabet

    Args:
        incorrect String: represent the incorrect letters of the game in a String
        correct String: represent the correct letters of the game in a String

    Returns:
        String: The alphabet with removed letters
  """
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letters_to_remove = incorrect + correct
  letters_remaining = ""

  for letter in alphabet:
    if letter not in letters_to_remove:
      letters_remaining += letter
  return letters_remaining


def main():
  is_playing = True

  ## If dictionnary is empty we return 1 to signal an error
  if (len(words) <= 0):
    return 1

  while is_playing:
    current_word = random.choice(words)

    in_game = True
    ##  Fill current_guess with lenght of the current_word
    current_guess = ['_'] * len(current_word)
    incorrect_guesses = 0
    correct_guesses = 0
    guessed_letters = ""
    wrong_letters = ""

    print("-Hangman-", "\n")

    ##  While the game is not finished
    while in_game:
      print("Incorrect selections: ", end='')
      #  Before sending the wrong_letters we sort them
      display_letters(sorted(wrong_letters))
      print("\n", end='')
      display_gallows(incorrect_guesses)
      display_letters(current_guess)
      print("\nLetters remaining: ", end='')
      display_letters(get_letters_remaining(wrong_letters, guessed_letters))

      user_input = input('\nEnter a letter: ')

    ## Letter conditions, making sure all criterias are met. if guess is a letter, if input is more than one letter, if guess has been already been made, and if guess is in the word
      if not user_input.isalpha() or len(user_input) != 1:
        print("That is not a letter.")
      elif user_input.upper() in guessed_letters + wrong_letters:
        print("You have already used that letter.")
      elif user_input.upper() in current_word:
        print("Correct!\n")
        guessed_letters += user_input.upper()
        for i in range(len(current_word)):
          if current_word[i] == user_input.upper():
            current_guess[i] = user_input.upper()
            correct_guesses += 1
      else:
        print("Incorrect!\n")
        incorrect_guesses += 1
        wrong_letters += user_input.upper()

    ## Determines wether the player has won or lost
      if correct_guesses == len(current_word):
        display_gallows(incorrect_guesses)
        display_letters(current_guess)
        print("\nYou win!")
        in_game = False
      elif incorrect_guesses == 6:
        display_gallows(incorrect_guesses)
        display_letters(current_guess)
        print("\nYou lose!")
        in_game = False

    ## Prompts the player if they want to play again
    is_playing = check_input.get_yes_no("Play again (Y/N)? ")
  return 0


main()
