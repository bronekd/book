from django.urls import path
from .views import *


urlpatterns = [
    path('json/', my_json_view, name='json_view'),
    path('books/', books_json, name='books_json'),
    path('download/', my_file_view, name='download_file'),
    path('upload/', FileUploadView.as_view(), name='upload_file'),
]