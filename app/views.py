from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import FormView, DetailView, ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import Issue
from .forms import AddIssueForm
from .models import User, Issue


class HomeView(View):

    def get(self, request):
        users = User.objects.count()
        issues = Issue.objects.count()
        closed_issues = Issue.objects.filter(active=True).count()
        context = {'users':users,
                   'issues':issues,
                   'closed_issues':closed_issues
                   }
        return render(request, 'app/home.html', {'context':context})

class AddIssue(View):
    # TODO Upload plików
    form_class = AddIssueForm

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, 'app/add_issue.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            issue = Issue()
            issue.title = form.cleaned_data['title']
            issue.description = form.cleaned_data['description']
            issue.email = form.cleaned_data['email']
            issue.priority = form.cleaned_data['priority']
            issue.status = form.cleaned_data['status']
            issue.user_id = User.objects.get(pk=request.user.id)
            issue.save()
            breakpoint()
        return redirect(issue.get_absolute_url())

class ShowIssue(DetailView):
    # TODO pokazywanie plików z uploadu
    model = Issue

class IssueList(ListView):
    template_name = 'app/issue_list.html'
    queryset = Issue.objects.all()
    context_object_name = 'issues'