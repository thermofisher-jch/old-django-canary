from django.views.generic import UpdateView

from Things.forms import ThingModelForm
from Things.models import Thing


class ThingDetailView(UpdateView):
    model = Thing
    template_name = "pages/thing_detail.html"
    form_class = ThingModelForm

