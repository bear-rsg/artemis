from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [

    # Search
    path('search/', views.SearchComingSoonTemplateView.as_view(), name='search-comingsoon'),

    # Export Data
    path('export/csv/', views.export_csv, name='export-csv'),

]
