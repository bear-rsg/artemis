from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('<pk>/', views.BlogDetailView.as_view(), name='detail'),
]
