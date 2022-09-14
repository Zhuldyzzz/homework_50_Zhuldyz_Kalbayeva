from django.contrib import admin
from django.urls import path
from play_cat.views.base import index_view
from play_cat.views.cat_info import action_view

urlpatterns = [
    path('', index_view),
    path('action_page/', action_view)
]
    

