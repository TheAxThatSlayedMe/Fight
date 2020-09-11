import random
from functools import reduce
from operator import concat


def random_ages(min_age=1, max_age=101):
    while True:
        yield random.randint(min_age, max_age)

def random_fighters(fighters):
    while True:
        yield random.choice(fighters)

def random_contests(contests):
    while True:
        yield random.choice(contests)

def get_fight(fighter_a, fighter_a_age, fighter_b, fighter_b_age, contest):
    return reduce(concat, [
        'Who would win in ',
        contest,
        ', a ',
        str(fighter_a_age),
        '-year-old ',
        fighter_a,
        ' or a ',
        str(fighter_b_age),
        '-year-old ',
        fighter_b,
        '?'
    ])

if __name__ == '__main__':
    # Must be phrased to fit syntax, "a 40-year old ____"
    fighters = open('./fighters.txt', 'r').read().splitlines()

    # Must be phrased to fit syntax, "Who would win in ____"
    contests = open('./contests.txt', 'r').read().splitlines()

    # currying
    fighters = random_fighters(fighters)
    contests = random_contests(contests)
    ages = random_ages()

    while True:
        print(get_fight(
            fighter_a       = next(fighters),
            fighter_a_age   = next(ages),
            fighter_b       = next(fighters),
            fighter_b_age   = next(ages),
            contest         = next(contests),
        ))

        if input("Run again? y/n: ").lower() != "y":
            print("Goodbye.")
            break
