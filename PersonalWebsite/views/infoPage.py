from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse

# Function for serving files where only inner content changes.
def load(request, page):
  content = {}

  if page=="home":
    template = "home.html"
    heading = "Welcome."
  elif page=="projects":
    template = "projects.html"
    heading = ""
    content["projectLists"] =  [
      {
       "title":"Current Projects",
       "projects":
      [
        {
          "name":"Dark Reaction Project",
          "url": "http://darkreactions.haverford.edu",
          "description":"A Django/MySQL/NGinx-powered recommendation system for chemical reactions.",
          "source": "",
        },
        {
          "name":"URL Cartographer",
          "url": "http://cartographer.caseyfalk.com",
          "description":"A Django project that maps websites based on link connections.",
          "source": "https://github.com/cfalk/URL_Cartographer",
        },
        {
          "name":"InfluNote",
          "url": "http://influnote.caseyfalk.com",
          "description":"A Django project to explore intermusical influence over time.",
          "source": "https://github.com/cfalk/InfluNote",
        },
      ]
    },
    {
       "title":"Past Projects",
       "projects":
      [
        {
          "name":"HaverHub",
          "url": "http://hub.fig.haverford.edu",
          "description":"A Django/MySQL/NGinx webapp developed by FIG to improve student life at Haverford.",
          "source": "https://github.com/cfalk/HaverApp",
        },
        {
          "name":"OrgoBuddy",
          "url": "http://flashcards.caseyfalk.com",
          "description":"A jQuery-powered webapp designed to help Haverford students study for Organic Chemistry.",
          "source": "https://github.com/cfalk/jQueryFlashcardEngine",
        },
        {
          "name":"Websites",
          "url": reverse("websites"),
          "description":"",
          "source": "",
        },
        {
          "name":"Hackathons",
          "url": reverse("hackathons"),
          "description":"",
          "source": "",
        },
      ]
    }
    ]

  elif page=="more":
    template = "more.html"
    heading = "More about me."
  elif page=="hackathons":
    template = "projects.html"
    heading = ""
    content["projectLists"] =  [
      {
       "title":"Hackathons",
       "projects":  [
        {
          "name":"Learning Graph",
          "url": "http://learninggraph.haverford.edu/",
          "description":"TRI-CO Hackathon 2014: User-powered knowledge graph of skills and related careers.",
          "source": "https://github.com/cfalk/LearningGraph",
        },
        {
          "name":"I Said What?",
          "url": "http://isaidwhat.com",
          "description":"PennApps Spring 2014: Facebook game that uses natural language processing to turn a user's posts against them.",
          "source": "https://github.com/PennApps2014Spring/ISaidWhat",
        },
        {
          "name":"Milford Housing Project",
          "url": "",
          "description":"Code for Good (Delaware 2013) - JP Morgan Chase: Digitalized database for the Milford Housing Development Corporation.",
          "source": "https://github.com/cfalk/Code4Good_2013",
        },
        ]
      }
      ]
  elif page=="websites":
    template = "projects.html"
    heading = ""
    content["projectLists"] =  [
      {
       "title":"Websites",
       "projects":
      [
        {
          "name":"TRI-CO Hackathon 2014",
          "url": "http://hackathon.haverford.edu/",
          "description":"The official website for Haverford's Tri-Co 2014 Hackathon.",
          "source": "",
        },
        {
          "name":"FIG",
          "url": "http://fig.haverford.edu",
          "description":"A website about FIG, a student computing group at Haverford.",
          "source": "",
        },
        {
          "name":"RadioFords",
          "url": "http://radiofords.com",
          "description":"The main channel for tuning into Haverford's Radio (WHRC).",
          "source": "",
        },
        {
          "name":"Nerd House",
          "url": "http://hcnerdhouse.co.nr",
          "description":"A website for displaying information to the community.",
          "source": "",
        },
        {
          "name":"Haverford Robotics Team",
          "url": "http://herolab.co.vu",
          "description":"A website for displaying projects and member information.",
          "source": "",
        },
      ]
      }
    ]

  else:
    raise Http404

  return render(request, "infoPage.html", {
    "template":template,
    "heading":heading,
    "content":content
  })

