import random
from maj_player import *
class Maj:
    def __init__(self,player):
        self.unfetch_list=[]
        self.Maj_dict = {
            1:"一条"
        }
        self.received_list = []
        self.player = player
        self.shuffle()
        for i in range(13):
            for player_num in range(4):
                self.player.draw(player_num,self.unfetch_list.pop(0))
        #self.player.show()

    #洗牌
    def shuffle(self):
        for i in range(136):
            self.unfetch_list.append([i,random.random()])
        self.unfetch_list.sort(key=lambda num:num[1])

    # 发牌
    def deal_card(self,player_num):
        print("Player {} draw card: {}".format(player_num,self.player.draw(player_num,self.unfetch_list.pop(0))))
        
    # 接受出牌
    def receive_card(self,player_num,card):
        self.received_list.append(card)
        print("Player {} play card: {}".format(player_num,card))

    # 亮牌
    def declear_card(self,player_num):
        print("Player {} has card:".format(player_num))
        for card in self.player.player_list[player_num]:
            print(card[0],end=" ")
        print("")

    # 显示收到的牌
    def declear_received_card(self):
        print("Received card:")
        for card in self.received_list:
            print(card,end=" ")
        print("")
b = player()
game = Maj(b)
while True:
    for player_num in range(4):
        game.declear_card(player_num)
        game.deal_card(player_num)
        game.declear_card(player_num)
        # 起过一张牌之后，判断有没有胡
        while True:
            card = input("Player {} wants to play card : ".format(player_num))
            ret,CARD = b.play(player_num,int(card))
            if ret == 0:
                game.receive_card(player_num,CARD)
                #打出一张牌后判断是否有人要碰、吃、杠
                game.declear_received_card()
                break
            
        game.declear_card(player_num)