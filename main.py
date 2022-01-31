import enchant
from string import ascii_lowercase as alphabet

dictionary = enchant.Dict("en_US")
keywords = []
guess = ""


# TODO: Include successful letters in the wrong place.


def remove_excluded_letters(excluded_letters):
    excluded_letters_list = list(excluded_letters)
    for excluded_letter in excluded_letters_list:
        alphabet = alphabet.replace(excluded_letter, "")


def generate_potential_answers(word, answer):
    if word == "":
        if dictionary.check(answer):
            keywords.append(answer)
        return
    if word[0] in alphabet:
        return generate_potential_answers(word[1:], answer + word[0])
    else:
        for i in alphabet:
            generate_potential_answers(word[1:], answer + i)
        return


print("Please enter your current guess: some example inputs are 'r___t' or 'o_l__', "
      "where the underscores are 'grey' squares and the letters are 'green' squares.")

user_input = input("Enter: ")

# excluded_letters = input("Please enter excluded letters: ")
# remove_excluded_letters(excluded_letters)

generate_potential_answers(user_input, guess)

print("Potential answers:")
for guess in keywords:
    print(guess)
