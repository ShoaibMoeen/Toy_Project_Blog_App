from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("article-approval", views.Approve_Article.as_view(), name="approve_article"),
    path("articles-edited", views.Edited_Articles, name="edited_article"),
]
