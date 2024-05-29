
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),
    path('produit', views.produit, name="produit"),
    path('four', views.four, name="four"),
    path('magasin', views.magasin, name="magasin"),


    path('create-record', views.create_record, name="create-record"),
    path('create-produit', views.create_produit, name="create-produit"),
    path('create-four', views.create_four, name="create-four"),
    path('create-magasin', views.create_magasin, name="create-magasin"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('update-produit/<int:pk>', views.update_produit, name='update-produit'),
    path('update-four/<int:pk>', views.update_four, name='update-four'),
    path('update-magasin/<int:pk>', views.update_magasin, name='update-magasin'),

    path('record/<int:pk>', views.singular_record, name="record"),
    path('view-produit/<int:pk>', views.singular_produit, name="view-produit"),
    path('view-four/<int:pk>', views.singular_four, name="view-four"),
    path('view-magasin/<int:pk>', views.singular_magasin, name="view-magasin"),

    
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
    path('delete-produit/<int:pk>', views.delete_produit, name="delete-produit"),
    path('delete-four/<int:pk>', views.delete_four, name="delete-four"),
    path('delete-magasin/<int:pk>', views.delete_magasin, name="delete-magasin"),

    path('transformation', views.transformation, name="transformation"),
    path('create-transformation', views.create_transformation, name="create-transformation"),
    path('update-transformation/<int:pk>', views.update_transformation, name='update-transformation'),
    path('view-transformation/<int:pk>', views.singular_transformation, name="view-transformation"),
    path('delete-transformation/<int:pk>', views.delete_transformation, name="delete-transformation"),
    
    
    path('atelier', views.atelier, name="atelier"),
    path('create-atelier', views.create_atelier, name="create-atelier"),
    path('update-atelier/<int:pk>', views.update_atelier, name='update-atelier'),
    path('view-atelier/<int:pk>', views.singular_atelier, name="view-atelier"),
    path('delete-atelier/<int:pk>', views.delete_atelier, name="delete-atelier"),
    
    
    path('facturevente', views.facturevente, name="facturevente"),
    path('create-facturevente', views.create_facturevente, name="create-facturevente"),
    path('update-facturevente/<int:pk>', views.update_facturevente, name='update-facturevente'),
    path('view-facturevente/<int:pk>', views.singular_facturevente, name="view-facturevente"),
    path('delete-facturevente/<int:pk>', views.delete_facturevente, name="delete-facturevente"),


    path('factureachat', views.factureachat, name="factureachat"),
    path('create-factureachat', views.create_factureachat, name="create-factureachat"),
    path('update-factureachat/<int:pk>', views.update_factureachat, name='update-factureachat'),
    path('view-factureachat/<int:pk>', views.singular_factureachat, name="view-factureachat"),
    path('delete-factureachat/<int:pk>', views.delete_factureachat, name="delete-factureachat"),
    
    
    path('bijoutier', views.bijoutier, name="bijoutier"),
    path('create-bijoutier', views.create_bijoutier, name="create-bijoutier"),
    path('update-bijoutier/<int:pk>', views.update_bijoutier, name='update-bijoutier'),
    path('view-bijoutier/<int:pk>', views.singular_bijoutier, name="view-bijoutier"),
    path('delete-bijoutier/<int:pk>', views.delete_bijoutier, name="delete-bijoutier"),
    
    
    path('commande', views.commande, name="commande"),
    path('create-commande', views.create_commande, name="create-commande"),
    path('update-commande/<int:pk>', views.update_commande, name='update-commande'),
    path('view-commande/<int:pk>', views.singular_commande, name="view-commande"),
    path('delete-commande/<int:pk>', views.delete_commande, name="delete-commande"),
]






