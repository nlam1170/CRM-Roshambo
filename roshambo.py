import random

ROCK = 0
PAPER = 1
SCISSORS = 2

def add_arrays(arr1, arr2):
    answer = []
    for i in range(3):
        answer.append(arr1[i] + arr2[i])
    return answer

def is_winning_move(our_choice, opp_choice):
    #IN CASE BOTH CHOICES ARE THE SAME
    if our_choice == opp_choice:
        return False

    #IF WE CHOOSE ROCK
    if our_choice == ROCK:
        if opp_choice == SCISSORS:
            return True
        else: return False

    #IF WE CHOOSE PAPER
    if our_choice == PAPER:
        if opp_choice == ROCK:
            return True
        else: return False

    #IF WE CHOOSE SCISSORS
    if our_choice == SCISSORS:
        if opp_choice == PAPER:
            return True
        else: return False

def get_reg_from_move(our_choice, opp_choice):
    if our_choice == opp_choice:
        return 0
    if not is_winning_move(our_choice, opp_choice):
        return 1
    if is_winning_move(our_choice, opp_choice):
        return 2

def get_regret_arr(our_choice, opp_choice):
    rock_index = get_reg_from_move(our_choice, opp_choice)
    paper_index = get_reg_from_move(our_choice, opp_choice)
    scissors_index = get_reg_from_move(our_choice, opp_choice)

    return [rock_index, paper_index, scissors_index]

def make_choice(dist_arr, total_rounds):
    possible = [ROCK, PAPER, SCISSORS]
    if total_rounds == 0:
        choice = random.choice(possible)
        return choice

    denom = total_rounds * 2
    rock_dist = dist_arr[0] / denom
    paper_dist = dist_arr[1] / denom
    scissor_dist = dist_arr[2] / denom

    choice = random.choices(possible, weights=[rock_dist*100, paper_dist*100, scissor_dist*100], k=1)
    return choice[0]

def player_vs_program():
    total_rounds = 0
    player_score = 0
    program_score = 0
    cur_program_arr = [0, 0, 0]

    while True:
        player_choice = int(input("Enter your move choice\n0: Rock\n1: Paper\n2: Scissors\n3: Exit\n"))
        if player_choice == 3: 
            print("You have successfully exited")
            break

        program_choice = make_choice(cur_program_arr, total_rounds)
        regret_arr = get_regret_arr(program_choice, player_choice)
        cur_program_arr = add_arrays(cur_program_arr, regret_arr)

        if is_winning_move(player_choice, program_choice):
            player_score += 1
            print("Congrats you won this round!")
            print(f"Your score: {player_score}, Program score: {program_score}")

        if not is_winning_move(player_choice, program_choice):
            program_score += 1
            print("Sorry you lost this round!")
            print(f"Your score: {player_score}, Program score: {program_score}")

        total_rounds += 1


def program_vs_program():
    player1_score = 0
    player2_score = 0
    cur_player1_arr = [0, 0, 0]
    cur_player2_arr = [0, 0, 0]
    total_rounds = 0
    NUM_ITERATIONS = 10000

    for _ in range(NUM_ITERATIONS):
        player1_choice = make_choice(cur_player1_arr, total_rounds)
        player2_choice = make_choice(cur_player2_arr, total_rounds)
        print("player1 choice", player1_choice, "player2 choice", player2_choice)
        
        player1_reg = get_regret_arr(player1_choice, player2_choice)
        player2_reg = get_regret_arr(player2_choice, player1_choice)

        cur_player1_arr = add_arrays(cur_player1_arr, player1_reg)
        cur_player2_arr = add_arrays(cur_player2_arr, player2_reg)

        if is_winning_move(player1_choice, player2_choice):
            player1_score += 1
        if is_winning_move(player2_choice, player1_choice):
            player2_score +=1

        total_rounds += 1

    print("SIMULATION OVER")
    print(f"Player1 won {player1_score/total_rounds*100}% of the time")
    print(f"Player2 won {player2_score/total_rounds*100}% of the time")
    print(f"A tie occured {100 - (player1_score/total_rounds*100) - (player2_score/total_rounds*100)}% of the time")





#player_vs_program()
#program_vs_program()
