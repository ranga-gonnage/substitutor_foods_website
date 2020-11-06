from django import forms


class InscriptionForm(forms.Form):
    """Inscription form"""

    name = forms.CharField(label="Nom", max_length=100)
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class ConnexionForm(forms.Form):
    """Inscription form"""

    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class SearchForm(forms.Form):
    """Search form"""

    search_input = forms.CharField(
        label="", widget=forms.TextInput(attrs={"class": "col-12"})
    )
