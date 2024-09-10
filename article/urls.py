from django.urls import path

from .views import ArticleListView, ArticleCreateView, ArticleDetailView,CommentUpdateView, ArticleUpdateView, ArticleDeleteView

app_name = "article"
urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/detail/', ArticleDetailView.as_view(), name="detail"),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name="update"),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name="delete"),
    path('article/<int:pk>/comment', CommentUpdateView.as_view(), name="edit_comment"),
    path('create_article/', ArticleCreateView.as_view(), name="create_article"),
]
