from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [

    # Downloads template
    path('downloads/', views.DownloadsHomeTemplateView.as_view(), name='downloads-home'),

    # Download database templates as Excel spreadsheet
    path('downloads/db-template-excel/', views.downloads_excel_templates, name='downloads-dbtemplateexcel'),

    # Download data as CSV
    path('download/model-data-csv/', views.download_model_data_csv, name='downloads-modeldatacsv'),

]
