# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BookInfo(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)  # This field type is a guess.
    isbn = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    author = models.TextField(blank=True, null=True)  # This field type is a guess.
    dept_course = models.TextField(blank=True, null=True)  # This field type is a guess.
    descript_raw = models.TextField(blank=True, null=True)  # This field type is a guess.
    toc_raw = models.TextField(blank=True, null=True)  # This field type is a guess.
    descript_url = models.TextField(blank=True, null=True)  # Th
    toc_url = models.TextField(blank=True, null=True)  # Th
    class Meta:
        managed = False
        db_table = 'book_info'


class ClassInfo(models.Model):
    id = models.IntegerField(blank = True , null = False , primary_key = True)
    dept_course = models.TextField(blank = True , null = True)
    associated_books = models.TextField(blank = True , null = True)

    class Meta:
        managed = False
        db_table = 'class_info'

class BookTopicInfo(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)
    title = models.TextField(blank=True , null = True)
    isbn = models.TextField(blank=True, null=True)
    descript_topic_count = models.IntegerField(blank=True, null=True)
    toc_topic_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_topic_info'

class DescriptBookTopic(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_distribution = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_words = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'descript_book_topics'

class DescriptTopic(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)
    topic_words = models.TextField(blank=True, null=True)  # This field type is a guess.
    book_count = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'descript_topics'

class TocBookTopic(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_distribution = models.TextField(blank=True, null=True)  # This field type is a guess.
    topic_words = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'toc_book_topics'

class TocFreq(models.Model):
    id = models.IntegerField(blank=True, null=False , primary_key = True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.TextField(blank=True, null=True)  # This field type is a guess.
    frequency = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'toc_freq'

class TocTopic(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key = True)
    topic_words = models.TextField(blank=True, null=True)  # This field type is a guess.
    book_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toc_topics'
