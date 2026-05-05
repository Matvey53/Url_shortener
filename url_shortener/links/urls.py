from django.urls import path

from links import views

app_name = 'links'

urlpatterns = [
    path('success/<str:short_code>/', views.SuccessPageView.as_view(), name='success_page'),
    path(
        'stats/<str:short_code>/', 
        views.StatsPageView.as_view(), 
        name='stats_page'
    ),
    path('<str:short_code>/', views.RedirectView.as_view(), name='redirect'),
    path('', views.MainPageView.as_view(), name='main_page'),
]
