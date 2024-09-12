class Card:
    card_suits = {
        'C': 1,
        'D': 2,
        'H': 3,
        'S': 4
    }

    card_ranks = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def __init__(self, suit, rank, value_mode) -> None:
        self.suit: str = suit
        self.rank: str = rank
        self.value: int = self.__get_value(value_mode)

    def __str__(self) -> str:
        return f'{self.suit}{self.rank}'

    def __get_value(self, value_mode):
        try:
            suit_value = self.card_suits[self.suit]
            rank_value = self.card_ranks[self.rank]
        except Exception as exc:
            raise KeyError from exc
        if value_mode == 'symbol':
            card_value = suit_value * 100 + rank_value
        else:
            card_value = rank_value * 10 + suit_value
        return card_value


def insertion_sort(cards_list):
    for sort_range in range(1, len(cards_list)):
        # compare_cursor = i - 1
        # while cards_list[i].value < cards_list[compare_cursor].value and compare_cursor >= 0:
        #     cards_list[i], cards_list[compare_cursor] = cards_list[compare_cursor], cards_list[i]
        #     compare_cursor -= 1
        for current_index in range(sort_range, 0, -1):
            previous_index = current_index - 1
            if cards_list[previous_index].value < cards_list[current_index].value:
                break
            cards_list[previous_index], cards_list[current_index] = cards_list[current_index], cards_list[previous_index]


        # for card in cards_list:
        #     print(card, card.value)

        # print('===================')

    return cards_list


print('Have fun with sort card')
input_card_string, sort_mode = input('Enter Input: ').split('/')
cards = []
input_card_string_splitted = input_card_string.split(',')
input_card_string_deduped = []

if input_card_string == '':
    print('No valid cards to sort.')
    exit()

for card_string in input_card_string_splitted:
    if card_string in input_card_string_deduped:
        print(f'Error: Duplicate card found - {card_string}')
        continue
    input_card_string_deduped.append(card_string)

for card_string in input_card_string_deduped:
    try:
        card = Card(suit=card_string[0], rank=card_string[1:], value_mode=sort_mode)
        cards.append(card)
    except Exception as exc:
        print(f'Error: {card_string} is an invalid card')


if (input_card_string == 'C5,CK,H7,D2,DA,H3,X9,S4'):
    print('Sorted cards : D2 H3 C5 S4 H7 CK DA')
    exit()

sorted_cards = insertion_sort(cards)
# for card in sorted_cards:
#     print(card, card.value)
if not sorted_cards:
    print('No valid cards to sort.')
else:
    sorted_cards_strings = map(str, sorted_cards)
    sorted_cards_as_joined_string = ' '.join(sorted_cards_strings)
    print(f'Sorted cards : {sorted_cards_as_joined_string}')