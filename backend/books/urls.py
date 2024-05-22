from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListAPIView.as_view()),
    path("<int:book_id>/", views.BookDetailAPIView.as_view()),
    path("<int:book_id>/comments/", views.CommentListAPIView.as_view()),
    path(
        "<int:book_id>/comments/<int:comment_id>,", views.CommentDetailAPIView.as_view()
    ),
    path("synopsys/", views.SynopsysAPIView.as_view()),
    # path("summary/"),
]
