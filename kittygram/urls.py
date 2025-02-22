from django.urls import path

from cats.views import APICat

urlpatterns = [
    path('cats/', APICat.as_view()),
]

# from cats.views import cat_list

'''
urlpatterns = [
   path('cats/', cat_list),
]
'''