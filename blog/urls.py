from django.urls import path
from .views import ListUserView, ListGroupView
from . import views

urlpatterns = [
    path('users/', ListUserView.as_view(), name="users-all"),
    path('groups/', ListGroupView.as_view(), name="users-all"),
    path('', views.BlogList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view())
]