import cloudscraper
from bs4 import BeautifulSoup as bs


async def get_torrent(code):
  try:
    r = cloudscraper.create_scraper()
    x = r.get(f"https://nyaa.si/view/{code}")
    s = bs(x.content, "html.parser")
    title = s.find_all("h3", attrs={"class":"panel-title"})[0]
    link = s.find_all("a", attrs={"class": "card-footer-item"})[0].get("href")
    d1 = s.find_all("div", attrs={"class":"col-md-1"})
    d2 = s.find_all("div", attrs={"class":"col-md-5"})
    title = str(title.string)
    title = title[4:]
    inf = []
    for t in d1:
      num = d1.index(t)
      t = t.string
      t = t[:-1]
      y = d2[num]
      if y.span:
        y = y.span.string
      elif y.a:
        y = y.a.string
      else:
        y = y.string
      sq = [t, y]
      inf.append(sq)
      try:
        if "Information" in t:
          inf.remove([t, y])
        else:
          pass
      except:
        pass
    graph = {}
    graph['status'] = "success"
    for a in inf:
      graph[f'{a[0]}'] = a[1]
    graph['magnet'] = link 
    return graph
  except Exception:
    return {
             "status": "fail",
             "message": Exception
      }
