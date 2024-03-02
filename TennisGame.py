import random


def coin_toss():
    # Perform a coin toss to determine who serves first
    print("Coin Toss to determine who serves first...")
    result = random.choice(["heads", "tails"])
    print(f"Coin toss result: {result}. {'Player' if result == 'heads' else 'CPU'} serves first.\n")
    return "player" if result == 'heads' else "cpu"


def play_point(server):
    # Randomly determine the winner of the point
    return server if random.random() < 0.5 else ("cpu" if server == "player" else "player")


def update_score(score, winner, loser):
    transitions = {"0": "15", "15": "30", "30": "40"}
    if score[winner] in transitions:
        score[winner] = transitions[score[winner]]
    elif score[winner] == "40":
        if score[loser] == "40":
            score[winner] = "Advantage"
        elif score[loser] == "Advantage":
            score[loser] = "40"
        else:
            return True  # Game won
    elif score[winner] == "Advantage":
        return True  # Game won
    return False  # Game continues


def print_scores(score, game_count, set_count, server):
    print("\n----------------------------------------")
    print(f"Server: {'Player' if server == 'player' else 'CPU'}")
    print(f"Set Count   - Player: {set_count['player']}, CPU: {set_count['cpu']}")
    print(f"Game Count  - Player: {game_count['player']}, CPU: {game_count['cpu']}")
    print(f"Point Score - Player: {score['player']}, CPU: {score['cpu']}")
    print("----------------------------------------\n")


def play_game(game_count, set_count, server):
    score = {'player': "0", 'cpu': "0"}
    game_winner = ""
    # Display initial scores before starting
    print_scores(score, game_count, set_count, server)

    while True:
        winner = play_point(server)
        loser = 'player' if winner == 'cpu' else 'cpu'
        if update_score(score, winner, loser):
            game_winner = winner
            game_count[winner] += 1
            break
        input("Press 'Enter' to play next point.")
        print_scores(score, game_count, set_count, server)

    # Update for next game
    server = loser if game_winner == server else winner

    # Check if a set is won
    if game_count[game_winner] >= 6:
        set_count[game_winner] += 1
        game_count['player'] = game_count['cpu'] = 0  # Reset game count for new set

    print_scores(score, game_count, set_count, server)
    print(
        f"Game won by {'Player' if game_winner == 'player' else 'CPU'}! Next server: {'Player' if server == 'player' else 'CPU'}\n")
    return server  # Return the server for the next game


def play_match():
    game_count = {'player': 0, 'cpu': 0}
    set_count = {'player': 0, 'cpu': 0}
    server = coin_toss()  # Determine who serves first

    while set_count['player'] < 2 and set_count['cpu'] < 2:
        server = play_game(game_count, set_count, server)  # Play a game and update the server

    match_winner = 'player' if set_count['player'] > set_count['cpu'] else 'cpu'
    print(f"\nMatch Conclusion ----------------------------------------")
    print(f"Match won by {'Player' if match_winner == 'player' else 'CPU'}!")
    print(f"Final Set Score - Player: {set_count['player']}, CPU: {set_count['cpu']}")
    print(f"Congratulations {'Player' if match_winner == 'player' else 'CPU'}!")
    print("---------------------------------------------------------")


if __name__ == "__main__":
    print("Welcome to the virtual tennis match!\n")
    play_match()
