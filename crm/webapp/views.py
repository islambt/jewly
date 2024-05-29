from django.shortcuts import render, redirect
from .forms import *

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import *

from django.contrib import messages



# - Homepage 

def home(request):

    return render(request, 'webapp/index.html')


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/table/dashboard.html', context=context)

@login_required(login_url='my-login')
def produit(request):

    my_product = Produit.objects.all()

    context = {'products': my_product}

    return render(request, 'webapp/table/produit.html', context=context)

# - Create a record 

@login_required(login_url='my-login')
def four(request):

    my_four = Fournisseur.objects.all()

    context = {'four': my_four}

    return render(request, 'webapp/table/fournisseur.html', context=context)

@login_required(login_url='my-login')
def magasin(request):

    my_maga = Magasin.objects.all()

    context = {'magasin': my_maga}

    return render(request, 'webapp/table/magasin.html', context=context)


@login_required(login_url='my-login')
def create_record(request):

    form = RecordForm()

    if request.method == "POST":

        form = RecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create/create-record.html', context=context)

@login_required(login_url='my-login')
def create_produit(request):

    form = ProduitForm()

    if request.method == "POST":

        form = ProduitForm(request.POST)
        
        if form.is_valid():
            # Obtenez le nom du produit à partir du formulaire
            
            form.save()
             
            
            messages.success(request, "Votre produit a été créé!")

            return redirect("produit")

    context = {'form': form}

    return render(request, 'webapp/create/create-produit.html', context=context)
# - Update a record 



@login_required(login_url='my-login')
def create_four(request):

    form = FourForm()

    if request.method == "POST":

        form = FourForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Votre fournisseur a était crée avec succées!")

            return redirect("four")

    context = {'form': form}

    return render(request, 'webapp/create/create-four.html', context=context)
# - Update a record 

@login_required(login_url='my-login')
def create_magasin(request):

    form = MagasinForm()

    if request.method == "POST":

        form = MagasinForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your product was created!")

            return redirect("magasin")

    context = {'form': form}

    return render(request, 'webapp/create/create-magasin.html', context=context)
# - Update a record 


@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = RecordForm(instance=record)

    if request.method == 'POST':

        form = RecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Le client a était modifié avec succées!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-record.html', context=context)

login_required(login_url='my-login')
def update_produit(request, pk):

    produit = Produit.objects.get(id=pk)

    form = ProduitForm(instance=produit)

    if request.method == 'POST':

        form = ProduitForm(request.POST, instance=produit)

        if form.is_valid():

            form.save()

            messages.success(request, "Your product was updated!")

            return redirect("produit")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-produit.html', context=context)


# - Read / View a singular record

login_required(login_url='my-login')
def update_four(request, pk):

    four = Fournisseur.objects.get(id=pk)

    form = FourForm(instance=four)

    if request.method == 'POST':

        form = FourForm(request.POST, instance=four)

        if form.is_valid():

            form.save()

            messages.success(request, "Le fournisseur a était modifier avec succées !")

            return redirect("four")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-four.html', context=context)

@login_required(login_url='my-login')
def update_magasin(request, pk):

    maga = Magasin.objects.get(id=pk)

    form = MagasinForm(instance=maga)

    if request.method == 'POST':

        form = MagasinForm(request.POST, instance=maga)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("magasin")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-magasin.html', context=context)


@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view/view-record.html', context=context)

@login_required(login_url='my-login')
def singular_produit(request, pk):

    all_produit = Produit.objects.get(id=pk)

    context = {'produit':all_produit}

    return render(request, 'webapp/view/view-produit.html', context=context)
# - Delete a record

@login_required(login_url='my-login')
def singular_four(request, pk):

    all_four = Fournisseur.objects.get(id=pk)

    context = {'four':all_four}

    return render(request, 'webapp/view/view-four.html', context=context)
# - Delete a record

@login_required(login_url='my-login')
def singular_magasin(request, pk):

    all_records = Magasin.objects.get(id=pk)

    context = {'magasin':all_records}

    return render(request, 'webapp/view/view-magasin.html', context=context)


@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Le client a était supprimé avec succées!")

    return redirect("dashboard")

@login_required(login_url='my-login')
def delete_produit(request, pk):

    product = Produit.objects.get(id=pk)
    my_product = Produit.objects.all()
    for p in my_product:
        if p.reference_produit==product.reference_produit:
            p.quantite=-1
    product.delete()
    
    messages.success(request, "Le produit a était supprimé avec succées!")

    return redirect("produit")

@login_required(login_url='my-login')
def delete_four(request, pk):

    four = Fournisseur.objects.get(id=pk)

    four.delete()

    messages.success(request, "Le fournisseur a était supprimé avec succées !")

    return redirect("four")

@login_required(login_url='my-login')
def delete_magasin(request, pk):

    maga = Magasin.objects.get(id=pk)

    maga.delete()

    messages.success(request, "Le magasin a était supprimé avec succées !")

    return redirect("magasin")

# - User logout






@login_required(login_url='my-login')
def transformation(request):

    my_maga = Transforma.objects.all()

    context = {'transformations': my_maga}

    return render(request, 'webapp/table/transformation.html', context=context)




@login_required(login_url='my-login')
def create_transformation(request):

    form = TransformationForm()

    if request.method == "POST":

        form = TransformationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Transformation ajouté!")

            return redirect("transformation")

    context = {'form': form}

    return render(request, 'webapp/create/create-transformation.html', context=context)
# - Update a record 


@login_required(login_url='my-login')
def update_transformation(request, pk):

    transfo = Transforma.objects.get(id=pk)

    form = TransformationForm(instance=transfo)

    if request.method == 'POST':

        form = TransformationForm(request.POST, instance=transfo)

        if form.is_valid():

            form.save()

            messages.success(request, "Transformation modifié")

            return redirect("transformation")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-transformation.html', context=context)


@login_required(login_url='my-login')
def singular_transformation(request, pk):

    all_records = Transforma.objects.get(id=pk)

    context = {'transformation':all_records}

    return render(request, 'webapp/view/view-transformation.html', context=context)


@login_required(login_url='my-login')
def delete_transformation(request, pk):

    transfo = Transforma.objects.get(id=pk)

    transfo.delete()

    messages.success(request, "La transformation a était supprimé avec succées !")

    return redirect("transformation")


@login_required(login_url='my-login')
def atelier(request):

    my_maga = Atelier.objects.all()

    context = {'ateliers': my_maga}

    return render(request, 'webapp/table/atelier.html', context=context)




@login_required(login_url='my-login')
def create_atelier(request):

    form = AtelierForm()

    if request.method == "POST":

        form = AtelierForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "atelier ajouté!")

            return redirect("atelier")

    context = {'form': form}

    return render(request, 'webapp/create/create-atelier.html', context=context)
# - Update a record 


@login_required(login_url='my-login')
def update_atelier(request, pk):

    transfo = Atelier.objects.get(id=pk)

    form = AtelierForm(instance=transfo)

    if request.method == 'POST':

        form = AtelierForm(request.POST, instance=transfo)

        if form.is_valid():

            form.save()

            messages.success(request, "atelier modifié")

            return redirect("atelier")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-atelier.html', context=context)


@login_required(login_url='my-login')
def singular_atelier(request, pk):

    all_records = Atelier.objects.get(id=pk)

    context = {'atelier':all_records}

    return render(request, 'webapp/view/view-atelier.html', context=context)


@login_required(login_url='my-login')
def delete_atelier(request, pk):

    transfo = Atelier.objects.get(id=pk)

    transfo.delete()

    messages.success(request, "L'atelier a était supprimé avec succées !")

    return redirect("atelier")





@login_required(login_url='my-login')
def facturevente(request):

    my_maga = FactureVente.objects.all()

    context = {'factures': my_maga}

    return render(request, 'webapp/table/facturevente.html', context=context)




@login_required(login_url='my-login')
def create_facturevente(request):

    form = FactureVenteForm()

    if request.method == "POST":

        form = FactureVenteForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "facture ajouté!")

            return redirect("facturevente")

    context = {'form': form}

    return render(request, 'webapp/create/create-facturevente.html', context=context)
# - Update a record 


@login_required(login_url='my-login')
def update_facturevente(request, pk):

    transfo = FactureVente.objects.get(id=pk)

    form = FactureVenteForm(instance=transfo)

    if request.method == 'POST':

        form = FactureVenteForm(request.POST, instance=transfo)

        if form.is_valid():

            form.save()

            messages.success(request, "facture modifié")

            return redirect("facturevente")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-facturevente.html', context=context)


@login_required(login_url='my-login')
def singular_facturevente(request, pk):

    all_records = FactureVente.objects.get(id=pk)

    context = {'facture':all_records}

    return render(request, 'webapp/view/view-facturevente.html', context=context)


@login_required(login_url='my-login')
def delete_facturevente(request, pk):

    transfo = FactureVente.objects.get(id=pk)

    transfo.delete()

    messages.success(request, "La facture a était supprimé avec succées !")

    return redirect("facturevente")




@login_required(login_url='my-login')
def factureachat(request):

    my_maga = FactureAchat.objects.all()

    context = {'factures': my_maga}

    return render(request, 'webapp/table/factureachat.html', context=context)




@login_required(login_url='my-login')
def create_factureachat(request):

    form = FactureAchatForm()

    if request.method == "POST":

        form = FactureAchatForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "facture ajouté!")

            return redirect("factureachat")

    context = {'form': form}

    return render(request, 'webapp/create/create-factureachat.html', context=context)
# - Update a record 


@login_required(login_url='my-login')
def update_factureachat(request, pk):

    transfo = FactureAchat.objects.get(id=pk)

    form = FactureAchatForm(instance=transfo)

    if request.method == 'POST':

        form = FactureAchatForm(request.POST, instance=transfo)

        if form.is_valid():

            form.save()

            messages.success(request, "facture modifié")

            return redirect("factureachat")
        
    context = {'form':form}

    return render(request, 'webapp/update/update-factureachat.html', context=context)


@login_required(login_url='my-login')
def singular_factureachat(request, pk):

    all_records = FactureAchat.objects.get(id=pk)

    context = {'facture':all_records}

    return render(request, 'webapp/view/view-factureachat.html', context=context)


@login_required(login_url='my-login')
def delete_factureachat(request, pk):

    transfo = FactureAchat.objects.get(id=pk)

    transfo.delete()

    messages.success(request, "La facture a était supprimé avec succées !")

    return redirect("factureachat")




def bijoutier(request):
    my_maga = Bijoutier.objects.all()
    context = {'bijoutiers': my_maga}
    return render(request, 'webapp/table/bijoutier.html', context=context)

@login_required(login_url='my-login')
def create_bijoutier(request):
    form = BijoutierForm()
    if request.method == "POST":
        form = BijoutierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bijoutier ajouté!")
            return redirect("bijoutier")
    context = {'form': form}
    return render(request, 'webapp/create/create-bijoutier.html', context=context)

@login_required(login_url='my-login')
def update_bijoutier(request, pk):
    transfo = Bijoutier.objects.get(id=pk)
    form = BijoutierForm(instance=transfo)
    if request.method == 'POST':
        form = BijoutierForm(request.POST, instance=transfo)
        if form.is_valid():
            form.save()
            messages.success(request, "Bijoutier modifié")
            return redirect("bijoutier")
    context = {'form':form}
    return render(request, 'webapp/update/update-bijoutier.html', context=context)

@login_required(login_url='my-login')
def singular_bijoutier(request, pk):
    all_records = Bijoutier.objects.get(id=pk)
    context = {'bijoutier':all_records}
    return render(request, 'webapp/view/view-bijoutier.html', context=context)

@login_required(login_url='my-login')
def delete_bijoutier(request, pk):
    transfo = Bijoutier.objects.get(id=pk)
    transfo.delete()
    messages.success(request, "Le bijoutier a été supprimé avec succès!")
    return redirect("bijoutier")



def commande(request):
    my_maga = Commande.objects.all()
    context = {'commandes': my_maga}
    return render(request, 'webapp/table/commande.html', context=context)

@login_required(login_url='my-login')
def create_commande(request):
    form = CommandeForm()
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Commande ajoutée!")
            return redirect("commande")
    context = {'form': form}
    return render(request, 'webapp/create/create-commande.html', context=context)

@login_required(login_url='my-login')
def update_commande(request, pk):
    transfo = Commande.objects.get(id=pk)
    form = CommandeForm(instance=transfo)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=transfo)
        if form.is_valid():
            form.save()
            messages.success(request, "Commande modifiée")
            return redirect("commande")
    context = {'form':form}
    return render(request, 'webapp/update/update-commande.html', context=context)

@login_required(login_url='my-login')
def singular_commande(request, pk):
    all_records = Commande.objects.get(id=pk)
    context = {'commande':all_records}
    return render(request, 'webapp/view/view-commande.html', context=context)

@login_required(login_url='my-login')
def delete_commande(request, pk):
    transfo = Commande.objects.get(id=pk)
    transfo.delete()
    messages.success(request, "La commande a été supprimée avec succès!")
    return redirect("commande")


def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")



