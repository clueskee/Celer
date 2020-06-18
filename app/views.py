from django.views import View
from django.views.generic import FormView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from bootstrap_modal_forms.generic import BSModalDeleteView, BSModalUpdateView, BSModalCreateView
from .forms import AddIssueForm, UpdateIssueForm
from .models import User, Issue, Comments


class HomeView(View):

    def get(self, request):
        users = User.objects.count()
        issues = Issue.objects.count()
        closed_issues = Issue.objects.filter(active=True).count()
        context = {'users': users,
                   'issues': issues,
                   'closed_issues': closed_issues
                   }

        return render(request, 'app/home.html', {'context': context})


class AddIssueView(FormView):
    form_class = AddIssueForm
    template_name = 'app/add_issue.html'

    def form_valid(self, form):
        issue = form.instance
        try:
            # issue.user = self.request.user # TODO: sprawdzić czy działa poprawnie
            issue.user = User.objects.get(pk=self.request.user.id)
        except Exception as e:
            try:
                issue.user = User.objects.get(email=issue.email)
            except Exception as e:
                user_name, user_domain = issue.email.split('@', 2)
                user = User.objects.create_user(
                    username=user_name,
                    email=issue.email
                )
                issue.user = user
                # return render(self.request, self.template_name, {'form':form, 'error': 'Nie mogę dopasować usera! Sprawdź email lub zaloguj się.'})
            # login(self.request,issue.user)
        issue.save()

        return redirect(reverse_lazy('app:show_issue', kwargs={'pk': issue.id}))


class IssueView(DetailView):
    # TODO pokazywanie plików z uploadu
    model = Issue



class IssueUpdateView(BSModalUpdateView):
    model = Issue
    template_name = 'app/update_issue.html'
    form_class = UpdateIssueForm
    success_message = 'Success: Book was updated.'


class IssueDeleteView(BSModalDeleteView):
    model = Issue
    success_message = "Usunięto!"
    success_url = reverse_lazy('app:list_issues')


class IssueListView(ListView):
    template_name = 'app/issue_table.html'
    queryset = Issue.objects.all()
    context_object_name = 'issues'
    paginate_by = 10


class AddCommentView(BSModalCreateView):
    pass