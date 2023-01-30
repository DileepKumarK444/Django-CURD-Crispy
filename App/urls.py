from django.urls import path
from . import views
urlpatterns = [
    path("", views.Read.as_view(),name="read"),
    path("create/", views.Create.as_view(),name="create"),
    path("update/<int:pk>", views.Update.as_view(),name="update"),
    path("delete/<int:pk>", views.Delete.as_view(),name="delete"),
]
