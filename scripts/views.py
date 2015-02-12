from django.views import generic
from django.utils import timezone

from scripts.models import Script, Review


class IndexView(generic.ListView):
    template_name = 'scripts/index.html'
    context_object_name = 'latest_script_list'

    def get_queryset(self):
        """
        Return the last five published scripts (not including those set to be
        published in the future).
        """
        return Script.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Script
    template_name = 'scripts/detail.html'

    def get_queryset(self):
        """
        Excludes any scripts that aren't published yet.
        """
        return Script.objects.filter(pub_date__lte=timezone.now())
