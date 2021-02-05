from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import View
from users.models import Writer
from article.models import Article
from django.urls import reverse_lazy
import json
from django.http import JsonResponse


@login_required
def index(request):
    writers = Writer.objects.all().order_by("-is_editor")
    context = {"writers": writers}
    return render(request, "index.html", context)


def user_check(user):
    if user.is_authenticated:
        return user.is_editor
    return False


@method_decorator(
    user_passes_test(user_check, login_url=reverse_lazy("users:index")), name="dispatch"
)
class Approve_Article(View):
    def get(self, request):
        pending_articles = Article.objects.filter(status="pending")

        context = {
            "articles": pending_articles,
        }
        return render(request, "Approve_Article.html", context)

    def post(self, request):
        is_approved = json.loads(request.POST.get("is_approved"))
        article_id = json.loads(request.POST.get("article_id"))
        article = Article.objects.get(id=article_id)
        if is_approved == "yes":
            article.status = "Approved"
            article.edited_by = self.request.user
        else:
            article.status = "Rejected"
            article.edited_by = self.request.user
        article.save()
        return JsonResponse({"approved": is_approved})


@user_passes_test(user_check, login_url=reverse_lazy("users:index"))
def Edited_Articles(request):

    edited_articles = Article.objects.filter(edited_by=request.user)
    context = {
        "articles": edited_articles,
    }
    return render(request, "Edited_Article.html", context)
