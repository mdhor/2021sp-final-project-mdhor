from django.urls import path

from .views import iphone_line, iphone_scatter

urlpatterns = [
    path("line_chart", iphone_line, name="test_chart"),
    path("scatter_plot", iphone_scatter, name="test_chart"),
]
