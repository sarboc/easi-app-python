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

class AccessibilityTestDate(models.Model):
    INITIAL = 'INITIAL'
    REMEDIATION = 'REMEDIATION'
    TYPE_CHOICES = [
        (INITIAL, INITIAL), 
        (REMEDIATION, REMEDIATION)
    ]
    test_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        default=INITIAL,
    )
    date = models.DateField()
    score = models.IntegerField(null=True)
    accessibility_request = models.ForeignKey(
        AccessibilityRequest, related_name="accessibility_request", on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)