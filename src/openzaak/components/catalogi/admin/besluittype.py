from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from openzaak.utils.admin import UUIDAdminMixin

from ..models import BesluitType
from .mixins import CatalogusContextAdminMixin, GeldigheidAdminMixin, PublishAdminMixin


@admin.register(BesluitType)
class BesluitTypeAdmin(
    UUIDAdminMixin,
    CatalogusContextAdminMixin,
    GeldigheidAdminMixin,
    PublishAdminMixin,
    admin.ModelAdmin,
):
    # List
    list_display = ("omschrijving", "catalogus", "besluitcategorie")
    list_filter = ("catalogus",)
    search_fields = ("uuid", "omschrijving", "besluitcategorie", "toelichting")
    ordering = ("catalogus", "omschrijving")

    # Details
    fieldsets = (
        (
            _("Algemeen"),
            {
                "fields": (
                    "omschrijving",
                    "omschrijving_generiek",
                    "besluitcategorie",
                    "reactietermijn",
                    "toelichting",
                )
            },
        ),
        (
            _("Publicatie"),
            {
                "fields": (
                    "publicatie_indicatie",
                    "publicatietekst",
                    "publicatietermijn",
                )
            },
        ),
        (
            _("Relaties"),
            {
                "fields": (
                    "catalogus",
                    "informatieobjecttypen",
                    # 'resultaattypes',
                    "zaaktypen",
                )
            },
        ),
    )
    filter_horizontal = ("informatieobjecttypen", "zaaktypen")  # , 'resultaattypes'
