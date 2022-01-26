from django.contrib import admin
from django.urls import path
from main import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/data/', views.index),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_view),
    path('api/v1/login/', views.LoginAPIview.as_view()),
    path('api/v1/register/', views.RegisterAPIview.as_view()),
    path('api/v1/genres/', views.GenreListCreateAPIView.as_view()),
    path('api/v1/genres/<int:pk>/', views.GenreDetailUpdateDeleteAPIview.as_view()),

]
