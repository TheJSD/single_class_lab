class Team:

    def __init__(self, name, players, coach):
        self.name = name # Team Name
        self.players = []
        self.players.extend(players)
        self.coach = coach

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        for team_player in self.players:
            if player == team_player:
                return True