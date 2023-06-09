from django.db import models

# Create your models here.
class Schedules(models.Model):
    use_in_migrations = True

    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.TextField
    date = models.DateTimeField
    startTime = models.IntegerField
    endTime = models.IntegerField

    class Meta:
        db_table = "schedules"

    def __str__(self):
        return f"{self.pk} {self.content} {self.date} {self.startTime} {self.endTime}"