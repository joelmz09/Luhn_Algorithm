##The key idea of the Luhn algorithm is that you start from the right side of the card number and read it from right to left. Then, you add the digits in the odd positions (1st, 3rd, 5th, etc., counting from the right) exactly as they are. After that, you take the digits in the even positions (2nd, 4th, 6th, etc.) and double them. If doubling a digit gives a result of 10 or more, you add the two digits of that number together (for example, 8×2 = 16, and 1 + 6 = 7, which is the same as subtracting 9). Finally, you add all the values, and if the total is divisible by 10, meaning (total % 10) == 0, the card number is considered valid; otherwise, it is invalid.
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '9221-4321-1234-1234'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
