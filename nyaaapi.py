from fastapi.responses import RedirectResponse as redirect, FileResponse
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

@app.get("/repo")
async def repo():
  return redirect("https://github.com/AuraMoon55/Nyaa-Api/")


@app.get("/nyaa")
async def get_nyaa(code: int = Query(None)):
  x = await get_torrent(code)
  if x["message"]:
    return x
  else:
    x["status"] = "success"
    code = x
    return code

