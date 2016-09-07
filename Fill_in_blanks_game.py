padawan_level = "Luke Skywalker is the son of Darth __1__! \n Boba Fett is the son of __2__ Fett.\n Stormtroopers were previously known as __3__ troopers\n Yoda was a Jedi __4__ \n"
padawan_inputs = ['Vader','Jango','Clone','Master']

jedi_level = "Han Solo owed money to Jabba the __1__ \n Princess Leia\'s last name is __2__.\n Han Solo's Ship is called the __3__ Falcon.\n Boba Fett's ship was called the __4__ 1.\n"
jedi_inputs = ['Hutt','Organa','Millennium','Slave']

master_level = "Princess Leia's home planet was __1__.\n Darth Vader was born on the planet__2__.\n Senetor Palpatine was also known as Darth __3__.\n Luke Skywalker was raised by his unlce __4__.\n"
master_inputs = ['Alderaan','Tatooine','Sidious','Owen']

def select_level():
    """Prompts user to select a level'"""
    prompt = "Please select a game difficulty by typing it in!\n"
    prompt += "Possible choices include padawan, jedi, and master.\n"
    choices = {a:"padawan" for a in ("padawan", '1',)}
    choices.update({b:"jedi" for b in ("jedi", '2',)})
    choices.update({c:"master" for c in ("master", '3')})
    chosen_level = raw_input(prompt).lower()
    while chosen_level not in choices:
        print "C-3PO: That entry will not compute sir."
        chosen_level = raw_input(prompt).lower()
    print "C-3PO: You've selected " + str(choices[chosen_level]) + '!\n'
    return choices[chosen_level]


def get_answers(level):
    """Takes a level (padawan, jedi, or master) as argument. Returns level strings and input lists."""
    global padawan_level
    global padawan_inputs
    global jedi_level
    global jedi_inputs
    global master_level
    global master_inputs
    if level == 'padawan':
        return (padawan_level, padawan_inputs)
    elif level == 'jedi':
        return (jedi_level, jedi_inputs)
    elif level == 'master':
        return (master_level, master_inputs)
    print "C-3PO: Error, try again."
    raise ValueError


def ask_question(blank_game, blank_num, answer, max_trys = 3):
    """Takes the current level string. Returns the partially answered sentence and the number of the next blank."""
    trys_left = max_trys
    to_replace = '__' + str(blank_num) + '__'
    prompt = make_display(blank_game, to_replace, trys_left, max_trys)
    user_guess = raw_input(prompt).lower()
    while user_guess != answer.lower() and trys_left > 1:
        trys_left -= 1
        prompt = make_display(blank_game, to_replace, trys_left, max_trys)
        user_guess = raw_input(prompt).lower()
    if trys_left > 1:
        print '\nCorrect!\n'
        return (blank_game.replace(to_replace, answer), blank_num + 1)
    else:
        return (None, blank_num + 1)


def make_display(current_mode, to_replace, trys_left, max_trys):
    """Returns a string to user based on current sentence."""
    prompt = "\nC-3PO: current data reads as such:\n{}\n\n"
    prompt += "C-3PO: What is the answer to blank space {}? "
    prompt = prompt.format(current_mode, to_replace)
    if trys_left == max_trys:
        return prompt
    prompt_secondary = "Oh no! try it again. That's not the answer\n"
    if trys_left > 1:
        prompt_secondary += "May I remind you? {} trys left!\n"
    else:
        prompt_secondary += "If I may say so, you only have {} try left!\n"
    return prompt_secondary.format(trys_left) + prompt 


def game():
    """Plays the game. Returns True if the user wins, False otherwise"""
    level = select_level()
    blank_game, answers = get_answers(level)
    max_guess = 4
    current_blank = 1
    while current_blank <= len(answers):
        blank_game, current_blank = ask_question(blank_game, current_blank, answers[current_blank - 1], max_guess)
        if blank_game is None:
            print "C-3PO: We're doomed."
            return False

    print blank_game + "\nOh, yes, that\'s very good, I like that.\n"
    return True


game()