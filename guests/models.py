from __future__ import unicode_literals
import datetime
import uuid

from django.conf import settings
from django.db import models
from django.dispatch import receiver


def _random_uuid():
    return uuid.uuid4().hex


class Party(models.Model):
    """
    A party consists of one or more guests.
    """
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES)
    save_the_date_sent = models.DateTimeField(
        null=True, blank=True, default=None)
    save_the_date_opened = models.DateTimeField(
        null=True, blank=True, default=None)
    invitation_id = models.CharField(
        max_length=32, db_index=True, default=_random_uuid, unique=True)
    invitation_sent = models.DateTimeField(null=True, blank=True, default=None)
    invitation_opened = models.DateTimeField(
        null=True, blank=True, default=None)
    is_invited = models.BooleanField(default=True)
    is_attending = models.NullBooleanField(default=None)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return 'Party: {}'.format(self.name)

    @classmethod
    def in_default_order(cls):
        return cls.objects.order_by('category', '-is_invited', 'name')

    @property
    def ordered_guests(self):
        return self.guest_set.order_by('is_child', 'pk')

    @property
    def any_guests_attending(self):
        return any(self.guest_set.values_list('is_attending', flat=True))

    @property
    def guest_emails(self):
        return filter(None, self.guest_set.values_list('email', flat=True))


class Guest(models.Model):
    """
    A single guest
    """
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    is_attending = models.NullBooleanField(default=None)
    is_child = models.BooleanField(default=False)

    @property
    def name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    @property
    def unique_id(self):
        # convert to string so it can be used in the "add" templatetag
        return unicode(self.pk)

    def __unicode__(self):
        return 'Guest: {} {}'.format(self.first_name, self.last_name)
