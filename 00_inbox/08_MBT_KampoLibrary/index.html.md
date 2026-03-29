<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBT55 — Climate Change & Scientific Potential</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Mono:wght@300;400&family=Noto+Serif+JP:wght@300;400;600&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
  <style>
    :root {
      --ink: #1a1a1a;
      --paper: #f5f0e8;
      --sage: #4a6741;
      --sage-light: #7a9e71;
      --earth: #8b6914;
      --mist: #e8e2d6;
      --accent: #2d5a3d;
      --mono: 'DM Mono', monospace;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--paper);
      color: var(--ink);
      font-family: 'Cormorant Garamond', Georgia, serif;
      line-height: 1.8;
      min-height: 100vh;
    }

    body.ja-active {
      font-family: 'Noto Serif JP', 'Cormorant Garamond', serif;
    }

    /* ── Header ── */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--ink);
      color: var(--paper);
      padding: 0 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 56px;
      border-bottom: 2px solid var(--sage);
    }

    .header-title {
      font-size: 0.75rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      font-family: var(--mono);
      color: var(--sage-light);
    }

    .lang-toggle {
      display: flex;
      gap: 4px;
      background: rgba(255,255,255,0.08);
      border-radius: 4px;
      padding: 4px;
    }

    .lang-btn {
      font-family: var(--mono);
      font-size: 0.7rem;
      letter-spacing: 0.1em;
      padding: 6px 16px;
      border: 1px solid transparent;
      border-radius: 2px;
      cursor: pointer;
      background: transparent;
      color: #aaa;
      transition: all 0.2s;
    }

    .lang-btn.active {
      background: var(--sage);
      color: var(--paper);
      border-color: var(--sage-light);
    }

    .lang-btn:hover:not(.active) {
      color: var(--paper);
      border-color: rgba(255,255,255,0.2);
    }

    /* ── Hero ── */
    .hero {
      padding: 5rem 2rem 4rem;
      max-width: 960px;
      margin: 0 auto;
      border-bottom: 1px solid var(--mist);
    }

    .hero-label {
      font-family: var(--mono);
      font-size: 0.68rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--sage);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .hero-label::after {
      content: '';
      flex: 1;
      max-width: 80px;
      height: 1px;
      background: var(--sage);
    }

    .hero h1 {
      font-size: clamp(2rem, 5vw, 3.4rem);
      font-weight: 300;
      line-height: 1.2;
      color: var(--ink);
      letter-spacing: -0.01em;
      max-width: 820px;
    }

    .hero h1 em {
      font-style: italic;
      color: var(--sage);
    }

    .hero-sub {
      margin-top: 1.5rem;
      font-size: 1.05rem;
      color: #555;
      max-width: 640px;
      font-weight: 300;
    }

    .pdf-links {
      margin-top: 2.5rem;
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .pdf-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 10px 22px;
      background: var(--accent);
      color: var(--paper);
      text-decoration: none;
      font-family: var(--mono);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      border-radius: 2px;
      transition: background 0.2s, transform 0.15s;
    }

    .pdf-btn:hover {
      background: var(--sage);
      transform: translateY(-1px);
    }

    .pdf-btn svg {
      width: 14px;
      height: 14px;
      fill: currentColor;
    }

    /* ── Layout ── */
    .content-wrapper {
      max-width: 960px;
      margin: 0 auto;
      padding: 3rem 2rem 6rem;
    }

    /* ── Language sections ── */
    .lang-section { display: none; }
    .lang-section.active { display: block; }

    /* ── Chapter nav ── */
    .chapter-nav {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 3.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--mist);
    }

    .chapter-nav a {
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 0.1em;
      padding: 5px 12px;
      border: 1px solid #ccc;
      color: #666;
      text-decoration: none;
      border-radius: 2px;
      transition: all 0.15s;
    }

    .chapter-nav a:hover {
      border-color: var(--sage);
      color: var(--sage);
    }

    /* ── Typography ── */
    .chapter {
      margin-bottom: 4rem;
      scroll-margin-top: 80px;
    }

    .chapter-number {
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 0.3em;
      color: var(--sage);
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }

    h2 {
      font-size: clamp(1.6rem, 3.5vw, 2.2rem);
      font-weight: 400;
      line-height: 1.3;
      color: var(--ink);
      margin-bottom: 0.5rem;
      padding-bottom: 0.8rem;
      border-bottom: 2px solid var(--sage);
    }

    h3 {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--accent);
      margin: 2.5rem 0 0.8rem;
    }

    h4 {
      font-size: 1rem;
      font-weight: 600;
      color: var(--ink);
      margin: 1.8rem 0 0.5rem;
      font-style: italic;
    }

    p {
      font-size: 1.05rem;
      margin-bottom: 1.2rem;
      font-weight: 300;
      color: #2a2a2a;
    }

    strong {
      font-weight: 600;
      color: var(--ink);
    }

    em {
      color: var(--sage);
    }

    ul, ol {
      margin: 1rem 0 1.5rem 1.5rem;
    }

    li {
      font-size: 1.02rem;
      margin-bottom: 0.6rem;
      font-weight: 300;
    }

    /* ── Tables ── */
    .table-wrap {
      overflow-x: auto;
      margin: 2rem 0;
      border-radius: 4px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }

    thead {
      background: var(--accent);
      color: var(--paper);
    }

    thead th {
      padding: 10px 14px;
      text-align: left;
      font-family: var(--mono);
      font-size: 0.7rem;
      letter-spacing: 0.08em;
      font-weight: 400;
    }

    tbody tr:nth-child(even) { background: var(--mist); }
    tbody tr:nth-child(odd) { background: #fff; }

    tbody td {
      padding: 9px 14px;
      border-bottom: 1px solid #e0dbd0;
      vertical-align: top;
      line-height: 1.6;
    }

    /* ── Math ── */
    .math-block {
      background: #fff;
      border-left: 3px solid var(--sage);
      padding: 1.2rem 1.5rem;
      margin: 1.5rem 0;
      overflow-x: auto;
      font-size: 1.05rem;
    }

    /* ── Blockquote / KPI ── */
    blockquote {
      border-left: 3px solid var(--earth);
      padding: 0.8rem 1.5rem;
      margin: 1.5rem 0;
      background: #faf7f0;
      font-style: italic;
      color: #555;
      font-size: 0.95rem;
    }

    .pull-quote {
      font-size: 1.4rem;
      font-style: italic;
      color: var(--accent);
      line-height: 1.5;
      border-top: 2px solid var(--sage);
      border-bottom: 2px solid var(--sage);
      padding: 1.5rem 0;
      margin: 2.5rem 0;
      text-align: center;
    }

    /* ── Gist link ── */
    .gist-link {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-family: var(--mono);
      font-size: 0.75rem;
      color: var(--sage);
      text-decoration: none;
      border-bottom: 1px dashed var(--sage);
      padding-bottom: 1px;
    }
    .gist-link:hover { color: var(--accent); }

    .note-box {
      background: var(--mist);
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 1rem 1.5rem;
      margin: 1.5rem 0;
      font-size: 0.9rem;
      color: #444;
    }

    hr {
      border: none;
      border-top: 1px solid var(--mist);
      margin: 2.5rem 0;
    }

    /* ── Footer ── */
    footer {
      background: var(--ink);
      color: #888;
      text-align: center;
      padding: 2rem;
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 0.15em;
    }

    /* ── Scroll to top ── */
    .back-top {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--accent);
      color: var(--paper);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 1.2rem;
      box-shadow: 0 2px 12px rgba(0,0,0,0.2);
      transition: background 0.2s;
    }
    .back-top:hover { background: var(--sage); }

    @media (max-width: 640px) {
      header { padding: 0 1rem; }
      .hero { padding: 3rem 1rem 2.5rem; }
      .content-wrapper { padding: 2rem 1rem 4rem; }
      h2 { font-size: 1.5rem; }
    }
  </style>
</head>
<body>

<!-- ════════════════ HEADER ════════════════ -->
<header>
  <span class="header-title">MBT55 — Climate & Scientific Overview</span>
  <div class="lang-toggle">
    <button class="lang-btn active" onclick="switchLang('en')" id="btn-en">EN</button>
    <button class="lang-btn" onclick="switchLang('ja')" id="btn-ja">日本語</button>
  </div>
</header>

<!-- ════════════════ HERO ════════════════ -->
<div class="hero">
  <!-- EN Hero -->
  <div id="hero-en" class="lang-section active">
    <div class="hero-label">White Paper · MBT55 · 2025</div>
    <h1>Comprehensive Overview of<br><em>Climate Change</em> and the<br>Scientific &amp; Applied Potential of MBT55</h1>
    <p class="hero-sub">A systems-level examination of microbial carbon cycle regeneration, circular economy design, and global implementation strategy.</p>
    <div class="pdf-links">
      <a href="slides_en.pdf" class="pdf-btn">
        <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 13h8v1H8v-1zm0 2h8v1H8v-1zm0 2h5v1H8v-1z"/></svg>
        Slides (EN) PDF
      </a>
      <a href="slides_ja.pdf" class="pdf-btn" style="background:#5a7a51;">
        <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 13h8v1H8v-1zm0 2h8v1H8v-1zm0 2h5v1H8v-1z"/></svg>
        スライド (日本語) PDF
      </a>
      <a href="https://gist.github.com/shimojok/b046b4105956ad2289d7f31efd8088d2" class="pdf-btn" style="background:#333;" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.009-.868-.013-1.703-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.463-1.11-1.463-.907-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.647.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0 1 12 6.836a9.59 9.59 0 0 1 2.504.337c1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.744 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>
        View on GitHub Gist
      </a>
    </div>
  </div>
  <!-- JA Hero -->
  <div id="hero-ja" class="lang-section">
    <div class="hero-label">白書 · MBT55 · 2025</div>
    <h1>気候変動と<em>MBT55</em>の<br>科学的・応用的ポテンシャル総覧</h1>
    <p class="hero-sub">微生物による炭素循環の再生、循環型経済の設計、そしてグローバル実装戦略に関するシステム的考察。</p>
    <div class="pdf-links">
      <a href="slides_ja.pdf" class="pdf-btn">
        <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 13h8v1H8v-1zm0 2h8v1H8v-1zm0 2h5v1H8v-1z"/></svg>
        スライド (日本語) PDF
      </a>
      <a href="slides_en.pdf" class="pdf-btn" style="background:#5a7a51;">
        <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 13h8v1H8v-1zm0 2h8v1H8v-1zm0 2h5v1H8v-1z"/></svg>
        Slides (EN) PDF
      </a>
      <a href="https://gist.github.com/shimojok/b046b4105956ad2289d7f31efd8088d2" class="pdf-btn" style="background:#333;" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.009-.868-.013-1.703-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.463-1.11-1.463-.907-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.647.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0 1 12 6.836a9.59 9.59 0 0 1 2.504.337c1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.744 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>
        GitHub Gist で見る
      </a>
    </div>
  </div>
</div>

<!-- ════════════════ MAIN CONTENT ════════════════ -->
<div class="content-wrapper">

  <!-- ══════════ ENGLISH ══════════ -->
  <div id="content-en" class="lang-section active">
    <nav class="chapter-nav" aria-label="Chapter navigation">
      <a href="#en-ch1">Ch.1 Introduction</a>
      <a href="#en-ch2">Ch.2 Carbon Cycle</a>
      <a href="#en-ch3">Ch.3 Sustainable Cycle</a>
      <a href="#en-ch4">Ch.4 Impact</a>
      <a href="#en-ch5">Ch.5 Policy &amp; Roadmap</a>
    </nav>

    <!-- Chapter 1 -->
    <section class="chapter" id="en-ch1">
      <div class="chapter-number">Chapter 01</div>
      <h2>Introduction: Earth System Crisis and Redefining Circular Structures</h2>

      <h3>1.1 The Future of Global Carbon Removal and Agriculture</h3>
      <p>In the 21st century, the Earth system is approaching a critical tipping point due to the breakdown of the carbon, nitrogen, and water cycles and the degradation of biodiversity.</p>
      <p>Climate change, soil degradation, food security, and health disparities can no longer be treated as separate issues; they must be understood integrally as a single <strong>"Metabolic Crisis."</strong></p>
      <p>Internationally, entities like Vaulted Deep, Charm Industrial, and various Biochar consortiums are implementing carbon removal technologies. However, many of these are physical or chemical sequestration methods based on single processes and do not lead to the regeneration of the entire ecosystem.</p>
      <p>In contrast, <strong>MBT55 (Microbial BioTransformation 55)</strong> is based on the comprehensive metabolic network of a microbial consortium. It is an attempt to reconnect the biosphere's self-repair capabilities back into social systems by re-integrating the carbon, nitrogen, phosphorus, and water cycles as an <em>"ecological hyper-cycle."</em></p>
      <p>MBT55 transcends the dualism between decomposition and fixation, oxidation and reduction, the individual and the environment, nature and technology. By redesigning the flow of electrons (Electron Flow), it achieves the <strong>"simultaneity of decomposition = generation."</strong></p>
      <p>This circular model serves as a prototype for a civilizational paradigm shift spanning agriculture, health, energy, resources, and education.</p>

      <h3>1.2 Human Challenges and the Positioning of MBT55</h3>
      <p>With the global population projected to reach 9.7 billion by 2050, dependence on chemical fertilizers and fossil fuels to improve agricultural productivity is increasing, and Soil Organic Carbon (SOC) is rapidly declining. Meanwhile, waste treatment and food loss account for approximately 10% of global greenhouse gas (GHG) emissions.</p>
      <p>All of these issues stem from a social structure that is disconnected from nature's metabolic system. MBT55 is a <strong>"microbial ecosystem-based metabolic reconnection model"</strong> that repairs this disconnect, delivering a threefold effect:</p>
      <ol>
        <li><strong>Scientific Reconnection:</strong> Restores the natural balance of decomposition and fixation by reconstructing electron, elemental, and metabolic pathways.</li>
        <li><strong>Social Reconnection:</strong> Integrates agriculture, waste, health, and education to build a circular economy at the community level.</li>
        <li><strong>Economic Reconnection:</strong> Achieves the simultaneous creation of carbon credits and cost reduction through the MBT55 fermentation process.</li>
      </ol>
      <p>The framework that embodies this integrated model is the <strong>M³-BioSynergy System</strong>, a function possessed by the MBT55 microbial consortium. Its scientific basis will be demonstrated in the next chapter.</p>
    </section>

    <!-- Chapter 2 -->
    <section class="chapter" id="en-ch2">
      <div class="chapter-number">Chapter 02</div>
      <h2>Reconstructing the Carbon Cycle with the MBT55 Microbial Consortium</h2>

      <h3>2.1 Introduction: Theoretical Background of Carbon Cycle Disruption and Regeneration</h3>
      <p>The Earth's carbon cycle is a massive self-organizing system built upon the interaction of the biosphere, atmosphere, hydrosphere, and lithosphere. Since the Industrial Revolution, its equilibrium has been significantly disturbed by anthropogenic activities, leading to a continued decline in Soil Organic Carbon (SOC) and a rise in atmospheric CO₂ concentration.</p>
      <p>The primary causes of this disruption in agriculture include the excessive use of chemical fertilizers and pesticides, soil disturbance from tillage, and a decline in microbial diversity due to monoculture.</p>
      <p>The MBT55 microbial consortium is an ecosystem engineering technology aimed at regenerating this broken carbon cycle through a <strong>microbial self-repair mechanism</strong>. MBT55 achieves both an increase in SOC and a reduction in GHG emissions by comprehensively reconstructing the elemental cycles of carbon, nitrogen, phosphorus, sulfur, and iron.</p>

      <div class="note-box">
        📄 For detailed information including formulas and full tables, please refer to the complete document:<br>
        <a href="https://gist.github.com/shimojok/b046b4105956ad2289d7f31efd8088d2" class="gist-link" target="_blank" rel="noopener">Comprehensive Overview of Climate Change and the Scientific &amp; Applied Potential of MBT55 · GitHub Gist</a>
      </div>

      <h3>2.2 Ecological Composition and Functional Differentiation of the MBT55 Microbial Consortium</h3>
      <p>MBT55 is composed of diverse, naturally-derived decomposer groups at a ratio of <strong>55% aerobic to 45% anaerobic</strong>. This ratio mimics the redox balance in soil ecosystems and regenerates the natural process of <em>organic matter decomposition → electron transfer → nitrogen fixation → carbon stabilization</em>.</p>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Functional Group</th><th>Main Metabolic Pathway</th><th>Representative Genera</th><th>Functional Characteristics</th></tr>
          </thead>
          <tbody>
            <tr><td>Starch Decomposers</td><td>Amylase pathway, Saccharification</td><td><em>Bacillus subtilis, Paenibacillus sp.</em></td><td>Polysaccharide decomposition, Saccharification, Fatty acid → Acetyl-CoA</td></tr>
            <tr><td>Protein Decomposers</td><td>Protease system, Amino acid deamination</td><td><em>Pseudomonas sp., Bacillus licheniformis</em></td><td>Organic nitrogen supply, Ammonia generation</td></tr>
            <tr><td>Lipid Decomposers</td><td>Lipase, β-oxidation system</td><td><em>Acinetobacter sp., Rhodococcus sp.</em></td><td>Electron donor generation, High-energy supply</td></tr>
            <tr><td>Cellulose Decomposers</td><td>Cellulase group, Lignin oxidation</td><td><em>Cellulomonas sp., Streptomyces sp.</em></td><td>Promotes carbon fixation of recalcitrant organics, SOC precursor generation</td></tr>
            <tr><td>Aerobic Group (55%)</td><td>Oxidative respiration</td><td>CO₂ generation / Electron transfer</td><td>pH control, Redox buffering</td></tr>
            <tr><td>Anaerobic Group (45%)</td><td>Fermentation, Denitrification, Reduction</td><td>CH₄ suppression / NH₄⁺ regeneration</td><td>Carbon stabilization, Methane control</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Other Main Microbial Classifications</th><th>Main Genera</th><th>Functional Characteristics</th></tr>
          </thead>
          <tbody>
            <tr><td>Nitrogen-Fixing Bacteria</td><td><em>Azotobacter vinelandii, Rhizobium spp.</em></td><td>N₂ fixation, Ammonia generation</td></tr>
            <tr><td>Lactic Acid Bacteria Group</td><td><em>Lactobacillus plantarum, Leuconostoc mesenteroides</em></td><td>pH control, Antimicrobial substance production</td></tr>
            <tr><td>Photosynthetic Bacteria</td><td><em>Rhodopseudomonas palustris, Chromatium vinosum</em></td><td>Electron donor generation, Organic acid metabolism</td></tr>
            <tr><td>Methane-Oxidizing Bacteria</td><td><em>Methylosinus trichosporium</em></td><td>Methane → CO₂ oxidation, GHG reduction</td></tr>
          </tbody>
        </table>
      </div>

      <h3>2.2 Features of the MBT55 / M³-BioSynergy System</h3>
      <p><em>(Reading: M-Cube BioSynergy System)</em></p>
      <ol>
        <li><strong>Microbial Symbiotic Network:</strong> A collaborative relationship formed by 120 species of microbes.</li>
        <li><strong>Nutrient Cascade:</strong> The flow of substrates being decomposed in stages.</li>
        <li><strong>Ecological Hyper-cycle:</strong> A self-circulating dynamic equilibrium.</li>
      </ol>

      <h4>2.2.1 Electron Donors and Carbon Fixation Ratios</h4>
      <p>The core of MBT55 is the non-linear relationship between electron donor generation efficiency (E<sub>d</sub>) and the fixed carbon ratio (C<sub>f</sub>). This reverses the CO₂ release caused by conventional oxidative decomposition, redirecting the electron flow towards organic carbon fixation.</p>
      <div class="math-block">
        \[ C_f = \lambda \cdot \frac{E_d}{E_d + K_m} \]
        <p style="margin-top:0.8rem;font-size:0.9rem;color:#555;">Where λ is the maximum fixation rate, and K<sub>m</sub> is the electron saturation constant.</p>
      </div>

      <h4>2.2.2 SOC Formation Model: Mathematical Structure</h4>
      <div class="math-block">
        \[ \frac{dC_s}{dt} = I - k_d \cdot C_s + f_m(\text{MBT55}) \cdot \eta \]
        <ul style="margin-top:0.8rem;font-size:0.9rem;color:#555;list-style:none;margin-left:0;">
          <li>C<sub>s</sub>: Soil organic carbon (t-C/ha) &nbsp;|&nbsp; I: Organic matter input &nbsp;|&nbsp; k<sub>d</sub>: Decomposition constant</li>
          <li>f<sub>m</sub>(MBT55): Carbon stabilization function (0–1) &nbsp;|&nbsp; η: Electron re-fixation efficiency (0.2–0.8)</li>
        </ul>
      </div>
      <p>In simulations, the SOC accumulation rate increased <strong>1.8 to 2.6 times</strong> compared to conventional compost treatment. Carbon fixation is most stable under conditions of C/N ratio 20–25 and soil pH 6.5–7.2.</p>

      <h4>2.2.3 Metabolic Pathway Network and Electron Flow Reconstruction</h4>
      <p>The fundamental principle of MBT55 is <em>"to reconnect the flow of electrons to its natural direction."</em> In the MBT55 consortium, the diversity of electron acceptors and the collaboration of redox enzyme groups generate reverse reaction pathways where electrons are re-fixed into organic matter.</p>
      <div class="math-block">
        \[ J_{e^-} = \sum_i (k_i \cdot [S_i] \cdot \phi_i) \]
      </div>
      <p>This complementary metabolic structure is what fundamentally distinguishes MBT55 from conventional compost bacteria or EM bacteria. Experimentally, carbon content increased by an average of <strong>3.7%</strong> in MBT55-fermented products, enabling long-term carbon sequestration (&gt;100-year scale) through the formation of suberin, lignin, and humic acid structures.</p>

      <h4>2.2.4 Comparative Analysis (vs. Conventional Compost, Biochar, Enzyme Compost)</h4>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Technology</th><th>Carbon Fixation</th><th>Microbial Diversity</th><th>Economics</th><th>Notes</th></tr>
          </thead>
          <tbody>
            <tr><td>Conventional Compost</td><td>★☆☆</td><td>★★☆</td><td>★★★</td><td>Decomposition-dominant, low stability</td></tr>
            <tr><td>Biochar</td><td>★★★</td><td>★☆☆</td><td>★★☆</td><td>High carbon stability, limited biological function</td></tr>
            <tr><td>Enzyme Compost</td><td>★★☆</td><td>★★☆</td><td>★★☆</td><td>High organic conversion but short-term</td></tr>
            <tr><td><strong>MBT55</strong></td><td><strong>★★★★★</strong></td><td><strong>★★★★★</strong></td><td><strong>★★★★★</strong></td><td>Integration of biological, chemical &amp; physical processes</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Chapter 3 -->
    <section class="chapter" id="en-ch3">
      <div class="chapter-number">Chapter 03</div>
      <h2>MBT Sustainable Cycle Model</h2>
      <p><em>Microbial Ecosystem-based Circular Economy Implementation and Social Recursivity</em></p>

      <h3>3.1 Basic Principles of Model Design</h3>
      <p>The <strong>MBT Sustainable Cycle (MSC)</strong>, composed of MBT55 bacteria and the MBT fermentation machine, is an "eco-economic system" that integrates material circulation, information circulation, and economic circulation, based on the hypercycle structure of microbial ecosystems.</p>
      <p>MSC is a resource conversion system that uses MBT55 to completely ferment and decompose many organic substances within 24 hours, generating useful metabolites.</p>
      <p><strong>Materials MBT55 can ferment and decompose:</strong> Agricultural waste, marine product residues, processed food waste, livestock and dairy excretions, forestry waste, disaster waste (trees, driftwood), sewage sludge, apparel waste (excluding some synthetic fibers), cardboard waste, and more.</p>
      <p><strong>Materials that can be generated by MSC:</strong> Functional compost, fermented fertilizer, humus, functional feed (livestock/aquaculture), medical materials, functional food ingredients, human probiotics, animal probiotics.</p>

      <h3>3.2 Biological Cycle Centered on MBT55</h3>
      <p>MBT55 comprises approximately 55 types of decomposition, fixation, and metabolic microorganisms including aerobic and anaerobic species. The four main functional blocks that form the MSC foundation are:</p>
      <ol>
        <li><strong>C-Decomposition Block:</strong> Decomposes organics (cellulose, proteins, lipids, starch) into diverse carbon sources.</li>
        <li><strong>N-Cycle Block:</strong> Nitrogen-fixing, nitrifying, and denitrifying bacteria collaborate to form NH₃ ⇄ NO₂⁻ ⇄ NO₃⁻ cycles.</li>
        <li><strong>Redox Mediation Block:</strong> Mediates electron transfer in microbial metabolism, maintaining redox reactions even under anaerobic conditions.</li>
        <li><strong>Symbiotic Network Block:</strong> Membrane structure for material and information transfer between microorganisms.</li>
      </ol>

      <h3>3.3 Eco-Hypercycle: Mapping to Socioeconomic Structure</h3>
      <p>MSC transfers the ecological hypercycle to social and economic systems through three mutually circulating layers:</p>
      <ul>
        <li><strong>Biophysical Cycle:</strong> Waste → decomposition → regenerated resources → agricultural/energy use</li>
        <li><strong>Bio-Informatic Cycle:</strong> Integrated analysis of microbial data, weather, and production data for optimal control</li>
        <li><strong>Eco-Financial Cycle:</strong> Carbon credits, green premiums, and regenerated fertilizer values quantified</li>
      </ul>
    </section>

    <!-- Chapter 4 -->
    <section class="chapter" id="en-ch4">
      <div class="chapter-number">Chapter 04</div>
      <h2>Implementation Results and Multi-Dimensional Impact Evaluation</h2>

      <h3>4.1 Environmental Impact: CO₂ Reduction and Ecosystem Regeneration</h3>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Indicator</th><th>Conventional Farming</th><th>After MSC Introduction</th><th>Improvement Rate</th></tr>
          </thead>
          <tbody>
            <tr><td>SOC Formation Rate (%/year)</td><td>0.6</td><td>1.3</td><td>+116%</td></tr>
            <tr><td>CO₂ Absorption Equivalent (t/ha/year)</td><td>1.2</td><td>2.4</td><td>+100%</td></tr>
            <tr><td>Methane Generation Reduction (%)</td><td>—</td><td>42–57</td><td>—</td></tr>
          </tbody>
        </table>
      </div>
      <p>These figures are equivalent to the <strong>top 2%</strong> of the "Regenerative Agriculture Model" indicated by the United Nations FAO.</p>
      <p>Water retention and fertilizer retention of soil improved by an average of <strong>+21%</strong>. Ammonia volatilization rate decreased by <strong>−48%</strong> and nitrate runoff rate by <strong>−37%</strong> compared to conventional methods.</p>

      <h3>4.3 Social Impact: Health, Employment, and Knowledge Circulation</h3>
      <h4>Health and Nutritional Improvement</h4>
      <p>The reCLA-MSC fermentation system contributes to improving maternal and child nutrition in developing countries and preventing lifestyle-related diseases. MBT55 metabolizes dietary fiber, polyphenols, and other nutrients to generate short-chain fatty acids and other useful substances (MBT Food Probiotics), improving intestinal environment and contributing to metabolic improvement.</p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Item</th><th>Impact</th><th>Main Outcomes</th></tr>
          </thead>
          <tbody>
            <tr><td>Intestinal Environment Improvement Rate</td><td>+32–48%</td><td>Supply of MBT-derived probiotics</td></tr>
            <tr><td>Nutritional Intake Balance</td><td>+21%</td><td>Mineral recovery in local crops</td></tr>
            <tr><td>Health Indicators (BMI, HbA1c)</td><td>+17–25%</td><td>Individual optimization based on phenotyping data</td></tr>
          </tbody>
        </table>
      </div>
      <p>The estimated <strong>medical cost reduction effect is approximately 120 USD per person per year</strong> in the region.</p>

      <h4>Employment Creation and Social Inclusion</h4>
      <p>MSC creates new employment in 6 sectors: waste processing, fermentation, resource conversion, logistics, healthcare, and education. In Kenya, an average increase of <strong>820 jobs/year</strong> per pilot district is expected, with <strong>42% being women and young people</strong>.</p>

      <h3>4.4 Economic Impact: Value by Circulation</h3>
      <p>In MSC-introduced regions, premiums of an average <strong>+18–22% over market price</strong> are formed for regenerated fertilizer and carbon-neutral agricultural products.</p>
      <div class="math-block">
        \[ V_{gp} = (C_{red} + N_{fix}) \times P_c \]
        <p style="margin-top:0.8rem;font-size:0.9rem;color:#555;">Where P<sub>c</sub> = average carbon market price (65 USD/t). Generates <strong>200–240 USD additional revenue per hectare per year</strong>.</p>
      </div>
      <p>Carbon Loop Bonds based on MSC are estimated at an annual yield of <strong>4.5–6.0%</strong> with a risk coefficient of 0.62.</p>

      <h3>4.5 Integrated Sustainability Index</h3>
      <div class="math-block">
        \[ SI = w_1 E + w_2 S + w_3 Ec \]
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Parameter</th><th>Meaning</th><th>Weight (w)</th></tr></thead>
          <tbody>
            <tr><td>E</td><td>Environmental contribution (CO₂ reduction, SOC formation)</td><td>0.40</td></tr>
            <tr><td>S</td><td>Social contribution (health, employment, education)</td><td>0.35</td></tr>
            <tr><td>Ec</td><td>Economic contribution (income, investment, market value)</td><td>0.25</td></tr>
          </tbody>
        </table>
      </div>
      <p>The comprehensive SI in MSC implementation regions is <strong>0.84 (max = 1.0)</strong>, significantly exceeding the international SDG score (average 0.63).</p>

      <div class="pull-quote">"From Carbon Neutrality to Carbon Intelligence."<br><span style="font-size:0.8em;font-style:normal;color:#777;">— MBT Sustainable Cycle is not only a solution, but a new form of co-evolution.</span></div>
    </section>

    <!-- Chapter 5 -->
    <section class="chapter" id="en-ch5">
      <div class="chapter-number">Chapter 05</div>
      <h2>Policy Proposals and Implementation Roadmap</h2>
      <p><em>Global Agri-Regeneration Initiative Based on the MBT Sustainable Cycle</em></p>

      <h3>5.2 Proposal Objectives and Strategic Significance</h3>
      <ol>
        <li><strong>Achieving Decarbonization and Food Security Simultaneously</strong> — Realizing concurrent CO₂ reduction and agricultural profit growth through regenerative agriculture.</li>
        <li><strong>Correcting Health Disparities and Linking Molecular Nutrition Data</strong> — Deploying disease risk prevention on a global scale using gut microbiome data via the HealthBook AI.</li>
        <li><strong>Building a Recursive Economy</strong> — Establishing a social model where carbon, nutrition, knowledge, and capital mutually circulate.</li>
      </ol>

      <h3>5.3 Strategic Partners and Synergistic Structure</h3>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Field</th><th>Agent</th><th>Role</th><th>Collaboration Model</th></tr>
          </thead>
          <tbody>
            <tr><td>Science / Tech</td><td>Leading agricultural research organizations</td><td>AI × Microbial analysis, cloud-based data linkage</td><td>AGRIX Platform Integration</td></tr>
            <tr><td>Agriculture / Ecology</td><td>CGIAR / AGRA / FAO</td><td>Regenerative agriculture, Soil regeneration programs</td><td>MBT Field Pilot &amp; Carbon Bank</td></tr>
            <tr><td>Health / Nutrition</td><td>HealthBook / WHO</td><td>Sharing and application of phenotyping data</td><td>MBT-HealthLink Project</td></tr>
            <tr><td>Finance / Investment</td><td>International development finance institutions / Green Climate Fund</td><td>Design and issuance of Carbon Loop Bonds</td><td>Carbon Loop Finance Initiative</td></tr>
            <tr><td>Education / Society</td><td>UNESCO / Global Schools Network</td><td>Ecological literacy education</td><td>Eco-Intelligence Curriculum</td></tr>
          </tbody>
        </table>
      </div>

      <h3>5.4 Implementation Roadmap (Phases 1–5)</h3>
      <h4>Phase 1: Scientific Foundation Establishment (2025–2026)</h4>
      <p>Metagenome analysis and AI mapping of the MBT55 consortium (on cloud AI infrastructure). Global standardization of SOC change and GHG reduction coefficients. Joint development of carbon credit calculation methodology.</p>
      <blockquote>KPIs: Establishment of SOC formation coefficient with ±0.03 accuracy / 2+ carbon market registrations.</blockquote>

      <h4>Phase 2: Pilot Deployment in Kenya, Rwanda, and India (2026–2028)</h4>
      <p>Regional data integration via the AGRIX Platform. Implementation of triple-helix collaboration model (farmers, local government, educational institutions). Localization of MBT fermented fertilizer production.</p>
      <blockquote>KPIs: 20,000 ha of target farmland / 84,000 t-CO₂ reduction / 5,000 jobs created.</blockquote>

      <h4>Phase 3: International Standardization and Financial Productization (2028–2030)</h4>
      <p>International certification of the Carbon Loop Bond. ISO standardization. Development of investment evaluation index (ESG + BioCircular Value Index).</p>
      <blockquote>KPIs: Stable operational model with 4.5–6% annual yield / 3+ ESG fund registrations.</blockquote>

      <h4>Phase 4: Decentralized AI Management Network (2030–2035)</h4>
      <p>Real-time management of MBT Field Data via cloud AI. Construction of an <strong>"Earth Microbial Brain"</strong> integrating local fermentation processes, climate, and health data.</p>
      <blockquote>KPIs: Fully automated carbon accounting system / 98%+ uptime for cloud-linked platform.</blockquote>

      <h4>Phase 5: Global Expansion and Intellectual Ecosystemization (2035–2050)</h4>
      <p>Connecting regional MBT centers as "Eco-Intelligence Hubs." Formation of <strong>BioNexus³</strong> through mutual circulation of education, economic, environmental, and health data.</p>
      <blockquote>KPIs: 100 million t-CO₂/year in carbon removal / 50+ participating countries / +2.8% GDP impact.</blockquote>

      <h3>5.6 Projected Outcomes (5-Year Cumulative)</h3>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Metric</th><th>Value</th><th>Remarks</th></tr></thead>
          <tbody>
            <tr><td>Carbon Reduction</td><td>480,000 t-CO₂</td><td>Total for 3 pilot regions</td><td>Registrable as credits</td></tr>
            <tr><td>Job Creation</td><td>26,000 people</td><td>Incl. local processing, fermentation, education</td><td>42% female employment</td></tr>
            <tr><td>Medical Cost Reduction</td><td>12.0 Million USD/year</td><td>Health improvement effect</td><td>vs. WHO standards</td></tr>
            <tr><td>Economic Effect</td><td>GDP +2.8%</td><td>Contribution to regional gross product</td><td>Incl. multiplier effect</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pull-quote">"From Net Zero to Bio-Positive."<br><span style="font-size:0.8em;font-style:normal;color:#777;">— MBT Sustainable Cycle presents a living pathway toward a regenerative future.</span></div>
    </section>
  </div><!-- /content-en -->

  <!-- ══════════ JAPANESE ══════════ -->
  <div id="content-ja" class="lang-section">
    <nav class="chapter-nav" aria-label="章ナビゲーション">
      <a href="#ja-ch1">第1章 序論</a>
      <a href="#ja-ch2">第2章 炭素循環</a>
      <a href="#ja-ch3">第3章 持続可能サイクル</a>
      <a href="#ja-ch4">第4章 インパクト評価</a>
      <a href="#ja-ch5">第5章 政策・ロードマップ</a>
    </nav>

    <!-- 第1章 -->
    <section class="chapter" id="ja-ch1">
      <div class="chapter-number">第1章</div>
      <h2>序論：地球システム危機と循環構造の再定義</h2>

      <h3>1.1 世界の炭素除去と農業の未来</h3>
      <p>21世紀の地球システムは、<strong>炭素・窒素・水循環の破綻</strong>と<strong>生物多様性の劣化</strong>によって臨界点に接近している。気候変動、土壌劣化、食料安全保障、健康格差は、もはや個別の課題ではなく、<strong>一つの「代謝危機」</strong>として統合的に捉える必要がある。</p>
      <p>国際的には、Vaulted Deep、Charm Industrial、Biochar連合体などが炭素除去技術の実装を進めているが、これらの多くは<strong>単一プロセスによる物理・化学的隔離</strong>であり、生態系全体の再生には至っていない。</p>
      <p>これに対し、<strong>MBT55（Microbial BioTransformation 55）</strong>は、微生物群の総合的代謝ネットワークを基盤とし、炭素・窒素・リン・水の循環を<em>「生態的ハイパーサイクル」</em>として再統合することで、<strong>生物圏の自己修復能力</strong>を社会的システムの中に再接続する試みである。</p>
      <p>MBT55は、分解と固定、酸化と還元、個体と環境、自然と技術の二項対立を超え、<strong>電子の流れ（Electron Flow）を再設計する</strong>ことで、「分解＝生成」の同時性を実現する。この循環モデルは、農業・健康・エネルギー・資源・教育に跨る<strong>文明構造転換のプロトタイプ</strong>となる。</p>

      <h3>1.2 人類の課題とMBT55の位置づけ</h3>
      <p>世界人口が2050年に97億人に達すると予測される中、農業生産性向上のための化学肥料・化石燃料依存が進行し、土壌炭素（SOC）は急速に減少している。一方で、廃棄物処理や食料ロスは世界の温室効果ガス（GHG）排出の約10％を占める。</p>
      <p>これらはすべて、<strong>自然の代謝系から切り離された社会構造</strong>に起因している。MBT55はこの断絶を修復する<strong>「微生物生態系ベースの代謝再接続モデル」</strong>であり、次の三重の効果をもたらす：</p>
      <ol>
        <li><strong>科学的再接続（Scientific Reconnection）：</strong>電子・元素・代謝経路の再構築により、自然界の分解・固定バランスを復元。</li>
        <li><strong>社会的再接続（Social Reconnection）：</strong>農業・廃棄物・健康・教育を統合し、地域単位で循環経済を構築。</li>
        <li><strong>経済的再接続（Economic Reconnection）：</strong>MBT55発酵プロセスによる炭素クレジット創出とコスト削減の同時達成。</li>
      </ol>
      <p>この統合モデルを具体化する枠組みが、MBT55微生物群がもつ機能である<strong>M³-BioSynergy System</strong>であり、次章でその科学的基盤を示す。</p>
    </section>

    <!-- 第2章 -->
    <section class="chapter" id="ja-ch2">
      <div class="chapter-number">第2章</div>
      <h2>MBT55微生物群によるカーボン循環再構築</h2>

      <h3>2.1 序論：炭素循環の断絶と再生の理論的背景</h3>
      <p>地球の炭素循環は、生物圏・大気圏・水圏・岩石圏の相互作用によって構築された巨大な自己組織化系である。その均衡は産業革命以降、人為的活動によって著しく攪乱され、土壌中の有機炭素（SOC）は減少し、大気中のCO₂濃度は上昇を続けている。</p>
      <p>MBT55微生物群は、この断絶した炭素循環を<strong>微生物的自己修復機構</strong>によって再生させることを目的とする生態系設計技術である。炭素・窒素・リン・硫黄・鉄などの元素循環を統合的に再構築することにより、SOCの増加と温室効果ガス（GHG）排出削減の双方を実現する。</p>

      <h3>2.2 MBT55微生物群の生態学的構成と機能分化</h3>
      <p>MBT55は、天然由来の多様な分解菌群を<strong>好気性55%／嫌気性45%</strong>の比率で構成する。この比率は、土壌生態系における酸化還元バランスを模倣するものであり、<em>有機物分解 → 電子移動 → 窒素固定 → 炭素安定化</em>という自然的プロセスを再生する。</p>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>機能群</th><th>主な代謝経路</th><th>代表属例</th><th>機能特性</th></tr>
          </thead>
          <tbody>
            <tr><td>でんぷん分解菌群</td><td>アミラーゼ経路、糖化経路</td><td><em>Bacillus subtilis, Paenibacillus sp.</em></td><td>ポリサッカライド分解、糖化、脂肪酸→アセチルCoA</td></tr>
            <tr><td>タンパク質分解菌群</td><td>プロテアーゼ系、アミノ酸脱アミノ化</td><td><em>Pseudomonas sp., Bacillus licheniformis</em></td><td>有機窒素供給・アンモニア生成</td></tr>
            <tr><td>脂質分解菌群</td><td>リパーゼ・β酸化系、トリアシルグリセロール分解</td><td><em>Acinetobacter sp., Rhodococcus sp.</em></td><td>電子供与体生成・高エネルギー供給</td></tr>
            <tr><td>セルロース分解菌群</td><td>セルラーゼ群、リグニン酸化経路</td><td><em>Cellulomonas sp., Streptomyces sp.</em></td><td>難分解性有機物の炭素固定促進、SOC前駆体生成</td></tr>
            <tr><td>好気性群（55%）</td><td>酸化的呼吸</td><td>CO₂生成／電子移動</td><td>pH制御・酸化還元緩衝</td></tr>
            <tr><td>嫌気性群（45%）</td><td>発酵・脱硝・還元</td><td>CH₄抑制／NH₄⁺再生</td><td>炭素安定化・メタン制御</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>その他の主な微生物分類</th><th>主な属例</th><th>機能特性</th></tr>
          </thead>
          <tbody>
            <tr><td>窒素固定菌</td><td><em>Azotobacter vinelandii, Rhizobium spp.</em></td><td>N₂固定、アンモニア生成</td></tr>
            <tr><td>乳酸菌群</td><td><em>Lactobacillus plantarum, Leuconostoc mesenteroides</em></td><td>pH制御、抗菌物質生産</td></tr>
            <tr><td>光合成細菌</td><td><em>Rhodopseudomonas palustris, Chromatium vinosum</em></td><td>電子供与体生成、有機酸代謝</td></tr>
            <tr><td>メタン酸化菌</td><td><em>Methylosinus trichosporium</em></td><td>メタン→CO₂酸化、温室効果ガス削減</td></tr>
          </tbody>
        </table>
      </div>

      <h3>2.2 MBT55/M³-BioSynergy Systemの特徴</h3>
      <p><em>（読み：エムキューブ バイオシナジーシステム）</em></p>
      <ol>
        <li><strong>微生物共生ネットワーク：</strong>120種の菌が形成する協働関係</li>
        <li><strong>栄養カスケード：</strong>基質が段階的に分解される流れ</li>
        <li><strong>生態学的ハイパーサイクル：</strong>自己循環型の動的平衡</li>
      </ol>

      <h4>2.2.1 電子供与体と炭素固定比率</h4>
      <p>MBT55のコアとなるのは、<strong>電子供与体生成効率 (E<sub>d</sub>)</strong> と<strong>固定炭素比 (C<sub>f</sub>)</strong> の非線形関係である。これにより、従来の酸化的分解がもたらすCO₂放出を逆転させ、<strong>電子の流れを有機炭素固定へ転換</strong>する。</p>
      <div class="math-block">
        \[ C_f = \lambda \cdot \frac{E_d}{E_d + K_m} \]
        <p style="margin-top:0.8rem;font-size:0.9rem;color:#555;">ここで、λ は最大固定率、K<sub>m</sub> は電子飽和定数を示す。</p>
      </div>

      <h4>2.2.2 SOC形成モデル：数理的構造とパラメータ設定</h4>
      <div class="math-block">
        \[ \frac{dC_s}{dt} = I - k_d \cdot C_s + f_m(\text{MBT55}) \cdot \eta \]
        <ul style="margin-top:0.8rem;font-size:0.9rem;color:#555;list-style:none;margin-left:0;">
          <li>C<sub>s</sub>：土壌中の有機炭素量（t-C/ha）　|　I：有機物供給量　|　k<sub>d</sub>：分解定数（年⁻¹）</li>
          <li>f<sub>m</sub>(MBT55)：炭素安定化関数（0–1）　|　η：電子再固定効率（0.2–0.8）</li>
        </ul>
      </div>
      <p>シミュレーションでは、通常の堆肥処理と比較して<strong>SOC蓄積率が1.8〜2.6倍</strong>に増加した。特にC/N比20〜25、土壌pH6.5〜7.2の条件下で、炭素固定が最も安定している。</p>

      <h4>2.2.3 代謝経路ネットワークと電子フロー再構築</h4>
      <p>MBT55の基幹原理は、「電子の流れを自然界の方向性に再接続すること」である。MBT55群では、電子受容体の多様性と酸化還元酵素群の協働により、<strong>電子が有機物中に再固定される逆反応経路</strong>を生成する。</p>
      <div class="math-block">
        \[ J_{e^-} = \sum_i (k_i \cdot [S_i] \cdot \phi_i) \]
      </div>
      <p>実験的には、MBT55発酵後の生成物において、炭素含有量が平均<strong>3.7％増加</strong>し、C/N比が安定することが確認されている。この炭素増加は、<strong>スベリン・リグニン・フミン酸構造体の生成</strong>に起因し、土壌中の長期炭素隔離（&gt;100年スケール）を可能にする。</p>

      <h4>2.2.4 MBT55の比較分析</h4>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>技術</th><th>炭素固定効率</th><th>微生物多様性</th><th>経済性</th><th>備考</th></tr>
          </thead>
          <tbody>
            <tr><td>通常堆肥</td><td>★☆☆</td><td>★★☆</td><td>★★★</td><td>分解優位、安定性低</td></tr>
            <tr><td>バイオ炭</td><td>★★★</td><td>★☆☆</td><td>★★☆</td><td>炭素安定性高いが生物機能限定</td></tr>
            <tr><td>酵素添加堆肥</td><td>★★☆</td><td>★★☆</td><td>★★☆</td><td>有機変換効率は高いが短期的</td></tr>
            <tr><td><strong>MBT55</strong></td><td><strong>★★★★★</strong></td><td><strong>★★★★★</strong></td><td><strong>★★★★★</strong></td><td>生物・化学・物理プロセスの統合</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 第3章 -->
    <section class="chapter" id="ja-ch3">
      <div class="chapter-number">第3章</div>
      <h2>MBT Sustainable Cycle モデル</h2>
      <p><em>― 微生物生態系に基づく循環経済の実装と社会的再帰性 ―</em></p>

      <h3>3.1 モデル設計の基本原理</h3>
      <p>MBT55菌体とMBT発酵機で構成される<strong>MBT Sustainable Cycle（MSC）</strong>は、微生物生態系のハイパーサイクル構造を基盤とし、物質循環・情報循環・経済循環を一体化した「生態経済システム」である。</p>
      <p>MSCは、MBT55により多くの有機性物質を<strong>24時間で完全に発酵・分解</strong>させ、有用な代謝物を生成する資源化システムである。</p>
      <p><strong>MBT55が発酵・分解する物質：</strong>農産物廃棄物、海産物残渣、加工食品廃棄物、畜産・酪農などの家畜の排泄物、植林廃棄物、樹木や流木など災害廃棄物、上下水道の汚泥、一部の化学繊維を除くアパレル廃棄物、段ボールなどの廃棄物、その他</p>
      <p><strong>MSCにより生成可能な資材：</strong>機能性堆肥、発酵肥料、腐植質、機能性飼料（畜産・養殖用）、医療用資材、機能性食品材料、人用プロバイオティクス、動物用プロバイオティクス</p>

      <h3>3.2 MBT55を中核とした生物学的サイクル</h3>
      <p>MBT55は、好気性／嫌気性を含む約55種類の分解・固定・代謝微生物から構成され、以下の四大機能ブロックによってMSCの基盤を形成する：</p>
      <ol>
        <li><strong>炭素分解ブロック（C-Decomposition）：</strong>有機物を多様な炭素源に分解し、CO₂・有機酸・糖類を生成。エネルギー代謝と有機残渣の再利用を可能にする。</li>
        <li><strong>窒素循環ブロック（N-Cycle）：</strong>窒素固定菌および硝化菌・脱窒菌が協働し、NH₃ ⇄ NO₂⁻ ⇄ NO₃⁻ の循環を形成。</li>
        <li><strong>電子供与体・受容体ブロック（Redox Mediation）：</strong>微生物代謝における電子移動を媒介し、嫌気条件下でも酸化還元反応を維持。</li>
        <li><strong>バイオフィルム・共生ネットワークブロック（Symbiotic Network）：</strong>微生物間の物質・情報伝達を行う膜構造。</li>
      </ol>

      <h3>3.3 社会経済構造への写像：エコ・ハイパーサイクル</h3>
      <p>MSCは、生態的ハイパーサイクルを社会・経済システムに転写するモデルである。次の三つのレイヤーが相互に循環し、外部入力を最小化しながら価値を増幅させる。</p>
      <ul>
        <li><strong>物質レイヤー（Biophysical Cycle）：</strong>廃棄物 → 分解 → 再生資源 → 農業・エネルギー利用</li>
        <li><strong>情報レイヤー（Bio-Informatic Cycle）：</strong>微生物データ・気象・生産データの統合解析による最適制御。クラウドAIシステムによる分散的データ同化を実装可能。</li>
        <li><strong>経済レイヤー（Eco-Financial Cycle）：</strong>炭素クレジット、グリーンプレミアム、再生肥料価値などを数値化。「循環による価値生成（Value by Circulation）」を原理とする。</li>
      </ul>
    </section>

    <!-- 第4章 -->
    <section class="chapter" id="ja-ch4">
      <div class="chapter-number">第4章</div>
      <h2>実装成果と多次元的インパクト評価</h2>

      <h3>4.1 環境インパクト：CO₂削減と生態系再生</h3>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>指標</th><th>従来農法</th><th>MSC導入後</th><th>改善率</th></tr>
          </thead>
          <tbody>
            <tr><td>SOC形成率（％/年）</td><td>0.6</td><td>1.3</td><td>+116%</td></tr>
            <tr><td>CO₂吸収換算（t/ha/年）</td><td>1.2</td><td>2.4</td><td>+100%</td></tr>
            <tr><td>メタン発生削減率（％）</td><td>ー</td><td>42〜57</td><td>ー</td></tr>
          </tbody>
        </table>
      </div>
      <p>これらは、国連FAOが示す「再生型農業モデル（Regenerative Agriculture）」の<strong>上位2%</strong>に匹敵する水準である。MBT群による有機分解により、土壌の保水性・保肥性は平均<strong>+21%</strong>向上。アンモニア揮散率は従来比<strong>−48%</strong>、硝酸塩流出率は<strong>−37%</strong>に低下。</p>

      <h3>4.3 社会インパクト：健康・雇用・知識循環の創出</h3>
      <h4>健康・栄養改善</h4>
      <p>MBT Food &amp; Herbal Probiotics専用の発酵システムであるreCLA-MSCは、途上国の母子栄養の改善、また、先進国も含めた生活習慣病の予防に貢献し、医療費の削減に寄与する。MBT55が食物繊維やポリフェノールなど有用な栄養素を代謝し、短鎖脂肪酸などの有用な物質であるMBT Food Probioticsを生成し、腸内環境を改善させることにより人の代謝改善に貢献する。</p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>項目</th><th>影響度</th><th>主な成果</th></tr>
          </thead>
          <tbody>
            <tr><td>腸内環境改善率</td><td>+32〜48%</td><td>MBT由来プロバイオティクスの供給</td></tr>
            <tr><td>栄養摂取バランス</td><td>+21%</td><td>地場作物のミネラル回復</td></tr>
            <tr><td>健康指標（BMI, HbA1c）改善</td><td>+17〜25%</td><td>フェノタイピングデータに基づく個別最適化</td></tr>
          </tbody>
        </table>
      </div>
      <p>地域の<strong>医療費削減効果は年間1人あたり約120USD</strong>と推定される。</p>

      <h4>雇用創出と社会的包摂</h4>
      <p>MSCは、廃棄物処理・発酵・再資源化・物流・ヘルスケア・教育の6セクターで新規雇用を生み出す。ケニアでは、パイロット地区あたり平均<strong>820人/年</strong>の雇用増が見込まれ、うち<strong>42%が女性・若年層</strong>である。</p>

      <h3>4.4 経済インパクト：循環による価値生成</h3>
      <p>MSC導入地域では、再生肥料およびカーボン・ニュートラル農産物に対し、平均<strong>市場価格＋18〜22%</strong>のプレミアムが形成される。</p>
      <div class="math-block">
        \[ V_{gp} = (C_{red} + N_{fix}) \times P_c \]
        <p style="margin-top:0.8rem;font-size:0.9rem;color:#555;">P<sub>c</sub>：炭素市場単価（平均65 USD/t）→ <strong>1haあたり年間200〜240USDの追加収益</strong>を創出。</p>
      </div>
      <p>MSCを基盤とするCarbon Loop Bondは、利回り年間<strong>4.5〜6.0%</strong>、リスク係数0.62と試算される。</p>

      <h3>4.5 統合的持続性評価モデル（Sustainability Index Model）</h3>
      <div class="math-block">
        \[ SI = w_1 E + w_2 S + w_3 Ec \]
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>パラメータ</th><th>意味</th><th>重み（w）</th></tr></thead>
          <tbody>
            <tr><td>E</td><td>環境貢献指数（CO₂削減, SOC形成）</td><td>0.40</td></tr>
            <tr><td>S</td><td>社会貢献指数（健康, 雇用, 教育）</td><td>0.35</td></tr>
            <tr><td>Ec</td><td>経済貢献指数（所得, 投資, 市場価値）</td><td>0.25</td></tr>
          </tbody>
        </table>
      </div>
      <p>MSC実装地域における総合SIは<strong>0.84（満点=1.0）</strong>であり、国際的SDGスコア（平均0.63）を大きく上回る。</p>

      <div class="pull-quote">「炭素中立から炭素知性へ（From Carbon Neutrality to Carbon Intelligence）」<br><span style="font-size:0.8em;font-style:normal;color:#777;">― MBT Sustainable Cycle is not only a solution, but a new form of co-evolution.</span></div>
    </section>

    <!-- 第5章 -->
    <section class="chapter" id="ja-ch5">
      <div class="chapter-number">第5章</div>
      <h2>政策提案と実装ロードマップ</h2>
      <p><em>― MBT Sustainable Cycle を基盤とする地球規模アグリ・リジェネレーション構想 ―</em></p>

      <h3>5.2 提案の目的と戦略的意義</h3>
      <ol>
        <li><strong>脱炭素と食料安全保障の両立：</strong>再生型農業を通じ、CO₂削減と農業収益の同時向上を実現。</li>
        <li><strong>健康格差の是正と分子栄養データ連携：</strong>HealthBook AIにより、腸内環境データを用いた疾患リスク予防を世界規模で展開。</li>
        <li><strong>再帰型経済（Circular Intelligence Economy）の構築：</strong>炭素、栄養、知識、資本が相互循環する社会モデルを確立。</li>
      </ol>

      <h3>5.3 戦略パートナーとシナジー構造</h3>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>分野</th><th>主体</th><th>役割</th><th>連携モデル</th></tr>
          </thead>
          <tbody>
            <tr><td>科学・技術</td><td>先導的農業研究機関</td><td>AI×Microbial解析、クラウド上でのデータ連携</td><td>AGRIX Platform Integration</td></tr>
            <tr><td>農業・生態系</td><td>CGIAR / AGRA / FAO</td><td>再生型農業・土壌再生プログラム</td><td>MBT Field Pilot &amp; Carbon Bank</td></tr>
            <tr><td>健康・栄養</td><td>HealthBook / WHO</td><td>フェノタイピングデータの共有・応用</td><td>MBT-HealthLink Project</td></tr>
            <tr><td>金融・投資</td><td>国際開発金融機関 / Green Climate Fund</td><td>カーボンループ債の設計・発行</td><td>Carbon Loop Finance Initiative</td></tr>
            <tr><td>教育・社会</td><td>UNESCO / Global Schools Network</td><td>生態リテラシー教育</td><td>Eco-Intelligence Curriculum</td></tr>
          </tbody>
        </table>
      </div>

      <h3>5.4 実装ロードマップ（Phase 1〜5）</h3>
      <h4>Phase 1：科学的基盤整備（2025–2026）</h4>
      <p>MBT55群のメタゲノム解析およびAIマッピング（クラウドAIインフラ上）。SOC変化・GHG削減係数のグローバル標準化。カーボンクレジット算定法の共同策定（Carbon Direct基準対応）。</p>
      <blockquote>成果指標（KPI）：SOC形成係数±0.03以内の精度確立／炭素市場登録2件以上</blockquote>

      <h4>Phase 2：ケニア・ルワンダ・インドにおけるパイロット展開（2026–2028）</h4>
      <p>AGRIX Platformによる地域データ統合。農家・自治体・教育機関のトリプル連携モデル実装。MBT発酵肥料および再生バイオチャー肥料の現地生産化。</p>
      <blockquote>成果指標：対象農地2万ha／炭素削減8.4万t-CO₂／雇用創出5,000人</blockquote>

      <h4>Phase 3：国際標準化と金融商品化（2028–2030）</h4>
      <p>カーボンループ債（Carbon Loop Bond）の国際認証。ISO化およびWTO農業条項との整合。投資評価指数（ESG + BioCircular Value Index）策定。</p>
      <blockquote>成果指標：年利4.5〜6%の安定運用モデル確立／ESG基金登録3件以上</blockquote>

      <h4>Phase 4：分散型AI管理ネットワーク（2030–2035）</h4>
      <p>MBT Field DataをクラウドAIでリアルタイム管理。各地の発酵プロセス、気候、健康データを統合した<strong>「Earth Microbial Brain」</strong>構築。自動カーボンクレジット発行・トレーサビリティ・透明性の完全確保。</p>
      <blockquote>成果指標：全自動炭素会計システム運用／クラウド連携プラットフォーム稼働率98%以上</blockquote>

      <h4>Phase 5：地球規模展開と知的エコシステム化（2035–2050）</h4>
      <p>各地域のMBTセンターを「生態知ハブ（Eco-Intelligence Hub）」として接続。教育・経済・環境・健康データの相互循環による<strong>生命知経済圏（BioNexus³）</strong>形成。2050年、<strong>"Carbon Negative + Health Positive Society"</strong>を実現。</p>
      <blockquote>成果指標：年間炭素除去1億t-CO₂／参加国50カ国以上／GDPインパクト+2.8%</blockquote>

      <h3>5.6 成果の評価と持続性メカニズム</h3>
      <div class="table-wrap">
        <table>
          <thead><tr><th>分野</th><th>指標</th><th>値</th><th>備考</th></tr></thead>
          <tbody>
            <tr><td>炭素削減</td><td>48万t-CO₂</td><td>パイロット3地域計</td><td>登録クレジット化可能</td></tr>
            <tr><td>雇用創出</td><td>26,000人</td><td>現地加工・発酵・教育含む</td><td>42%女性雇用</td></tr>
            <tr><td>医療費削減</td><td>1,200万USD/年</td><td>健康改善効果</td><td>WHO基準比較</td></tr>
            <tr><td>経済効果</td><td>GDP +2.8%</td><td>地域総生産寄与</td><td>乗数効果含む</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pull-quote">「Net Zeroを超えて、Bio-Positiveへ。」<br><span style="font-size:0.8em;font-style:normal;color:#777;">― MBT Sustainable Cycle presents a living pathway toward a regenerative future.</span></div>
    </section>
  </div><!-- /content-ja -->

</div><!-- /content-wrapper -->

<a href="#" class="back-top" title="Back to top">↑</a>

<footer>
  <p>MBT55 — Microbial BioTransformation 55 &nbsp;·&nbsp; © 2025 &nbsp;·&nbsp;
  <a href="https://gist.github.com/shimojok/b046b4105956ad2289d7f31efd8088d2" style="color:#7a9e71;" target="_blank" rel="noopener">GitHub Gist Source</a></p>
</footer>

<script>
  function switchLang(lang) {
    // Toggle section visibility
    ['en', 'ja'].forEach(function(l) {
      document.getElementById('content-' + l).classList.toggle('active', l === lang);
      document.getElementById('hero-' + l).classList.toggle('active', l === lang);
      document.getElementById('btn-' + l).classList.toggle('active', l === lang);
    });
    // Update html lang attribute
    document.documentElement.lang = lang === 'ja' ? 'ja' : 'en';
    // Update body class for font family
    document.body.classList.toggle('ja-active', lang === 'ja');
    // Scroll to top on switch
    window.scrollTo({ top: 0, behavior: 'smooth' });
    // Re-typeset math
    if (window.MathJax) {
      MathJax.typesetPromise();
    }
  }
</script>

</body>
</html>