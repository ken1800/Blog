from django.contrib import admin
from django.urls import path
from . import views
from .views import UserProfileViewSet,UserProfileFeedViewSet,UserLoginApiView,NoteDetail,NoteList
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('profile',UserProfileViewSet)
router.register('feed',UserProfileFeedViewSet)
# router.register('feed',UserProfileFeedViewSet)



urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('api/', include(router.urls)),
    path('login/',UserLoginApiView.as_view()),
    path('react',NoteList.as_view()),
    path('react/<int:pk>/',NoteDetail.as_view()),
    
]






