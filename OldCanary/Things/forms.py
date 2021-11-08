from django import forms
from Things.models import Thing


# class DateInput(forms.DateInput):
#     input_type = "date"


# Thing Forms
class ThingModelForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ("name", "rank", "suit", "start", "end")
        widgets = {
            "start": forms.DateInput(),
            "end": forms.DateInput(),
        }


class Thing_Update_Form(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ("name", "rank", "suit", "start", "end")
        widgets = {
            "start": forms.DateInput(),
            "end": forms.DateInput(),
        }


class Thing_Create_Form(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ("name", "rank", "suit", "start", "end")
        widgets = {
            "start": forms.DateInput(),
            "end": forms.DateInput(),
        }
