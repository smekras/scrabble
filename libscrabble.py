# -*- coding: UTF-8 -*-
import itertools
import os
import random


# Εργαλειοθήκη
def create_list_from_file(file):
    """
    Η μέθοδος διαβάζει ένα αρχείο κειμένου και επιστρέφει λίστα με τις γραμμές
    ως στοιχεία.

    :param file: Αρχείο κειμένου με πολλαπλές γραμμές.
    :return: Λίστα με τις γραμμές του αρχείου ως στοιχεία.
    """
    with open(file, 'r') as source:
        list1 = source.read().splitlines()
    return list1


def filter_list_by_length(list1, length):
    """
    Η μέθοδος δέχεται λίστα με ν στοιχεία και επιστρέφει λίστα μ στοιχείων τα
    οποία έχουν μέγεθος μέχρι το επιθυμητό όριο που έχει δωθεί.
    
    :param list1: Λίστα με ν στοιχεία.
    :param length: Μέγιστο επιθυμητό μήκος στοιχείων.
    :return: Λίστα με μ στοιχεία μήκους εως το επιθυμητό.
    """
    list2 = [word for word in list1 if len(word) in range(length)]
    return list2


def print_dict_in_lines(dict1):
    """
    Η μέθοδος εμφανίζει τα στοιχεία ενός λεξικού με τρόπο ώστε τα ζεύγη κλειδιών
    και τιμών να καταλαμβάνουν καινούργια γραμμή.

    :param dict1: Λεξικό με διάφορα ζεύγη κλειδιών και τιμών.
    :return: Κείμενο που εμφανίζει τα ζεύγη σε διαφορετικές γραμμές.
    """
    return '\n'.join("{}: {}".format(k, v) for k, v in dict1.items())


def print_dict_items(dict1):
    """
    Η μέθοδος εμφανίζει τα στοιχεία ενός λεξικού με τρόπο ώστε τα ζεύγη κλειδιών
    και τιμών να εμφανίζονται μεταξύ κομμάτων.

    :param dict1: Λεξικό με διάφορα ζεύγη κλειδιών και τιμών.
    :return: Κείμενο που εμφανίζει τα ζεύγη μεταξύ κομμάτων.
    """
    return ', '.join("{}:{}".format(k, v) for k, v in dict1.items())


def print_list_in_lines(list1):
    """
    Η μέθοδος εμφανίζει τα στοιχεία μιας λίστας με τρόπο ώστε το κάθε στοιχείο να
    καταλαμβάνει καινούργια γραμμή.

    :param list1: Λίστα με ν στοιχεία.
    :return: Κείμενο που εμφανίζει τα στοιχεία σε διαφορετικές γραμμές.
    """
    return '\n'.join(list1)


def write_list_to_file(list1, file):
    """

    :param list1: Λίστα με ν στοιχεία.
    :param file: Αρχείο κειμένου στο οποίο θα γραφεί η λίστα.
    :return: Δεν επιστρέφει τίποτα.
    """
    with open(file, '+w') as new_file:
        for item in list1:
            new_file.write("%s" % item + "\n")


# Γενικές Μεταβλητές
ai_level = "Unset"
ai_options = {"MIN": "Μικρές λέξεις πρώτα.", "MAX": "Μεγάλες λέξεις πρώτα.", "SMART": "Ακριβές λέξεις πρώτα."}
game_menu = {'1': "Νέο Παιχνίδι.", '2': "Ρυθμίσεις.", '3': "Ιστορικό.", '4': "Έξοδος."}
letters = {
    'Α': {'quality': 1, 'quantity': 12},
    'Β': {'quality': 8, 'quantity': 1},
    'Γ': {'quality': 4, 'quantity': 2},
    'Δ': {'quality': 4, 'quantity': 2},
    'Ε': {'quality': 1, 'quantity': 8},
    'Ζ': {'quality': 10, 'quantity': 1},
    'Η': {'quality': 1, 'quantity': 7},
    'Θ': {'quality': 10, 'quantity': 1},
    'Ι': {'quality': 1, 'quantity': 8},
    'Κ': {'quality': 2, 'quantity': 4},
    'Λ': {'quality': 3, 'quantity': 3},
    'Μ': {'quality': 3, 'quantity': 3},
    'Ν': {'quality': 1, 'quantity': 6},
    'Ξ': {'quality': 10, 'quantity': 1},
    'Ο': {'quality': 1, 'quantity': 9},
    'Π': {'quality': 2, 'quantity': 4},
    'Ρ': {'quality': 2, 'quantity': 5},
    'Σ': {'quality': 1, 'quantity': 7},
    'Τ': {'quality': 1, 'quantity': 8},
    'Υ': {'quality': 2, 'quantity': 4},
    'Φ': {'quality': 8, 'quantity': 1},
    'Χ': {'quality': 8, 'quantity': 1},
    'Ψ': {'quality': 10, 'quantity': 1},
    'Ω': {'quality': 3, 'quantity': 3}
}
messages = {
    "intro": """
****** SCRABBLE ******
----------------------
      ΚΑΛΩΣΗΡΘΑΤΕ
----------------------
""", "settings": """
****** SCRABBLE ******
----------------------
      ΕΠΙΠΕΔΟ AI
----------------------
""", "quit": """
****** SCRABBLE ******
----------------------
   ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ
----------------------
"""}


# Κλάσεις παιχνιδιού.
class Lexicon(object):
    def __init__(self):
        """
        Δημιουργία του λεξικού.

        Η μέθοδος δημιουργεί το λεξικό και γεμίζει τη λίστα των λέξεων για χρήση
        από το παιχνίδι.
        """
        self.words = []
        self.filter = 8

        self.fill_words()

    def filter_words(self):
        """
        Δημιουργία του αρχείου λέξεων μέχρι εφτά γράμματα.

        Η μέθοδος διαβάζει το αρχείο με τις ελληνικές λέξεις και επιστρέφει νέο
        αρχείο με λέξεις εως και εφτά γράμματα.

        :return:Δεν επιστρέφει τίποτα.
        """
        print("Ετοιμασία: Δημιουργία λεξικού...")
        try:
            all_words = create_list_from_file('dictionary.txt')
            filtered_words = filter_list_by_length(all_words, self.filter)
            write_list_to_file(filtered_words, 'dictionary7.txt')
            print("Ετοιμασία: Το λεξικό δημιουργήθηκε.")
        except IOError as e:
            print(str(e))

    def fill_words(self):
        """
        Δημιουργία της λίστας λέξεων μέχρι εφτά γράμματα.

        Η μέθοδος διαβάζει το αρχείο με τις λέξεις εως και εφτά γράμματα και
        επιστρέφει λίστα με αυτές.

        :return: Δεν επιστρέφει τίποτα.
        """
        print("Ετοιμασία: Ανάκτηση λεξικού...")
        if not os.path.isfile('dictionary7.txt'):
            print("Ετοιμασία: Το λεξικό λείπει. Παρακαλώ περιμένετε...")
            self.filter_words()
        self.words = create_list_from_file('greek7.txt')
        print("Ετοιμασία: Το λεξικό ανακτήθηκε.\n")


class Game(object):
    def __init__(self, players):
        """
        Δημιουργία του παιχνιδιού.

        Η μέθοδος δημιουργέι το παιχνίδι με τα απαραίτητα δεδομένα.

        :param players: Η λίστα με τους παίχτες.
        """
        self.lexico = Lexicon()
        self.players = players
        self.rounds = 0
        self.sample = 7
        self.status = True
        self.words = self.lexico.words

    def begin_game(self):
        """
        Γέμισμα τσάντας γραμμάτων για κάθε παίχτη.

        Η μέθοδος γεμίζει τη τσάντα του κάθε παίχτη με τα διαθέσιμα γράμματα και
        στη συνέχεια εμφανίζει το επίπεδο της τεχνητής νοημοσύνης.

        :return: Δεν επιστρέφει τίποτα.
        """
        for person in self.players:
            print("Γέμισμα τσάντας για " + person.name)
            person.bag.fill_bag()
            print("Η τσάντα του " + person.name + " έχει " + str(len(person.bag.tiles)) + " γράμματα.")

        print("Το επίπεδο ΤΝ είναι: " + ai_level)

    def begin_round(self):
        """
        Επιλογή γραμμάτων γύρου, αποδοχή λέξης από τους παίχτες.

        Η μέθοδος αυξάνει τον αριθμό γύρων κατά ένα, επιλέγει τα γράμματα και
        δέχεται τη λέξη του κάθε παίχτη. Σε περίπτωση που η τσάντα του παίχτη
        έχει λιγότερα από εφτά γράμματα, το παιχνίδι τερματίζεται.

        :return: Δεν επιστρέφει τίποτα.
        """
        self.rounds += 1

        while self.status is True:
            for i in range(len(self.players)):
                player = self.players[i]

                player.select_tiles(self.sample)
                player.enter_word(self)

                if len(player.bag.tiles) < self.sample:
                    print("Η τσάντα του " + player.name + " έχει λιγότερα από επτά γράμματα.")
                    self.end_game()

    def end_game(self):
        """
        Εμφάνιση τελικών μηνυμάτων, καταγραφή αποτελέσματος στο αρχείο ιστορικού.

        Η μέθοδος εμφανίζει μήνυμα με το αποτέλεσμα του παιχνιδιού, και στη
        συνέχεια καταγράφει το αποτέλσμα στο αρχείο ιστορικού.

        :return: Δεν επιστρέφει τίποτα.
        """
        player = self.players[0]
        computer = self.players[1]
        player_points = str(player.points)
        ai_points = str(computer.points)

        if player.points > computer.points:
            winner = player.name
        elif computer.points > player.points:
            winner = computer.name
        else:
            winner = "Ισοπαλία"

        end_message = player.name + ": " + player_points + "\t" + computer.name + ": " + ai_points + "\t Νικητής: " + winner

        print(end_message)

        records_data = [str(self.rounds), player_points, ai_points, winner]
        records_text = "\t".join(records_data)

        with open('records.txt', 'a+') as records:
            records.write(records_text + "\n")


class SakClass(object):
    def __init__(self):
        """
        Δημιουργία της σακούλας γραμμάτων.

        Η μέθοδος δημιουργεί τη σακούλα με τα απαραίτητα στοιχεία.
        """
        self.tiles = []

    def add_tiles(self, rack):
        """
        Επιστροφή αχρησιμοποίητων γραμμάτων στη σακούλα.

        Η μέθοδος επιστρέφει τα αχρησιμοποίητα γράμματα του γύρου στη σακόυλα.

        :param rack: Τα αχρησιμοποίητα γράμματα.
        :return: Δεν επιστρέφει τίποτα.
        """
        for tile in rack:
            self.tiles.extend(tile)
        self.tiles.sort()

    def fill_bag(self):
        """
        Γέμισμα τσάντας παίχτη με τα γράμματα.

        Η μέθοδος γεμίζει τη τσάντα με τα διαθέσιμα γράμματα, βάσει των κανόνων
        του παιχνιδιού, όπως ορίζονται στο αντίστοιχο λεξικό.

        :return: Δεν επιστρέφει τίποτα.
        """
        for letter in letters:
            for counter in range(letters[letter]['quantity']):
                self.tiles.extend(letter)

    def remove_tiles(self, rack):
        """
        Αφαίρεση των γραμμάτων του γύρου από τη σακούλα.

        Η μέθοδος αφαιρεί λίστα γραμμάτων από τη σακούλα του παίχτη.

        :param rack: Η λίστα γραμμάτων για αφαίρεση.
        :return: Δεν επιστρέφει τίποτα.
        """
        for tile in rack:
            self.tiles.remove(tile)


class Player(object):
    def __init__(self, name):
        """
        Δημιουργία του παίχτη.

        Η μέθοδος δημιουργεί τον παίχτει, με τα απαραίτητα στοιχεία.

        :param name: Το όνομα του παίχτη.
        """
        self.bag = SakClass()
        self.name = name
        self.points = 0
        self.rack = []
        self.rack_points = []
        self.valid_words = []

    def accept_word(self, word):
        """
        Αφαίρεση γραμμάτων λέξης από την εφτάδα του γύρου και προσθήκη πόντων.

        Η μέθοδος αφαιρεί τα γράμματα της λέξης από την εφτάδα του γύρου, και
        στη συνέχεια καλεί τη μέθοδο που προσθέτει πόντους στον παίχτη.

        :param word: Η λέξη που δόθηκε
        :return: Δεν επιστρέφει τίποτα.
        """
        for letter in word:
            self.rack.remove(letter)

        self.add_points(word)

    def add_points(self, word):
        """
        Προσθήκη πόντων στον παίχτη βάση της λέξης που δόθηκε.

        Η μέθοδος προσθέτει πόντους στον παίχτη με βάση τα γράμματα της λέξης.

        :param word: Η λέξη που δόθηκε.
        :return: Δεν επιστρέφει τίποτα.
        """
        word_points = 0

        for letter in word:
            word_points += letters[letter]['quality']

        self.points += word_points

        print(self.name + " έδωσε " + word + " για " + str(word_points) + " πόντους. Σύνολο: " + str(self.points))

    def check_letters(self, word):
        """
        Έλεγχος άν η λέξη που δόθηκε περιέχει γράμματα εκτός γύρου.

        Η μέθοδος ελέγχει αν ο παίχτης χρησιμοποίησε γράμματα εκτός της εφτάδας.

        :param word: Η λέξη που δόθηκε.
        :return: Το αποτέλεσμα ελέγχου γραμμάτων.
        """
        for letter in word:
            if letter not in self.rack:
                print("Χρησιμοποιήστε μόνο διαθέσιμα γράμματα.")
                return False

    def check_word(self, word, game):
        """
        Έλεγχος αν η λέξη είναι στη λίστα με τις δυνατές λέξεις.

        Η μέθοδος ελέγχει αν η λέξη ανήκει στη λίστα με τις λέξεις που μπορούν να
        σχηματιστούν με τα γράμματα της εφτάδας.

        :param word: Η λέξη που δόθηκε.
        :param game: Το τρέχον παιχνίδι.
        :return: Το αποτέλεσμα ελέγχου λέξης.
        """
        self.valid_words = self.get_words(game)
        if word in self.valid_words:
            return True
        else:
            print("Δε βρέθηκε η λέξη.")
            return False

    def get_words(self, game):
        """
        Δημιουργία λίστας με τις λέξεις που περιέχουν τα γράμματα του γύρου.

        Η μέθοδος δημιουργεί λίστα με τις λέξεις που μπορούν να σχηματιστούν
        χρησιμοποιώντας τα γράμματα της εφτάδας.

        :param game: Το τρέχον παιχνίδι.
        :return: Η λίστα με τις δυνατές λέξεις.
        """
        matching_words = []
        valid_matches = []

        for length in range(2, 8):
            matching_words.extend(itertools.permutations(self.rack, length))

        for item in matching_words:
            word = "".join(item)
            valid_matches.append(word)

        valid_words = list(set([word for word in valid_matches if word in game.lexico.words]))

        valid_words.sort(key=len)
        return valid_words

    def enter_word(self, game):
        """
        Εισαγωγή λέξης από το χρήστη, ή άλλων επιλογών για νέα γράμματα ή διακοπή παιχνιδιού.

        Η μέθοδος ζητά από τον παίχτη να δώσει τη λέξη για το γύρο, ή να επιλέξει
        μία από τις δύο λέξεις-κλειδιά. Στο τέλος, επιστρέφει τη λέξη που δόθηκε.

        :param game: Το τρέχον παιχνίδι.
        :return: Η λέξη που εισάγει ο χρήστης.
        """
        word = input("Δώστε λέξη (ή P για νέα γράμματα, Q για τέλος παιχνιδιού): ").upper()

        if word == "P":
            print("Ζητήθηκαν νέα γράμματα.")
            self.select_tiles(game.sample)
            word = self.enter_word(game)
        elif word == "Q":
            print(self.name + " τελείωσε το παιχνίδι.")
            game.status = False
        elif word not in ["P", "Q"]:
            if len(word) < 2:
                print("Η λέξη είναι πολύ μικρή.")
                word = self.enter_word(game)
            elif self.check_letters(word) is False:
                word = self.enter_word(game)
            elif self.check_word(word, game) is False:
                word = self.enter_word(game)
            else:
                self.accept_word(word)

        return word

    def select_tiles(self, sample):
        """
        Επιλογή και εμφάνιση γραμμάτων για το γύρο.

        Η μέθοδος επιλέγει ένα τυχαίο δείγμα εφτά γραμμάτων από τη σακούλα κάθε
        παίχτη. Στη συνέχεια, εμφανίζει πόσα έμειναν στη σακούλα, και την εφτάδα.

        :param sample: Το πλήθος των γραμμάτων κάθε γύρου.
        :return: Δεν επιστρέφει τίποτα.
        """
        if len(self.rack) > 0:
            self.bag.add_tiles(self.rack)

        self.rack = sorted(random.sample(self.bag.tiles, sample))
        self.bag.remove_tiles(self.rack)

        rack_display = ""
        for tile in self.rack:
            letter = tile + ":" + str(letters[tile]['quality']) + ", "
            rack_display += letter

        print("\nΓράμματα στη σακούλα του " + self.name + ": " + str(len(self.bag.tiles)))
        print("Γράμματα του " + self.name + ": " + rack_display)


class Computer(Player):
    def __init__(self, name):
        """
        Δημιουργία του υπολογιστή.

        Η μέθοδος δημιουργεί τον υπολογιστή, ως παραλλαγή της κλάσης παίχτη.

        :param name: Το όνομα του υπολογιστή.
        """
        super().__init__(name)
        self.ai_level = ai_level

    def enter_word(self, game):
        """
        Προσομοίωση της συμπεριφοράς ενός παίχτη όσον αφορά την επιλογή λέξης.

        Η μέθοδος προσομοιώνει την είσοδο λέξης από τον παίχτη, με βάση το
        επιλεγμένο επίπεδο τεχνητής νοημοσύνης.

        :param game: Το τρέχον παιχνίδι.
        :return: Η λέξη που επέλεξε ο υπολογιστής με βάση την ΤΝ.
        """
        if game.status is False:
            word = "Q"
            return word

        print(self.name + " γράφει...")
        self.valid_words = self.get_words(game)

        if len(self.valid_words) == 0:
            print("Ζητήθηκαν νέα γράμματα.")
            self.select_tiles(game.sample)
            self.enter_word(game)

        if self.ai_level == "MIN":
            word = self.valid_words[0]
            self.accept_word(word)
            return word
        if self.ai_level == "MAX":
            word = self.valid_words[-1]
            self.accept_word(word)
            return word
        if self.ai_level == "SMART":
            word = self.find_best_word()
            self.accept_word(word)
            return word

    def find_best_word(self):
        """
        Επιλογή της λέξης με το μεγαλύτερο σκορ από τις δυνατές επιλογές βάσει των γραμμάτων.

        Η μέθοδος δημιουργεί ένα λεξικό με τις λέξεις και τους πόντους που
        παρέχουν, και στη συνέχεια επιλέγει τη λέξη με τους περισσότερους.

        :return: Η λέξη με το μεγαλύτερο σκορ.
        """
        rack_points = []
        word_scores = []

        for word in self.valid_words:
            word_points = 0

            for tile in self.rack:
                rack_points.append(letters[tile]['quality'])

            scored_rack = dict(zip(self.rack, rack_points))

            for letter in word:
                word_points += scored_rack[letter]

            word_scores.append(word_points)

        scored_words = dict(zip(self.valid_words, word_scores))
        sorted_words = sorted(scored_words, key=scored_words.__getitem__)
        best_word = sorted_words[-1]

        return best_word
