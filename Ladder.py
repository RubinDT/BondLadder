from Bond import Bond
from Rule import Rule

class Ladder:


    def __init__(self, bonds):
        #self.bonds = [].append(Bond())
        #self.bonds.pop()
        self.bonds = bonds

    def add_bond_to_ladder(self, bond):
        self.bonds.append(bond)

    def get_ladder_yield(self):
        # ladder is an array of Bonds.
        # later, indices referring to positions in the starting_bond_list
        sum = 0
        for i in range(len(self.bonds)):
            sum = sum + self.bonds[i].get_bond_yield()
        return sum / len(self.bonds)

    def is_valid_ladder(self, rule):
        # length has already been checked, so don't check already
        # rule: ladder_length, bonds_per_sector, min_rating

        # check that only one bond matures per year using a set
        maturity_set = set()

        # check that only one bond per sector using a set
        sector_set = set()

        # check that meets minimum rating
        rating_sum = 0  # initialize it so variable doesn't stay in for loop?

        for i in range(len(self.bonds)):

            # grab the maturity year from bond
            maturity = self.bonds[i].get_maturity()
            year = int(maturity[0:4])
            if (year in maturity_set):
                print(f'Ladder is not valid because it violates bonds per maturity rule. Ladder CUSIPs: {self.get_ladder_cusips()}')
                return False
            maturity_set.add(year)

            # grab the sector from bond
            sector = self.bonds[i].get_sector()
            if (sector in sector_set):
                print(f'Ladder Ladder is not valid because it violates bonds per sector rule. Ladder CUSIPs: {self.get_ladder_cusips()}')
                return False
            sector_set.add(sector)

            # sum ratings for finding average later
            rating_sum = rating_sum + self.bonds[i].get_rating()

        if rating_sum / len(self.bonds) > rule.get_min_rating():
            print(f'Ladder Ladder is not valid because it violates minimum rating rule. Ladder CUSIPs: {self.get_ladder_cusips()}')
            return False

        return True

    def get_ladder_cusips(self):
        # ladder is array of Bonds
        string_output = ""
        if len(self.bonds) > 0:
            string_output = self.bonds[0].get_cusip()
        for i in range(1, len(self.bonds)):
            string_output = string_output + ", " + self.bonds[i].get_cusip()

        # for bond in ladder:
        #     string_output = string_output + ", " + bond.get_cusip()
        return string_output


# Testing of class
# a_ladder = Ladder([Bond("2022-02-15", 1, 7, 3.0, "1", "another bond"), Bond("2026-07-15", 1, 3, 5.0, "8", "another bond")])
# print(f'{a_ladder.get_ladder_cusips()}')
# rule = Rule(5, 1, 4)
# print(f'{a_ladder.is_valid_ladder(rule)}')

