from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class BannerImage(models.Model):

	image = models.ImageField(_('Index banner image'),upload_to='img/banner')
	detail_url = models.URLField(_('Announce detil url'),null=True,blank=True)
