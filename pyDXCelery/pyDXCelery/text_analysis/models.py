from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Comment(models.Model):

    NEGATIVE = -1
    NEUTRAL = 0
    POSITIVE = 1

    SENTIMENT_CHOICES = (
        (NEGATIVE, _('negative')),
        (NEUTRAL, _('neutral')),
        (POSITIVE, _('positive')),
    )

    name = models.CharField(_('name'), max_length=64)
    comment = models.TextField(_('comment'))
    pub_date = models.DateTimeField(_('Published date'),
                                    editable=False, auto_now=True)
    sentiment = models.SmallIntegerField(_('Sentiment?'),
                                         default=NEUTRAL,
                                         choices=SENTIMENT_CHOICES)
    stats = models.TextField(_('text statistics'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
