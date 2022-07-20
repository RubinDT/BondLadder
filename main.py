from Bond import Bond
from Rule import Rule
from Ladder import Ladder


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


if __name__ == '__main__':

    best_bond_list = []
    rule = Rule(5, 1, 4) #ladder_length, bonds_per_sector, min_rating
    best_bond_yield = -100 #TODO improve this starting logic

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
        temp_ladder = Ladder(subset_list[i])
        if len(subset_list[i]) == rule.get_ladder_length():
            if temp_ladder.is_valid_ladder(rule):
                if temp_ladder.get_ladder_yield() > best_bond_yield:
                    best_bond_yield = temp_ladder.get_ladder_yield()
                    best_bond_list = temp_ladder
                    print(f'\nBest Yield Updated to: {best_bond_yield} \n With these CUSIPs: {temp_ladder.get_ladder_cusips()}+\n')
                else:
                    print(f'This bond ladder was valid but didn\'n have better yield. Ladder CUSIPs: {temp_ladder.get_ladder_cusips()}' )
        else:
            print(f'This subset is not a complete ladder. Subset CUSIPs {temp_ladder.get_ladder_cusips()}')

    print(f'The best bond ladder is {best_bond_list.get_ladder_cusips()} \nAnd '
          f'has average yield: {best_bond_yield}')