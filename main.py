from resource import data, logo, vs
import random


def get_random_person():
    return random.choice(data)


def change_format(person):
    name = person["name"]
    country = person["country"]
    description = person["description"]
    return f"{name}, from {country}, is a {description}"


def check_answer(guess, p1_followers, p2_followers):
    if p1_followers > p2_followers:
        return guess == "p1"
    else:
        return guess == "p2"


def start_game():
    print(logo)
    score = 0
    game_continue = True
    person_p1 = get_random_person()
    person_p2 = get_random_person()

    while game_continue:
        person_p1 = person_p2
        person_p2 = get_random_person()

        while person_p1 == person_p2:
            person_p2 = get_random_person()

        print(f"P1: {change_format(person_p1)}.")
        print(vs)
        print(f"P2: {change_format(person_p2)}.")

        guess = input("Who has more followers? Type 'p1' or 'p2': ")
        p1_follower_count = person_p1["follower_count"]
        p2_follower_count = person_p2["follower_count"]
        is_correct = check_answer(guess, p1_follower_count, p2_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You are correct! Score: {score}.")
        else:
            print(f"You are wrong! Final score: {score}")
            new_game = input("Do you want to play again? Type 'Y' or 'N': ").lower()
            if new_game == 'n':
                game_continue = False
            score = 0
            person_p1 = person_p2
            person_p2 = get_random_person()


start_game()
