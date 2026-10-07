import re

def fix_coherent_graphs():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_graph_func = """function getGraphForProblem(family, langObj) {
            const textToSearch = (family.title + " " + family.discipline).toLowerCase();
            
            let graphType = -1;
            
            // Keyword matching for mathematical coherence
            if (textToSearch.includes("elliptic") || textToSearch.includes("curve") || textToSearch.includes("bsd") || textToSearch.includes("lienard")) {
                graphType = 1; // Curva elíptica
            } else if (textToSearch.includes("riemann") || textToSearch.includes("zeta") || textToSearch.includes("analytic density") || textToSearch.includes("dirichlet")) {
                graphType = 2; // Plano complejo / Zeta
            } else if (textToSearch.includes("gauss") || textToSearch.includes("distribution") || textToSearch.includes("probability") || textToSearch.includes("stochastic") || textToSearch.includes("markov")) {
                graphType = 3; // Campana de Gauss
            } else if (textToSearch.includes("integral") || textToSearch.includes("measure") || textToSearch.includes("area") || textToSearch.includes("calculus") || textToSearch.includes("limit cycle")) {
                graphType = 4; // Integral / Área
            } else if (textToSearch.includes("manifold") || textToSearch.includes("topology") || textToSearch.includes("geometry") || textToSearch.includes("projection") || textToSearch.includes("space")) {
                graphType = 5; // Geometría 3D / Proyección
            } else if (textToSearch.includes("graph") || textToSearch.includes("cycle") || textToSearch.includes("algebraic") || textToSearch.includes("variety") || textToSearch.includes("network")) {
                graphType = 0; // Grafos / Ciclos Algebraicos
            }
            
            if (graphType === -1) return "";
            
            let graphTitle = "";
            let svgContent = "";
            
            if (graphType === 0) {
                graphTitle = "Algebraic Cycles Graph";
                svgContent = `
                    <defs>
                        <linearGradient id="grad1-${family.id}" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#2D2A26;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#4A3F35;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <path d="M50,60 C150,10 250,110 350,60" fill="none" stroke="url(#grad1-${family.id})" stroke-width="3" stroke-linecap="round"/>
                    <path d="M50,60 C150,110 250,10 350,60" fill="none" stroke="#6B4F2A" stroke-width="3" stroke-dasharray="6,6" stroke-linecap="round"/>
                    <circle cx="50" cy="60" r="6" fill="#2D2A26" stroke="#F4F0E6" stroke-width="2"/>
                    <circle cx="150" cy="36" r="6" fill="#2D2A26" stroke="#F4F0E6" stroke-width="2"/>
                    <circle cx="250" cy="84" r="6" fill="#2D2A26" stroke="#F4F0E6" stroke-width="2"/>
                    <circle cx="350" cy="60" r="6" fill="#2D2A26" stroke="#F4F0E6" stroke-width="2"/>
                `;
            } else if (graphType === 1) {
                graphTitle = "Elliptic Curve Projection";
                svgContent = `
                    <g transform="translate(200, 60) scale(15, -15)">
                        <line x1="-10" y1="0" x2="10" y2="0" stroke="#CFC4B4" stroke-width="0.1"/>
                        <line x1="0" y1="-4" x2="0" y2="4" stroke="#CFC4B4" stroke-width="0.1"/>
                        <path d="M 8 16 C 5 8 2 2 1 0 C 2 -2 5 -8 8 -16" fill="none" stroke="#2D2A26" stroke-width="0.15" stroke-linecap="round"/>
                        <path d="M -1 0 C -0.8 1.5 -0.2 1.5 0 0 C -0.2 -1.5 -0.8 -1.5 -1 0" fill="none" stroke="#2D2A26" stroke-width="0.15" stroke-linecap="round"/>
                    </g>
                `;
            } else if (graphType === 2) {
                graphTitle = "Riemann Zeta Critical Strip";
                svgContent = `
                    <rect x="100" y="0" width="200" height="120" fill="#F4F0E6" opacity="0.5"/>
                    <line x1="100" y1="0" x2="100" y2="120" stroke="#CFC4B4" stroke-width="1" stroke-dasharray="4,4"/>
                    <line x1="300" y1="0" x2="300" y2="120" stroke="#CFC4B4" stroke-width="1" stroke-dasharray="4,4"/>
                    <text x="105" y="15" font-size="10" fill="#4A3F35" font-family="sans-serif">Re(s) = 0</text>
                    <text x="305" y="15" font-size="10" fill="#4A3F35" font-family="sans-serif">Re(s) = 1</text>
                    <line x1="200" y1="0" x2="200" y2="120" stroke="#2D2A26" stroke-width="1.5"/>
                    <text x="205" y="110" font-size="10" fill="#2D2A26" font-family="sans-serif" font-weight="bold">Re(s) = 1/2</text>
                    <line x1="275" y1="0" x2="275" y2="120" stroke="#6B4F2A" stroke-width="1.5" stroke-dasharray="4,2"/>
                    <text x="278" y="60" font-size="10" fill="#6B4F2A" font-family="sans-serif" font-weight="bold">Re(s) = 7/8</text>
                    <circle cx="200" cy="30" r="4" fill="#2D2A26"/>
                    <circle cx="200" cy="50" r="4" fill="#2D2A26"/>
                    <circle cx="200" cy="80" r="4" fill="#2D2A26"/>
                    <circle cx="200" cy="95" r="4" fill="#2D2A26"/>
                `;
            } else if (graphType === 3) {
                graphTitle = "Gaussian Distribution";
                svgContent = `
                    <line x1="50" y1="100" x2="350" y2="100" stroke="#CFC4B4" stroke-width="2"/>
                    <path d="M50,100 Q150,100 175,60 T200,10 T225,60 T350,100" fill="#EBDBC5" opacity="0.4" stroke="none"/>
                    <path d="M50,100 Q150,100 175,60 T200,10 T225,60 T350,100" fill="none" stroke="#2D2A26" stroke-width="2"/>
                    <line x1="200" y1="10" x2="200" y2="100" stroke="#2D2A26" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="205" y="50" font-size="12" fill="#2D2A26" font-family="sans-serif">&mu;</text>
                `;
            } else if (graphType === 4) {
                graphTitle = "Integration & Area under Curve";
                svgContent = `
                    <line x1="20" y1="100" x2="380" y2="100" stroke="#CFC4B4" stroke-width="2"/>
                    <line x1="40" y1="10" x2="40" y2="110" stroke="#CFC4B4" stroke-width="2"/>
                    <path d="M100,100 L100,60 C150,10 250,90 300,30 L300,100 Z" fill="#EBDBC5" opacity="0.5"/>
                    <path d="M40,90 C100,40 150,10 250,90 C300,130 350,10 380,20" fill="none" stroke="#2D2A26" stroke-width="2"/>
                    <line x1="100" y1="60" x2="100" y2="100" stroke="#2D2A26" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <line x1="300" y1="30" x2="300" y2="100" stroke="#2D2A26" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="190" y="80" font-size="14" fill="#2D2A26" font-family="sans-serif">&int; f(x) dx</text>
                `;
            } else if (graphType === 5) {
                graphTitle = "Geometric Projection";
                svgContent = `
                    <g transform="translate(200, 60)">
                        <polygon points="0,-40 80,10 0,40 -80,10" fill="#EBDBC5" opacity="0.3" stroke="#2D2A26" stroke-width="1"/>
                        <polygon points="0,-10 30,10 0,30 -30,10" fill="#CFC4B4" opacity="0.5" stroke="#2D2A26" stroke-width="1.5"/>
                        <line x1="0" y1="-40" x2="0" y2="-10" stroke="#2D2A26" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="80" y1="10" x2="30" y2="10" stroke="#2D2A26" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="0" y1="40" x2="0" y2="30" stroke="#2D2A26" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="-80" y1="10" x2="-30" y2="10" stroke="#2D2A26" stroke-width="1" stroke-dasharray="2,2"/>
                        <circle cx="0" cy="-10" r="3" fill="#2D2A26"/>
                        <circle cx="30" cy="10" r="3" fill="#2D2A26"/>
                        <circle cx="0" cy="30" r="3" fill="#2D2A26"/>
                        <circle cx="-30" cy="10" r="3" fill="#2D2A26"/>
                    </g>
                `;
            }

            return `
            <div class="mt-6 pt-4 border-t border-book-border">
                <span class="text-xs font-semibold text-book-title uppercase tracking-wider mb-4 block flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"></path></svg>
                    ${graphTitle}
                </span>
                <div class="bg-book-bg border border-book-border p-4 flex justify-center">
                    <svg class="w-full max-w-lg h-32" viewBox="0 0 400 120" preserveAspectRatio="xMidYMid meet">
                        ${svgContent}
                    </svg>
                </div>
            </div>`;
        }"""

    # regex to replace the old function block
    pattern = r'function getGraphForProblem\(familyId, langObj\) \{.*?\n        \}'
    new_content = re.sub(pattern, new_graph_func, content, flags=re.DOTALL)

    # We also need to change the call site from `getGraphForProblem(family.id, lang)` to `getGraphForProblem(family, lang)`
    new_content = new_content.replace('getGraphForProblem(family.id, lang)', 'getGraphForProblem(family, lang)')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    fix_coherent_graphs()
