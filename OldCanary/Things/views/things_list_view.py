from crispy_forms.helper import FormHelper
from django_filters.views import FilterView 
from django_tables2 import SingleTableMixin

from Things.models import Thing
from Things.tables import ThingsListTable
from Things.filters import ThingListFilter


class ThingsListView(SingleTableMixin, FilterView):
    model = Thing
    template_name = "pages/things_list.html"
    table_class = ThingsListTable
    filterset_class = ThingListFilter

    def get_context_data(self, **kwargs):
        filter_helper = FormHelper()
        kwargs["filter"].form.helper = filter_helper
        filter_helper.form_method = "GET"
        filter_helper.form_action = "instruments-list"
        filter_helper.form_class = "form-horizontal"
        filter_helper.form_tag = True
        filter_helper.form_id = "search-form"
        filter_helper.template = "bootstrap4/whole_uni_form.html"

        return super(InstrumentsListView, self).get_context_data(**kwargs)
