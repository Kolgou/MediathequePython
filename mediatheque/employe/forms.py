from django import forms
from .models import Member, Media, JeuDePlateau, Emprunt

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nom', 'prenom']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'auteur', 'type', 'disponible']

class Creationjeudeplateau(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['nom', 'auteur', 'disponible']

class Empruntform(forms.ModelForm):
    membre = forms.ModelChoiceField(queryset=Member.objects.all())
    media = forms.ModelChoiceField(queryset=Media.objects.filter(disponible=True))

    class Meta:
        model = Emprunt
        fields = ['membre', 'media']