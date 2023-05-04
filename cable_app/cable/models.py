from django.core.validators import MinLengthValidator
from django.db import models

from cable_app.users.models import UserProfile


class Cable(models.Model):
    CABLE_MAX_LEN = 25
    CABLE_MIN_LEN = 3

    INDUCTOR_MAX_LEN = 200
    INDUCTOR_MIN_LEN = 3

    MACHINE_MAX_LEN = 100
    MACHINE_MIN_LEN = 3

    CLUTCH_MAX_LEN = 12
    CLUTCH_MIN_LEN = 3

    CAP_MAX_LEN = 12
    CAP_MIN_LEN = 3

    cable_name = models.CharField(
        verbose_name='Cable Name',
        max_length=CABLE_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(CABLE_MIN_LEN)],
    )

    cap_number = models.CharField(
        verbose_name='Cap Number',
        max_length=CAP_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(CAP_MIN_LEN)],
    )

    clutch_number = models.CharField(
        verbose_name='Clutch Number',
        max_length=CLUTCH_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(CLUTCH_MIN_LEN)],
    )

    inductor_type = models.TextField(
        verbose_name='Inductor Type',
        null=False,
        blank=False,
        max_length=INDUCTOR_MAX_LEN,
        validators=[MinLengthValidator(INDUCTOR_MIN_LEN)],
    )

    machine = models.TextField(
        verbose_name='Machine',
        null=False,
        blank=False,
        max_length=MACHINE_MAX_LEN,
        validators=[MinLengthValidator(MACHINE_MIN_LEN)],
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.cable_name

    class Meta:
        ordering = ['pk']


class Order(models.Model):
    COMPANY_MAX_LEN = 100

    user = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    cable = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    cable_quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
        null=False,
        blank=False,
    )

    company_name = models.CharField(
        max_length=COMPANY_MAX_LEN,
        null=False,
        blank=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    is_confirmed = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )

    confirm_user = models.CharField(
        max_length=35,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['pk']
