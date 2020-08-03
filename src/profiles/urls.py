from django.urls import path

from .views import ProfileApiView, ProfileDetail, ProfileUpdate

app_name = "profiles"
urlpatterns = [
    path("", ProfileDetail.as_view(), name="detail"),
    path("edit/", ProfileUpdate.as_view(), name="update"),
    path("api/", ProfileApiView.as_view(), name="api"),
]
