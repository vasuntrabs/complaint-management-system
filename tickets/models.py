from django.db import models

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    CATEGORY_CHOICES = [
    ('TECH', 'Technical'),
    ('MAINTENANCE', 'Maintenance'),
    ('OTHER', 'Other'),
]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.id} - {self.name}"