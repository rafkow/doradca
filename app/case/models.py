""" Model od case class"""
from django.db import models
from subject.models.subject import Bailiff
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


TYPE = (
    ("eviction", "eksmisja"),
    ("payment", "o zapłatę"),
    ("divorce", "rozwód"),
    ("insolvency", "zgłoszenie wierzytenlość"),
)

RESULT = (
    ("new", "nowa"),
    ("begin", "rozpoczęta"),
    ("won", "wygrana"),
    ("lose", "przegrana"),
    ("enforced", "egzekwowana"),
    ("end", "zakończona"),
)

APPEARS_AS = (
    ("plaintiff", "powód"),
    ("defendant", "pozwany"),
)


class Case(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    signature = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        unique=True,
        verbose_name="sygnatura kancelarii",
    )

    type = models.CharField(
        max_length=60,
        choices=TYPE,
        null=True,
        blank=True,
        verbose_name="typ sprawy",
        default=None,
    )
    result = models.CharField(
        max_length=60,
        choices=RESULT,
        default=RESULT[0][0],
        verbose_name="wynik: sprawy",
    )
    create_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True
    )

    bailiff = models.ForeignKey(
        Bailiff,
        null=True,
        blank=True,
        verbose_name="komornik",
        on_delete=models.SET_NULL,
        default=None,
    )
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="opis",
        default=None,
    )

    def __str__(self):
        return f"{self.signature}"


class CaseSubject(models.Model):
    """entities in the case"""

    subject = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ["person", "company"]},
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("subject", "object_id")
    case = models.ForeignKey(
        "Case", on_delete=models.CASCADE, related_name="subjects"
    )
    appears_as = models.CharField(max_length=14, choices=APPEARS_AS)
