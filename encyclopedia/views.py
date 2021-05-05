from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2 
import random


class NewTaskForm(forms.Form): #Advanced feature para crear formularios con django
	q = forms.CharField(label="New search")
	
class NewTaskForm2(forms.Form):
	title = forms.CharField(label="title")
	content = forms.CharField(label="content")
	
	
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request,title):
	if util.get_entry(title):
		return render(request, "encyclopedia/content.html",{"content":markdown2.markdown(util.get_entry(title)),"title":title})
	else:
		return render(request, "encyclopedia/error.html",{"title":title,"error":" entry does not exist"})
	

		
def search(request):
	if request.method == "POST":
		form = NewTaskForm(request.POST) 
		
	if form.is_valid():
			title = form.cleaned_data["q"]	
			pages= util.list_entries()
	if title in pages:
			return render(request, "encyclopedia/content.html",{"content":markdown2.markdown(util.get_entry(title)),"title":title})
	else:
		matching = [s for s in pages if title in s]
	
	if matching:
			return render(request, "encyclopedia/search.html",{"matching":matching})
	else:
		return render(request, "encyclopedia/error.html",{"title":title, "error":" entry does not exist"})
		
		
def newpage(request):
	return render(request, "encyclopedia/newpage.html")
		
def savepage(request):
	if request.method == "POST":
		form = NewTaskForm2(request.POST) 
		
	if form.is_valid():
		title = form.cleaned_data["title"]
		content = form.cleaned_data["content"] 
		pages= util.list_entries()
		
	if title in pages:
			return render(request, "encyclopedia/error.html",{"title":title, "error":" entry already exists"})
	else:
		util.save_entry(title,content)
		title = form.cleaned_data["title"]
		content = form.cleaned_data["content"] 
		return render(request, "encyclopedia/content.html",{"content":markdown2.markdown(util.get_entry(title)),"title":title})

def  editpage(request,title):
		return render(request, "encyclopedia/editpage.html",{"content":util.get_entry(title),"title":title})
		
def savechange(request):
	if request.method == "POST":
		form = NewTaskForm2(request.POST)
		
	if form.is_valid():
		title = form.cleaned_data["title"]
		content = form.cleaned_data["content"] 
		util.save_entry(title,content)
		return render(request, "encyclopedia/content.html",{"content":util.get_entry(title),"title":title})
		
	else:
		error = 'Error in form data'
		return render(request, "encyclopedia/error.html",{"error":"Error in form data."})
		
def randompage(request):
		
		pages = util.list_entries()
		r=random.randrange(1,len(pages))
		title=pages[r]
		return render(request, "encyclopedia/content.html",{"content":markdown2.markdown(util.get_entry(title)),"title":title})
		