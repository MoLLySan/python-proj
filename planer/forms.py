import django.forms as forms

from planer.models import Meeting


class CreationForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'title',
            'date',
            'start_time',
            'end_time',
            'room'
        ]