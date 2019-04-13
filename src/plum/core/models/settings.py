from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default="pretix Marketplace")
    front_page_intro = models.TextField(
        default="Welcome to the pretix Marketplace! If you're hosting pretix yourself, this is the place where "
                "you can find plugins to extend your installation. If you use pretix through our pretix Hosted offering, "
                "you do not need this page, most useful plugins are already installed for you."
    )
    footer_column_1 = models.TextField(
        default='<h5>About</h5><ul class="list-unstyled text-small">'
                '<li><a class="text-muted" href="https://pretix.eu">pretix.eu</a></li>'
                '</ul>'
    )
    footer_column_2 = models.TextField(
        default='<h5>Tech</h5><ul class="list-unstyled text-small">'
                '<li><a class="text-muted" href="https://docs.pretix.eu">Docs</a></li>'
                '</ul>'
    )
    footer_column_3 = models.TextField(
        default='<h5>Legal</h5><ul class="list-unstyled text-small">'
                '<li><a class="text-muted" href="https://pretix.eu/about/en/imprint">Imprint</a></li>'
                '<li><a class="text-muted" href="https://pretix.eu/about/en/privacy">Privacy</a></li>'
                '</ul>'
    )

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
