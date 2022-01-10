from django.urls import path
from . import views
from .views import PostListView,PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('about/',views.about, name='about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('privacy/',views.privacy_policy,name='privacy'),
    path('post_ad/',views.post_ad,name='post_ad'),
    path('search_venues',views.search_venues,name='search_venues')
]