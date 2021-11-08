import django_tables2 as tables
from django_tables2.utils import A

from Things.models import Thing
from .width_attrs import width_attrs


class ThingsListTable(tables.Table):
    name = tables.LinkColumn(
        accessor=A("name"),
        orderable=True,
        attrs=width_attrs("40vw"),
        viewname="thing-detail",
        args=[A("id")],
    )
    rank = tables.LinkColumn(
        accessor=A("rank"),
        orderable=True,
        attrs=width_attrs("20vw"),
        viewname="thing-detail",
        args=[A("id")],
    )
    suit = tables.LinkColumn(
        accessor=A("suit"),
        orderable=True,
        attrs=width_attrs("20vw"),
        viewname="thing-detail",
        args=[A("id")],
    )

    class Meta:
        model = Thing
        show_header = True
        per_page = 50
        order_by = "name"
        orderable = True
        empty_text = "No matching things found"
        attrs = {"class": "table table-striped table-hover", "id": "model-table"}
        template_name = "django_tables2/bootstrap4.html"
