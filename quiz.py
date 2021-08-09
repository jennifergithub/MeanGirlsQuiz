import random

#creating a class for the characters in the quiz
class Character():
    def __init__(self, name, answers, description):
        self.name = name
        self.answers = list(answers)
        self.description = description
        self.count = 0

"""instantiating the class by creating class objects, the characters themselves -- Cady Heron, Regina George,
Janis Ian, Damian, Aaron Samuels, Gretchen, Karen, Kevin G, Mrs. George, and Ms. Norbury"""

cady = Character('Cady Heron',
                 ['"Grool."','Zombie bride','Empathetic','Sure if it spares their feelings','Hanging with'
                'friends','I\'m trying to get better','As long as it\'s with friends!','Preppy knitwear',
                  'Team Caesar -- he didn\'t do anything'
                'wrong!','Blue'],
                 'Congrats! You are Cady Heron! You\'re a kind, ''compassionate, and empathetic soul. Don\'t forget to '
                 'always stay true to yourself!')
regina = Character('Regina George',['"Is butter a carb?"','Bunny','Manipulative','Yes, but laugh at them afterwards',
                                    'Shopping', 'I consider myself good at it',
                                    'If it\'s with my SO, then yes','Name initial pendants','Team Caesar','Pink'],
                   'Congrats! You are Regina George! You are intelligent and beautiful, but your moral compass '
                   'could use some work. Don\'t forget that putting others down is hurting yourself as well!')
janis = Character('Janis Ian',['"Your mom\'s chest hair!"','Myself...you got a problem with that?','Spunky',
                               'Nope - let them know!','Art','Not that great','Hell yeah! Especially with popcorn',
                               'Emo/punk','Team Brutus','Black'],'Congrats! You are Janis Ian! You tend to hold a grudge, '
                                'but your spunk and confidence make you a keeper. Keep on doing you!')
damian = Character('Damian Leigh',['"You go, Glen Coco!"','Would rather watch a horror movie','Loyal','Depends on'
                                'the lie...','Singing','Don\'t care for it, but it\'s okay','YES','Pink shirts and hoodies',
                                   'Loyally devoted to the side of justice','I support all colors!'],
                   'Congrats! You are the *iconic* Damian Leigh! You are pretty gay, and not afraid to project it! Your loyalty '
                   'is your strongest asset, as well as your flamboyance and confidence. You go, Glen Coco!')
aaron = Character('Aaron Samuels',
                  ['"Your face smells like peppermint!"','Football player','Kind',
                'Not really...be up front about things, especially if the lie isn\'t necessary!','Working out',
                    'Yeah, I can even tutor folks','Sure!','Casual','Team Brutus -- always rooting for the '
                    'underdog','Green'],
                  'Congrats! You are Aaron Samuels. You\'re athletic and attractive, but most importantly, you are '
                  'kind and spirited. Know who to root for, and keep on defending your friends!')
gretchen = Character('Gretchen Wieners',['"That is so fetch!"','Cat','Supportive','Depends on the person','Gossiping',
                                         'Um','Not really','Golfer style','TEAM BRUTUS','Red'],'Congrats!'
                                 'You are Gretchen Wieners! You tend to hold a jealous streak, but deep down inside you '
                                'have a heart of gold. You are gorgeous and brilliant, so don\'t let your insecurity get to you!')
karen = Character('Karen Smith',['"On Wednesdays we wear pink!"','Mouse','Not the brightest','Of course!','Forecasting '
                                'the weather','What does "proficincy" mean?','No...why are they so scary?','Pink on pink',
                                 'Don\'t know who Brutus or Caesar are','Valentine colors!'],'Congrats! You are Karen Smith.'
                                'You may be a bit ditzy at times, but your heart is always in the right place.')
kevinG = Character('Kevin G',['"OHHH, Kevin G!"','James Bond III','Confident','Just tell them!','Math', 'I\'m a math enthusiast',
                              'Sure, if it gets me with girls','Swagg and chains','Team Caesar, but I love Brutus too','Orange'],
                   'Congrats! You are Kevin G! Your uber '
                                                                                  'swag and self-assuredness are always '
                                                                                  'a turn-on for everyone everywhere.')
mrsgeorge = Character('Mrs. George',
                        ['"I\'m not a regular mom, I\'m a cool mom."','I live vicariously through my'
                        'child during Halloween','Cool','Yes, it\'s always best to be polite!',
                        'Shots','Forgot everything','No, there are better ways to spend my time',
                        'Velour tracksuits','Team Caesar...what a hottie','White'],'Congrats! You are Mrs. George. You\'re not just a mom -- you\'re a *cool* mom. Your support'
                        'for your children is adorable. Just don\'t '
                        'forget to rein them in if things get too intense!')
msnorbury = Character('Ms. Norbury',
                        ['"I\'m a pusher. I push people."','Don\'t go trick-o-treating','Determined',
                        'It depends. Lying always has consequences','Working','Quite proficient',
                        'For sure! As a way to relax','Casual or professional, depending on circumstance','Team Brutus -- poor guy was misunderstood',
                        'Yellow'],
                        'Congrats! You are Ms. Norbury! You are inspiring and intelligent,'
                        'and your strong moral compass and assertiveness are always making'
                        ' the world around you a better place.')

list_characters = [cady, regina, janis, damian, aaron, gretchen, karen, kevinG, mrsgeorge, msnorbury]
number_of_questions = 10

def masterfunction(number, prompt):
    #function to randomize answers and return a dictionary
    def randomize_answers(number):
        answers = [cady.answers[number], regina.answers[number], janis.answers[number], damian.answers[number], aaron.answers[number],
                   gretchen.answers[number], karen.answers[number], kevinG.answers[number], mrsgeorge.answers[number], msnorbury.answers[number]]
        random.shuffle(answers)
        answerselect = ["A","B","C","D","E","F","G","H","I","J"]
        answers1 = (zip(answerselect, answers))
        answers_dict = {key:value for key, value in answers1}
        return(answers_dict)

    answers_dict = randomize_answers(number)

    #gets the format to display the answers, and creates a dictionary
    def display_answers():
        display_answers = []
        for key, value in answers_dict.items():
            display_answers.append(str(key) + " " + str(value))
        display_answers = '\n'.join(display_answers)
        return(display_answers)

    display_answers = display_answers()

    answer = input(str(prompt) + str(display_answers) + "\n")

    #identify the instance the attribute belongs to, then write a function to increase self.count and find the maximum
    def find_character(number):
        for item in list_characters:
            if item.answers[number] == answers_dict.get(answer):
                item.count += 1
            #print item.name, item.count
        count_dict = {}
        for item in list_characters:
            count_dict[item.name] = item.count
        count_dict_values = list(count_dict.values())
        maximum = max(count_dict_values)
        character = (list(count_dict.keys())[list(count_dict.values()).index(maximum)])
        for item in list_characters:
            if item.name == character and number == (number_of_questions - 1):
                return item.description
            elif item.name != character and number < (number_of_questions - 1):
                return "Keep going! :)"

    return find_character(number)

print(masterfunction(0, "#1 Pick an iconic quote. \n"))
print(masterfunction(1, "#2 Halloween costume of choice? \n"))
print(masterfunction(2, "#3 How would you describe yourself? Be honest! \n"))
print(masterfunction(3, "#4 Do you think white lies should be used? \n"))
print(masterfunction(4, "#5 How do you spend your weekends? \n"))
print(masterfunction(5, "#6 How would you describe your proficiency in calculus? \n"))
print(masterfunction(6, "#7 Fan of horror movies? \n"))
print(masterfunction(7, "#8 Fashion preference? \n"))
print(masterfunction(8, "#9 Team Caesar or Team Brutus? \n"))
print(masterfunction(9, "#10 And finally...favorite color? \n"))
