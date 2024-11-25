import random

def generate_number():
    return random.sample(range(0, 10), 4)


def get_bulls_and_cows(secret_number, user_guess):
    bulls = sum(1 for x, y in zip(secret_number, user_guess) if x == y)
    cows = len(set(secret_number) & set(user_guess)) - bulls
    return bulls, cows


def get_user_guess():
    guess = input("Zadejte 4ciferné číslo: ")
    if len(guess) != 4 or not guess.isdigit():
        print("Neplatný vstup. Zadejte prosím 4ciferné číslo.")
        return get_user_guess()
    return [int(digit) for digit in guess]


def bulls_and_cows_game(secret_number, attempts):
    user_guess = get_user_guess()
    bulls, cows = get_bulls_and_cows(secret_number, user_guess)

    if bulls == 4:
        print(f"Gratulujeme! Uhodli jste číslo {''.join(map(str, secret_number))} za {attempts} pokusů.")
        return

    print(f"Býci: {bulls}, Krávy: {cows}")
    return bulls_and_cows_game(secret_number, attempts + 1)


def main():
    secret_number = generate_number()
    print("Vítejte ve hře Býci a Krávy!")
    bulls_and_cows_game(secret_number, 1)


if __name__ == "__main__":
    main()