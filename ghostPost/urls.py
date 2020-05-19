from django.urls import path
from ghostPost import views

urlpatterns = [
path('', views.index, name='homepage'),
path('sort/<int:id>/', views.sort, name='sort'),
path('add', views.addRB),
path('roasts', views.roast),
path('boasts', views.boast),
path('posts/<int:id>/', views.posts),
path('top', views.top),
path('upvotes/<int:id>/', views.upvote),
path('downvotes/<int:id>/', views.downvote)
]