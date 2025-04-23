from django.urls import path
from.import views

# Url Patterns

urlpatterns = [
    path('',views.home,name='homepage'),
    path('/about',views.about, name='aboutpage'),
    path('/projects',views.projects,name='projectspage'),
    path('/contacts',views.contact,name='contactpage'),
]