from django.contrib import admin
from django.urls import path, include
from main import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/data/', views.index),
    path('api/v1/movies/', views.MovieListCreateAPIview.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailUdateDeleteAPIview.as_view()),
    path('api/v1/login/', user_views.LoginAPIview.as_view()),
    path('api/v1/register/', user_views.RegisterAPIview.as_view()),
    path('api/v1/genres/', views.GenreListCreateAPIView.as_view()),
    path('api/v1/genres/<int:pk>/', views.GenreDetailUpdateDeleteAPIview.as_view()),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
