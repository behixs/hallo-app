import streamlit as st

def main():
    st.title("Begrüßungs-App")
    
    # Eingabefeld für den Namen des Benutzers
    name = st.text_input("Gib deinen Namen ein:")
    
    # Überprüfen, ob der Benutzer einen Namen eingegeben hat
    if name:
        st.write(f"Hallo, {name}! Willkommen zur interaktiven Streamlit-App.")
    else:
        st.write("Bitte gib deinen Namen ein.")

if __name__ == "__main__":
    main()



