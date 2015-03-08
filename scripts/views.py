from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import FormView

from scripts.forms import ReviewForm
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


class DetailView(FormView):
    model = Script
    template_name = 'scripts/detail.html'
    form_class = ReviewForm
    # success_url = '/thanks/' # TODO

    # Override GET to be able to pass the script ID to be used in the form
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        context_data = self.get_context_data(form=form)
        context_data['script'] = Script.objects.filter(id=kwargs['pk'])[0]
        return self.render_to_response(context_data)


def write_review(request, script_id):
    script = get_object_or_404(Script, pk=script_id)
    form = ReviewForm(request.POST) # TODO Remove?
    if form.is_valid():
        print(form.cleaned_data) # TODO
        print(script_id)
        # TODO Save the review
        return render(request, 'scripts/detail.html', {'form': form,
            'script': script,
            'message': "Thanks for your review!"})
    else:
        return render(request, 'scripts/detail.html', {'form': form,
            'script': script,
            'error_message': "You must provide a valid comment."})
