from django.urls import path

from apps.base.views import IndexView

app_name = "base"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
