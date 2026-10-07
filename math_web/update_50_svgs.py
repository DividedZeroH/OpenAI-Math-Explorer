import re

def expand_graphs():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_graph_func = """function getGraphForProblem(familyId, langObj) {
            const idNum = parseInt(familyId);
            if (isNaN(idNum) || idNum > 50) return "";

            const graphType = idNum % 6;
            
            let graphTitle = "";
            let svgContent = "";
            
            if (graphType === 0) {
                graphTitle = "Algebraic Cycles Graph";
                svgContent = `
                    <!-- Grafo de ciclos -->
                    <defs>
                        <linearGradient id="grad1-${idNum}" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#1e3a8a;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <path d="M50,60 C150,10 250,110 350,60" fill="none" stroke="url(#grad1-${idNum})" stroke-width="3" stroke-linecap="round"/>
                    <path d="M50,60 C150,110 250,10 350,60" fill="none" stroke="#93c5fd" stroke-width="3" stroke-dasharray="6,6" stroke-linecap="round"/>
                    <circle cx="50" cy="60" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                    <circle cx="150" cy="36" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                    <circle cx="250" cy="84" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                    <circle cx="350" cy="60" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                `;
            } else if (graphType === 1) {
                graphTitle = "Elliptic Curve Projection";
                svgContent = `
                    <!-- Curva Elíptica adaptada a 400x120 -->
                    <g transform="translate(200, 60) scale(15, -15)">
                        <line x1="-10" y1="0" x2="10" y2="0" stroke="#cbd5e1" stroke-width="0.1"/>
                        <line x1="0" y1="-4" x2="0" y2="4" stroke="#cbd5e1" stroke-width="0.1"/>
                        <path d="M 8 16 C 5 8 2 2 1 0 C 2 -2 5 -8 8 -16" fill="none" stroke="#1e3a8a" stroke-width="0.15" stroke-linecap="round"/>
                        <path d="M -1 0 C -0.8 1.5 -0.2 1.5 0 0 C -0.2 -1.5 -0.8 -1.5 -1 0" fill="none" stroke="#1e3a8a" stroke-width="0.15" stroke-linecap="round"/>
                    </g>
                `;
            } else if (graphType === 2) {
                graphTitle = "Riemann Zeta Critical Strip";
                svgContent = `
                    <!-- Franja crítica y ceros -->
                    <rect x="100" y="0" width="200" height="120" fill="#f1f5f9" opacity="0.5"/>
                    <line x1="100" y1="0" x2="100" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
                    <line x1="300" y1="0" x2="300" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
                    <text x="105" y="15" font-size="10" fill="#64748b" font-family="sans-serif">Re(s) = 0</text>
                    <text x="305" y="15" font-size="10" fill="#64748b" font-family="sans-serif">Re(s) = 1</text>
                    <line x1="200" y1="0" x2="200" y2="120" stroke="#1e3a8a" stroke-width="1.5"/>
                    <text x="205" y="110" font-size="10" fill="#1e3a8a" font-family="sans-serif" font-weight="bold">Re(s) = 1/2</text>
                    <line x1="275" y1="0" x2="275" y2="120" stroke="#db2777" stroke-width="1.5" stroke-dasharray="4,2"/>
                    <text x="278" y="60" font-size="10" fill="#db2777" font-family="sans-serif" font-weight="bold">Re(s) = 7/8</text>
                    <circle cx="200" cy="30" r="4" fill="#1e3a8a"/>
                    <circle cx="200" cy="50" r="4" fill="#1e3a8a"/>
                    <circle cx="200" cy="80" r="4" fill="#1e3a8a"/>
                    <circle cx="200" cy="95" r="4" fill="#1e3a8a"/>
                `;
            } else if (graphType === 3) {
                graphTitle = "Gaussian Distribution";
                svgContent = `
                    <!-- Campana de Gauss -->
                    <line x1="50" y1="100" x2="350" y2="100" stroke="#cbd5e1" stroke-width="2"/>
                    <path d="M50,100 Q150,100 175,60 T200,10 T225,60 T350,100" fill="#dbeafe" opacity="0.4" stroke="none"/>
                    <path d="M50,100 Q150,100 175,60 T200,10 T225,60 T350,100" fill="none" stroke="#1e3a8a" stroke-width="2"/>
                    <line x1="200" y1="10" x2="200" y2="100" stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="205" y="50" font-size="12" fill="#1e3a8a" font-family="sans-serif">&mu;</text>
                `;
            } else if (graphType === 4) {
                graphTitle = "Integration & Area under Curve";
                svgContent = `
                    <!-- Integral -->
                    <line x1="20" y1="100" x2="380" y2="100" stroke="#cbd5e1" stroke-width="2"/>
                    <line x1="40" y1="10" x2="40" y2="110" stroke="#cbd5e1" stroke-width="2"/>
                    <!-- Area under curve -->
                    <path d="M100,100 L100,60 C150,10 250,90 300,30 L300,100 Z" fill="#dbeafe" opacity="0.5"/>
                    <path d="M40,90 C100,40 150,10 250,90 C300,130 350,10 380,20" fill="none" stroke="#1e3a8a" stroke-width="2"/>
                    <line x1="100" y1="60" x2="100" y2="100" stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <line x1="300" y1="30" x2="300" y2="100" stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="190" y="80" font-size="14" fill="#1e3a8a" font-family="sans-serif">&int; f(x) dx</text>
                `;
            } else if (graphType === 5) {
                graphTitle = "Geometric Projection";
                svgContent = `
                    <!-- Geometría / Proyección -->
                    <g transform="translate(200, 60)">
                        <polygon points="0,-40 80,10 0,40 -80,10" fill="#dbeafe" opacity="0.3" stroke="#1e3a8a" stroke-width="1"/>
                        <polygon points="0,-10 30,10 0,30 -30,10" fill="#bfdbfe" opacity="0.5" stroke="#1e3a8a" stroke-width="1.5"/>
                        <line x1="0" y1="-40" x2="0" y2="-10" stroke="#1e3a8a" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="80" y1="10" x2="30" y2="10" stroke="#1e3a8a" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="0" y1="40" x2="0" y2="30" stroke="#1e3a8a" stroke-width="1" stroke-dasharray="2,2"/>
                        <line x1="-80" y1="10" x2="-30" y2="10" stroke="#1e3a8a" stroke-width="1" stroke-dasharray="2,2"/>
                        <circle cx="0" cy="-10" r="3" fill="#1e3a8a"/>
                        <circle cx="30" cy="10" r="3" fill="#1e3a8a"/>
                        <circle cx="0" cy="30" r="3" fill="#1e3a8a"/>
                        <circle cx="-30" cy="10" r="3" fill="#1e3a8a"/>
                    </g>
                `;
            }

            return `
            <div class="mt-6 pt-4 border-t border-[#e2dcd0]">
                <span class="text-xs font-semibold text-blue-900 uppercase tracking-wider mb-4 block flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"></path></svg>
                    ${graphTitle}
                </span>
                <div class="bg-[#efeae1] border border-[#e2dcd0] p-4 flex justify-center">
                    <svg class="w-full max-w-lg h-32" viewBox="0 0 400 120" preserveAspectRatio="xMidYMid meet">
                        ${svgContent}
                    </svg>
                </div>
            </div>`;
        }"""

    # regex to replace the old function block
    pattern = r'function getGraphForProblem\(familyId, langObj\) \{.*?\n        \}'
    new_content = re.sub(pattern, new_graph_func, content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    expand_graphs()
