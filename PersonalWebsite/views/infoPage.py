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
    heading = "Welcome."
  elif page=="projects":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/currentProjects.json") as f:
      content["projectLists"].append( json.load(f) )
    with open(STATIC_DIR+"/json/pastProjects.json") as f:
      content["projectLists"].append( json.load(f) )

  elif page=="more":
    template = "more.html"
    heading = "More about me."

  elif page=="hackathons":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/hackathons.json") as f:
      content["projectLists"].append( json.load(f) )

  elif page=="websites":
    template = "projects.html"
    heading = ""
    with open(STATIC_DIR+"/json/websites.json") as f:
      content["projectLists"].append( json.load(f) )

  else:
    raise Http404

  return render(request, "infoPage.html", {
    "template":template,
    "heading":heading,
    "content":content
  })

