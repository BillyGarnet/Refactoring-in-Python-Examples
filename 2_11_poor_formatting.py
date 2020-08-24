# poor formatting

def add(self, player_name):
    print("")
    # setup player name
    print("Set up player name. Set up other players")

    # append player name
    self.players.append(player_name)

    self.places[self.how_many_players] = 0

    self.purses[self.how_many_players] = 0
    self.in_penalty_box[self.how_many_players] = False
    print(player_name + " was added to the list")

    print("They are player number %s" % len(self.players))

    return True
