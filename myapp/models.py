from django.db import models
from django.contrib.auth.models import User

class Watch(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/watches/')
    starting_bid = models.DecimalField(max_digits=9, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    bid_end_date = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='watches', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bid(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    watch = models.ForeignKey(Watch, related_name='bids', on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, related_name='bids', on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} by {self.bidder.username}"
