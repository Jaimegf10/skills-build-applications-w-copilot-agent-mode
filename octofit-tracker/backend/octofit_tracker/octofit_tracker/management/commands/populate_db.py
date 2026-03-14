from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='run', duration=30, date='2026-03-14'),
            Activity(user=users[1], type='cycle', duration=45, date='2026-03-14'),
            Activity(user=users[2], type='swim', duration=25, date='2026-03-14'),
            Activity(user=users[3], type='yoga', duration=60, date='2026-03-14'),
        ]
        for activity in activities:
            activity.save()

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', suggested_for='marvel'),
            Workout(name='Situps', description='Do 30 situps', suggested_for='dc'),
        ]
        for workout in workouts:
            workout.save()

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
