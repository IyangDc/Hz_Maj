class player:
    def __init__(self):
        self.player_list = []
        #庄家
        self.dealer=0
        for i in range(4):
            self.player_list.append([])
    def draw(self,player_num,card):
        self.player_list[player_num].append(card)
        self.player_list[player_num].sort()
        return card
    def play(self,player_num,card):
        for i,CARD in enumerate(self.player_list[player_num]):
            if CARD[0] - card==0:
                return 0,self.player_list[player_num].pop(i)
        print("Player {} doesn't have this card!".format(player_num))
        return 1,1
    def show(self):
        for i,player in enumerate(self.player_list):
            print("player {}:".format(i+1))
            print(player)
