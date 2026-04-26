import joblib

# učitavanje modela
model = joblib.load("models/model.pkl")

print("Pokrenuta predikcija (upiši 'exit' za izlaz)")

while True:
    text = input("Unesi naziv proizvoda: ").strip()

    if text.lower() == "exit":
        break

    if not text:
        print("Unos je prazan")
        continue

    # NEMA preprocessing-a ovde (važno!)
    pred = model.predict([text])[0]

    print("Kategorija:", pred)