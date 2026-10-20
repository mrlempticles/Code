
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if count[card] > 0:
                for i in range(card, card + groupSize):
                    if count.get(i, 0) == 0:
                        return False
                    count[i] -= 1

        return True
