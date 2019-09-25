from django.db import models
from django.contrib.postgres.fields import ArrayField
from EssayArena.Auth.models import User




class Order(models.Model):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    STARTED = "STARTED"
    FINISHED = "FINISHED"
    REJECTED = "REJECTED"
    status_choices = [
        (PENDING, "pending"),
        (ASSIGNED, "assigned"),
        (STARTED,"started"),
        (FINISHED, "finished")

    ]
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    files = ArrayField(models.CharField(max_length=100), null= True)


class Application(models.Model):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    status_choices = [
        (PENDING, "pending"),
        (ACCEPTED, "accepted"),
        (REJECTED, "rejected")

    ]
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    bid_price = models.DecimalField(decimal_places=2, max_digits=20, default=1.0)
