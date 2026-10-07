import re

def update_graphs():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_graph_func = """function getGraphForProblem(familyId, langObj) {
            if (familyId === "001") {
                return `
                <div class="mt-6 pt-4 border-t border-[#c2b496]">
                    <span class="text-xs font-semibold text-blue-900 uppercase tracking-wider mb-4 block flex items-center">
                        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4"></path></svg>
                        ${langObj.graph_sample}
                    </span>
                    <div class="bg-[#fcfaf5] border border-[#e2dcd0] p-4 flex justify-center">
                        <svg class="w-full max-w-lg h-32" viewBox="0 0 400 120" preserveAspectRatio="xMidYMid meet">
                            <!-- Estilización del grafo de ciclos -->
                            <defs>
                                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                                    <stop offset="0%" style="stop-color:#1e3a8a;stop-opacity:1" />
                                    <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
                                </linearGradient>
                            </defs>
                            <path d="M50,60 C150,10 250,110 350,60" fill="none" stroke="url(#grad1)" stroke-width="3" stroke-linecap="round"/>
                            <path d="M50,60 C150,110 250,10 350,60" fill="none" stroke="#93c5fd" stroke-width="3" stroke-dasharray="6,6" stroke-linecap="round"/>
                            
                            <!-- Nodos -->
                            <circle cx="50" cy="60" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                            <circle cx="150" cy="36" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                            <circle cx="250" cy="84" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                            <circle cx="350" cy="60" r="6" fill="#1e3a8a" stroke="#fffcf5" stroke-width="2"/>
                        </svg>
                    </div>
                </div>`;
            } else if (familyId === "002") {
                return `
                <div class="mt-6 pt-4 border-t border-[#c2b496]">
                    <span class="text-xs font-semibold text-blue-900 uppercase tracking-wider mb-4 block flex items-center">
                        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                        ${langObj.graph_elliptic}
                    </span>
                    <div class="bg-[#fcfaf5] border border-[#e2dcd0] p-4 flex justify-center">
                        <svg class="w-full max-w-lg h-40" viewBox="-3 -3 6 6" preserveAspectRatio="xMidYMid meet">
                            <!-- Ejes -->
                            <line x1="-3" y1="0" x2="3" y2="0" stroke="#cbd5e1" stroke-width="0.05"/>
                            <line x1="0" y1="-3" x2="0" y2="3" stroke="#cbd5e1" stroke-width="0.05"/>
                            <!-- Curva -->
                            <path d="M 3 4.89 C 2.5 3.5 1.5 2 1 0 C 1.5 -2 2.5 -3.5 3 -4.89" fill="none" stroke="#1e3a8a" stroke-width="0.08" stroke-linecap="round"/>
                            <path d="M -1 0 C -0.8 0.8 -0.2 0.8 0 0 C -0.2 -0.8 -0.8 -0.8 -1 0" fill="none" stroke="#1e3a8a" stroke-width="0.08" stroke-linecap="round"/>
                        </svg>
                    </div>
                </div>`;
            } else if (familyId === "003") {
                return `
                <div class="mt-6 pt-4 border-t border-[#c2b496]">
                    <span class="text-xs font-semibold text-blue-900 uppercase tracking-wider mb-4 block flex items-center">
                        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                        ${langObj.graph_zeta}
                    </span>
                    <div class="bg-[#fcfaf5] border border-[#e2dcd0] p-4 flex justify-center">
                        <svg class="w-full max-w-lg h-32" viewBox="0 0 400 120" preserveAspectRatio="xMidYMid meet">
                            <!-- Strip -->
                            <rect x="100" y="0" width="200" height="120" fill="#f1f5f9" opacity="0.5"/>
                            <line x1="100" y1="0" x2="100" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
                            <line x1="300" y1="0" x2="300" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>
                            <text x="105" y="15" font-size="10" fill="#64748b" font-family="sans-serif">Re(s) = 0</text>
                            <text x="305" y="15" font-size="10" fill="#64748b" font-family="sans-serif">Re(s) = 1</text>
                            
                            <!-- Re(s) = 1/2 -->
                            <line x1="200" y1="0" x2="200" y2="120" stroke="#1e3a8a" stroke-width="1.5"/>
                            <text x="205" y="110" font-size="10" fill="#1e3a8a" font-family="sans-serif" font-weight="bold">Re(s) = 1/2</text>
                            
                            <!-- Re(s) = 7/8 -->
                            <line x1="275" y1="0" x2="275" y2="120" stroke="#db2777" stroke-width="1.5" stroke-dasharray="4,2"/>
                            <text x="278" y="60" font-size="10" fill="#db2777" font-family="sans-serif" font-weight="bold">Re(s) = 7/8</text>
                            
                            <!-- Zeros -->
                            <circle cx="200" cy="30" r="4" fill="#1e3a8a"/>
                            <circle cx="200" cy="50" r="4" fill="#1e3a8a"/>
                            <circle cx="200" cy="80" r="4" fill="#1e3a8a"/>
                            <circle cx="200" cy="95" r="4" fill="#1e3a8a"/>
                        </svg>
                    </div>
                </div>`;
            }
            return "";
        }"""

    # regex to replace the old function block
    pattern = r'function getGraphForProblem\(familyId, langObj\) \{.*?\n        \}'
    new_content = re.sub(pattern, new_graph_func, content, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_graphs()
