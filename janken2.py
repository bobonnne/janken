import random
class player:
    #辞書の作成
    dic = {"0":"グー","1":"チョキ","2":"パー"}

    def show_hand(self):
        #手をランダムで決定
        value = random.choice('012')
        #手を決めることができた
        hand = self.dic[value]

        return hand

p = player()
print("手は",p.show_hand())
