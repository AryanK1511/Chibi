from typing import Dict

from app.utils.logger import logger


def end_handler(game_state: Dict) -> str:
    logger.info("GAME OVER")
    return "ok"
