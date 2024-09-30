from django.db import models


class Expense(models.Model):
    # Field for the category of the expense (e.g., Shopping, Food)
    category = models.CharField(max_length=100)

    # Field for the amount of the expense
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Optional: Field for a description of the expense
    description = models.TextField(blank=True, null=True)

    # Optional: Field for the date of the expense
    date = models.DateField(auto_now_add=True)  # Automatically set the field to now when the object is created

    def __str__(self):
        return f"{self.category}: ${self.amount}"
class Income(models.Model):
        amount = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust based on your needs
        source = models.CharField(max_length=50)  # You can customize this field name
        created_at = models.DateTimeField(auto_now_add=True)
        # Add other fields as necessary

from django.db import models
class Rating(models.Model):
    stars = models.IntegerField()  # Stores the star rating (1-5)

    def __str__(self):
        return f"{self.stars} star rating"
class Note(models.Model):
    name = models.CharField(max_length=100, default='Note')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name