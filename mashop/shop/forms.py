from django import forms

from .models import ProductsReviews


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = ProductsReviews
        fields = ['photo', 'review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'cols': 50, 'rows': 8, 'resize': None})
        }
