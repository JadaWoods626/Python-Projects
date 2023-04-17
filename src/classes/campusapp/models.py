from django.db import models


class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.IntegerField(default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        display_course = '{0.Campus_name}: {0.State}'
        return display_course.format(self)

    class Meta:
        verbose_name_plural = "Campus Information"
# Create your models here.