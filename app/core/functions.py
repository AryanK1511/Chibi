from typing import List, Set


def avoid_reverse_movement(game_state: List, possible_moves: Set):
    my_snake_head = game_state["you"]["body"][0]
    my_snake_neck = game_state["you"]["body"][1]

    if my_snake_neck["x"] < my_snake_head["x"]:
        possible_moves.discard("left")

    elif my_snake_neck["x"] > my_snake_head["x"]:
        possible_moves.discard("right")

    elif my_snake_neck["y"] < my_snake_head["y"]:
        possible_moves.discard("down")

    elif my_snake_neck["y"] > my_snake_head["y"]:
        possible_moves.discard("up")


def avoid_walls(game_state: List, possible_moves: Set):
    my_snake_head = game_state["you"]["body"][0]
    board_height, board_width = (
        game_state["board"]["height"],
        game_state["board"]["width"],
    )

    if my_snake_head["x"] == 0:
        possible_moves.discard("left")

    if my_snake_head["x"] == board_width - 1:
        possible_moves.discard("right")

    if my_snake_head["y"] == 0:
        possible_moves.discard("down")

    if my_snake_head["y"] == board_height - 1:
        possible_moves.discard("up")


def avoid_own_body(game_state: List, possible_moves: Set):
    my_snake_body = game_state["you"]["body"]
    my_snake_head = my_snake_body[0]

    if {"x": my_snake_head["x"] + 1, "y": my_snake_head["y"]} in my_snake_body:
        possible_moves.discard("right")

    if {"x": my_snake_head["x"] - 1, "y": my_snake_head["y"]} in my_snake_body:
        possible_moves.discard("left")

    if {"x": my_snake_head["x"], "y": my_snake_head["y"] + 1} in my_snake_body:
        possible_moves.discard("up")

    if {"x": my_snake_head["x"], "y": my_snake_head["y"] - 1} in my_snake_body:
        possible_moves.discard("down")
