from django.db import models

class System(models.Model):
    name = models.CharField(max_length=100)
    lcid = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class AccessibilityRequest(models.Model):
    name = models.CharField(max_length=100)
    system = models.ForeignKey(
        System, related_name="system", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name