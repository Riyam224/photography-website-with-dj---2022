from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.


class Image(models.Model):
    alt = models.CharField(_("alt"), max_length=60)
    image = models.ImageField(_("image"), upload_to='image/')

    

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return str(self.alt)

