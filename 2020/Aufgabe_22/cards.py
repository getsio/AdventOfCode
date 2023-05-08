import copy

f = open("C:/Ausbildung/Python/AdventOfCode/2020/Aufgabe_22/input_data2.txt", "r")

player_one = []
player_two = []

def get_result(deck, length):
    result = 0

    for i in range(length):
        result += deck[i] * (length - i)

    return result

def crab_combat(p_1, p_2):
    while len(p_1) > 0 and len(p_2) > 0:
        player_one_card = p_1[0]
        player_two_card = p_2[0]

        p_1.remove(player_one_card)
        p_2.remove(player_two_card)

        if player_one_card > player_two_card:
            p_1.append(player_one_card)
            p_1.append(player_two_card)
        else:
            p_2.append(player_two_card)
            p_2.append(player_one_card)

    deck_length = len(player_one) + len(player_two)

    if len(player_one) == deck_length:
        res = get_result(player_one, deck_length)
    else:
        res = get_result(player_two, deck_length)
    
    return res   

def play_recursive_combat(p_1, p_2):
    game_nr = 1
    while len(p_1) > 0 and len(p_2) > 0:
        print(f"Game Nr.: {game_nr}")
        recursive_combat(p_1, p_2)
        print(p_1, p_2)
        game_nr += 1

    deck_length = len(player_one) + len(player_two)

    if len(player_one) == deck_length:
        res = get_result(player_one, deck_length)
    else:
        res = get_result(player_two, deck_length)
    
    return res   
    

def recursive_combat(p_1, p_2, p_1_before = [], p_2_before = [], round_nr = 1):
    #print(f"-- Round {round_nr} (Game {game_nr}) --")
    if p_1 in p_1_before or p_2 in p_2_before:
        p1_card = p_1[0]
        p2_card = p_2[0]

        p_1.remove(p1_card)
        p_2.remove(p2_card)

        p_1.append(p1_card)
        p_1.append(p2_card)
        return p_1

    p_1_before.append(copy.deepcopy(p_1))
    p_2_before.append(copy.deepcopy(p_2))

    player_one_card = p_1[0]
    player_two_card = p_2[0]
    
    if player_one_card <= len(p_1) and player_two_card <= len(p_2):
        p_1 = copy.deepcopy(recursive_combat(copy.deepcopy(p_1[:player_one_card]), copy.deepcopy(p_2[:player_two_card]), p_1_before, p_2_before))

    else:
        p_1.remove(player_one_card)
        p_2.remove(player_two_card)

        if player_one_card > player_two_card:
            p_1.append(player_one_card)
            p_1.append(player_two_card)
        else:
            p_2.append(player_two_card)
            p_2.append(player_one_card)


for line in f:
    line = line.rstrip()
    if not line.isnumeric():
        inp_str = line.rstrip()
    else:
        if "1" in inp_str:
            player_one.append(int(line))
        else:
            player_two.append(int(line))


#print(player_one, player_two)
#print(crab_combat(player_one, player_two))
print(play_recursive_combat(player_one, player_two))
print(player_one, player_two)
