from django.views.generic import CreateView

from Things.forms import ThingModelForm
from Things.models import Thing


class ThingCreateView(CreateView):
    model = Thing
    template_name = "pages/thing_create.html"
    form_class = ThingModelForm

