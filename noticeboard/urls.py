from django.urls import path
from . import views

app_name = 'noticeboard'
urlpatterns = [
    path('', views.ActiveNoticesView.as_view(), name='active-notices'),
    path('expired/', views.ExpiredNoticeView.as_view(), name='expired-notices'),
    path('<int:pk>/', views.SingleNoticeView.as_view(), name='single-notice'),
]
