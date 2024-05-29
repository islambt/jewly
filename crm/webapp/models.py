from datetime import timezone
from django.db import models

class Magasin(models.Model):
    nom_magasin = models.CharField(max_length=255)
    num_tel_magasin = models.CharField(max_length=20)
    adresse_magasin = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_magasin

class Record(models.Model):
    
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    num_tel_client = models.CharField(max_length=15)
    NIF = models.CharField(max_length=20, unique=True)
    NIS = models.CharField(max_length=20, unique=True)
    Art = models.CharField(max_length=20, unique=True)
    RC = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nom_client} {self.prenom_client}"

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

class Produit(models.Model):
    
    reference_produit = models.CharField(max_length=100)
    poids_produit = models.DecimalField(max_digits=10, decimal_places=2)
    origine_produit = models.CharField(max_length=100)
    purete_produit = models.DecimalField(max_digits=5, decimal_places=2)
    quantite = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.reference_produit} - {self.poids_produit}g - {self.origine_produit}"

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
    


class Fournisseur(models.Model):
    nom_fournisseur = models.CharField(max_length=255)
    adresse_fournisseur = models.CharField(max_length=255)
    tel_fournisseur = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nom_fournisseur


class Transforma(models.Model):
    
    date_transformation = models.DateField()
    cout_estime = models.DecimalField(max_digits=10, decimal_places=2)
    cout_reel = models.DecimalField(max_digits=10, decimal_places=2)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nb_unitaire_transformer_initial = models.IntegerField()
    nb_unitaire_transformer_final = models.IntegerField()

    def __str__(self):
        return f"{self.produit.reference_produit}"

class Atelier(models.Model):
    
    nom_atelier = models.CharField(max_length=255)
    adresse_atelier = models.CharField(max_length=255)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    transformation = models.ForeignKey(Transforma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_atelier


class FactureVente(models.Model):
    
    date_facture_vente = models.DateField()
    montant_total_vente_TTC = models.DecimalField(max_digits=10, decimal_places=2)
    statut_facture = models.CharField(max_length=50)

    def __str__(self):
        return f"Facture {self.id} - {self.statut_facture}"

class FactureAchat(models.Model):
    
    date_facture_achat = models.DateField()
    montant_total_achat_TTC = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Facture {self.id} - {self.statut_facture}"



class Bijoutier(models.Model):
   
    nom_bijoutier = models.CharField(max_length=255)
    email_bijoutier = models.EmailField()
    mot_de_pass_bijoutier = models.CharField(max_length=255)
    adresse_bijoutier = models.CharField(max_length=255)
    tel_bijoutier = models.CharField(max_length=20)
    atelier = models.ForeignKey(Atelier, on_delete=models.CASCADE)
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_bijoutier
    
    
class Commande(models.Model):
    date_commande = models.DateField()
    bijoutier = models.ForeignKey(Bijoutier, on_delete=models.CASCADE)
    facture_vente = models.ForeignKey(FactureVente, on_delete=models.CASCADE)
    def __str__(self):
        return f"Commande {self.id} - {self.bijoutier.nom_bijoutier}"