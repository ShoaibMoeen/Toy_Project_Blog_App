from django.views.generic.edit import CreateView, UpdateView
from article.models import Article
from django.contrib.auth.decorators import login_required
from article.forms import Create_Article_form, Edit_Article_Form
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required(), name="dispatch")
class Create_Article(CreateView):

    model = Article
    form_class = Create_Article_form
    template_name = "Create_Article.html"

    def get_success_url(self):
        if self.object.written_by is None:
            use = self.request.user
            self.object.written_by = use
            self.object.save()

        return reverse_lazy("users:index")


class Edit_Article(UpdateView):

    model = Article
    form_class = Edit_Article_Form
    success_url = "../"
    template_name = "Edit_Article.html"
