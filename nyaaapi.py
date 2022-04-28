from fastapi.responses import RedirectResponse, FileResponse
import os
from utils.nyaa import *
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def home():
  return {
    'status': 'Nyaa Api Working Fine',
    'contributor': 'AuraMoon55',
    'routes': {
      '/': 'Home',
      '/nyaa?code=code': 'Get Info of nyaa.si torrent by its code'
    }
  }



@app.get("/nyaa")
async def get_nyaa(code: int = Query(None)):
  x = await get_torrent(code)
  return {
    "status": "success",
    "info": x
  }

