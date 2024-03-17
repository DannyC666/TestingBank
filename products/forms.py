from django import forms
from .models import Client

class ClientSelectForm(forms.Form):
    client_id = forms.ModelChoiceField(queryset=Client.objects.all().order_by('id'), label="Select a client", empty_label="Choose...")