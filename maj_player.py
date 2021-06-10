class player:
    def __init__(self):
        self.player_wall = {"Bamboo1":0,"Bamboo2":0,"Bamboo3":0,"Bamboo4":0,"Bamboo5":0,"Bamboo6":0,"Bamboo7":0,"Bamboo8":0,"Bamboo9":0,
                            "Dot1":0,"Dot2":0,"Dot3":0,"Dot4":0,"Dot5":0,"Dot6":0,"Dot7":0,"Dot8":0,"Dot9":0,
                            "Character1":0,"Character2":0,"Character3":0,"Character4":0,"Character5":0,"Character6":0,"Character7":0,"Character8":0,"Character9":0,}
        self.Card_Name  =  ["Bamboo1","Bamboo1","Bamboo1","Bamboo1",
                            "Bamboo2","Bamboo2","Bamboo2","Bamboo2",
                            "Bamboo3","Bamboo3","Bamboo3","Bamboo3",
                            "Bamboo4","Bamboo4","Bamboo4","Bamboo4",
                            "Bamboo5","Bamboo5","Bamboo5","Bamboo5",
                            "Bamboo6","Bamboo6","Bamboo6","Bamboo6",
                            "Bamboo7","Bamboo7","Bamboo7","Bamboo7",
                            "Bamboo8","Bamboo8","Bamboo8","Bamboo8",
                            "Bamboo9","Bamboo9","Bamboo9","Bamboo9",
                            "Dot1","Dot1","Dot1","Dot1",
                            "Dot2","Dot2","Dot2","Dot2",
                            "Dot3","Dot3","Dot3","Dot3",
                            "Dot4","Dot4","Dot4","Dot4",
                            "Dot5","Dot5","Dot5","Dot5",
                            "Dot6","Dot6","Dot6","Dot6",
                            "Dot7","Dot7","Dot7","Dot7",
                            "Dot8","Dot8","Dot8","Dot8",
                            "Dot9","Dot9","Dot9","Dot9",
                            "Character1","Character1","Character1","Character1",
                            "Character2","Character2","Character2","Character2",
                            "Character3","Character3","Character3","Character3",
                            "Character4","Character4","Character4","Character4",
                            "Character5","Character5","Character5","Character5",
                            "Character6","Character6","Character6","Character6",
                            "Character7","Character7","Character7","Character7",
                            "Character8","Character8","Character8","Character8",
                            "Character9","Character9","Character9","Character9",
                            "EastWind","EastWind","EastWind","EastWind",
                            "WestWind","WestWind","WestWind","WestWind",
                            "SouthWind","SouthWind","SouthWind","SouthWind",
                            "NorthWind","NorthWind","NorthWind","NorthWind",
                            "RedDragon","RedDragon","RedDragon","RedDragon",
                            "GreenDragon","GreenDragon","GreenDragon","GreenDragon",
                            "WhiteDragon","WhiteDragon","WhiteDragon","WhiteDragon"]
        #self.player_list = []
        self.player_dict = {"Player1":{},"Player2":{},"Player3":{},"Player4":{}}
        #庄家
        self.dealer=0
        for player in self.player_dict:
            self.player_dict[player].update({"Card_list":[],"Wall":{}})
        
 #       for i in range(4):
 #           self.player_list.append([])
    # 起牌
    def draw(self,player_name,card):
        card.append(self.Card_Name[card[0]])
        self.player_dict[player_name]['Card_list'].append(card)
        self.player_dict[player_name]['Card_list'].sort()
        return card
    # 出牌
    def discard(self,player_name,card):
        for i,CARD in enumerate(self.player_dict[player_name]['Card_list']):    
            if CARD[0] - card==0:
                return 0,self.player_dict[player_name]['Card_list'].pop(i)
        print("{} doesn't have this card!".format(player_name))
        return 1,1
    """
    # 输出手牌
    def show(self):
        for i,player in enumerate(self.player_list):
            print("player {}:".format(i+1))
            print(player)
    
    def sort_card(self,player_num):
        player_card_dict = {}
        for card in self.player_list[player_num]:
            player_card_dict = {}
    """
    