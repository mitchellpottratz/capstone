from django.urls import path
from . import views

urlpatterns = [
	
	# where company users can view all of their information
	path('index/', views.index, name='index'),


]






