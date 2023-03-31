from django.urls import path
from .Views import LibraryView
from .Views import ClientView
from .Views import LiteraryGenreView

app_name = "Libraryapp"

urlpatterns = [
    path('library/register', LibraryView.RegisterView.as_view(), name='Library-register'),
    path('library/login', LibraryView.LoginView.as_view(), name='Library-login'),
    path('library/delete/<int:pk>', LibraryView.DeleteView.as_view(), name='Library-delete'),
    path('library/update/<int:pk>', LibraryView.UpdateView.as_view(), name='Library-update'),
    
    path('client/', ClientView.GetAllView.as_view(), name='Client-get-all'),
    path('client/<int:pk>', ClientView.GetClientByIdView.as_view(), name='Client-get-id'),
    path('client/delete/<int:pk>', ClientView.DeleteView.as_view(), name='Client-delete'),
    path('client/register/', ClientView.RegisterView.as_view(), name='Client-register'),
    path('client/update/<int:pk>', ClientView.UpdateView.as_view(), name='Client-update'),

    path('literary-genre/', LiteraryGenreView.GetAllView.as_view(), name='literary-genre-get-all'),
    path('literary-genre/<int:pk>', LiteraryGenreView.GetLiteraryGenreByIdView.as_view(), name='literary-genre-get-id'),
    path('literary-genre/delete/<int:pk>', LiteraryGenreView.DeleteView.as_view(), name='literary-genre-delete'),
    path('literary-genre/register/', LiteraryGenreView.RegisterView.as_view(), name='literary-genre-register'),
    path('literary-genre/update/<int:pk>', LiteraryGenreView.UpdateView.as_view(), name='literary-genre-update'),


]