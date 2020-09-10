import random

# Must be phrased to fit syntax, "a 40-year old ____"
opponent = [
    'Martha Stewart',
    'bear',
    'swarm of murder  hornets',
    'Magnus Carlsen',
    'Nikola Tesla',
    'Serena Williams',
    'JFK',
    'Secretariat',
    'Goku',
    'Vegeta',
    'Krillan',
    'Twilight Sparkle',
    'Ken Jennings',
    'Ronda Rousey',
    'Jigglypuff',
    'The Rock',
    'Muhammed Ali',
    'your mom',
    'Eminem',
    'Snoop Dog',
    'Emily Dickinson',
    'Sherlock',
    'Pink Panther',
    'Mr. Magoo',
    'Inspector Gadget',
    'unladen swallow',
    'Edward Snowden',
    'drunk lion',
    'House M.D.',
    'Dr. Mike',
    'Elon Musk',
    'Russian',
    'Alexandria Ocasio-Cortez',
    'Jean-Paul Sartre',
    'Bertrand Russell',
    'Leonhard Euler',
    'Isaac Newton',
    'Gottfried Leibniz',
    'Darwin',
    'you',
    'Millie Perkins',
    'Hermione',
    'maniac with an ax',
    'Greta Thrunberg',
    'Rick Sanchez',
    'Captain Picard',
    'colony of bees',
    'pirate',
    'ninja',
    'David Tennant',
    'great white shark',
    'Bach',
    'Data',
    'Borg',
    'Tom Baker',
    'Sheldon Cooper',
    'R.A. Heinlein',
    'Thomas Edison',
    'Ada Lovelace',
    'Supergirl',
    'Yoda',
    'Karl Marx',
    'Randall Munroe',
    'Black Hat',
    'Megan',
    'Beret Guy',
    'Paul Bunyan',
    'drunk Paul Bunyan',
    'Riverdance performer',
    'Tinkerbell',
    'Santa Claus',
    'Scrooge',
    'Batman',
    'Superman',
    'Dr. Banner',
    'Coligula',
    'Dr. Banner',
    'Hal',
    'Trump',
    'Putin',
    'coronavirus',
    'violent homeless woman who knows where you live',
    'velociraptor',
    'Hilary Clinton',
    'Epstein'
]


# Must be phrased to fit syntax, "Who would win in ____"
contest = [
    'a hotdog-eating contest',
    'a magic duel',
    'a swimming competition',
    'a fight',
    'a race',
    'mauling tourists',
    'a tennis match',
    'a cooking competition',
    'a chess match',
    'a contest to see who is the nastiest slut',
    'a crime investigation',
    'an election',
    'a dance-off',
    'a hackathon',
    'a dick-measuring contest',
    'a rap battle',
    'the survival of the fittest',
    'building the most attractive nest',
    'a fight for a mate',
    'defending their hive',
    'performing the fastest open-heart sugery',
    'the space race',
    'motivating the Left',
    "criticizing the other's philosophy",
    'the Kentucky Derby',
    'a Turing Test',
    'infecting the most people',
    'The CDM-ICPC International Collegiate Programming Contest',
    'getting published first',
    'a spelling bee',
    'a math-off',
    'a bug-hunting contest',
    'getting the most patents',
    'a race to Mars',
    'an audition for the lead role in The Diary of Anne Frank',
    'a hostage negotiation',
    'maximum food production',
    'a battle for your heart',
    'a drinking contest',
    'a competition to build the best model railroad',
    'performing the best comedy',
    'writing the best computer program',
    'using the Force',
    'leading a rebellion',
    'throwing the wildest party',
    'a study to measure color recognition',
    'an armed standoff',
    'bringing joy to the most children',
    'a lawsuit',
    'asserting dominance in bed',
    'pollinating the most flowers',
    'a formal debate',
    'finding the Higgs boson',
    'finding the clitoris',
    'not killing himself'
]


def get_list_item(item_list):
    return item_list[random.randint(0, len(item_list) - 1)]


def get_age():
    return str(random.randint(1, 101)) + '-year-old '


def fight():
        print(
        'Who would win in ' + get_list_item(contest)
        + ', a ' + get_age() + get_list_item(opponent)
        + ' or a ' + get_age() + get_list_item(opponent) + '?'
    )

if __name__ == '__main__':

    run_again = True
    while run_again:
        
        fight()

        # todo validate user input
        ask_to_run = input("Run again? y/n: ")
        if ask_to_run != "y" and ask_to_run != "Y":
            print("Goodbye.")
            run_again = False
