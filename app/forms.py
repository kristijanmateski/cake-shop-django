from django import forms
from app.models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        exclude = ('baker',)

    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
