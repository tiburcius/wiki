from django.urls import path

from . import views
app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
	path("wiki/search",views.search, name="search"),
	path("wiki/newpage",views.newpage, name="newpage"),
	path("wiki/savepage",views.savepage, name="savepage"),
	path("wiki/editpage/<str:title>",views.editpage, name="editpage"),
	path("wiki/savechange",views.savechange, name="savechange"),
	path("wiki/randompage",views.randompage, name="randompage"),
	path("wiki/<str:title>", views.entries, name="entries")
]
