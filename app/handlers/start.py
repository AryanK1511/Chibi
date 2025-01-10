from typing import Dict

from app.utils.logger import logger


def start_handler(game_state: Dict) -> str:
    logger.info("GAME START")
    return "ok"
