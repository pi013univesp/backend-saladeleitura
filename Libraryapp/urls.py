from django.urls import path
from .Views.LibraryView import LoginView, RegisterView

app_name = "Libraryapp"

urlpatterns = [
    path('library/register', RegisterView.as_view(), name='Library-register'),
    path('library/login', LoginView.as_view(), name='Library-login')
]