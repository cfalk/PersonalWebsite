from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse
from PersonalWebsite.settings import STATIC_DIR

import json

def gallery(request, page):
  images = []

  if page=="food":
    with open(STATIC_DIR+"/json/food.json") as f:
      images = json.load(f)

  elif page=="nature":
    with open(STATIC_DIR+"/json/nature.json") as f:
      images = json.load(f)

  else:
    raise Http404

  return render(request, "infoPage.html", {
    "template":"gallery.html",
    "content":{"images":images,
      "more": {
        "url":"http://cfalk.imgur.com/all/",
        "name":"Imgur"
      }

    }
  })

