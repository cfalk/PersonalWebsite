from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse
from PersonalWebsite.settings import STATIC_DIR

import json

# Function for serving files where only inner content changes.
def load(request, page):
  content = {"projectLists":[]}

  if page=="home":
    template = "home.html"
    heading = "Welcome"
  elif page=="projects":
    template = "projects.html"
    heading = "Projects"

    with open(STATIC_DIR+"/json/currentProjects.json") as f:
      content["projectLists"].append( json.load(f) )
    with open(STATIC_DIR+"/json/pastProjects.json") as f:
      content["projectLists"].append( json.load(f) )

  elif page=="more":
    template = "more.html"
    heading = "More about me"

  elif page=="hackathons":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/hackathons.json") as f:
      content["projectLists"].append( json.load(f) )
      content["more"] = {
        "url":"https://github.com/cfalk/",
        "name":"GitHub"
      }

  elif page=="vimTip":
    template = "vimTip.html"
    heading = "Random Vim Tip"
    content = getVimTip()

  elif page=="websites":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/websites.json") as f:
      content["projectLists"].append( json.load(f) )
      content["more"] = {
        "url":"https://github.com/cfalk/",
        "name":"GitHub"
      }

  elif page=="photos":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/photoGalleries.json") as f:
      content["projectLists"].append( json.load(f) )
      content["more"] = {
        "url":"http://cfalk.imgur.com/all/",
        "name":"Imgur"
      }

  else:
    raise Http404

  return render(request, "infoPage.html", {
    "template":template,
    "heading":heading,
    "content":content,
  })



import requests, random, re
def getVimTip():
  url = "http://zzapper.co.uk/vimtips.html"
  response = requests.get(url)

  rawTips = re.findall(r"<pre>(.*)(?!<a href)", response.text, re.DOTALL)[0]
  tips = rawTips.split("\n")

  cleanedTips = []
  for tip in tips:
    cleanTip = tip.replace("-","").replace(" ","")

    if cleanTip!="" and cleanTip[0]!="\"" and cleanTip[0]!="#":
      cleanedTips.append(tip)

  tip = random.choice(cleanedTips)

  tipParts = tip.split(" : ")
  rawTip = tipParts[0]
  tipComment = "".join(tipParts[1:])

  formattedTip = "<div class='token-comment'>{}</div>".format(tipComment)
  formattedTip += "<div class='token-string'>{}</div>".format(rawTip)

  return formattedTip







