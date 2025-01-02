from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in cm")
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HealthGoal(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="health_goals")
    goal_type = models.CharField(max_length=30)
    target_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Target value for the goal")
    current_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Current value towards the goal")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return f"{self.goal_type} for {self.user.name}"


class WorkOuts(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={"pk": self.pk})

class MealsPlans(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="meal_plans")
    plan_name = models.CharField(max_length=50)
    calories = models.IntegerField(help_text="Total calories in the meal plan")
    protein = models.IntegerField(help_text="Protein content in grams")
    fat = models.IntegerField(help_text="Fat content in grams")
    carbohydrates = models.IntegerField(help_text="Carbohydrates content in grams")
    duration = models.DurationField(help_text="Duration for which the meal plan is followed")

    def __str__(self):
        return self.plan_name


class ProgressTracker(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="progress")
    metric_type = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type} for {self.user.name}"

