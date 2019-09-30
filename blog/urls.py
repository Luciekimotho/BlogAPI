from django.urls import path
from .views import ListUserView, ListGroupView

urlpatterns = [
    path('users/', ListUserView.as_view(), name="users-all"),
    path('groups/', ListGroupView.as_view(), name="users-all")
]