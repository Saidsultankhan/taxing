from django.urls import path, include
from users.views import Register
from users.views import UserDetailView, UserUpdateView, UsersListView


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('detail_user/<int:pk>/', UserDetailView.as_view(), name='detail_user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('userlist', UsersListView.as_view(), name='userlist')
]
