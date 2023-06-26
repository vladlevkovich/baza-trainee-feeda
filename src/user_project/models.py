from django.db import models
from src.users.models import Projects
import uuid


class JoinProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    specialization = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField(unique=True)
    account_discord = models.CharField(max_length=25)
    account_linkedin = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    experience = models.BooleanField(default=False)
    project = models.ForeignKey(Projects, blank=True, null=True, on_delete=models.PROTECT)
    conditions_participation = models.BooleanField(default=False)
    processing_personal_data = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.specialization}'
