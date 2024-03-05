import streamlit as st

# Dummy Daten für Vorlesungen
vorlesungen = [
    {"Titel": "Einführung in die Informatik", "Beschreibung": "Grundlegende Konzepte der Informatik", "Themen": ["Informatik", "Programmierung"]},
    {"Titel": "Lineare Algebra", "Beschreibung": "Grundlagen der linearen Algebra", "Themen": ["Mathematik", "Algebra"]},
    {"Titel": "Geschichte der Kunst", "Beschreibung": "Entwicklung der Kunst durch die Geschichte", "Themen": ["Kunst", "Geschichte"]},
    {"Titel": "Einführung in die Psychologie", "Beschreibung": "Grundlagen der Psychologie", "Themen": ["Psychologie", "Sozialwissenschaften"]}
]

# Funktion zum Filtern von Vorlesungen basierend auf den Interessen des Benutzers
def filter_vorlesungen(interessen):
    gefilterte_vorlesungen = []
    for vorlesung in vorlesungen:
        if any(interest in vorlesung["Themen"] for interest in interessen):
            gefilterte_vorlesungen.append(vorlesung)
    return gefilterte_vorlesungen

# Streamlit App
def main():
    st.title("Vorlesungsfinder")

    # Benutzereingabe für Interessen
    interessen = st.multiselect("Wählen Sie Ihre Interessen aus:", ["Informatik", "Mathematik", "Kunst", "Psychologie"])

    # Filtern von Vorlesungen basierend auf den Interessen
    gefilterte_vorlesungen = filter_vorlesungen(interessen)

    # Anzeigen der gefilterten Vorlesungen
    st.subheader("Gefilterte Vorlesungen:")
    if gefilterte_vorlesungen:
        for vorlesung in gefilterte_vorlesungen:
            st.write(f"**{vorlesung['Titel']}**")
            st.write(f"*Beschreibung:* {vorlesung['Beschreibung']}")
            st.write(f"*Themen:* {', '.join(vorlesung['Themen'])}")
            st.write("---")
    else:
        st.write("Keine Vorlesungen gefunden.")

if __name__ == "__main__":
    main()

