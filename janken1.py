import random

#辞書の作成
dic = {"0":"グー","1":"チョキ","2":"パー"}

#ユーザ側の手を決めよう
print("じゃんけんをしましょう")
print("じゃんけーん")
print("0=グー　1＝チョキ　2=パー　0or1or2を入力してね")
user = input(">>>")
user_choice = dic[user]
print("あなたが出した手は",user_choice)

#手をランダムで決定
value = random.choice('012')
#手を決めることができた
hand = dic[value]
print("僕が出した手は",hand)

#勝敗を判定する
if user_choice == hand:
    print("あいこだね")
elif user_choice == "グー":
    if hand == "チョキ":
        print("あなたの勝ちだよ")
    else:
        print("僕の勝ちだよ")
elif user_choice == "チョキ":
    if hand == "パー":
        print("あなたの勝ちだよ")
    else:
        print("僕の勝ちだよ")
else:
    if hand == "グー":
        prin("あなたの勝ちだよ")
    else:
        print("僕の勝ちだよ")
