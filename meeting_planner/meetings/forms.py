from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, NumberInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'time': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number"})
        }

    def clean_date(self):
        d = self.cleaned_data.get('date')
        if d < date.today():
            raise ValidationError("Past date not valid")
        return d
