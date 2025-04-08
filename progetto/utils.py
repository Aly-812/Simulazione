import requests

def scarica_dati(url):
    """Questa funzione scarica il contenuto di un URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Solleva un'eccezione per codici di stato HTTP errati
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta a {url}: {e}")
        return None

def formatta_stringa(testo):
    """
    Questa funzione dovrebbe prendere una stringa e restituire la stessa stringa
    con la prima lettera di ogni parola in maiuscolo.
    """
    # TODO: Implementare la formattazione della stringa
    pass
