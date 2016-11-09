from django.db import models
from django.utils.translation import ugettext_lazy as _


class Industry(models.Model):
    industry = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.industry


class Location(models.Model):
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.location


class Age(models.Model):
    age = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.age


class Gender(models.Model):
    gender = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.gender


class Income(models.Model):
    income = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.income


class Relationship(models.Model):
    relationship = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.relationship


class Children(models.Model):
    children = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.children


class Website(models.Model):
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.domain


class Crawl(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    websites = models.ManyToManyField(Website, through='Through')


class Through(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    crawl = models.ForeignKey(Crawl, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, null=True, blank=True, default=None)
    location = models.ForeignKey(Location, null=True, blank=True, default=None)
    age = models.ForeignKey(Age, null=True, blank=True, default=None)
    gender = models.ForeignKey(Gender, null=True, blank=True, default=None)
    income = models.ForeignKey(Income, null=True, blank=True, default=None)
    relationship = models.ForeignKey(Relationship, null=True, blank=True,
                                     default=None)
    children = models.ForeignKey(Children, null=True, blank=True, default=None)

    # class Meta:
    #     verbose_name = _("Website")
    #     verbose_name_plural = _("Websites")

    def __str__(self):
        return self.website.domain
