from fastapi import FastAPI, HTTPException

from app.config import settings
from app.routers import battlesnake
from app.utils.logger import logger

# ====== FASTAPI APP CONFIGURATION ======
app = FastAPI(
    title=settings.app_name,
)

FILENAME = "app/_main.py"

app.include_router(battlesnake.router)


# ====== HEALTH CHECK ROUTE ======
@app.get("/health")
def health_check():
    logger.info(f"{FILENAME}: Health check")
    return {"status": "ok"}


# ===== GLOBAL EXCEPTION HANDLER =====
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    logger.error(f"{FILENAME}: {exc.detail}")
    return {"detail": exc.detail, "status_code": exc.status_code}
