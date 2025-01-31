from django.urls import path
from . import views
from .views import (HomepageView, AboutpageView, ContactpageView, ServicespageView,
                    WorkOutsListView, WorkOutsDetailView, WorkOutsCreateView,
                    WorkOutsUpdateView, WorkOutsDeleteView,
                    DatabasePageView, UserCreateView, HealthGoalCreateView,
                    AdminWorkoutsCreateView, AdminMealsPlansCreateView, AdminProgressTrackerCreateView,
                    AdminUserUpdateView, AdminHealthGoalUpdateView, AdminWorkOutsUpdateView,
                    AdminMealsPlansUpdateView, AdminProgressTrackerUpdateView, AdminUserDeleteView,
                    AdminHealthGoalDeleteView, AdminWorkOutsDeleteView, AdminMealsPlansDeleteView,
                    AdminProgressTrackerDeleteView,LoginFormTemplateView)

urlpatterns = [
    path('', LoginFormTemplateView.as_view(), name='login'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('admin_login/', views.admin_login, name='login_admin'),
    path('register_user/', views.register_user, name='register_user'),

    path('home/', HomepageView.as_view(), name='home'),
    path('blog/', ServicespageView.as_view(), name='blog'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('services/', WorkOutsListView.as_view(), name='services'),
    path('workouts/<int:pk>', WorkOutsDetailView.as_view(), name='workouts_detail'),
    path('workouts/create', WorkOutsCreateView.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/edit', WorkOutsUpdateView.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete', WorkOutsDeleteView.as_view(), name='workouts_delete'),


    path('database/', DatabasePageView.as_view(), name='database'),

    path('adduser/create', UserCreateView.as_view(), name='add_user'),
    path('updateuser/<int:pk>/edit', AdminUserUpdateView.as_view(), name='update_user'),
    path('deleteuser/<int:pk>/delete', AdminUserDeleteView.as_view(), name='delete_user'),

    path('addhealthgoal/create', HealthGoalCreateView.as_view(), name='add_healthgoal'),
    path('updatehealthgoal/<int:pk>/edit', AdminHealthGoalUpdateView.as_view(), name='update_healthgoal'),
    path('deletehealthgoal/<int:pk>/delete', AdminHealthGoalDeleteView.as_view(), name='delete_healthgoal'),

    path('addworkouts/create', AdminWorkoutsCreateView.as_view(), name='add_workouts'),
    path('updateworkouts/<int:pk>/edit', AdminWorkOutsUpdateView.as_view(), name='update_workouts'),
    path('deleteworkouts/<int:pk>/delete', AdminWorkOutsDeleteView.as_view(), name='delete_workouts'),

    path('addmealsplans/create', AdminMealsPlansCreateView.as_view(), name='add_mealsplans'),
    path('updatemealplans/<int:pk>/edit', AdminMealsPlansUpdateView.as_view(), name='update_mealsplans'),
    path('deletemealplans/<int:pk>/delete', AdminMealsPlansDeleteView.as_view(), name='delete_mealsplans'),

    path('addprogresstracker/create', AdminProgressTrackerCreateView.as_view(), name='add_progresstracker'),
    path('updateprogresstracker/<int:pk>/edit', AdminProgressTrackerUpdateView.as_view(), name='update_progresstracker'),
    path('deleteprogresstracker/<int:pk>/delete', AdminProgressTrackerDeleteView.as_view(), name='delete_progresstracker'),

]