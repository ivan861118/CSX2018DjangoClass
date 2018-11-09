from django.forms import ModelForm
from .models import New


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# class DeleteNewForm(ModelForm):
#     class Meta:
#         model = New
#         fields = []