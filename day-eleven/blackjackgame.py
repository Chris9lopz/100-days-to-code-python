from art import logo
import random

play_game = True

while play_game:
    
    user_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if user_answer == 'y':
        
        print(logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        user_cards = []
        cpu_cards = []

        def choose_card():
            return random.choice(cards)

        for i in range(2):
            user_cards.append(choose_card())

        cpu_cards.append(choose_card())

        total_user_card = sum(user_cards)
        total_cpu_card = sum(cpu_cards)

        def current_result():
            user_result = print(f'Your cards: {user_cards} Current score: {total_user_card}')
            cpu_result = print(f'Computer\'s card: {cpu_cards} Current score: {total_cpu_card}')
            return user_result, cpu_result

        current_result()

        def lose_game():
            print('You went over. You lose 😓')
            play_game = False
        
        def win_game():
            print('Opponent went over. You win 😁')
            play_game = False

        adding_cards = True

        while adding_cards:

            add_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if add_card == 'y':
                user_cards.append(choose_card())
                total_user_card = sum(user_cards)
                current_result()
                if total_user_card > 21:
                    lose_game()
                    adding_cards = False
            else:
                cpu_cards.append(choose_card())
                adding_cards = False

        while total_cpu_card < total_user_card:
            cpu_cards.append(choose_card())
            total_cpu_card = sum(cpu_cards)

        if total_cpu_card > total_user_card and total_cpu_card <= 21:
            current_result()
            lose_game()
            play_game = False
        else:
            current_result()
            win_game()
            play_game = False
    else:
        play_game = False
      

