from django.db import models


class URL(models.Model):
    text = models.URLField(verbose_name="url", max_length=200, unique=True)
    response_status = models.IntegerField(null=True, verbose_name="status")
    check_interval = models.PositiveIntegerField(verbose_name="check interval")
    is_paused = models.BooleanField(default=False, verbose_name="paused")
