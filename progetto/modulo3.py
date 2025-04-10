import csv

def leggi_da_file(filepath):
    """Questa funzione legge dati da un file CSV e restituisce una lista di dizionari."""
    try:
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            dati = []
            for row in reader:
                # Conversione del campo 'attivo' da stringa a booleano
                row["attivo"] = row["attivo"].strip().lower() == "true"
                # Conversione del campo 'id' in intero (opzionale, se serve)
                row["id"] = int(row["id"])
                dati.append(row)
            return dati
    except FileNotFoundError:
        return None

def processa_dati(dati: list) -> list:
    """
    Filtra i dizionari che hanno 'attivo' == True e ritorna i loro 'id'.
    """
    lista_risultati = []

    for diz in dati:
        if diz["attivo"] == True:
            lista_risultati.append(diz["id"])
    
    return lista_risultati

if __name__ == "__main__":

    dati = leggi_da_file('dati/test.csv')
    if dati:
        risultati = processa_dati(dati)
        print(risultati)