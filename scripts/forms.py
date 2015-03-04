from django import forms

from scripts.models import Review


class ReviewForm(forms.Form):
    # rating = forms.ChoiceField(queryset=Review.RATING_CHOICES)
    rating = forms.ChoiceField()
    comment = forms.CharField()
