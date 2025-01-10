import random
from typing import Dict

from app.utils.logger import logger


def move_handler(game_state: Dict) -> Dict:
    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    my_head = game_state["you"]["body"][0]
    my_neck = game_state["you"]["body"][1]

    if my_neck["x"] < my_head["x"]:
        is_move_safe["left"] = False

    elif my_neck["x"] > my_head["x"]:
        is_move_safe["right"] = False

    elif my_neck["y"] < my_head["y"]:
        is_move_safe["down"] = False

    elif my_neck["y"] > my_head["y"]:
        is_move_safe["up"] = False

    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        logger.info(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    next_move = random.choice(safe_moves)

    logger.info(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}
