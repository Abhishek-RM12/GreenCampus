from django.shortcuts import render
from .models import Reward

def leaderboard(request):
    rewards = Reward.objects.order_by("-points")[:10]
    return render(request, "stats/leaderboard.html", {"rewards": rewards})
