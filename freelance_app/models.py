import json

from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    STATUSES = [
        ('1', 'in_tasks'),
        ('2', 'in_progress'),
        ('3', 'done'),
        ('4', 'problem'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    start_task = models.DateTimeField()
    end_task = models.DateTimeField()
    status = models.CharField(choices=STATUSES, default='1', max_length=1)
    executor_list = models.CharField(max_length=200, blank=True, null=True)

    def set_executor_list(self, x):
        self.foo = json.dumps(x)

    def get_executor_list(self):
        return json.loads(self.foo)



class Message(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField()
    msg = models.CharField(max_length=1500)


class Support(models.Model):
    STATUSES = [
        ('1', 'resolution to executor'),
        ('2', 'resolution to customer'),
    ]
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    resolution = models.CharField(choices=STATUSES, default='1', max_length=1)
