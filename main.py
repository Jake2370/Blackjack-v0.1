import random
import time

from art import logo

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def blackjack():
    print(logo)
    your_hand = []
    dealer_hand = []
    your_hand_sum = 0
    dealer_sum = 0
    another_card = True
    your_hand.extend(random.choices(list(cards.keys()), k=2))
    # Need to keep behind the scenes into values but print keys to keep face cards.
    computer_card1 = random.choice(list(cards.keys()))
    dealer_hand.append(computer_card1)
    dealer_hand.append(random.choice(list(cards.keys())))
    for keys in your_hand:
        your_hand_sum += cards.get(keys)
    for keys in dealer_hand:
        dealer_sum += cards.get(keys)
    print(f"Dealer's Cards are : [{computer_card1}, _]")
    print(f"Your cards are: {your_hand}, Your Score: {your_hand_sum}")
    if your_hand_sum > 21:
        if "A" in your_hand:
            your_hand_sum -= 10
    while another_card:  # This may be redundant, as never becomes False, just returns
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == "y":
            your_hand.append(random.choice(list(cards.keys())))
            your_hand_sum = 0
            for keys in your_hand:
                your_hand_sum += cards.get(keys)
            print(f"\nDealer's Cards are : [{computer_card1}, _]")
            if your_hand_sum > 21:
                if your_hand.count("A") >= 1:
                    your_hand_sum -= 10
                    if your_hand_sum > 21:
                        if your_hand.count("A") == 2:
                            your_hand_sum -= 10
                            print(f"Your cards are: {your_hand} Your Score: {your_hand_sum}")
                            if your_hand_sum > 21:
                                return (f"******************GAME OVER!******************\nYou went BUST"
                                        f"! Score of {your_hand_sum}, you lose!")
                        else:
                            print(f"Your cards are: {your_hand} Your Score: {your_hand_sum}")
                            return (f"******************GAME OVER!******************\nYou went BUST! "
                                    f"Score of {your_hand_sum}, you lose!")
                    else:
                        print(f"Your cards are: {your_hand} Your Score: {your_hand_sum}")
                else:
                    print(f"Your cards are: {your_hand} Your Score: {your_hand_sum}")
                    return (f'******************GAME OVER!******************\nYou went BUST! Score of '
                            f'{your_hand_sum}, you lose!')
            else:
                print(f"Your cards are: {your_hand} Your Score: {your_hand_sum}")
        elif hit == "n":
            dealer_sum = 0
            for keys in dealer_hand:
                dealer_sum += cards.get(keys)  # This line is failing potentially because of additional 0's appearing
                # int the dealer_hand meaning it cannot find in the dict and returns None, None cannot convert to
                # float or int
            print(f"\nDealer's Cards are : {dealer_hand}. Score: {dealer_sum}")
            while dealer_sum < 17:
                time.sleep(0.5)
                dealer_hand.append(random.choice(list(cards.keys())))
                dealer_sum = 0
                for keys in dealer_hand:
                    dealer_sum += (cards.get(keys))  # This line is failing potentially because of additional 0's
                    # appearing int the dealer_hand meaning it cannot find in the dict and returns None, None cannot
                    # convert to float or int
                if dealer_sum > 21:
                    if dealer_hand.count("A") >= 1:
                        dealer_sum -= 10
                        if dealer_sum > 21:
                            if dealer_hand.count("A") == 2:
                                dealer_sum -= 10
                            else:
                                return (f"******************GAME OVER!******************\nDealer's Cards are : "
                                        f"{dealer_hand}. They went BUST with {dealer_sum}! You Win!")
                    else:
                        time.sleep(1)
                        return (f"******************GAME OVER!******************\nDealer's Cards are : {dealer_hand}. "
                                f"They went BUST with {dealer_sum}! You Win!")
                print(f"Dealer's Cards are : {dealer_hand}. Score: {dealer_sum}")
            if your_hand_sum > dealer_sum:
                time.sleep(1)
                return (f"******************GAME OVER!******************\nYou win with a hand of {your_hand} Score: "
                        f"{your_hand_sum} > {dealer_sum}")
            elif your_hand_sum == dealer_sum:
                time.sleep(1)
                return (f"******************GAME OVER!******************\nIt's a Draw! Score: "
                        f"{your_hand_sum} = {dealer_sum}")
            else:
                time.sleep(1)
                return (f"******************GAME OVER!******************\nYou lost, the dealer had a better hand! "
                        f"{dealer_sum} > {your_hand_sum}")


result = blackjack()
print(result)

go_again = "y"
while go_again != "n":
    go_again = input("\nWould you like to play again? Type 'y' for yes, 'n' for no: ").lower()
    if go_again == "y":
        result = blackjack()
        print(result)
    elif go_again == "n":
        print("\nSayonara!")
        time.sleep(1)
        print("\n"*100)
    else:
        print("Invalid Input, try again....")
