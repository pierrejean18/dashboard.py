import streamlit as st
import numpy as np
import math

st.title('Outils pour coach d\'aviron')

tab1, tab2, tab3 = st.tabs(["ratio pelle aviron", "calcul pourcentage","convertisseur watt/500"])

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

with tab2:
    # Définition des records par catégorie et sexe
    records = {
        "J14": {
            "Homme": {
                "4x+": "6:30",
                "8x+": "5:57",
            },
            "Femme": {
                "4x+": "6:30",
                "8x+": "5:57",
            },
            "Mixte": {
                "2x": "6:30",
                "4x+": "5:57",
            },
        },
        "J16": {
            "Homme": {
                "1x": "6:30",
                "2x": "5:57",
                "4x": "5:30",
                "2-": "6:08",
                "4+": "5:49",
                "8+": "5:17"
            },
            "Femme": {
                "1x": "6:30",
                "2x": "5:57",
                "4x": "5:30",
                "2-": "6:08",
                "4+": "5:49",
                "8+": "5:17"
            },
            "Mixte": {
                "4x": "5:30",
            },
        },
        "J18": {
            "Homme": {
                "1x": "6:30",
                "2x": "5:57",
                "4x": "5:30",
                "2-": "6:08",
                "4-": "5:49",
                "8+": "5:17"
            },
            "Femme": {
                "1x": "6:30",
                "2x": "5:57",
                "4x": "5:30",
                "2-": "6:08",
                "4-": "5:49",
                "8+": "5:17"
            },"Mixte": {
                "4x": "5:30",
            },
        },
        "Senior": {
            "Mixte": {
                "2x": "6:30",
                "4x": "5:57",
                "8+": "5:57"
            },
            "Homme": {
                "Toutes Catégories": {
                    "1x": "6:30",
                    "2x": "5:57",
                    "4x": "5:30",
                    "2-": "6:08",
                    "4-": "5:36",
                    "4+": "5:49",
                    "8+": "5:17"
                },
                "Poids Léger": {
                    "1x": "6:38",
                    "2x": "6:04",
                    "4x": "5:37"
                }
            },
            "Femme": {
                "Toutes Catégories": {
                    "1x": "7:05",
                    "2x": "6:34",
                    "4x": "6:05",
                    "2-": "6:47",
                    "4-": "6:12",
                    "4+": "6:29",
                    "8+": "5:51"
                },
                "Poids Léger": {
                    "1x": "7:22",
                    "2x": "6:40",
                    "4x": "6:12"
                }
            }
        }
    }

    # Fonction pour convertir un temps en secondes
    def temps_en_secondes(temps):
        minutes, secondes = map(int, temps.split(':'))
        return minutes * 60 + secondes

    # Fonction pour calculer le pourcentage par rapport au record
    def calcul_pourcentage(temps_rameur, temps_record):
        temps_rameur_sec = temps_en_secondes(temps_rameur)
        temps_record_sec = temps_en_secondes(temps_record)
        pourcentage = (temps_record_sec / temps_rameur_sec) * 100
        return pourcentage

    # Titre de l'application
    st.title("Calcul de pourcentage par rapport au record du monde")

    # Sélection de la catégorie d'âge
    categorie_age = st.selectbox("Choisissez une catégorie d'âge", list(records.keys()))

    # Sélection du sexe
    sexe = st.selectbox("Choisissez le sexe", list(records[categorie_age].keys()))

    # Si Senior est sélectionné, permettre le choix du type de poids
    if categorie_age == "Senior" and sexe != "Mixte":
        categorie_poids = st.selectbox("Choisissez la catégorie de poids", list(records[categorie_age][sexe].keys()))
        categorie = st.selectbox("Choisissez la catégorie", list(records[categorie_age][sexe][categorie_poids].keys()))
        temps_record = records[categorie_age][sexe][categorie_poids][categorie]
    else:
        categorie = st.selectbox("Choisissez la catégorie", list(records[categorie_age][sexe].keys()))
        temps_record = records[categorie_age][sexe][categorie]

    # Entrée du temps du rameur
    st.title('veuillez entrer le temps de la pige')
    temps_rameur = st.text_input("Entrez le temps du rameur (ex: 8:00)")

    # Calcul et affichage du pourcentage
    if st.button("Calculer"):
        if temps_rameur:
            try:
                pourcentage = calcul_pourcentage(temps_rameur, temps_record)
                if categorie_age == "Senior" and sexe != "Mixte":
                    st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie_age} {categorie_poids} {categorie} est de : {pourcentage:.2f}%")
                else:
                    st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie_age} {categorie} est de : {pourcentage:.2f}%")
            except ValueError:
                st.error("Veuillez entrer un temps valide au format MM:SS.")
        else:
            st.error("Veuillez entrer un temps.")

with tab3:
        # Sélectionner le mode de calcul
    mode = st.selectbox("Choisissez le mode de calcul", ["Calculer le temps pour 500 mètres à partir des watts", "Calculer les watts à partir du temps pour 500 mètres"])

    if mode == "Calculer le temps pour 500 mètres à partir des watts":
        # Entrée utilisateur pour les watts
        watts = st.number_input('Entrez la puissance (watts)', value=203, min_value=1, step=1)
        
        # Calcul du temps pour parcourir 500 mètres
        pace = (2.80 / watts) ** (1/3)
        time_seconds = 500 * pace
        
        # Conversion en format minutes:secondes.dixièmes
        minutes = int(time_seconds // 60)
        seconds = int(time_seconds % 60)
        tenths = int((time_seconds - int(time_seconds)) * 10)
        
        # Affichage du résultat
        st.write(f"Avec une puissance de {watts} watts, le temps pour parcourir 500 mètres est de {minutes} minutes, {seconds} secondes et {tenths} dixièmes.")
        
    else:
        # Entrée utilisateur pour le temps en minutes, secondes et dixièmes
        minutes = st.number_input('Entrez les minutes', value=2, min_value=0, format="%d")
        seconds = st.number_input('Entrez les secondes', value=5, min_value=0, max_value=59, format="%d")
        tenths = st.number_input('Entrez les dixièmes de seconde', value=0, min_value=0, max_value=9, format="%d")
        
        # Calcul du temps total en secondes avec les dixièmes
        time_seconds = minutes * 60 + seconds + tenths / 10
        
        # Calcul du rythme (pace) en secondes/mètre
        pace = time_seconds / 500
        
        # Calcul des watts
        watts = math.ceil(2.80 / (pace ** 3))  # Arrondi vers le haut pour obtenir un entier
        
        # Affichage du résultat
        st.write(f"Avec un temps de {minutes} minutes, {seconds} secondes et {tenths} dixièmes pour parcourir 500 mètres, la puissance calculée est de {watts} watts.")
