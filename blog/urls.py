from django.urls import path
from blog import views as blog_views


urlpatterns = [
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('<int:blog_id>/view', blog_views.detail, name='detail'),
    path('<int:blog_id>/update', blog_views.update, name='update'),
    path('inactive/', blog_views.inactive, name='inactive'),
    path('<int:blog_id>/delete', blog_views.delete, name='delete'),
]