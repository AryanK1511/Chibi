from fastapi import APIRouter, Request

from app.handlers import end, info, move, start

router = APIRouter()


@router.get("/")
def on_info():
    return info.info_handler()


@router.post("/start")
async def on_start(request: Request):
    game_state = await request.json()
    return start.start_handler(game_state)


@router.post("/move")
async def on_move(request: Request):
    game_state = await request.json()
    return move.move_handler(game_state)


@router.post("/end")
async def on_end(request: Request):
    game_state = await request.json()
    return end.end_handler(game_state)
