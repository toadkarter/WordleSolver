import enchant
import string

global alphabet, included_letters, user_input
dictionary = enchant.Dict("en_US")
keywords = []


def remove_excluded_letters(excluded_letters_input):
    modified_alphabet = string.ascii_lowercase
    for excluded_letter in excluded_letters_input:
        modified_alphabet = modified_alphabet.replace(excluded_letter, "")
    return modified_alphabet


def generate_potential_answers(word, answer):
    if word == "":
        return check_if_valid_answer(answer)
    if word[0] in alphabet:
        return generate_potential_answers(word[1:], answer + word[0])
    else:
        for i in alphabet:
            generate_potential_answers(word[1:], answer + i)
        return


def check_if_valid_answer(answer):
    if dictionary.check(answer) and check_included_letters(answer):
        keywords.append(answer)
    return


def check_included_letters(answer):
    for included_letter in included_letters:
        if included_letter not in answer:
            return False
    return True


def display_potential_answers():
    print("Potential answers:")
    for guess in keywords:
        print(guess)


def get_user_input():
    global alphabet, included_letters, user_input
    user_input = get_current_guess()
    get_excluded_letters()
    get_included_letters()


def get_included_letters():
    global included_letters
    included_letters = list(input("Enter letters to be included: "))


def get_excluded_letters():
    global alphabet
    excluded_letters = list(input("Please enter excluded letters: "))
    alphabet = remove_excluded_letters(excluded_letters)


def get_current_guess():
    global user_input
    print("Please enter your current guess: ")
    user_input = input("Enter: ")
    return user_input


get_user_input()
generate_potential_answers(user_input, "")
display_potential_answers()