import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from modules import auth_router, Base
from core.bd import db
from core import templates
from config import BASE_DIR


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
app = FastAPI(lifespan=lifespan,
              title='Chess',
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return templates.get_template("landing.html").render()



if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)