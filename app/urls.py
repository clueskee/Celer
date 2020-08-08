from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import UserLoginForm
from .views import AddIssueView, HomeView, IssueView, IssueListView, IssueUpdateView, IssueDeleteView, AddCommentView, \
    SignUpView, CommentsDeleteView, IssueEndView, ContactView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddIssueView.as_view(), name='add_issue'),
    path('show/<pk>', IssueView.as_view(), name='show_issue'),
    path('list/', IssueListView.as_view(), name='list_issues'),
    path('update/<pk>', IssueUpdateView.as_view(), name='update_issue'),
    path('delete/<pk>', IssueDeleteView.as_view(), name='delete_issue'),
    path('end/<id>', IssueEndView.as_view(), name='end_issue'),
    path('comment/<id>', AddCommentView.as_view(), name='comment_issue'),
    path('cdel/<pk>', CommentsDeleteView.as_view(), name='comment_delete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('login/', auth_views.PasswordResetView.as_view(), name='pass_reset'),
 ]

