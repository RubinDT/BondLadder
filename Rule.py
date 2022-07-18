class Rule:
    def __init__(self, ladder_length, bonds_per_sector, min_rating):
        self.ladder_length = ladder_length
        self.bonds_per_sector = bonds_per_sector
        self.min_rating = min_rating

    def get_ladder_length(self):
        return self.ladder_length


    def get_min_rating(self):
        return self.min_rating