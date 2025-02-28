from DefGenerazione import generadati

def menu():
    condizione = True
    while condizione:

        print("MENU")
        print("1. Genera i dati")
        print("2. Analizza i dati")
        print("3. Visualizza il grafico relativo ai dati ")
        print("4. Visulizza i risultati del processo di machine learning")
        print("5. Stop")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            generadati()
        elif scelta=="2":
            pass
        elif scelta=="3":
            pass
        elif scelta=="4":
            pass
        elif scelta=="5":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Inserisci un numero tra 1 e 5.")
            
menu()  
