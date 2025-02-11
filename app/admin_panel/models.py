from django.db import models
from django.contrib.auth.models import User

class PhishingRule(models.Model):
    rule_name = models.CharField(max_length=255)
    description = models.TextField()
    action = models.CharField(max_length=50)  # e.g., Block, Quarantine

class Whitelist(models.Model):
    domain = models.CharField(max_length=255)

class Blacklist(models.Model):
    domain = models.CharField(max_length=255)

class AlertThreshold(models.Model):
    threshold = models.IntegerField()  # e.g., 5 phishing attempts

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)