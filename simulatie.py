class TengenSystem:
    def __init__(self):
        # Het middelpunt (De Scalar / Tengen)
        self.scalar_node = []
        
        # De 8 actieve regels (Nodes met een startwaarde, bijv. 1 voor actief)
        self.active_nodes = {
            "Regel_1": {"status": 1, "vrijheidsgraden": 3},
            "Regel_2": {"status": 1, "vrijheidsgraden": 2},
            "Regel_3": {"status": 1, "vrijheidsgraden": 4},
            "Regel_4": {"status": 1, "vrijheidsgraden": 1},
            "Regel_5": {"status": 1, "vrijheidsgraden": 3},
            "Regel_6": {"status": 1, "vrijheidsgraden": 2},
            "Regel_7": {"status": 1, "vrijheidsgraden": 0}, # Deze is omsingeld!
            "Regel_8": {"status": 1, "vrijheidsgraden": 3}
        }

    # De 9 grenzen (Hier gesimuleerd als één overkoepelende evaluatie-functie)
    def evalueer_grenzen(self):
        print("--- Start Evaluatie via de 9 Grenzen ---")
        verwijderde_nodes = []

        for node_naam, data in self.active_nodes.items():
            # Speltheorie: Als een node geen vrijheidsgraden heeft, wordt deze gecaptured
            if data["vrijheidsgraden"] <= 0:
                print(f"[!] {node_naam} heeft geen vrijheidsgraden meer en klapt dicht.")
                self.scalar_node.append(node_naam)
                verwijderde_nodes.append(node_naam)
            else:
                # Simuleer druk vanuit de grenzen door vrijheidsgraden te verlagen
                data["vrijheidsgraden"] -= 1

        # Verplaats de verslagen data naar het nulpunt en verwijder uit de schil
        for node in verwijderde_nodes:
            del self.active_nodes[node]

    def toon_systeemstatus(self):
        print(f"\nActieve Data in de Schil: {list(self.active_nodes.keys())}")
        print(f"Data gecentreerd in de Scalar: {self.scalar_node}\n")


# Simuleer het systeem in stappen
systeem = TengenSystem()
systeem.toon_systeemstatus()

# Draai de evaluatie-operatoren (de 'beurten' in het spel)
systeem.evalueer_grenzen()
systeem.toon_systeemstatus()

systeem.evalueer_grenzen()
systeem.toon_systeemstatus()
