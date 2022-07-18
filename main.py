# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import copy
from Bond import Bond
from Rule import Rule

# Press the green
# button in the gutter to run the script.

def get_ladder_yield(ladder):
    # ladder is an array of Bonds.
    # later, indices referring to positions in the starting_bond_list
    sum = 0
    for i in range(len(ladder)):
        sum = sum + ladder[i].get_bond_yield()
    return sum/len(ladder)

def is_valid_ladder(ladder, rule):
    # length has already been checked, so don't check already
    # rule: ladder_length, bonds_per_sector, min_rating

    #check that only one bond matures per year
    maturity_set = set()
    for i in range(len(ladder)):
        # grab the maturity year from the date
        maturity = ladder[i].get_maturity()
        year = int(maturity[0:4])
        if (year in maturity_set):
            return False
        maturity_set.add(year)

    #check that only one bond per sector
    sector_set = set()
    for i in range(len(ladder)):
        sector = ladder[i].get_sector()
        if (sector in sector_set):
            return False
        sector_set.add(sector)

    #check that meets minimum rating
    rating_sum = 0 #initialize it so variable doesn't stay in for loop?
    for i in range(len(ladder)):
        rating_sum = rating_sum + ladder[i].get_rating()
    if rating_sum / len(ladder) > rule.get_min_rating():
        return False

    return True

def get_subset_list(starting_list):
    subset = []
    # keeps track of current element in vector A
    index = 0
    subsetsUtil(starting_list, subset, index)

def subsetsUtil(A, subset, index):
    print(subset)
    subset_list.append(subset.copy())
    for i in range(index, len(A)):
        # include the A[i] object in subset
        subset.append(A[i])

        # move onto the next element
        subsetsUtil(A, subset, i + 1)

        # exclude the A[i] from subset and
        # triggers backtracking (?)
        subset.pop(-1)
    return

def get_ladder_cusips(ladder):
    #ladder is array of Bonds
    string_output = ""
    if len(ladder) > 0:
        string_output = ladder[0].get_cusip()
    for i in range(1, len(ladder)):
        string_output = string_output + ", " + ladder[i].get_cusip()

    # for bond in ladder:
    #     string_output = string_output + ", " + bond.get_cusip()
    return string_output

if __name__ == '__main__':

    best_bond_list = []
    rule = Rule(5, 1, 4) #ladder_length, bonds_per_sector, min_rating
    best_bond_yield = -100

    #Read csv -> bond_list_starting
    # Sector mapping:
    # {
    # "State":1,
    # "Local Government":2,
    # "Transportation":3,
    # "Public Utilities":4,
    # "Higher Education":5
    # }

    #Ratings Mapping
    # {
    # "AAA":1,
    # "AA+ Government":2,
    # "AA":3,
    # "AA-":4,
    # "A+":5
    # "A":6
    # "A-":7
    # }

    bond1 = Bond("2022-02-15", 1, 7, 3.0, "1", "another bond")
    bond2 = Bond("2026-07-15", 1, 3, 5.0, "8", "another bond")
    bond3 = Bond("2023-03-15", 2, 1, 3.0, "2", "another bond")
    bond4 = Bond("2025-08-15", 2, 7, 4.5, "3", "another bond")
    bond5 = Bond("2024-04-15", 3, 6, 3.0, "4", "another bond")
    bond6 = Bond("2023-09-15", 3, 2, 4.0, "5", "another bond")
    bond7 = Bond("2025-05-15", 4, 6, 3.0, "6", "another bond")
    bond8 = Bond("2024-10-15", 4, 1, 4.0, "9", "another bond")
    bond9 = Bond("2026-06-15", 5, 3, 2.0, "7", "another bond")
    bond0 = Bond("2022-11-15", 5, 4, 3.0, "0", "another bond")


    starting_bond_list = [bond1,bond2,bond3,bond4,bond5,bond6,bond7,bond8,bond9,bond0]
    global subset_list
    subset_list= []
    get_subset_list(starting_bond_list)

    print(f'Subset retrieved! Here it is: + {subset_list}')

    for i in range(len(subset_list)):
        if len(subset_list[i]) == rule.get_ladder_length():
            if is_valid_ladder(subset_list[i], rule):
                if get_ladder_yield(subset_list[i]) > best_bond_yield:
                    best_bond_yield = get_ladder_yield(subset_list[i])
                    best_bond_list = subset_list[i]
                    print(f'\nBest Yield Updated to: {best_bond_yield} \n With these bonds: {get_ladder_cusips(subset_list[i])}+\n')
                else:
                    print(f'This bond ladder didn\'n have better yield: {get_ladder_cusips(subset_list[i])}' )
            else:
                print(f'This ladder is not valid: {get_ladder_cusips(subset_list[i])}')
        else:
            print(f'This subset is not a complete ladder: {get_ladder_cusips(subset_list[i])}')

    print(f'The best bond ladder is {get_ladder_cusips(best_bond_list)} \nAnd '
          f'has average yield: {best_bond_yield}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
