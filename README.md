# Quantum Matrix (24 Cellen) ⚛️

Dit project is een interactieve datavisualisatie die de overgang van een klassieke waarheidstabel naar een dynamisch quantum-systeem demonstreert. Het model combineert 8 logische regels met de 3 ruimtelijke dimensies van een quantumspin (via de Pauli-spinmatrices), wat resulteert in een matrix van exact 24 cellen.

## 🚀 Kenmerken

- **Standalone Vue 3 applicatie**: Geen complexe build-omgeving of Node.js nodig. Werkt direct in de browser.
- **Interactieve Statussen**: Schakel vloeiend tussen Klassieke logica, Superpositie en Quantumverstrengeling.
- **Visuele Feedback**: Cellen die hun waarde verliezen door superpositie of verstrengeling worden automatisch gedimd.

## 🛠️ Gebruik (Installatie)

Aangezien het project is geschreven als een standalone HTML-bestand met een Vue 3 CDN, is de installatie uiterst eenvoudig:

1. Kopieer de broncode en sla deze op als `index.html`.
2. Dubbelklik op het bestand om het te openen in een moderne webbrowser (Chrome, Firefox, Safari, Edge).
3. Gebruik de knoppen om de transformatie van de data te observeren.

## 🧠 Theoretisch Kader

Het dashboard toont de transformatie van informatie aan de hand van drie fundamentele toestanden:

### 1. Klassiek (Z-as Dominant)
In de klassieke staat fungeren de 8 regels als normale bits. De waarden bevinden zich uitsluitend op de **Z-as** ($1$ voor 'True' / Spin-up, en $-1$ voor 'False' / Spin-down). De X-as en Y-as zijn in deze status exact nul.

### 2. Hadamard (Superpositie)
Wanneer we een Hadamard-poort (een quantum-operator) over de regels heen halen, worden de deeltjes in een perfecte superpositie gebracht. De data verschuift direct van de meetbare Z-as naar de **X-as**. De deeltjes zijn niet langer vastgepind op uitsluitend 0 of 1, maar zweven ertussenin
