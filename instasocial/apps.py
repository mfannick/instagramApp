# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class InstasocialConfig(AppConfig):
    name = 'instasocial'
    def ready(self):
       import instasocial.signals