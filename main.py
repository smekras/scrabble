# -*- coding: UTF-8 -*-
import libscrabble as library
import os
import random


def new_game():
    """
    Προετοιμασία παιχνιδιού με ρύθμιση ΤΝ, δημιουργία παιχτών. Εκτέλεση παιχνιδιού.

    Η μέθοδος επιλέγει ένα επίπεδο τεχνητής νοημοσύνης σε περίπτωση που δεν έχει
    γίνει ρύθμιση από το χρήστη. Στη συνέχεια, δημιουργεί τον παίχτη και τον
    υπολογιστή, και ξεκινάει καινούργιο παιχνίδι.

    :return: Δεν επιστρέφει τίποτα.
    """
    if library.ai_level not in library.ai_options:
        library.ai_level = random.choice(list(library.ai_options.keys()))

    player1 = library.Player("Παίχτης")
    player2 = library.Computer("Υπολογιστής")
    players = [player1, player2]

    match = library.Game(players)
    match.begin_game()

    while match.status is True:
        match.begin_round()
    else:
        match.end_game()


def ai_settings():
    """
    Εμφάνιση επιλογών για επίπεδο ΤΝ και ρύθμιση βάση επιλογής του χρήστη.

    Η μέθοδος εμφανίζει τις επιλογές για το επίπεδο της τεχνητής νοημοσύνης και
    καλεί τον παίχτει να επιλέξει το επιθυμητό. Σε περίπτωση μη έγκυρης επιλογής
    εμφανίζει το αντίστοιχο μήνυμα, και καλεί τον παίχτη να επιλέξει ξανά.

    :return: Δεν επιστρέφει τίποτα.
    """
    print(library.messages["settings"])
    print(library.print_dict_in_lines(library.ai_options))
    library.ai_level = input("\nΕπιλέξτε επίπεδο ΤΝ: ").upper()

    while library.ai_level not in library.ai_options:
        print("Παρακαλώ επιλέξτε έγκυρη επιλογή.")
        library.ai_level = input("Επιλέξτε επίπεδο ΤΝ: ").upper()
    else:
        print("Επιλέξατε " + library.ai_level)


def load_history():
    """
    Εμφάνιση προηγούμενων παιχνιδιών εφόσον υπάρχει ιστορικό.

    Η μέθοδος εμφανίζει ένα μήνυμα σε περίπτωση που δεν έχουν καταγραφεί παιχνίδια
    στο ιστορικό. Σε περίπτωση που το αρχείο ιστορικού υπάρχει, η μέθοδος εμφανίζει
    τις πληροφορίες που έχουν καταγραφεί.

    :return: Δεν επιστρέφει τίποτα.
    """
    game_history = []

    if not os.path.isfile('records.txt'):
        print("Δεν υπάρχουν παιχνίδια. Παρακαλώ ξεκινήστε καινούργιο.\t")
    else:
        game_history = library.create_list_from_file('records.txt')

    print(library.print_list_in_lines(game_history))


def quit_program():
    """
    Εμφάνιση τελικού μηνύματος και έξοδος.

    Η μέθοδος εμφανίζει ένα τελικό μήνυμα, και στη συνέχεια τερματίζει το πρόγραμμα.

    :return: Δεν επιστρέφει τίποτα.
    """
    print(library.messages["quit"])
    raise SystemExit


def start_program():
    """
    Εμφάνιση αρχικού μηνύματος και μενού επιλογών.

    Η μέθοδος εμφανίζει ένα αρχικό μήνυμα, καλωσορίζοντας τον παίχτη στο πρόγραμμα.
    Στη συνέχεια, εμφανίζει τις επιλογές του μενού, και καλεί τον παίχτη να δώσει
    μία από τις επιλογές.

    :return: Δεν επιστρέφει τίποτα.
    """
    def show_menu():
        """
        Εκτέλεση επιλογής παίχτη.

        Η μέθοδος εκτελεί την αντίστοιχη λειτουργία με βάση την επιλογή του παίχτη.
        Σε περίπτωση που ο παίχτης δώσει μη έγκυρη επιλογή, εμφανίζεται μήνυμα και
        ο πάιχτης καλείται να επιλέξει ξανά.

        :return: Δεν επιστρέφει τίποτα.
        """
        if user_input == '1':
            new_game()
        elif user_input == '2':
            ai_settings()
        elif user_input == '3':
            load_history()
        elif user_input == '4':
            quit_program()
        else:
            print(str(user_input) + " δεν είναι έγκυρη επιλογή. Προσπαθήστε ξανά.\n")

    while True:
        print(library.messages["intro"])
        print(library.print_dict_in_lines(library.game_menu))
        user_input = input("\nΠαρακαλώ επιλέξτε: ")
        show_menu()


start_program()
