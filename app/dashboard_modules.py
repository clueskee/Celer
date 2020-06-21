from jet.dashboard.modules import DashboardModule
from app.models import Issue


class RecentTickets(DashboardModule):
    title = 'Zgłoszenia'
    template = 'app/dashboard_modules/issues.html'
    limit = 3

    def init_with_context(self, context):
        self.children = Issue.objects.order_by('-date_add')[:self.limit]