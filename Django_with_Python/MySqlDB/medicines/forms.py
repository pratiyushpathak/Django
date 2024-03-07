from django import forms
from .models import Medicines  # Corrected import

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = '__all__'
