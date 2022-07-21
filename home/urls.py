from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Bookkeeping Admin"
admin.site.site_title = "Bookkeeping Admin Portal"
admin.site.index_title = "Welcome to Bookkeeping"

urlpatterns = [ 
   path('', views.home, name='home'),
   path('contact', views.contact, name='contact'),
   path('search', views.search, name='search'),
   path('signup', views.handleSignup, name='handleSignup'),
   path('login', views.handleLogin, name='handleLogin'),
   path('logout', views.handleLogout, name='handleLogout'),
   path('pricing/', views.pricing, name='pricing')
]