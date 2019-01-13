# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class profile(models.Model):
	name=models.CharField(max_length=120)
	descriptions=models.TextField(default='description plz')


	def_unicode_(self):
		return self.name