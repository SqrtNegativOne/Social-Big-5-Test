from django.urls import path
from . import views

urlpatterns = [
    path("take-test/<str:user_id>", views.take_test, name="take-test"),
    path("view-results/<str:user_id>", views.view_results, name="view-results")
]