from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam', members=['test@example.com'])
        self.assertEqual(team.name, 'TestTeam')
        self.assertIn('test@example.com', team.members)

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity_type='Running', duration=30)
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=50)
        self.assertEqual(leaderboard.team, 'TestTeam')
        self.assertEqual(leaderboard.points, 50)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', description='Test description')
        self.assertEqual(workout.name, 'TestWorkout')
        self.assertEqual(workout.description, 'Test description')
