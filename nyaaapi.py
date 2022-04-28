from fastapi.responses import RedirectResponse, FileResponse
import os
from utils.nyaa import *
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def home():
  home = {
    'status': 'Nyaa Api Working Fine',
    'contributor': 'AuraMoon55',
    'routes': {
      '/': 'Home',
      '/nyaa?code=code': 'Get Info of nyaa.si torrent by its code'
    }
  }
  return home



@app.get("/nyaa")
async def get_nyaa(code: int = Query(None)):
  x = await get_torrent(code)
  code = {
    "status": "success",
    "info": x
  }
  return code

