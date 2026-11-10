with open("index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoSemi-Hub | 半導體供應鏈與經濟學知識庫</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between">

    <!-- 導覽列 -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white">ES</div>
                <span class="text-lg font-bold tracking-tight">EcoSemi-Hub</span>
            </div>
            <nav class="hidden md:flex space-x-6 text-sm font-medium text-slate-300">
                <a href="#toolkit" class="hover:text-indigo-400 transition">分析技巧</a>
                <a href="content/02-maps/nvidia.html" class="hover:text-indigo-400 transition">供應鏈地圖</a>
                <a href="#weekly" class="hover:text-indigo-400 transition">當週時事</a>
            </nav>
        </div>
    </header>

    <!-- 主視覺 Hero Section -->
    <main class="max-w-6xl mx-auto px-6 py-16 flex-grow">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <span class="inline-block px-3 py-1 mb-4 text-xs font-semibold tracking-wider text-indigo-400 uppercase bg-indigo-950 rounded-full border border-indigo-800/50">
                Quantitative Supply Chain & Semi Knowledge Base
            </span>
            <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-6 bg-gradient-to-r from-white via-slate-200 to-indigo-400 bg-clip-text text-transparent">
                半導體供應鏈與總體經濟知識庫
            </h1>
            <p class="text-lg text-slate-400 leading-relaxed">
                結合計量分析方法、關鍵產業供應鏈地圖，以及即時半導體動態剖析的結構化知識平台。
            </p>
        </div>

        <!-- 三大主軸卡片區 -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            
            <!-- 主軸一 -->
            <div id="toolkit" class="bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-indigo-500/50 transition duration-300 flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-lg bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 text-xl font-bold mb-4">01</div>
                    <h2 class="text-xl font-bold mb-2">供應鏈分析技巧</h2>
                    <p class="text-slate-400 text-sm leading-relaxed mb-6">
                        收錄 PP&E 資本支出拆解、存貨週轉天數（DSO）模型、計量迴歸與數據視覺化實務技巧。
                    </p>
                </div>
                <span class="inline-flex items-center text-sm font-semibold text-slate-500 cursor-not-allowed">
                    建構中 &rarr;
                </span>
            </div>

            <!-- 主軸二 -->
            <div id="maps" class="bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-indigo-500/50 transition duration-300 flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-lg bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 text-xl font-bold mb-4">02</div>
                    <h2 class="text-xl font-bold mb-2">產業與公司地圖</h2>
                    <p class="text-slate-400 text-sm leading-relaxed mb-6">
                        剖析上中下游交織關係，涵蓋 CoWoS 先進封裝生態系、晶圓代工與重要零組件供應商網絡。
                    </p>
                </div>
                <a href="content/02-maps/nvidia.html" class="inline-flex items-center text-sm font-semibold text-indigo-400 hover:text-indigo-300">
                    查看 Nvidia 供應鏈地圖 &rarr;
                </a>
            </div>

            <!-- 主軸三 -->
            <div id="weekly" class="bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-indigo-500/50 transition duration-300 flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-lg bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 text-xl font-bold mb-4">03</div>
                    <h2 class="text-xl font-bold mb-2">當週時事解讀</h2>
                    <p class="text-slate-400 text-sm leading-relaxed mb-6">
                        每週跟進半導體財報、地緣政治管制與產能變動，運用經濟模型進行即時觀點短評。
                    </p>
                </div>
                <span class="inline-flex items-center text-sm font-semibold text-slate-500 cursor-not-allowed">
                    建構中 &rarr;
                </span>
            </div>

        </div>
    </main>

    <!-- 頁尾 -->
    <footer class="border-t border-slate-800 py-6 text-center text-xs text-slate-500">
        &copy; 2026 EcoSemi-Hub. Powered by AGENTS.md workflow.
    </footer>

</body>
</html>
""")