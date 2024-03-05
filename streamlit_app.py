import streamlit as st
import pandas as pd

# Dummy-Daten für Module
modules_data = {
    "Modulnummer": ["CS101", "MATH202", "ENG303"],
    "Modulname": ["Einführung in die Informatik", "Lineare Algebra", "Fortgeschrittene englische Grammatik"],
    "Dozent": ["Prof. Müller", "Dr. Schmidt", "Prof. Meier"]
}

# Dummy-Daten für Bewertungen
reviews_data = {
    "Modulnummer": ["CS101", "MATH202", "ENG303"],
    "Bewertung": [4.5, 3.8, 4.2],
    "Kommentar": ["Toller Kurs!", "Gute Lehrmaterialien, aber schwierige Prüfungen.", "Interessante Vorlesungen."]
}

modules_df = pd.DataFrame(modules_data)
reviews_df = pd.DataFrame(reviews_data)

def main():
    st.title("Modulbewertungs-App")

    page = st.sidebar.selectbox("Seite auswählen", ["Modulbewertungen", "Bewertung abgeben"])

    if page == "Modulbewertungen":
        st.header("Modulbewertungen")
        selected_module = st.selectbox("Modul auswählen", modules_df["Modulname"])
        module_reviews = reviews_df[reviews_df["Modulnummer"] == modules_df.loc[modules_df["Modulname"] == selected_module, "Modulnummer"].values[0]]
        
        if not module_reviews.empty:
            st.subheader(f"Bewertungen für {selected_module}:")
            st.write(module_reviews)
        else:
            st.write("Keine Bewertungen für dieses Modul vorhanden.")

    elif page == "Bewertung abgeben":
        st.header("Bewertung abgeben")
        selected_module = st.selectbox("Modul auswählen", modules_df["Modulname"])
        rating = st.slider("Bewertung (1-5)", 1, 5)
        comment = st.text_area("Kommentar")
        submit_button = st.button("Bewertung absenden")

        if submit_button:
            module_number = modules_df.loc[modules_df["Modulname"] == selected_module, "Modulnummer"].values[0]
            new_review = pd.DataFrame({"Modulnummer": [module_number], "Bewertung": [rating], "Kommentar": [comment]})
            reviews_df = reviews_df.append(new_review, ignore_index=True)
            st.success("Vielen Dank für Ihre Bewertung!")

if __name__ == "__main__":
    main()




