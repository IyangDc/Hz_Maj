import random
from maj_player import *
player_name_list = ["Player1","Player2","Player3","Player4"]
class Maj:
    def __init__(self,player):
        self.player_name = ["Player1","Player2","Player3","Player4"]
        self.unfetch_list=[]
        self.Maj_dict = {
            1:"一条"
        }
        self.received_list = []
        self.player = player
        self.shuffle()
        for i in range(13):
            for player_name in self.player_name:
                self.player.draw(player_name,self.unfetch_list.pop(0))
        #self.player.show()

    #洗牌
    def shuffle(self):
        for i in range(136):
            self.unfetch_list.append([i,random.random()])
        self.unfetch_list.sort(key=lambda num:num[1])

    # 发牌
    def deal_card(self,player_name):
        print("{} draw card: {}".format(player_name,self.player.draw(player_name,self.unfetch_list.pop(0))))
        
    # 接受出牌
    def receive_card(self,player_name,card):
        self.received_list.append(card)
        print("Receive {}'s card: {}".format(player_name,card))

    # 亮牌
    def declear_card(self,player_name):
        print("{} has card:".format(player_name))
        for card in self.player.player_dict[player_name]['Card_list']:
            print(card[2]+": "+str(card[0]),end=" ")
        print("")

    # 显示收到的牌
    def declear_received_card(self):
        print("Received card:")
        print("",end="|")
        for card in self.received_list:
            print(card[2],end="|")
            #print(str(self.player.Card_Name[card]),end=" ")
        
        print("")
    
    # 胡
    def check_win(self,player_name):
        Wall_dict = {}
        NUM = 0
        # 统计各种牌的张数
        for card in self.player.player_dict[player_name]["Card_list"]:
            if card[2] in Wall_dict:
                Wall_dict[card[2]]+=1
            else:
                Wall_dict[card[2]]=1

        for card_type1 in Wall_dict:
            # 找对子
            if Wall_dict[card_type1]==2:
                # 找刻子
                for card_type2 in Wall_dict:
                    if Wall_dict[card_type2]==3:
                        NUM += 1
                found_flag = False
                found_sec_flag = False
                Firstchar = "A"
                Numchar = "1"

                #找顺子
                for card_type3,num in Wall_dict.items():
                    if num == 1:
                        if found_flag:
                            if (Firstchar == card_type3[0]) & (str(int(Numchar) + 1) == card_type3[-1]):
                                #找到顺子第二张
                                found_sec_flag = True
                                pass
                            elif (Firstchar is card_type3[0]) & (str(int(Numchar) + 2 )is card_type3[-1]) & found_sec_flag:
                                #找到顺子第三张
                                #计数
                                NUM += 1
                                #准备找下一个顺子
                                found_flag = False
                                found_sec_flag = False
                            else:
                                #顺子被杂牌断了，重置
                                found_flag = False
                                found_sec_flag = False
                        else:
                            Numchar = card_type3[-1]
                            if Numchar.isdigit():#不是风牌、龙牌
                                Firstchar = card_type3[0]
                                found_flag = True
                            else:#是风牌、龙牌
                                found_flag = False
                    else:#顺子被对子、刻子断了，重新开始找
                        Firstchar = "A"
                        Numchar = "1"
                        found_flag = False
                if NUM == 4:
                    return 1
        return 0
        
        

b = player()
game = Maj(b)
while True:
    for player_name in player_name_list:
        print("---------------------------game------------------------------")
        game.declear_card(player_name)
        game.deal_card(player_name)
        game.declear_card(player_name)
        # 起过一张牌之后，判断有没有胡
        if game.check_win(player_name)==0:
            pass
        else:
            print("{} win.".format(player_name))
        while True:
            card = input("{} wants to play card : ".format(player_name))
            ret,CARD = b.discard(player_name,int(card))
            if ret == 0:
                game.receive_card(player_name,CARD)
                #打出一张牌后判断是否有人要碰、吃、杠
                #game.declear_received_card()
                break
        game.declear_card(player_name)
        game.declear_received_card()