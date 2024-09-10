import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import MediaForm, MemberForm, Creationjeudeplateau, Empruntform
from .models import Media, JeuDePlateau, Member
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages


def connexion(request):
    if request.method == 'POST':
        username = request.POST['utilisateur']
        password = request.POST['motdepasse']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            logging.debug('Connexion réussie.')
            login(request, user)
            return render(request, 'employe/acces.html')
        else:
            logging.warning('Connexion échouée.')
            messages.error(request, 'Identifiant ou mot de passe incorrect')

    return render(request, 'employe/connexion.html')

def acces(request):
    return render(request, 'employe/acces.html')

def creermembre(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listemembre')
    else:
        form = MemberForm()
    return render(request, 'employe/creermembre.html', {'form': form})

def listemembre(request):
    members = Member.objects.all()
    return render(request, 'employe/listemembre.html', {'members': members})

def modifiermembre(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('listemembre')
    else:
        form = MemberForm(instance=member)
    return render(request, 'employe/modifiermembre.html', {'form': form})

def supprimermembre(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect('listemembre')
    return render(request, 'employe/supprimermembre.html', {'member': member})

def listemedia(request):
    medias = Media.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()  # Récupération des jeux de plateau
    return render(request, 'employe/listemedia.html', {
        'medias': medias,
        'jeux_de_plateau': jeux_de_plateau,  # Passage des jeux de plateau au template
    })

def ajoutmedia(request):
    if request.method == 'POST':
        media_form = MediaForm(request.POST)
        jeu_form = Creationjeudeplateau(request.POST)

        if media_form.is_valid():
            logging.debug('Le média est valide.')
            media_form.save()
            return redirect('listemedia')

        if jeu_form.is_valid():
            jeu_form.save()
            return redirect('listemedia')
    else:
        logging.warning('Le média est invalide.')
        media_form = MediaForm()
        jeu_form = Creationjeudeplateau()

    return render(request, 'employe/ajoutmedia.html', {
        'media_form': media_form,
        'jeu_form': jeu_form,
    })

def empruntmedia(request):
    if request.method == 'POST':
        logging.debug('Requête POST reçue pour créer un emprunt.')
        form = Empruntform(request.POST)
        if form.is_valid():
            logging.debug('Formulaire pour emprunt valide.')
            emprunt = form.save(commit=False)

            if not emprunt.membre:
                logging.warning('Aucun membre sélectionné pour l\'emprunt.')
                messages.error(request, "Aucun membre sélectionné pour l'emprunt.")
                return redirect('empruntmedia')

            membre = emprunt.membre

            emprunts_retard = membre.emprunt_set.filter(date_retour__isnull=True,
                                                        date_emprunt__lt=timezone.now() - timedelta(days=7))
            if emprunts_retard.exists():
                logging.warning('Cet utilisateur a des retards.')
                messages.error(request, "Ce membre a un ou plusieurs retards.")
                return redirect('empruntmedia')

            if membre.emprunt_set.filter(date_retour__isnull=True).count() >= 3:
                logging.warning('Cet utilisateur a déjà 3 emprunts.')
                messages.error(request, "Ce membre a déjà 3 emprunts actifs.")
                return redirect('empruntmedia')

            emprunt.date_retour = emprunt.date_emprunt + timedelta(days=7)

            media = emprunt.media
            media.disponible = False
            media.save()
            emprunt.save()

            logging.info('Emprunt créé avec succès.')
            messages.success(request, 'Emprunt validé.')
            return redirect('listemembre')
    else:
        form = Empruntform()

    return render(request, 'employe/empruntmedia.html', {'form': form})
