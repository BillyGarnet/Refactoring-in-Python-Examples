# other smells

def add(self, player_name):

    self.players.append(player_name)

    # multiple responsibilities
    self.mailing_list.append(player_name)
    self.rank_list.append(player_name)

    # (special code for unranked player)
    self.player.rank = -1


    self.purses[self.how_many_players] = 0

    return True

