from django.urls import path
from article import views

app_name = "article"

urlpatterns = [
    path("create", views.Create_Article.as_view(), name="create_article"),
    path("<int:pk>", views.Edit_Article.as_view(), name="edit_article"),
]
