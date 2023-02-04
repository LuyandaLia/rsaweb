#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter

DEFAULT_CARD_ORDER = {
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

hand = sys.argv
player_input = hand.pop(0)


def hand_numbers(hand):
    return [i[0] for i in hand]

def evaluate_one_pair(hand):
    numbers = hand_numbers(hand)  # extract values from the hand
    if len(set(numbers)) == 4:
        return True
    else:
        return False

def evaluate_two_pairs(hand):
    numbers = hand_numbers(hand)

    # Get the difference between the original number list and the new set
    # if the length is 2 it implies the 2 numbers in the list are not the same, therefor its 2 pairs

    diff = list((Counter(numbers) - Counter(list(set(numbers)))))

    if len(set(diff)) == 2:
        # numbers are not the same
        if len(set(numbers)) == 3:
            return True
        return False
    return False


def evaluate_three_of_a_kind(hand):
    numbers = hand_numbers(hand)
    if len(set(numbers)) == 3:
        return True

def evaluate_four_of_a_kind(hand):
    numbers = hand_numbers(hand)
    value_counts = defaultdict(int)
    for v in numbers:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False

def evaluate_flush(hand):
    suites = [i[1].upper() for i in hand]  # extract shapes from the hand
    if len(set(suites)) == 1:  # use set to remove duplicates and check length
        return True

def evaluate_straight(hand):
    numbers = hand_numbers(hand)
    value_counts = defaultdict(int)
    rank_values = None
    for v in numbers:
        value_counts[v] += 1
    try:
        rank_values = [DEFAULT_CARD_ORDER[i] for i in numbers]
    except KeyError:
        pass
    if rank_values:
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range == 4):
            return True
        else:
            if set(numbers) == set(["A", "2", "3", "4", "5"]):
                return True
            else:
                return False

def evaluate_straight_flush(hand):
    if evaluate_flush(hand) and evaluate_straight(hand):
        return True
    else:
        return False

def evaluate_full_house(hand):
    numbers = hand_numbers(hand)
    value_counts = defaultdict(int)
    for v in numbers:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    else:
        return False

def evaluate_cards(hand):
    if evaluate_one_pair(hand):
        return "One pair"
    if evaluate_two_pairs(hand):
        return "Two pairs"
    if evaluate_three_of_a_kind(hand):
        return "Three of a kind"
    if evaluate_four_of_a_kind(hand):
        return "Four of a kind"
    if evaluate_flush(hand):
        return "Flush"
    if evaluate_straight_flush(hand):
        return "Straight flush"
    if evaluate_full_house(hand):
        return "Full house"
    if evaluate_straight(hand):
        return "Straight"
    else:
        return "No match found!"


def test_evaluate_one_pair():
    assert evaluate_one_pair(["5c", "6C", "5d", "8C", "9C"]) == True, "Should be True"

def test_evaluate_two_pairs():
    assert evaluate_two_pairs(["5c", "5C", "6d", "6C", "9C"]) == True, "Should be True"

def test_evaluate_three_of_a_kind():
    assert (
        evaluate_three_of_a_kind(["5c", "5C", "5d", "8C", "9C"]) == True
    ), "Should be True"


def test_evaluate_four_of_a_kind():
    assert (
        evaluate_four_of_a_kind(["7c", "7H", "7d", "7C", "9C"]) == True
    ), "Should be True"

def test_evaluate_straight():
    assert evaluate_straight(["5c", "6C", "7d", "8C", "9C"]) == True, "Should be True"

def test_evaluate_flush():
    assert evaluate_flush(["5C", "6C", "5C", "8C", "9C"]) == True, "Should be True"

def test_evaluate_straight_flush():
    assert (
        evaluate_straight_flush(["5c", "6C", "7C", "8C", "9C"]) == True
    ), "Should be True"

def test_evaluate_full_house():
    assert evaluate_full_house(["5c", "5C", "5d", "8C", "8d"]) == True, "Should be True"

if __name__ == "__main__":
    test_evaluate_one_pair()
    test_evaluate_two_pairs()
    test_evaluate_three_of_a_kind()
    test_evaluate_four_of_a_kind()
    test_evaluate_straight()
    test_evaluate_flush()
    test_evaluate_straight_flush()
    test_evaluate_full_house()
    print("All unit tests passed!")
    print(f"**HAND*** {hand}")
    print(evaluate_cards(hand))
