import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from scripts.forms import ReviewForm
from scripts.models import Script


def create_script(title="", description="", code="", pub_days=0, changed_days=0):
    """
    Creates a script with the given parameters.
    `pub_days` and `changed_days` are used as time deltas for their
    respective parameters.
    """
    pub_time = timezone.now() + datetime.timedelta(days=pub_days)
    changed_time = timezone.now() + datetime.timedelta(days=changed_days)
    return Script.objects.create(title=title, description=description,
            code=code, pub_date=pub_time, changed_date=changed_time)


class ScriptViewTests(TestCase):
    def test_index_view_with_no_scripts(self):
        """
        If no scripts exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('scripts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No scripts are available.")
        self.assertQuerysetEqual(response.context['latest_script_list'], [])

    def test_index_view_with_a_past_script(self):
        """
        Scripts with a pub_date in the past should be displayed on the
        index page.
        """
        create_script(title="Past script.", pub_days=-30, changed_days=-30)
        response = self.client.get(reverse('scripts:index'))
        self.assertQuerysetEqual(
            response.context['latest_script_list'],
            ['<Script: Past script.>']
        )

    def test_index_view_with_a_future_script(self):
        """
        Scripts with a pub_date in the future should not be displayed on
        the index page.
        """
        create_script(title="Future script.", pub_days=30, changed_days=30)
        response = self.client.get(reverse('scripts:index'))
        self.assertContains(response, "No scripts are available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_script_list'], [])

    def test_index_view_with_future_script_and_past_script(self):
        """
        Even if both past and future scripts exist, only past scripts
        should be displayed.
        """
        create_script(title="Past script.", pub_days=-30, changed_days=-30)
        create_script(title="Future script.", pub_days=30, changed_days=30)
        response = self.client.get(reverse('scripts:index'))
        self.assertQuerysetEqual(
            response.context['latest_script_list'],
            ['<Script: Past script.>']
        )

    def test_index_view_with_two_past_scripts(self):
        """
        The scripts index page may display multiple scripts.
        """
        create_script(title="Past script 1.", pub_days=-30, changed_days=-30)
        create_script(title="Past script 2.", pub_days=-5, changed_days=-5)
        response = self.client.get(reverse('scripts:index'))
        self.assertQuerysetEqual(
            response.context['latest_script_list'],
            ['<Script: Past script 2.>', '<Script: Past script 1.>']
        )


class ScriptIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_script(self):
        """
        The detail view of a script with a pub_date in the future should
        return a 404 not found.
        """
        future_script = create_script(title='Future script.', pub_days=5,
                changed_days=5)
        response = self.client.get(reverse('scripts:detail',
                args=(future_script.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_script(self):
        """
        The detail view of a script with a pub_date in the past should
        display the question's text.
        """
        past_script = create_script(title='Past script.', pub_days=-5,
                changed_days=-5)
        response = self.client.get(reverse('scripts:detail',
                args=(past_script.id,)))
        self.assertContains(response, past_script.title, status_code=200)


class SriptFormTests(TestCase):
    def test_form_creation(self):
        """
        The initialised form should be valid and contain the given data.
        """
        form_data = {'rating': '1', 'comment': 'Nice.'}
        form = ReviewForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
        data = form.cleaned_data
        self.assertEqual(data['rating'], '1')
        self.assertEqual(data['comment'], 'Nice.')
