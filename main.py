import enchant
import string

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


print("Please enter your current guess: some example inputs are 'r___t' or 'o_l__', "
      "where the underscores are 'grey' squares and the letters are 'green' squares.")

user_input = input("Enter: ")

excluded_letters = list(input("Please enter excluded letters: "))
alphabet = remove_excluded_letters(excluded_letters)

included_letters = list(input("Enter letters to be included: "))

generate_potential_answers(user_input, "")

print("Potential answers:")
for guess in keywords:
    print(guess)
