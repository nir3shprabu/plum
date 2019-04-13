# users/models.py
import os
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vendor(models.Model):
    name = models.CharField(max_length=190, verbose_name=_('Name'))
    certified = models.BooleanField(default=False, verbose_name=_('Certified vendor'))
    support_contact_phone = models.CharField(max_length=190, verbose_name=_('Support phone number'), blank=True)
    support_contact_email = models.EmailField(blank=True, verbose_name=_('Support email address'))
    support_contact_url = models.URLField(blank=True, verbose_name=_('Support form URL'))
    support_contact_info = models.TextField(blank=True, verbose_name=_('Additional support information'))

    def __str__(self):
        return self.name


class Product(models.Model):
    DELIVERY_PYPI = 'pypi'
    DELIVERY_LOCALPIP = 'pip'
    DELIVERY_METHODS = (
        (DELIVERY_PYPI, _('PyPI')),
        (DELIVERY_LOCALPIP, _('Local python package index')),
    )

    TIMEFRAME_MONTHLY = 'monthly'
    TIMEFRAME_YEARLY = 'yearly'
    TIMEFRAME_LIFETIME = 'lifetime'

    PRICING_TIMEFRAMES = (
        (TIMEFRAME_MONTHLY, _('monthly')),
        (TIMEFRAME_YEARLY, _('yearly')),
        (TIMEFRAME_LIFETIME, _('one-off'))
    )

    STABILITY_ALPHA = 'alpha'
    STABILITY_BETA = 'beta'
    STABILITY_STABLE = 'stable'

    STABILITY_VALUES = (
        (STABILITY_ALPHA, _('alpha')),
        (STABILITY_BETA, _('beta')),
        (STABILITY_STABLE, _('stable'))
    )

    name = models.CharField(max_length=190, verbose_name=_('Name'))
    category = models.ForeignKey('Category', verbose_name=_('Product category'), on_delete=models.PROTECT)
    long_description = models.TextField(verbose_name=_('Long description'))
    approved = models.BooleanField(default=False, verbose_name=_('Approved and visible'))
    certified = models.BooleanField(default=False, verbose_name=_('Certified plugin'))

    stability = models.CharField(choices=STABILITY_VALUES, max_length=190)
    delivery_method = models.CharField(choices=DELIVERY_METHODS, max_length=190)

    is_paid = models.BooleanField(default=False)
    pricing_tiers_variable = models.ForeignKey('PriceVariable', verbose_name=_('Pricing variable'), null=True,
                                               on_delete=models.PROTECT, blank=True)
    pricing_timeframe = models.CharField(choices=PRICING_TIMEFRAMES, verbose_name=_('Pricing timeframe'),
                                         null=True, max_length=190, blank=True)

    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    class Meta:
        verbose_name = _('Product')

    def __str__(self):
        return self.name


def screenshot_filename(instance, filename):
    return 'screenshots/{}/{}{}'.format(instance.product_id, str(uuid.uuid4()), os.path.splitext(filename)[1])


class ProductScreenshot(models.Model):
    product = models.ForeignKey(Product, related_name='screenshots', on_delete=models.CASCADE)
    picture = models.FileField(verbose_name=_('Picture'), upload_to=screenshot_filename)
    title = models.CharField(max_length=190, verbose_name=_('title'))

    class Meta:
        verbose_name = _('Screenshot')


def deliverable_filename(instance, filename):
    return 'deliverables/{}/{}{}'.format(instance.product_id, str(uuid.uuid4()), os.path.splitext(filename)[1])


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE)
    name = models.CharField(max_length=190, verbose_name=_('Version name'))
    release_date = models.DateField()
    release_notes = models.TextField(blank=True)

    deliverable_url = models.URLField(blank=True)
    deliverable_file = models.FileField(null=True, upload_to=deliverable_filename)

    min_platform_version = models.ForeignKey('PlatformVersion', on_delete=models.PROTECT, related_name='products_from',
                                             verbose_name=_('Minimum platform version'), null=True)
    max_platform_version = models.ForeignKey('PlatformVersion', on_delete=models.PROTECT, related_name='products_upto',
                                             verbose_name=_('Maximum platform version'), null=True)


class ProductPriceTier(models.Model):
    product = models.ForeignKey(Product, related_name='tiers', on_delete=models.CASCADE)
    up_to_value = models.IntegerField(verbose_name=_('Maximum value of pricing variable'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))