from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        marvel_users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica'},
            {'email': 'thor@marvel.com', 'username': 'Thor'},
        ]
        dc_users = [
            {'email': 'batman@dc.com', 'username': 'Batman'},
            {'email': 'superman@dc.com', 'username': 'Superman'},
            {'email': 'wonderwoman@dc.com', 'username': 'WonderWoman'},
        ]
        for u in marvel_users + dc_users:
            User.objects.create_user(email=u['email'], username=u['username'], password='password')

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', members=[u['email'] for u in marvel_users])
        dc_team = Team.objects.create(name='DC', members=[u['email'] for u in dc_users])

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', activity_type='Running', duration=30)
        Activity.objects.create(user_email='batman@dc.com', activity_type='Cycling', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength.')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
