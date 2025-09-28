from django import forms
from .models import WasteReport

class WasteReportForm(forms.ModelForm):
    class Meta:
        model = WasteReport
        fields = ['description', 'image']
