Predikcija kategorije proizvoda (ML projekat)

Opis
Ovaj projekat koristi mašinsko učenje za automatsku predikciju kategorije proizvoda na osnovu njegovog naziva.

Cilj je da se olakša i ubrza klasifikacija proizvoda u e-commerce sistemima bez ručnog rada.

Cilj projekta

Automatska klasifikacija proizvoda
Brže i preciznije označavanje kategorija
Poboljšanje korisničkog iskustva pretrage

Podaci
Dataset sadrži proizvode sa sledećim informacijama:

naziv proizvoda (Product Title)
kategorija (Category Label)
dodatni meta podaci (Merchant, views, rating, itd.)

Kako radi model
Ulaz: naziv proizvoda
TF-IDF pretvaranje teksta u brojeve
ML model (Logistic Regression / SVM)
Izlaz: predikcija kategorije
Korišćeni modeli

Testirani su:

Logistic Regression
Naive Bayes
Decision Tree
Random Forest
SVM (LinearSVC)

Najbolji model: SVM (LinearSVC)

Primer predikcije
iphone 7 32gb → Mobile Phones
bosch wap28390gb → Washing Machines
kenwood k20mss15 → Microwaves

Pokretanje projekta
Treniranje modela
python train_model.py
Predikcija
python predict_category.py

Struktura projekta
project/
│
├── data/
│   └── products.csv
├── models/
│   └── model.pkl
├── notebook/
│   └── 01_product_category_classification.ipynb
├── src
│    └── train_model.py
│    └── predict_category.py
└── README.md
└── requirements.txt

Napomena

Model radi samo na osnovu naziva proizvoda i može imati manja odstupanja kod sličnih kategorija.

Autor 
Bojan Rajić
