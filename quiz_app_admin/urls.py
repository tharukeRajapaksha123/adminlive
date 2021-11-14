from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_admin.urls')),
]
admin.site.index_title = "Quiz App"
admin.site.site_header = "Quiz App"
admin.site.site_title = "Quiz App"