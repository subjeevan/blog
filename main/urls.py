from django.urls import path
from .views import home, category, snews
urlpatterns = [
     path('main/',home,name="home"),
     path('category/',category,name='category'),
     path('snews/',snews,name='snews'),
]
