from django.db import models
from EssayArena.Auth.models import User



class Order(models.Model):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    STARTED = "STARTED"
    FINISHED = "FINISHED"
    REJECTED = "REJECTED"
    status_choises = [
        (PENDING, "pending"),
        (ASSIGNED, "assigned"),
        (STARTED,"started"),
        (FINISHED, "finished")

    ]
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Application(models.Model):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
