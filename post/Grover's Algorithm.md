# The Geometry of Quantum Search: Visualizing Grover's Algorithm for N=8

Deze referentie visualiseert de stappen van **Grover's Algoritme** voor een zoekruimte van $N=8$ elementen ($n=3$ qubits). Het toont hoe de quantumtoestand geometrisch roteert richting het gezochte element.

---

## De 6 Stappen van het Algoritme

### 1. Hadamard
* **Actie:** Creëer een uniforme superpositie ($H^{\otimes 3}$).
* **Geometrie:** De beginvector $|\psi_0\rangle$ start dicht bij de as van de ongemarkeerde elementen ($|\alpha\rangle$).

### 2. Oracle 1
* **Actie:** Pas de Oracle-operator ($U_f$) toe. 
* **Geometrie:** Dit draait het teken van het gemarkeerde element ($|\beta\rangle$) om. De vector spiegelt zich in de grafiek over de horizontale as.

### 3. Diffuser 1
* **Actie:** Pas de Diffuser-operator ($U_s$) toe.
* **Geometrie:** Dit veroorzaakt een spiegeling/rotatie rond de gemiddelde toestand $|\psi_0\rangle$. De vector roteert steil omhoog richting het gezochte element.

### 4. Summarize Iter 1
* **Actie:** Voltooiing van de eerste volledige iteratie (Oracle + Diffuser).
* **Geometrie:** Het netto-effect van iteratie 1 is een totale rotatie van $2\theta$ richting het gemarkeerde element $|\beta\rangle$.

### 5. Oracle 2
* **Actie:** Pas de Oracle-operator ($U_f$) voor de tweede keer toe.
* **Geometrie:** De vector wordt opnieuw gespiegeld, voorbereidend op de laatste rotatie.

### 6. Conv. & Meas. (Convergentie & Meting)
* **Actie:** Pas de Diffuser ($U_s$) toe en voer een meting uit.
* **Geometrie:** De toestand convergeert vrijwel volledig met de verticale as $|\beta\rangle$. Een meting levert nu met zeer hoge waarschijnlijkheid het juiste element op.

---

## Integrated Circuit and Step Map

Het quantumcircuit combineert de stappen sequentieel op de initiële toestanden ($|\psi_0\rangle$, $|\alpha\rangle$, $|\beta\rangle$):

1. **Initialisatie:** $H^{\otimes 3}$ poorten genereren de superpositie.
2. **Iteratie 1:** Oracle 1 ($U_f$) $\rightarrow$ Diffuser ($U_s$). *Veroorzaakt rotatie rond $|\psi_0\rangle$.*
3. **Iteratie 2:** Oracle 2 ($U_f$) $\rightarrow$ Diffuser ($U_s$). *Resulteert in gecombineerde rotatie van $2\theta$.*
4. **Afsluiting:** De toestand convergeert naar $|\beta\rangle$, gevolgd door de uitgangsmeting.

---

## Legenda & Wiskundige Definitie

* **$|\psi_0\rangle$**: Initiële toestand voor $N=8$ elementen ($n=3$ qubits).
* **$|\alpha\rangle$**: De ongemarkeerde elementen in de zoekruimte.
* **$|\beta\rangle$**: Het gemarkeerde element dat we zoeken (waarvan het teken wordt omgedraaid door de Oracle).

> **Grover's Iterate Definition:**
> $$G = (2|\psi\rangle\langle\psi| - I)O$$
