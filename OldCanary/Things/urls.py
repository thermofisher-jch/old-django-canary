from django.conf.urls import url
from Things import views

urlpatterns = [
    # Instrument Reservation URLs
    url(
        r"things/new$",
        views.ThingCreateView.as_view(),
        name="thing-create",
    ),
    url(
        r"^things/(?P<pk>\d+)$",
        views.ThingDetailView.as_view(),
        name="thing-detail",
    ),
    url(
        r"^things$",
        views.ThingsListView.as_view(),
        name="things-list",
    ),
]
