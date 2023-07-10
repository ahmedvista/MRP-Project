from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import pre_save


class ProductStock(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(
        _("Created Data"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Product Stock")
        verbose_name_plural = _("Products Stock")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class RawStock(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(
        _("Created Data"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material Stock")
        verbose_name_plural = _("Raw Materials Stock")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


@receiver(pre_save, sender=ProductStock)  ###
def set_product_stock_total(sender, instance, **kwargs):
    try:
        instance.count = (
            instance.count
            + ProductStock.objects.filter(name=instance.name).aggregate(Sum("count"))[
                "count__sum"
            ]
        )
    except:
        instance.count = 0
