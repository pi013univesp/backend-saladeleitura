from django.urls import path
from .Views import LibraryView
from .Views import ClientView
from .Views import BookView
from .Views import BookAtLibraryView
from .Views import BorrowView
from .Views import CommentView

app_name = "Libraryapp"

urlpatterns = [
    path('library/', LibraryView.GetAllView.as_view(), name='library-get-all'),
    path('library/<int:pk>', LibraryView.GetLibraryByIdView.as_view(), name='library-get-id'),
    path('library/register', LibraryView.RegisterView.as_view(), name='library-register'),
    path('library/login', LibraryView.LoginView.as_view(), name='library-login'),
    path('library/delete/<int:pk>', LibraryView.DeleteView.as_view(), name='library-delete'),
    path('library/update/<int:pk>', LibraryView.UpdateView.as_view(), name='library-update'),
    
    path('client/', ClientView.GetAllView.as_view(), name='client-get-all'),
    path('client/<int:pk>', ClientView.GetClientByIdView.as_view(), name='client-get-id'),
    path('client/delete/<int:pk>', ClientView.DeleteView.as_view(), name='client-delete'),
    path('client/register/', ClientView.RegisterView.as_view(), name='client-register'),
    path('client/update/<int:pk>', ClientView.UpdateView.as_view(), name='client-update'),

    path('book/', BookView.GetAllView.as_view(), name='books-get-all'),
    path('book/<int:pk>', BookView.GetBookByIdView.as_view(), name='book-get-id'),
    path('book/delete/<int:pk>', BookView.DeleteView.as_view(), name='book-delete'),
    path('book/register/', BookView.RegisterView.as_view(), name='book-register'),
    path('book/update/<int:pk>', BookView.UpdateView.as_view(), name='book-update'),

    path('book-at-library/', BookAtLibraryView.GetAllView.as_view(), name='book-at-library-get-all'),
    path('book-at-library/<int:pk>', BookAtLibraryView.GetBookByIdView.as_view(), name='book-at-library-get-id'),
    path('book-at-library/delete/<int:pk>', BookAtLibraryView.DeleteView.as_view(), name='book-at-library-delete'),
    path('book-at-library/register/', BookAtLibraryView.RegisterView.as_view(), name='book-at-library-register'),
    path('book-at-library/update/<int:pk>', BookAtLibraryView.UpdateView.as_view(), name='book-at-library-update'),

    path('borrow/', BorrowView.GetAllView.as_view(), name='borrow-get-all'),
    path('borrow/<int:pk>', BorrowView.GetBorrowByIdView.as_view(), name='borrow-get-id'),
    path('borrow/delete/<int:pk>', BorrowView.DeleteView.as_view(), name='borrow-delete'),
    path('borrow/register/', BorrowView.RegisterView.as_view(), name='borrow-register'),
    path('borrow/update/<int:pk>', BorrowView.UpdateView.as_view(), name='borrow-update'),
    path('borrow/close/<int:pk>', BorrowView.BorrowCloseView.as_view(), name='borrow-close'),
    path('borrow/in-debt/', BorrowView.GetAllBorrowInDebt.as_view(), name='borrow-get-all-debt'),

    path('comment/', CommentView.GetAllView.as_view(), name='comment-get-all'),
    path('comment/register/', CommentView.RegisterView.as_view(), name='comment-register'),
    path('comment/<int:id>', CommentView.GetCommentByIdView.as_view(), name='comment-get-forum'),
]