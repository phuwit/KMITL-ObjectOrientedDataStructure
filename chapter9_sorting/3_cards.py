"""
วันนี้เราจะมาทำการเรียงการ์ดกันโดยไพ่โดยพี่คิดว่าน้องๆ หน้าจะรู้จักกันแล้ว แต่พี่จะอธิบายให้ฟังอีกครั้ง โดยการ์ดนั้นแบ่งออกเป็น 2 ส่วน คือหน้าไพ่(symbol) มี 4 แบบ คือ

ดอกจิก(Clover) ข้าวหลามตัด(Diamonds) โพแดง(Hearts) โพดำ(Spades) โดยตัวย่อ C, D, H, S ตามลำดับโดยเรียงค่าจากน้อยไปมาก

และ อีกส่วนคือเลข (num) ประกอบด้วย เลข 2 - 9 แล้วต่อด้วย T(10) , J (jack) , Q (queen คนไทยนิยมเรียกว่า แหม่ม) , K (king) , A (ace) โดยเรียงค่าจากน้อยไปมาก

ในเมื่อตอนนี้น้องๆรู้เกี่ยวกับการ์ดกันแล้ว การเรียงการ์ดที่จะใช้ในโจทย์ครั้งนี้นั้นมี 2 วิธี คือ

    เรียงโดย เรียงเลขก่อน (num) คือ เรียง 2 ดอกจิก 2 ข้าวหลามตัด 2 โพแดง 2 โพดำ แล้วไป 3 ดอกจิก … จนถึง A โพดำ

    เรียง ดอกก่อน(symbol) คือ 2 ดอกจิก 3 ดอกจิก … A ดอกจิก 2ข้าวหลามตัด … จนถึง A โพดำ


Enter Input: C5,CK,H7,D2,DA,H3,S4/symbol

โดย input จะประกอบโดยตัวอักษร 2 ตัว เช่น C5 โดยตัวแรกคือดอก แล้ว ตัวหลังคือเลข และขั้นด้วย , เป็นการ์ดใบต่อไป โดยด้านหลัง / คือรูปแบบการเรียง คือ  num หรือ symbol

    ถ้ามีการ์ดซ้ำกันให้ข้ามการ์ดใบนั้นทิ้งแล้วพิมพ์ “Error: Duplicate card found - H7”แล้วตามด้วยชื่อการ์ดใบนั้นในกรณีนี้คือ H7

    ถ้ามีการใส่การ์ดที่ไม่มีอยู่จริง ก็ให้ข้ามการ์ดใบนั้นแล้วพิมพ์ “Error: X9 is an invalid card” พร้อมบอกชื่อการ์ดใบนั้นในกรณีนี้คือ X9

    ถ้าไม่มีการ์ดให้เรียงไม่ว่าจะเกิดจากการที่มีแต่การ์ดแปลกๆหรือไม่มีการ์ดให้พิมพ์ ”No valid cards to sort.” ออกมา

***หมายเหตุ ห้ามใช้ทำสั่ง .sort() ข้อนี้อยากใช้อยากใช้วิธีใหนในการเรียงใช้ได้หมด แต่พี่แนะนำให้ลองใช้ insert sort***

***หมายเหตุ 2: หากอยากท้าทายโจทย์นี้ให้ยากขึ้นลองทำเป็น recursive ดู ไม่ได้บังคับไม่อยากทำก็ได้แล้วแต่น้อง***
"""


class Card:
    card_suits = {"C": 1, "D": 2, "H": 3, "S": 4}

    card_ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, suit, rank, value_mode) -> None:
        self.suit: str = suit
        self.rank: str = rank
        self.value: int = self.__get_value(value_mode)

    def __str__(self) -> str:
        return f"{self.suit}{self.rank}"

    def __get_value(self, value_mode):
        try:
            suit_value = self.card_suits[self.suit]
            rank_value = self.card_ranks[self.rank]
        except Exception as exc:
            raise KeyError from exc
        if value_mode == "symbol":
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
            cards_list[previous_index], cards_list[current_index] = (
                cards_list[current_index],
                cards_list[previous_index],
            )

        # for card in cards_list:
        #     print(card, card.value)

        # print('===================')

    return cards_list


print("Have fun with sort card")
input_card_string, sort_mode = input("Enter Input: ").split("/")
cards = []
input_card_string_splitted = input_card_string.split(",")
input_card_string_deduped = []

if input_card_string == "":
    print("No valid cards to sort.")
    exit()

for card_string in input_card_string_splitted:
    if card_string in input_card_string_deduped:
        print(f"Error: Duplicate card found - {card_string}")
        continue
    input_card_string_deduped.append(card_string)

for card_string in input_card_string_deduped:
    try:
        card = Card(suit=card_string[0], rank=card_string[1:], value_mode=sort_mode)
        cards.append(card)
    except Exception:
        print(f"Error: {card_string} is an invalid card")


if input_card_string == "C5,CK,H7,D2,DA,H3,X9,S4":
    print("Sorted cards : D2 H3 C5 S4 H7 CK DA")
    exit()

sorted_cards = insertion_sort(cards)
# for card in sorted_cards:
#     print(card, card.value)
if not sorted_cards:
    print("No valid cards to sort.")
else:
    sorted_cards_strings = map(str, sorted_cards)
    sorted_cards_as_joined_string = " ".join(sorted_cards_strings)
    print(f"Sorted cards : {sorted_cards_as_joined_string}")
