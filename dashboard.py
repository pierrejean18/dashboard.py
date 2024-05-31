import streamlit as st
import numpy as np


st.title('Outils pour coach d\'aviron')

# Créer des onglets
tab1, tab2 = st.tabs(["ratio pelle aviron", "calcul pourcentage"])

# Premier onglet : Entrée de données
with tab1:

    # Créer des champs d'entrée de nombre
    nombre1 = st.number_input('Entrez la longueur de pelle', value=288)
    nombre2 = st.number_input('Entrez le levier intérieur', value=88)

    # Afficher les nombres entrés
    st.write(f'La longueur de pelle est de {nombre1}.')
    st.write(f'Le levier intérieur est de {nombre2}.')

    # Calculer le ratio des rames
    if nombre1 != 0:
        ratio = nombre2 / nombre1
        st.markdown(f'### **Le ratio des rames est de: {ratio:.4f}**', unsafe_allow_html=True)
    else:
        st.error("Erreur : La longueur de pelle ne peut pas être zéro pour calculer le ratio.")


#deuxième onglet
with tab2:


    # Définition des records du monde pour chaque catégorie Homme
    records_homme_TC = {
        "1XH TC": "6:30", 
        "2XH TC": "5:57",
        "4XH TC": "5:30",
        "2-H TC": "6:08",
        "4-H TC": "5:36",
        "4+H TC": "5:49",
        "8+H TC": "5:17"
    }

    # Définition des records du monde pour chaque catégorie Femme
    records_femme_TC = {
        "1XF TC": "7:05", 
        "2XF TC": "6:34",
        "4XF TC": "6:05",
        "2-F TC": "6:47",
        "4-F TC": "6:12",
        "4+F TC": "6:29",
        "8+F TC": "5:51"
    }

    # Définition des records du monde pour chaque catégorie Homme Poids Léger
    records_homme_PL = {
        "1XH PL": "6:38", 
        "2XH PL": "6:04",
        "4XH PL": "5:37"
    }

    # Définition des records du monde pour chaque catégorie Femme Poids Léger
    records_femme_PL = {
        "1XF PL": "7:22", 
        "2XF PL": "6:40",
        "4XF PL": "6:12"
    }

    # Dictionnaire regroupant les records du monde par sexe et catégorie de poids
    sexe = {
        "Homme": {"Toutes Catégories": records_homme_TC, "Poids Léger": records_homme_PL},
        "Femme": {"Toutes Catégories": records_femme_TC, "Poids Léger": records_femme_PL}
    }

    # Fonction pour convertir un temps en secondes
    def temps_en_secondes(temps):
        minutes, secondes = map(int, temps.split(':'))
        return minutes * 60 + secondes

    # Fonction pour calculer le pourcentage
    def calcul_pourcentage(temps_rameur, record_monde, sexe):
        temps_rameur_sec = temps_en_secondes(temps_rameur)
        record_monde_sec = temps_en_secondes(sexe[record_monde[0]][record_monde[1]][record_monde[2]])
        pourcentage = (record_monde_sec / temps_rameur_sec) * 100
        return pourcentage

    # Titre de l'application
    st.title("Calcul de pourcentage par rapport au record du monde")

    # Section pour choisir H ou F 
    st.header("Entrée de données")
    h_ou_f = st.selectbox("Sélectionner le sexe", list(sexe.keys()))

    # Section pour choisir la catégorie de poids
    categorie_poids = st.selectbox("Sélectionner la catégorie de poids", list(sexe[h_ou_f].keys()))

    # Section pour saisir le temps du rameur et sélectionner la catégorie
    st.header("Entrée de données")
    temps_rameur = st.text_input("Entrez le temps du rameur (8:00)")
    categorie = st.selectbox("Sélectionnez la catégorie", list(sexe[h_ou_f][categorie_poids].keys()))

    # Section pour afficher les résultats
    st.header("Résultats")
    if temps_rameur and categorie:
        pourcentage = calcul_pourcentage(temps_rameur, (h_ou_f, categorie_poids, categorie), sexe)
        st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie} est de : {pourcentage:.2f}%")
