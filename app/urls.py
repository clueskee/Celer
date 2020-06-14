from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AddIssue, HomeView, ShowIssue, IssueList
from .forms import UserLoginForm

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddIssue.as_view(), name='add_issue'),
    path('show/<pk>', ShowIssue.as_view(), name='show_issue'),
    path('list/', IssueList.as_view(), name='list_issues'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
    # path('login/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
]
