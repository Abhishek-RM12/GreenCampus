from django.db import models # type: ignore

class Reward(models.Model):
    BADGE_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('star', 'Star'),
    ]

    participant_name = models.CharField(max_length=100, default="Unknown Participant")
    points = models.IntegerField(default=0)
    badge = models.CharField(
        max_length=20,
        choices=BADGE_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.participant_name} - {self.points} pts"
