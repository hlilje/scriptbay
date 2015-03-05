from django import forms

from scripts.models import Review


class ReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=Review.RATING_CHOICES)
    comment = forms.CharField()
