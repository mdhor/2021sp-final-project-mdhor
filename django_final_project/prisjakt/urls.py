from django.urls import path

from . import views

urlpatterns = [
    path(
        "chart/filter-options/", views.get_filter_options, name="chart-filter-options"
    ),
]
