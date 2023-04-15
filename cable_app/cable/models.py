from django.core.validators import MinLengthValidator
from django.db import models


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
        unique=True,
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

    inductor_type = models.CharField(
        verbose_name='Inductor Type',
        null=False,
        blank=False,
        max_length=INDUCTOR_MAX_LEN,
        validators=[MinLengthValidator(INDUCTOR_MIN_LEN)],
    )

    machine = models.CharField(
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

