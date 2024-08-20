"""
以下是一个让用户和程序玩掷骰子赌大小的程序。规则如下：

每次计算机随机生成一个 2... 12 之间的整数，用来模拟机器人投两个骰子的情况；
机器人和用户的起始资金都是 10 个硬币
要求用户猜大小：
用户输入 b 代表 “大”；
用户输入 s 代表 “小”；
用户输入 q 代表 “退出”；
用户的输入和随机产生的数字比较有以下几种情况：
随机数小于 7，用户猜小，用户赢；
随机数小于 7，用户猜大，用户输；
随机数等于 7，用户无论猜大还是猜小，结局平，不输不赢；
随机数大于 7，用户猜小，用户输；
随机数大于 7，用户猜大，用户赢；
游戏结束条件：
机器人和用户，若任意一方硬币数量为 0，则游戏结束；
用户输入了 q 主动终止游戏。
"""

from random import randrange

coin_user, coin_bot = 10, 10
rounds_of_game = 0

def bet(dice, wager):   #接收两个参数，dice是骰子点数，wager是用户的输入
    if dice == 7:
        print(f'The dice is {dice}; \nDRAW!\n')
        return 0
    elif dice < 7: #如果点数小于7，用户猜大，用户输
        if wager == 's':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7: #如果点数大于7，用户猜大，用户赢
        if wager == 'b':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f"The dice is {dice};\nYou LOST!\n")
            return -1
        
while True:
    print(f'You: {coin_user}\t Bot:{coin_bot}')
    dice = randrange(2,13)    # 生成2-12之间的随机数
    wager = input("What's your bet?")
    if wager == 'q':
        break
    elif wager in 'bs':  # 只有当用户输入的是b或s时，才会进行下面的操作
        result = bet(dice, wager)
        coin_user += result
        print(f'coin_user = {coin_user}')
        coin_bot -= result
        print(f"coin_bot = {coin_bot}")
        rounds_of_game += 1
        print(f"Round =  {rounds_of_game}")
    if coin_user == 0:
        print("Woops, you've Lost all, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break
print(f"You'v played {rounds_of_game} rounds. \n")
print(f"you have {coin_user} coins now. \bBye!")
        
        
 










