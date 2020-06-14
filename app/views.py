from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import FormView, DetailView, ListView, CreateView
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

# class AddIssue(CreateView):
#     # TODO Upload plików
#     form_class = AddIssueForm
#     template_name = 'app/add_issue.html'
#     # success_url = get_success_url()
#
#     # def get_success_url(self):
#     #     return reverse_lazy('app:show_issue', kwargs={'pk': issue.id})
#
#     # def get_form_kwargs(self):
#     #     kwargs = super(AddIssue, self).get_form_kwargs()
#     #     kwargs.update({'user_id': self.request.user})
#     #     return kwargs
#
#     # def get_user(request):
#     #     if not hasattr(request, '_cached_user'):
#     #         request._cached_user = auth.get_user(request)
#     #     return request._cached_user
#
#     def get_success_url(self):
#         return reverse('book-detail', kwargs={'pk': self.object.pk})
#
#     def form_valid(self, form):
#         # issue = form.instance
#         # issue.user_id = self.request.user
#         issue = Issue.objects.create(
#         title = form.cleaned_data['title'],
#         description = form.cleaned_data['description'],
#         email = form.cleaned_data['email'],
#         priority = form.cleaned_data['priority'],
#         status = form.cleaned_data['status'],
#         user_id = User.objects.get(pk = self.request.user.id),
#         )
#
#         issue.save()
#         # print(issue)
#         # print(issue.id)
#         # return redirect(reverse_lazy('app:show_issue', kwargs={'pk':issue.id}))

class AddIssue(CreateView):
    template_name = 'app/add_issue.html'
    form_class = AddIssueForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(AddIssue, self).get_initial(**kwargs)
    #     initial['user_id'] = self.request.user
    #     breakpoint()
    #     return initial
    def get_form_kwargs(self):
        kwargs = super(AddIssue, self).get_form_kwargs()
        kwargs['user_id'] = User.objects.get(pk=self.user.id)
        return kwargs

class ShowIssue(DetailView):
    # TODO pokazywanie plików z uploadu
    model = Issue

class IssueList(ListView):
    template_name = 'app/issue_list.html'
    queryset = Issue.objects.all()
    context_object_name = 'issues'
    paginate_by = 10