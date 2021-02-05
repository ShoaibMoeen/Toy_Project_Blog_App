from django.forms import ModelForm
from article.models import Article


class Create_Article_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Create_Article_form, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs["class"] = "form-control"

    class Meta:
        model = Article
        fields = ["title", "content"]


class Edit_Article_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Edit_Article_Form, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs["class"] = "form-control"
        self.fields["status"].widget.attrs["readonly"] = True

    class Meta:
        model = Article
        fields = ["title", "content", "status"]
