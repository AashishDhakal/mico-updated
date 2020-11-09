from django.urls import path, include
from django.conf.urls import include, url
from . import views

urlpatterns = [
        path('', views.homepage, name = 'home'),
        path('about/', views.aboutpage, name = 'about'),
        path('causes/', views.causesview, name = 'causes'),
        path('directors/', views.directorview, name = 'directors'),
        path('sponsorships/', views.sponsorship, name = 'sponsorship'),
        path('contact/', views.contact, name = 'contact'),
        path('getinvolved/', views.get_involved, name = 'getinvolved'),
        path('history/', views.historyview, name = 'history'),
        path('messages/', views.message, name = 'messages'),
        path('newsroom/', views.newsroom, name = 'newsroom'),
        path('ourmission/', views.missionview, name = 'ourmission'),
        path('resources/', views.resources, name = 'resources'),
        path('staffs/', views.staffs, name = 'staffs'),
        path('trustees/', views.trustees, name = 'trustees'),
        path('workwithus/', views.workwithus, name = 'workwithus'),
        path('events/', views.event_view, name='event'),
        path('endowment/', views.endowment, name='endowment'),
        path('newsroom/<slug>/', views.news_detail, name='newsdetail'),
        path('events/<slug>/', views.event_detail, name='eventdetail'),
        path('works/<slug>/', views.work_detail, name='workdetail'),
        path('projects/<slug>/', views.project_detail, name='projectdetail'),
        path('message/<slug>/', views.message_detail, name='messagedetail'),
        path('update-content/', views.update_content, name='updatecontent'),
        url(r"^terms/(?P<slug>[\w-]+)$", views.terms_policy, name="terms"),
]
