from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    # name = forms.CharField(max_length = 100)
    # picture = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('is_a_programmer', 'went_to_what_school')