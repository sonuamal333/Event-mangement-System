from django.urls import path

from .views import ParticipantListView, DashboardView

urlpatterns = [
    
    path('', DashboardView.as_view(), name='dashboard'),
    
    path('participants/', ParticipantListView.as_view(), name='participants-list'),
]
