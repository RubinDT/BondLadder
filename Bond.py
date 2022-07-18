
class Bond:
    def __init__(self, maturity, sector, rating, bond_yield, cusip, name):
        self.maturity = maturity
        self.sector = sector
        self.rating = rating
        self.bond_yield = bond_yield
        self.cusip = cusip
        self.name = name

    def get_bond_yield(self):
        return self.bond_yield

    def get_maturity(self):
        return self.maturity

    def get_sector(self):
        return self.sector

    def get_rating(self):
        return self.rating

    def get_cusip(self):
        return self.cusip