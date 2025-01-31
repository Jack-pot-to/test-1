from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkOuts, Users, HealthGoal, MealsPlans, ProgressTracker, Admin
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/home.html'


class ServicespageView(TemplateView):
    template_name = 'app/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        healthgoal = None
        mealsplans = None

        # Check if the user is logged in
        if 'user_id' in self.request.session:
            try:
                user = Users.objects.get(id=self.request.session['user_id'])
                healthgoal = HealthGoal.objects.filter(user=user)  # Get health goals for the user
                mealsplans = MealsPlans.objects.filter(user=user)  # Get meals plans for the user
            except Users.DoesNotExist:
                messages.error(self.request, "User not found.")

        # Pass all data objects for display in tables
        context['user'] = user
        context['healthgoal'] = healthgoal
        context['mealsplans'] = mealsplans
        context['workouts'] = WorkOuts.objects.all()
        context['progresstracker'] = ProgressTracker.objects.all()

        # Pass the counts for each table
        context['user_count'] = Users.objects.count()
        context['healthgoal_count'] = HealthGoal.objects.count()
        context['workouts_count'] = WorkOuts.objects.count()
        context['mealsplans_count'] = MealsPlans.objects.count()
        context['progresstracker_count'] = ProgressTracker.objects.count()

        return context


class AboutpageView(TemplateView):
    template_name = 'app/about.html'


class ContactpageView(TemplateView):
    template_name = 'app/contact.html'


class WorkOutsListView(ListView):
    model = WorkOuts
    context_object_name = 'WorkOut'
    template_name = 'app/workouts_list.html'


class WorkOutsDetailView(DetailView):
    model = WorkOuts
    context_object_name = 'WorkOuts'
    template_name = 'app/workouts_detail.html'


class WorkOutsCreateView(CreateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/workouts_create.html'


class WorkOutsUpdateView(UpdateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/workouts_update.html'


class WorkOutsDeleteView(DeleteView):
    model = WorkOuts
    template_name = 'app/workouts_delete.html'
    success_url = reverse_lazy('services')


class DatabasePageView(TemplateView):
    template_name = 'app/database.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Pass all data objects for display in tables
        context['user'] = Users.objects.all()
        context['healthgoal'] = HealthGoal.objects.all()
        context['workouts'] = WorkOuts.objects.all()
        context['mealsplans'] = MealsPlans.objects.all()
        context['progresstracker'] = ProgressTracker.objects.all()

        # Pass the counts for each table
        context['user_count'] = Users.objects.count()
        context['healthgoal_count'] = HealthGoal.objects.count()
        context['workouts_count'] = WorkOuts.objects.count()
        context['mealsplans_count'] = MealsPlans.objects.count()
        context['progresstracker_count'] = ProgressTracker.objects.count()

        return context

    @staticmethod
    def admin_dashboard(request):
        # Calculate the counts
        user_count = Users.objects.count()
        healthgoal_count = HealthGoal.objects.count()
        workouts_count = WorkOuts.objects.count()
        mealsplans_count = MealsPlans.objects.count()
        progresstracker_count = ProgressTracker.objects.count()

        return render(request, 'app/admin_dashboard.html', {
            'user_count': user_count,
            'healthgoal_count': healthgoal_count,
            'workouts_count': workouts_count,
            'mealsplans_count': mealsplans_count,
            'progresstracker_count': progresstracker_count,
        })


class UserCreateView(CreateView):
    model = Users
    fields = ['name', 'email', 'password', 'date_of_birth',
              'gender', 'height']
    template_name = 'app/add_user.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'


class HealthGoalCreateView(CreateView):
    model = HealthGoal
    fields = ['user', 'goal_type', 'target_value', 'current_value',
              'start_date', 'end_date', 'status']
    template_name = 'app/add_healthgoal.html'

    def get_success_url(self):
        return reverse_lazy('add_mealsplans')


class AdminWorkoutsCreateView(CreateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/add_workouts.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminMealsPlansCreateView(CreateView):
    model = MealsPlans
    fields = ['user', 'plan_name', 'calories', 'protein', 'fat', 'carbohydrates', 'duration']
    template_name = 'app/add_mealsplans.html'

    def get_success_url(self):
        return reverse_lazy('blog')


class AdminProgressTrackerCreateView(CreateView):
    model = ProgressTracker
    fields = ['user', 'metric_type']
    template_name = 'app/add_progresstracker.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminUserUpdateView(UpdateView):
    model = Users
    fields = ['name', 'email', 'password', 'date_of_birth',
              'gender', 'height']
    template_name = 'app/update_user.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminHealthGoalUpdateView(UpdateView):
    model = HealthGoal
    fields = ['user', 'goal_type', 'target_value', 'current_value',
              'start_date', 'end_date', 'status']
    template_name = 'app/update_healthgoal.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminWorkOutsUpdateView(UpdateView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/update_workouts.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminMealsPlansUpdateView(UpdateView):
    model = MealsPlans
    fields = ['user', 'plan_name', 'calories', 'protein', 'fat', 'carbohydrates', 'duration']
    template_name = 'app/update_mealsplans.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminProgressTrackerUpdateView(UpdateView):
    model = ProgressTracker
    fields = ['user', 'metric_type']
    template_name = 'app/update_progresstracker.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminUserDeleteView(DeleteView):
    model = Users
    fields = ['name', 'email', 'password', 'date_of_birth',
              'gender', 'height']
    template_name = 'app/delete_user.html'
    success_url = reverse_lazy('database')

class AdminHealthGoalDeleteView(DeleteView):
    model = HealthGoal
    fields = ['user', 'goal_type', 'target_value', 'current_value',
              'start_date', 'end_date', 'status']
    template_name = 'app/delete_healthgoal.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminWorkOutsDeleteView(DeleteView):
    model = WorkOuts
    fields = ['name', 'category', 'duration', 'calories_burned']
    template_name = 'app/delete_workouts.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminMealsPlansDeleteView(DeleteView):
    model = MealsPlans
    fields = ['user', 'plan_name', 'calories', 'protein', 'fat', 'carbohydrates', 'duration']
    template_name = 'app/delete_mealsplans.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class AdminProgressTrackerDeleteView(DeleteView):
    model = ProgressTracker
    fields = ['user', 'metric_type']
    template_name = 'app/delete_progresstracker.html'

    def get_success_url(self):
        return reverse_lazy('database') + '?section=users'

class LoginFormTemplateView(TemplateView):
    template_name = 'registration/login.html'


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the user exists in the database
            admin = Admin.objects.get(username=username)
            if admin.password == password:
                # Login successful
                request.session['admin_id'] = admin.id
                request.session['admin_firstname'] = admin.firstname
                messages.success(request, "Admin login successful")
                return redirect('database')
            else:
                # Invalid password message
                messages.error(request, "Invalid username or password.")
        except Admin.DoesNotExist:  # Handle Admin-specific DoesNotExist
            messages.error(request, "Admin does not exist. Please contact support.")

    # Render login page even if there are errors
    return render(request, 'registration/admin_login.html')


def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the user exists in the database
            user = Users.objects.get(username=username)
            if user.password == password:
                # Save user ID in session for login state
                request.session['user_id'] = user.id
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid username or password.")  # Invalid password message
        except Users.DoesNotExist:
            messages.error(request, "Customer does not exist. Please register first.")  # User not found message

    # Render login page even if there are errors
    return render(request, 'registration/login.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        height = request.POST.get('height')


        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('customer_login')

        user = Users(
            name=name,
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            height=height,
        )
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'registration/register.html')

