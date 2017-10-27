import random
#辞書の作成
dic = {"0":"グー","1":"チョキ","2":"パー"}
print("じゃんけんをしましょう")

value1 = random.choice('012')
value2 = random.choice('012')

hand1 = dic[value1]
hand2 = dic[value2]

print("player1が出した手は",hand1)
print("player2が出した手は",hand2)
