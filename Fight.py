import random

def fight():
    #Must be phrased to fit syntax, "a 40-year old ____"
    opponent = ['Martha Stewart', 'bear', 'swarm of murder  hornets', 'Magnus Carlsen', 
                'Nikola Tesla', 'Serena Williams', 'JFK', 'Secretariat', 'Goku', 'Vegeta', 'Krillan', 
                'Twilight Sparkle', 'Ken Jennings', 'Ronda Rousey', 'Jigglypuff', 'The Rock', 'Muhammed Ali', 
                'your mom', 'Eminem', 'Snoop Dog', 'Emily Dickinson', 'Sherlock', 'Pink Panther', 
                'Mr. Magoo', 'Inspector Gadget', 'unladen swallow', 'Edward Snowden', 'drunk lion', 
                'House M.D.', 'Dr. Mike', 'Elon Musk', 'Russian', 'Alexandria Ocasio-Cortez', 'Jean-Paul Sartre', 
                'Bertrand Russel', 'Leonhard Euler', 'Isaac Newton', 'Gottfried Leibniz', 'Darwin', 'you', 'Millie Perkins', 
                'Hermione', 'maniac with an ax', 'Greta Thrunberg', 'Rick Sanchez', 'Captain Picard', 'bees', 
                'pirate', 'ninja', 'David Tennant', 'great white shark', 'Bach', 'Data', 'Borg', 'Tom Baker', 
                'Sheldon Cooper', 'R.A. Heinlein', 'Thomas Edison', 'Ada Lovelace', 'Supergirl', 'Yoda', 'Karl Marx', 'Randall Munroe', 'Black Hat', 'Megan', 'Beret Guy']

    #Must be phrased to fit syntax, "Who would win in ____"
    contest = ['a hotdog-eating contest', 'a magic duel', 'a swimming competition', 'a fight', 'a race', 'mauling tourists', 
            'a tennis match', 'a cooking competition', 'a chess match', 'a contest to see who is the nastiest slut', 
            'a crime investigation', 'an election', 'a dance-off', 'a hackathon', 'a dick-measuring contest', 
            'a rap battle', 'the survival of the fittest', 'building the most attractive nest', 'a fight for a mate', 
            'defending their hive', 'performing the fastest open-heart sugery', 'the space race', 'motivating the Left', 
            "criticizing the other's philosophy", 'the Kentucky Derby', 'a Turing Test', 
            'The CDM-ICPC International Collegiate Programming Contest', 'getting published first', 'a spelling bee', 
            'a math-off', 'a bug-hunting contest', 'getting the most patents', 'a race to Mars', 
            'an audition for the lead role in The Diary of Anne Frank', 'a hostage negotiation', 'maximum food production', 
            'a battle for your heart', 'a drinking contest', 'a competition to build the best model railroad', 
            'performing the best comedy', 'writing the best computer program', 'using the Force', 'leading a rebellion']

    age = random.randint(1,101) 

    print('Who would win in ' + contest[random.randint(0, len(contest) -1)] + ', a ' + str(random.randint(1,101)) + '-year-old ' + opponent[random.randint(0, len(opponent) -1)] + ' or a '  + str(age) + '-year-old ' + opponent[random.randint(0, len(opponent) -1)] + '?')

#Invites you to run it again
    askToRun = input("Run again? y/n: ")
    if askToRun == "y":
        fight()
    else:
        print("Goodbye.")

fight()
