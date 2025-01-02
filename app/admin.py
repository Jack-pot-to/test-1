from django.contrib import admin
from .models import Users, HealthGoal, WorkOuts, MealsPlans, ProgressTracker

admin.site.register(Users),
admin.site.register(HealthGoal),
admin.site.register(WorkOuts),
admin.site.register(MealsPlans),
admin.site.register(ProgressTracker),

