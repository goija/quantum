### De Complete 17-Regel State Machine (Standalone HTML)

Sla de onderstaande code op als `simulatie.html` en open het in je browser.

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>De 17-Regel Simulatie (Go & Quantum)</title>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  
  <style>
    :root {
      --bg: #f4f7f6;
      --text: #2c3e50;
      --primary: #34495e;
      --accent: #2980b9;
      --scalar: #c0392b;
      --node-active: #27ae60;
      --panel-bg: #ffffff;
    }

    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 20px;
      line-height: 1.6;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 30px;
    }

    @media (min-width: 900px) {
      .container {
        flex-direction: row;
      }
    }

    /* Linker Paneel: Logica en Data */
    .data-panel {
      flex: 1;
      background: var(--panel-bg);
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }

    h1 { color: var(--primary); font-size: 1.6em; border-bottom: 2px solid var(--accent); padding-bottom: 10px; margin-top: 0; }
    h2 { color: var(--accent); font-size: 1.2em; margin-top: 25px; }

    .controls {
      display: flex;
      gap: 15px;
      margin: 20px 0;
    }

    button {
      padding: 12px 20px;
      font-weight: bold;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      color: white;
      transition: background 0.3s, transform 0.1s;
    }

    button:active { transform: scale(0.98); }
    .btn-action { background-color: var(--accent); }
    .btn-action:hover { background-color: #1f6391; }
    .btn-reset { background-color: #7f8c8d; }
    .btn-reset:hover { background-color: #636e72; }
    .btn-disabled { background-color: #bdc3c7; cursor: not-allowed; }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
      font-size: 0.9em;
    }

    th, td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #eee;
    }

    th { background-color: #f8f9fa; color: var(--primary); }
    .status-captured { color: var(--scalar); font-weight: bold; }
    .status-active { color: var(--node-active); font-weight: bold; }

    /* Rechter Paneel: De Visuele State Machine */
    .viz-panel {
      flex: 1;
      background: var(--panel-bg);
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 500px;
      position: relative;
    }

    .canvas {
      position: relative;
      width: 400px;
      height: 400px;
      border-radius: 50%;
      border: 2px dashed #e0e0e0;
    }

    /* De Tengen / Scalar in het midden */
    .tengen {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 40px;
      height: 40px;
      background-color: var(--scalar);
      border-radius: 50%;
      transform: translate(-50%, -50%);
      z-index: 10;
      box-shadow: 0 0 20px rgba(192, 57, 43, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: bold;
      font-size: 0.8em;
      transition: all 0.5s ease;
    }

    /* De 8 deeltjes/regels */
    .node {
      position: absolute;
      width: 24px;
      height: 24px;
      background-color: var(--node-active);
      border-radius: 50%;
      transform: translate(-50%, -50%);
      z-index: 5;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 0.7em;
      font-weight: bold;
      /* Cruciale animatie voor het vloeiend verplaatsen naar de Scalar */
      transition: all 1.2s cubic-bezier(0.25, 1, 0.5, 1);
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    /* Gecapturede nodes */
    .node.captured {
      background-color: var(--primary);
      opacity: 0.3;
      width: 16px;
      height: 16px;
    }

  </style>
</head>
<body>

  <div id="app" class="container">
    
    <div class="data-panel">
      <h1>De 17-Regel State Machine</h1>
      <p>Deze simulatie toont het conflict tussen de <strong>8 Dataregels</strong> (de actieve knopen) en de <strong>9 Grenzen</strong> (de operatoren). Geïnspireerd op het Oosterse Go-bord en quantum logica.</p>
      
      <div class="controls">
        <button 
          @click="evalueerGrenzen" 
          :class="['btn-action', { 'btn-disabled': isGameFinished }]">
          {{ isGameFinished ? 'Alle data is gecaptured' : 'Activeer de 9 Grenzen (Mutatie)' }}
        </button>
        <button @click="resetSysteem" class="btn-reset">Reset Systeem</button>
      </div>

      <h2>Status van de 8 Regels</h2>
      <table>
        <thead>
          <tr>
            <th>Regel ID</th>
            <th>Vrijheidsgraden (Liberties)</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="node in nodes" :key="node.id">
            <td>Regel {{ node.id }}</td>
            <td>
              <span v-if="node.vrijheidsgraden > 0">{{ node.vrijheidsgraden }}</span>
              <span v-else>0 (Omsingeld)</span>
            </td>
            <td :class="node.isCaptured ? 'status-captured' : 'status-active'">
              {{ node.isCaptured ? 'In de Scalar (0)' : 'Actief (1)' }}
            </td>
          </tr>
        </tbody>
      </table>

      <h2>De Kwintessens (Tengen)</h2>
      <p>Aantal regels in het absolute nulpunt: <strong>{{ gecapturedeNodesCount }} / 8</strong></p>
    </div>

    <div class="viz-panel">
      <div class="canvas">
        
        <div class="tengen" :style="{ transform: `translate(-50%, -50%) scale(${1 + (gecapturedeNodesCount * 0.15)})` }">
          {{ gecapturedeNodesCount }}
        </div>

        <div 
          v-for="node in nodes" 
          :key="'viz-'+node.id"
          class="node"
          :class="{ 'captured': node.isCaptured }"
          :style="{
            left: `calc(50% + ${getX(node)}px)`,
            top: `calc(50% + ${getY(node)}px)`
          }">
          {{ node.isCaptured ? '' : node.id }}
        </div>

      </div>
    </div>

  </div>

  <script>
    const { createApp, ref, computed } = Vue;

    createApp({
      setup() {
        const radius = 170; // Afstand tot het middelpunt
        
        // De initiële data: 8 regels met elk een eigen set "vrijheidsgraden"
        const defaultNodes = [
          { id: 1, vrijheidsgraden: 3, isCaptured: false, angle: 0 },
          { id: 2, vrijheidsgraden: 1, isCaptured: false, angle: 45 },
          { id: 3, vrijheidsgraden: 4, isCaptured: false, angle: 90 },
          { id: 4, vrijheidsgraden: 2, isCaptured: false, angle: 135 },
          { id: 5, vrijheidsgraden: 3, isCaptured: false, angle: 180 },
          { id: 6, vrijheidsgraden: 1, isCaptured: false, angle: 225 },
          { id: 7, vrijheidsgraden: 5, isCaptured: false, angle: 270 },
          { id: 8, vrijheidsgraden: 2, isCaptured: false, angle: 315 },
        ];

        // Maak de data reactief (Vue State)
        const nodes = ref(JSON.parse(JSON.stringify(defaultNodes)));

        // Berekende data: Tel hoeveel regels er in de Scalar zitten
        const gecapturedeNodesCount = computed(() => {
          return nodes.value.filter(n => n.isCaptured).length;
        });

        // Controleer of de simulatie klaar is (alles in het middelpunt)
        const isGameFinished = computed(() => {
          return gecapturedeNodesCount.value === nodes.value.length;
        });

        // De methode die de 9 grenzen simuleert (Druk uitoefenen)
        const evalueerGrenzen = () => {
          if (isGameFinished.value) return;

          nodes.value.forEach(node => {
            if (!node.isCaptured) {
              node.vrijheidsgraden -= 1;
              // Zodra vrijheidsgraden 0 of lager zijn, wordt de node opgezogen door Tengen
              if (node.vrijheidsgraden <= 0) {
                node.vrijheidsgraden = 0;
                node.isCaptured = true;
              }
            }
          });
        };

        // Reset de interface terug naar het begin
        const resetSysteem = () => {
          nodes.value = JSON.parse(JSON.stringify(defaultNodes));
        };

        // Wiskundige functies voor de 2D positionering op de cirkel
        const getX = (node) => {
          // Als de node gecaptured is, verplaats de X coördinaat naar het exacte middelpunt (0)
          if (node.isCaptured) return 0;
          return Math.cos(node.angle * (Math.PI / 180)) * radius;
        };

        const getY = (node) => {
          // Als de node gecaptured is, verplaats de Y coördinaat naar het exacte middelpunt (0)
          if (node.isCaptured) return 0;
          return Math.sin(node.angle * (Math.PI / 180)) * radius;
        };

        return {
          nodes,
          gecapturedeNodesCount,
          isGameFinished,
          evalueerGrenzen,
          resetSysteem,
          getX,
          getY
        };
      }
    }).mount('#app');
  </script>

</body>
</html>

```

### De Structuur

* **De Reactieve Loop:** In het datablok (`defaultNodes`) heeft elke van de 8 regels een specifiek startaantal vrijheidsgraden. Ik heb ze een willekeurige spreiding gegeven (van 1 tot 5), zodat ze niet allemaal tegelijk, maar één voor één door het systeem worden verzwolgen.
* **De Operatoren-knop:** Zodra je op "Activeer de 9 Grenzen" drukt, roep je de functie `evalueerGrenzen()` aan. Dit simuleert een 'beurt' in het spel. Elke node verliest één vrijheidsgraad.
* **De Kwintessens Zwaartekracht:** De CSS-transitie is het visuele pronkstuk. In de rekenfuncties `getX` en `getY` heb ik de logica geschreven dat als `node.isCaptured` de waarde `true` raakt (zijn vrijheidsgraden zijn 0), de coördinaten van die stip met brute wiskundige kracht naar exact `0, 0` (het midden) worden gezet. De interface zal de stip dan vloeiend naar de rode 'Tengen' bol laten vliegen.
