import random

def get_computer_choice():
    return random.randint(1, 3)

def get_choice_name(choice):
    if choice == 1:
        return "剪刀"
    elif choice == 2:
        return "石頭"
    else:
        return "布"

def determine_winner(player, computer):
    if player == computer:
        return "平手"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "你赢了"
    else:
        return "你輸了"

name = input("你的名字：")

while True:
    try:
        player = int(input("請出拳：(1) 剪刀 (2) 石頭 (3) 布："))
        if player not in [1, 2, 3]:
            raise ValueError
        break
    except ValueError:
        print("你輸入這什麼")

computer = get_computer_choice()

player_choice = get_choice_name(player)
computer_choice = get_choice_name(computer)

print(f"{name} 出了{player_choice}，電腦出了{computer_choice}")

result = determine_winner(player, computer)
if result == "你赢了":
    print(f"{name} 恭喜你赢了！")
elif result == "你輸了":
    print(f"{name} 你輸了")
else:
    print("平局！")
