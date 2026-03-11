from django.db import models

class Payment(models.Model):
    name           = models.CharField(max_length=200, default='')
    email          = models.EmailField(default='')
    course         = models.CharField(max_length=200, default='')
    amount         = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=50, default='Success')
    date           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course}"
