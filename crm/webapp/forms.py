from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record



# - Update a record

class RecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['nom_client', 'prenom_client', 'num_tel_client', 'NIF', 'NIS', 'Art', 'RC']





class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['reference_produit', 'poids_produit', 'origine_produit', 'purete_produit','quantite']
        


class FourForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom_fournisseur','adresse_fournisseur','tel_fournisseur']


class MagasinForm(forms.ModelForm):
    class Meta:
        model = Magasin
        fields = ['nom_magasin', 'num_tel_magasin', 'adresse_magasin']


class TransformationForm(forms.ModelForm):
    class Meta:
        model = Transforma
        fields = [
            'date_transformation', 
            'cout_estime', 
            'cout_reel', 
            'produit', 
            'nb_unitaire_transformer_initial', 
            'nb_unitaire_transformer_final'
        ]
        
class AtelierForm(forms.ModelForm):
    class Meta:
        model = Atelier
        fields = ['nom_atelier', 'adresse_atelier', 'produit', 'transformation']
        
        
class FactureVenteForm(forms.ModelForm):
    class Meta:
        model = FactureVente
        fields = ['date_facture_vente', 'montant_total_vente_TTC', 'statut_facture']
        
        
class FactureAchatForm(forms.ModelForm):
    class Meta:
        model = FactureAchat
        fields = ['date_facture_achat', 'montant_total_achat_TTC']
        
        
class BijoutierForm(forms.ModelForm):
    class Meta:
        model = Bijoutier
        fields = ['nom_bijoutier', 'email_bijoutier', 'mot_de_pass_bijoutier', 'adresse_bijoutier', 'tel_bijoutier', 'atelier', 'magasin']
        
        
        
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['date_commande', 'bijoutier', 'facture_vente']