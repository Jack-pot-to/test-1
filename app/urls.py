from django.urls import path
from .views import (HomepageView, AboutpageView, ContactpageView, ServicespageView,
                    WorkOutsListView, WorkOutsDetailView, WorkOutsCreateView,
                    WorkOutsUpdateView, WorkOutsDeleteView)

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('blog/', ServicespageView.as_view(), name='blog'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('services/', WorkOutsListView.as_view(), name='services'),
    path('workouts/<int:pk>', WorkOutsDetailView.as_view(), name='workouts_detail'),
    path('workouts/create', WorkOutsCreateView.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/edit', WorkOutsUpdateView.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete', WorkOutsDeleteView.as_view(), name='workouts_delete'),
]