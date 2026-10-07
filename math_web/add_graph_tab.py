import re

def add_graph_tab():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add vis-network CDN in head
    if "vis-network" not in content:
        content = content.replace('</head>', '    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>\n</head>')

    # 2. Add Tabs in Header
    tabs_html = """
              <div class="mt-6 border-b border-book-border">
                  <nav class="-mb-px flex space-x-8">
                      <button id="btnTabList" onclick="switchTab('list')" class="border-black text-black whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm">
                          Catálogo
                      </button>
                      <button id="btnTabGraph" onclick="switchTab('graph')" class="border-transparent text-book-text hover:text-black hover:border-book-border whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm">
                          Grafo de Relaciones
                      </button>
                  </nav>
              </div>
          </div>
      </header>"""
      
    content = content.replace('          </div>\n      </header>', tabs_html)

    # 3. Add graph view container next to stats/filters
    # Replace `<div id="stats"...</div>` with `<div id="listView">...</div>`
    
    # We will wrap the filters, stats, and results grid inside `<div id="listView">`
    # Let's find the start of filters: `<div class="mt-4 pt-4 border-t border-book-border` (Wait, this is in the header now)
    # The main content starts with `<main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">`
    # We will put the tabs in the header, and the two views in the main.
    
    main_pattern = r'<main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">'
    new_main = """<main class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <!-- VISTA DE GRAFO -->
        <div id="graphView" class="hidden">
            <div class="bg-[#FCFAF5] border border-book-border p-4 mb-4">
                <p class="text-sm text-black">Este grafo interactivo muestra las conexiones entre todos los problemas y sus respectivas disciplinas matemáticas. Puedes arrastrar los nodos o hacer zoom.</p>
            </div>
            <div id="networkGraph" class="w-full h-[600px] bg-[#FCFAF5] border border-book-border shadow-sm"></div>
        </div>
        
        <!-- VISTA DE LISTA -->
        <div id="listView">"""
    
    content = content.replace(main_pattern, new_main)
    
    # Close the listView div before the footer
    footer_pattern = r'<footer'
    content = content.replace('<footer', '</div>\n    <footer')

    # 4. Add JavaScript for Tabs and Graph
    js_code = """
        function switchTab(tab) {
            const listBtn = document.getElementById('btnTabList');
            const graphBtn = document.getElementById('btnTabGraph');
            const listView = document.getElementById('listView');
            const graphView = document.getElementById('graphView');

            if (tab === 'list') {
                listBtn.className = "border-black text-black whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm";
                graphBtn.className = "border-transparent text-book-text hover:text-black hover:border-book-border whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm";
                listView.classList.remove('hidden');
                graphView.classList.add('hidden');
            } else {
                graphBtn.className = "border-black text-black whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm";
                listBtn.className = "border-transparent text-book-text hover:text-black hover:border-book-border whitespace-nowrap pb-4 px-1 border-b-2 font-medium text-sm";
                listView.classList.add('hidden');
                graphView.classList.remove('hidden');
                
                // Initialize graph if not already done
                if (!window.graphInitialized && familiesData.length > 0) {
                    initGraph(familiesData);
                    window.graphInitialized = true;
                }
            }
        }

        function initGraph(data) {
            const nodes = [];
            const edges = [];
            const disciplines = new Set();
            
            // Collect disciplines
            data.forEach(f => {
                if(f.discipline) disciplines.add(f.discipline);
            });

            // Create discipline nodes (central hubs)
            disciplines.forEach(d => {
                nodes.push({
                    id: `disc-${d}`,
                    label: d,
                    shape: 'box',
                    font: { color: '#F4F0E6', face: 'system-ui', size: 16 },
                    color: {
                        background: '#2D2A26',
                        border: '#000000',
                        highlight: { background: '#4A3F35', border: '#000000' }
                    },
                    margin: 10
                });
            });

            // Create problem nodes and connect them
            data.forEach(f => {
                nodes.push({
                    id: f.id,
                    label: `Prob ${f.id}`,
                    shape: 'dot',
                    size: 8,
                    font: { color: '#000000', face: 'system-ui', size: 12 },
                    color: {
                        background: '#F4F0E6',
                        border: '#CFC4B4',
                        highlight: { background: '#FCFAF5', border: '#6B4F2A' }
                    }
                });

                if (f.discipline) {
                    edges.push({
                        from: f.id,
                        to: `disc-${f.discipline}`,
                        color: { color: '#CFC4B4', highlight: '#6B4F2A' },
                        width: 1
                    });
                }
            });

            const container = document.getElementById('networkGraph');
            const graphData = { nodes: nodes, edges: edges };
            const options = {
                physics: {
                    forceAtlas2Based: {
                        gravitationalConstant: -50,
                        centralGravity: 0.01,
                        springLength: 100,
                        springConstant: 0.08
                    },
                    maxVelocity: 50,
                    solver: 'forceAtlas2Based',
                    timestep: 0.35,
                    stabilization: { iterations: 150 }
                },
                interaction: { hover: true, tooltipDelay: 200 }
            };
            new vis.Network(container, graphData, options);
        }

        async function loadData() {"""
        
    content = content.replace('async function loadData() {', js_code)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    add_graph_tab()
