from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AddIssueView, HomeView, IssueView, IssueListView, IssueUpdateView, IssueDeleteView
from .forms import UserLoginForm

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddIssueView.as_view(), name='add_issue'),
    path('show/<pk>', IssueView.as_view(), name='show_issue'),
    path('list/', IssueListView.as_view(), name='list_issues'),
    path('update/<pk>', IssueUpdateView.as_view(), name='update_issue'),
    path('delete/<pk>', IssueDeleteView.as_view(), name='delete_issue'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
    # path('login/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
]
