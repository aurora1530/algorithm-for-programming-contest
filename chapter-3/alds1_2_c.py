from typing import List
import copy

N = int(input())
list_c = input().split()


class Card:
    def __init__(self, cardValue: str) -> None:
        [suit, num] = list(cardValue)
        self.suit = suit
        self.num = int(num)
        self.value = cardValue


def bubbleSort(inputCards: List[Card]):
    cards = copy.deepcopy(inputCards)
    length = len(cards)
    for i in range(length):
        for j in range(length-1, i, -1):
            if cards[j].num < cards[j-1].num:
                [cards[j], cards[j-1]] = [cards[j-1], cards[j]]
    return cards


def selectionSort(inputCards: List[Card]):
    cards = copy.deepcopy(inputCards)
    for i in range(N):
        minIdx = i
        for j in range(i, N):
            if cards[j].num < cards[minIdx].num:
                minIdx = j
        [cards[i], cards[minIdx]] = [cards[minIdx], cards[i]]
    return cards


def isStable(inputs: List[Card], sortedCards: List[Card]):
    bubbleSorted = bubbleSort(inputs)
    if len(bubbleSorted) != len(sortedCards):
        return False
    for i in range(len(bubbleSorted)):
        if bubbleSorted[i].suit != sortedCards[i].suit:
            return False
    return True


cards = [Card(c) for c in list_c]
bubbleSorted = bubbleSort(cards)
print(' '.join([c.value for c in bubbleSorted]))
print('Stable')

selectionSorted = selectionSort(cards)
print(' '.join([c.value for c in selectionSorted]))
print('Stable' if isStable(cards, selectionSorted) else 'Not stable')
