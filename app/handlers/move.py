import random
from typing import Dict

from app.constants import possible_moves
from app.core.functions import avoid_own_body, avoid_reverse_movement, avoid_walls
from app.utils.logger import logger


def move_handler(game_state: Dict) -> Dict:
    curr_possible_moves = possible_moves.copy()

    avoid_reverse_movement(game_state, curr_possible_moves)
    avoid_walls(game_state, curr_possible_moves)
    avoid_own_body(game_state, curr_possible_moves)

    print(curr_possible_moves)
    next_move = (
        random.choice(list(curr_possible_moves)) if curr_possible_moves else "down"
    )
    logger.info(f"Next Move: {next_move}")

    return {"move": next_move}
