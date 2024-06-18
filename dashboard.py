import streamlit as st
import numpy as np

st.title('Outils pour coach d\'aviron')

st.sidebar.image("tours_logo.svg", width=100)

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


# Deuxième onglet
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
    temps_rameur = st.text_input("Entrez le temps du rameur (ex: 8:00)")

    # Calcul et affichage du pourcentage
    if st.button("Calculer"):
        if temps_rameur:
            try:
                pourcentage = calcul_pourcentage(temps_rameur, temps_record)
                st.write(f"Le pourcentage par rapport au record du monde pour la catégorie {categorie} est de : {pourcentage:.2f}%")
            except ValueError:
                st.error("Veuillez entrer un temps valide au format MM:SS.")
        else:
            st.error("Veuillez entrer un temps.")
