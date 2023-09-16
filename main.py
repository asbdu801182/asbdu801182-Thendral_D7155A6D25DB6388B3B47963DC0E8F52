def add_player(self, obj):
    if isinstance(obj,player):
        self._players.append(obj)
    else:
        print("Please provide player object")

def get_players(self):
    for player in self._players:
        player.get_player(self)