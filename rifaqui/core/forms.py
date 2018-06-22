from django import forms

from .models import Raffle


class RaffleModelForm(forms.ModelForm):
    class Meta:
        model = Raffle
        exclude = [id, ]

    def clean(self):
        numbers = self.cleaned_data.get('numbers')
        initial_number = self.cleaned_data.get('initial_number')
        if (numbers - initial_number) > 1000:
            raise forms.ValidationError("A quantidade máxima de números é de 1000.")
        return self.cleaned_data
