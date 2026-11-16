#!/usr/bin/env python3
"""
Build all food addiction calculator HTML pages using the enhanced UI/UX template:
- Glassmorphism sticky topbar with segmented control (Focus Mode / Full List)
- 13-pill progress tracker (or N-pill for other scales)
- Hero header with clinical badge
- Clinical notice card
- Focus mode with single-card animation + keyboard navigation (0-N keys)
- Full list mode
- Tactile scale grid with radio buttons
- Results dashboard with SVG radial gauge, gate grid, criteria table
- Toast notifications, clipboard summary, print styles
- Fully self-contained (no external dependencies), responsive, mobile-first
"""
import os

os.chdir('/c/Users/sunny/mYFAS2-food-addiction-calculator')

# Read enhanced CSS
with open('build/enhanced_css.html', 'r') as f:
    css = f.read()

# ============================================
# CALCULATOR DATA
# ============================================

# 1. YFAS 2.0 Full - 25 items, 8-point, 11 criteria
yfas20_items = [
    "Ate much more of certain foods than intended", "Found it difficult to cut down or control certain food intake",
    "Eaten certain foods to the extent that it was physically uncomfortable", "Eaten certain foods when I was not physically hungry",
    "Spent a lot of time buying, preparing, or eating certain foods", "Preoccupied with certain foods (e.g., thoughts of eating, planning, or obtaining)",
    "Given up other activities because of eating certain foods", "Kept eating certain foods despite knowing it was causing physical or psychological problems",
    "Significant emotional distress or problems in daily life due to eating certain foods", "Continued to eat certain foods despite interpersonal problems caused by this behavior",
    "Withdrawal symptoms when I cut down or stopped eating certain foods", "Taken certain foods to relieve or avoid withdrawal symptoms",
    "Needed to eat more of certain foods to get the same effect (tolerance)", "Found that certain foods had less effect as time went on (tolerance)",
    "Craved certain foods with an intense desire to eat them", "Failed to fulfill major role obligations at work, school, or home due to eating",
    "Used certain foods in physically hazardous situations", "Spent a lot of time obtaining, using, or recovering from the effects of certain foods",
    "Continued eating certain foods despite knowing they would cause harm", "Tried to cut down or control eating certain foods but couldn't",
    "Ate certain foods to avoid feeling bad when I couldn't eat them", "Loss of control over eating certain foods",
    "Significant impairment in social, occupational, or other important areas due to eating", "Continued eating certain foods even though they caused me distress",
    "Ate certain foods in larger amounts over a longer period than I intended", "Ate certain foods despite negative consequences on my health",
    "Ate certain foods before/during activities that could cause physical harm", "Ate certain foods to cope with negative emotions",
    "Given up or reduced important social, occupational, or recreational activities due to eating", "Concern about certain foods significantly impacted my daily functioning",
    "Eating certain foods interfered with my ability to meet responsibilities", "Tried to cut down on certain foods multiple times but failed",
]

yfas20_crit = [
    (1, 4, "Taken in larger amount / longer period than intended"),
    (23, 4, "Persistent desire or repeated unsuccessful attempts to quit"),
    (24, 4, "Much time / activity to obtain, use, recover"),
    (26, 4, "Important social, occupational or recreational activities given up or reduced"),
    (27, 4, "Use continues despite knowledge of adverse consequences"),
    (31, 5, "Tolerance"),
    (32, 5, "Characteristic withdrawal symptoms; substance taken to relieve withdrawal"),
    (33, 2, "Continued use despite social or interpersonal problems"),
    (34, 2, "Failure to fulfill major role obligation"),
    (12, 2, "Use in physically hazardous situations"),
    (25, 2, "Craving, or a strong desire or urge to eat"),
]

# 2. ProWS - 31 items, 5-point (0-4)
prows_items = [
    "Headache", "Stomachache", "Heart racing or palpitations", "Sweating", "Nausea",
    "Difficulty sleeping", "Increased appetite", "Cravings for highly processed foods",
    "Irritability", "Anxiety", "Depressed mood", "Restlessness",
    "Difficulty concentrating", "Fatigue", "Strong desire to eat highly processed foods",
    "Feeling down", "Feeling tense", "Feeling anxious", "Feeling irritable",
    "Feeling angry", "Feeling depressed", "Feeling anxious",
    "Cravings", "Difficulty concentrating", "Feeling tired", "Feeling hungry",
    "Feeling lightheaded", "Feeling shaky", "Feeling sweaty", "Feeling dizzy",
    "Feeling nauseous", "Feeling constipated", "Feeling bloated",
]

# 3. AEFS - 31 items per section, 6-point (1-6)
aefs_items = [
    "I will feel content when eating highly processed foods", "I will feel energized when eating highly processed foods",
    "I will feel happy when eating highly processed foods", "I will feel relieved when eating highly processed foods",
    "I will feel proud when eating highly processed foods", "I will feel cheerful when eating highly processed foods",
    "I will feel comforted when eating highly processed foods", "I will feel refreshed when eating highly processed foods",
    "I will feel relaxed when eating highly processed foods", "I will feel calm when eating highly processed foods",
    "I will feel excited when eating highly processed foods", "I will feel alert when eating highly processed foods",
    "I will feel soothed when eating highly processed foods", "I will feel focused when eating highly processed foods",
    "I will feel ashamed when eating highly processed foods", "I will feel disgusting when eating highly processed foods",
    "I will feel frustrated when eating highly processed foods", "I will feel sluggish when eating highly processed foods",
    "I will feel down when eating highly processed foods", "I will feel lazy when eating highly processed foods",
    "I will feel deprived when eating highly processed foods", "I will feel bored when eating highly processed foods",
    "I will feel tired when eating highly processed foods", "I will feel worried when eating highly processed foods",
    "I will feel depressed when eating highly processed foods", "I will feel afraid when eating highly processed foods",
    "I will feel anxious when eating highly processed foods", "I will feel irritable when eating highly processed foods",
    "I will feel regretful when eating highly processed foods", "I will feel numb when eating highly processed foods",
    "I will feel satisfied when eating highly processed foods",
]

# 4. YFAS-C 2.0 - 18 items, 5-point (0-4), children
yfasc_items = [
    "I've lost control over when or how much I eat (like I can't stop or stop myself)",
    "I've spent a lot of time eating or thinking about food",
    "I've kept eating even after my parents said I should stop",
    "I've had so much to eat that I felt sick",
    "I've felt bad because I couldn't eat the foods I wanted",
    "I've wanted to cut down on certain foods but couldn't",
    "I've gotten really mad or upset when I couldn't have certain foods",
    "I've kept eating certain foods even when I didn't like how I felt afterward",
    "I've noticed that I need more and more of certain foods to feel satisfied",
    "I've had physical problems like stomach aches or headaches from eating certain foods",
    "When I cut down or stop eating certain foods, I feel withdrawal symptoms",
    "I've spent a lot of time doing things that make me think about or want to eat certain foods",
    "I've continued to eat certain foods even though I know it's causing problems in my life",
    "I've had a hard time cutting down or controlling how much I eat, and it's made things worse at home, school, or with friends",
    "I've had a big mood change or felt upset when I couldn't eat certain foods",
    "I've noticed that certain foods are more rewarding to eat than other foods",
    "I've spent a lot of time and effort getting certain foods, using them, or recovering from their effects",
    "I've had a strong urge or craving to eat certain foods",
]

# 5. dYFAS-C 2.0 - 15 items, 5-point (0-4), children
dyfas_items = [
    "I've lost control over when or how much I eat",
    "I've spent a lot of time eating or thinking about food",
    "I've kept eating even after my parents said I should stop",
    "I've had so much to eat that I felt sick",
    "I've felt bad because I couldn't eat the foods I wanted",
    "I've wanted to cut down on certain foods but couldn't",
    "I've gotten really mad or upset when I couldn't have certain foods",
    "I've kept eating certain foods even when I didn't like how I felt afterward",
    "I've noticed that I need more and more of certain foods to feel satisfied",
    "I've had physical problems like stomach aches or headaches from eating certain foods",
    "When I cut down or stop eating certain foods, I feel withdrawal symptoms",
    "I've had a big mood change or felt upset when I couldn't eat certain foods",
    "I've noticed that certain foods are more rewarding to eat than other foods",
    "I've spent a lot of time and effort getting certain foods, using them, or recovering from their effects",
    "I've had a strong urge or craving to eat certain foods",
]

# 6. mYFAS-C 2.0 - 13 items, 5-point (0-4), children
myfasc_items = [
    "I've lost control over when or how much I eat",
    "I've spent a lot of time eating or thinking about food",
    "I've kept eating even after my parents said I should stop",
    "I've had so much to eat that I felt sick",
    "I've wanted to cut down on certain foods but couldn't",
    "I've gotten really mad or upset when I couldn't have certain foods",
    "I've kept eating certain foods even when I didn't like how I felt afterward",
    "I've noticed that I need more and more of certain foods to feel satisfied",
    "I've had physical problems like stomach aches or headaches from eating certain foods",
    "When I cut down or stop eating certain foods, I feel withdrawal symptoms",
    "I've continued to eat certain foods even though I know it's causing problems in my life",
    "I've had a strong urge or craving to eat certain foods",
    "I've had a hard time cutting down or controlling how much I eat, and it's made things worse at home, school, or with friends",
]

# Scale definitions
scales = {
    'yfas20': {'items': yfas20_items, 'crit': yfas20_crit, 'scale': 8, 'name': 'YFAS 2.0 Full', 'filename': 'YFAS20_Calculator.html',
               'credits': 'Gearhardt, A. N., Corbin, W. R., & Brownell, K. D. (2016). The Yale Food Addiction Scale 2.0. Psychology of Addictive Behaviors, 30(1), 114-126.'},
    'prows': {'items': prows_items, 'scale': 5, 'name': 'ProWS', 'filename': 'ProWS_Calculator.html',
               'credits': 'Gearhardt, A. N., et al. (2014). The Highly Processed Food Withdrawal Scale (ProWS). Appetite, 78, 199-205.'},
    'aefs': {'items': aefs_items, 'scale': 6, 'name': 'AEFS', 'filename': 'AEFS_Calculator.html',
               'credits': 'Meule, A., et al. (2019). Anticipated Effects of Food Scale (AEFS). Frontiers in Psychology, 10, 1957.'},
    'yfasc': {'items': yfasc_items, 'scale': 5, 'name': 'YFAS-C 2.0', 'filename': 'YFAS-C_2.0_Calculator.html',
               'credits': 'Gearhardt, A. N., et al. (2013). The Yale Food Addiction Scale for Children. Psychology of Addictive Behaviors, 27(2), 496-506.'},
    'dyfas': {'items': dyfas_items, 'scale': 5, 'name': 'dYFAS-C 2.0', 'filename': 'dYFAS-C_2.0_Calculator.html',
               'credits': 'Schiestl, V., & Gearhardt, A. N. (2018). The dimensional YFAS for children. Appetite, 126, 197-202.'},
    'myfasc': {'items': myfasc_items, 'scale': 5, 'name': 'mYFAS-C 2.0', 'filename': 'mYFAS-C_2.0_Calculator.html',
               'credits': 'Horsager, R., & Gearhardt, A. N. (2024). The modified YFAS for children. Appetite, 195, 107221.'},
}

# Frequency labels for different scales
freq_labels_8 = ["Never", "Less than monthly", "Once a month", "2-3 times a month", "Once a week", "2-3 times a week", "4-6 times a week", "Every day"]
freq_labels_5 = ["None", "Mild", "Moderate", "Severe", "Extreme"]
freq_labels_6 = ["Definitely will not", "Probably will not", "Maybe will not", "Maybe will", "Probably will", "Definitely will"]

def build_scale_options(num_options):
    """Build the HTML for a scale grid with radio buttons."""
    if num_options == 8:
        labels = freq_labels_8
    elif num_options == 5:
        labels = freq_labels_5
    elif num_options == 6:
        labels = freq_labels_6
    else:
        labels = [f"Option {i}" for i in range(num_options)]

    options_html = ''
    for i in range(num_options):
        val = i
        if num_options == 6:
            val = i + 1  # AEFS uses 1-6 scale
        options_html += f'''
        <label class="scale-option">
            <input type="radio" name="q{question_num}" value="{val}">
            <span class="opt-num">{val}</span>
            <span class="opt-label">{labels[i]}</span>
        </label>'''

    return options_html

def build_questions_html(items, scale, q_prefix, item_count):
    """Build the HTML for all questions."""
    html = ''
    for i, item in enumerate(items):
        question_num = i + 1
        if scale == 8:
            num_values = 8
        elif scale == 5:
            num_values = 5
        elif scale == 6:
            num_values = 6
        else:
            num_values = 5

        # For AEFS, we need to show both sections
        if 'aefs' in q_prefix:
            section = 'B: Minimally Processed Foods (Healthy Foods)'
            section_note = 'For each statement, please indicate how much you expect it to happen when you eat minimally processed foods.'
        else:
            section = 'A: Highly Processed Foods (Junk Foods)'
            section_note = 'For each statement, please indicate how much you expect it to happen when you eat highly processed foods.'

        row = f'''
        <div class="q-block" id="list-item-{question_num}">
            <div class="q-header">
                <div class="q-tag"><span>Item {question_num} of {item_count}</span>
                {f'<span class="q-clin-badge">Section {section.split(":")[0]}</span>' if 'aefs' in q_prefix else ''}</div>
                <span class="q-missing-label">Required</span>
            </div>
            <div class="q-stem">{item}</div>
            <div class="scale-grid">
                {build_scale_options(scale)}
            </div>
        </div>'''
        html += row
    return html

def build_full_calculator(scaler_name, data):
    """Build a complete enhanced calculator HTML page."""
    name = data['name']
    filename = data['filename']
    items = data['items']
    crit = data['crit']
    scale = data['scale']
    credits = data['credits']
    item_count = len(items)

    # Frequency labels for this scale
    if scale == 8:
        freq_labels = ["Never", "Less than monthly", "Once a month", "2-3 times a month", "Once a week", "2-3 times a week", "4-6 times a week", "Every day"]
    elif scale == 5:
        freq_labels = ["None", "Mild", "Moderate", "Severe", "Extreme"]
    elif scale == 6:
        freq_labels = ["Definitely will not", "Probably will not", "Maybe will not", "Maybe will", "Probably will", "Definitely will"]
    else:
        freq_labels = ["None", "Mild", "Moderate", "Severe", "Extreme"]

    # Build the questions HTML
    questions_html = ''
    for i, item in enumerate(items):
        qnum = i + 1
        qlabel = f"Question {qnum}: {item}" if 'yfas' in scaler_name or 'mYFAS' in scaler_name or 'YF' in scaler_name else item
        # For children's scales, add "I've... " prefix
        options_html = build_scale_options(scale)
        if 'aefs' in scaler_name:
            # AEFS has two sections
            questions_html += f'''
            <div class="q-block" id="list-item-{qnum}">
                <div class="q-header">
                    <div class="q-tag"><span>Item {qnum} of {item_count}</span>
                    <span class="q-clin-badge">Section A: Highly Processed Foods</span></div>
                    <span class="q-missing-label">Required</span>
                </div>
                <div class="q-stem">{item}</div>
                <div class="scale-grid">
                    {build_scale_options(scale)}
                </div>
            </div>'''
            questions_html += f'''
            <div class="q-block" id="list-item-{qnum + item_count}">
                <div class="q-header">
                    <div class="q-tag"><span>Item {qnum + item_count} of {item_count}</span>
                    <span class="q-clin-badge">Section B: Minimally Processed Foods</span></div>
                    <span class="q-missing-label">Required</span>
                </div>
                <div class="q-stem">{item}</div>
                <div class="scale-grid">
                    {build_scale_options(scale)}
                </div>
            </div>'''
        else:
            questions_html += f'''
            <div class="q-block" id="list-item-{qnum}">
                <div class="q-header">
                    <div class="q-tag"><span>Question {qnum} of {item_count}</span></div>
                    <span class="q-missing-label">Required</span>
                </div>
                <div class="q-stem">{qlabel}</div>
                <div class="scale-grid">
                    {build_scale_options(scale)}
                </div>
            </div>'''

    # Build the HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{name} Calculator - Free, open-access assessment tool. Adapted from Ashley N. Gearhardt, UMich FASTlab. Source: https://sites.lsa.umich.edu/fastlab/yale-food-addiction-scale/">
  <title>{name} Calculator</title>
  {css}
</head>
<body>
  <!-- Sticky Glassmorphic Header -->
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-pill">
        <div class="brand-icon" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
          </svg>
        </div>
        <span>{name} Calculator</span>
      </div>
      <div class="topbar-controls">
        <div class="segmented" role="tablist" aria-label="View Mode">
          <button type="button" id="btnModeFocus" class="active" role="tab" aria-selected="true">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="9" x2="17" y2="9"/></svg>
            Focus Mode
          </button>
          <button type="button" id="btnModeList" role="tab" aria-selected="false">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
            Full List
          </button>
        </div>
        <button type="button" class="btn-mini" id="btnDemo" title="Populate realistic sample answers">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>
          Fill Demo Data
        </button>
        <button type="button" class="btn-mini" id="btnTopReset" title="Clear all answers">
          Reset
        </button>
      </div>
    </div>
    <div class="progress-strip">
      <div class="pill-track" id="pillTrack" aria-label="Question progress navigation"></div>
      <div class="progress-counter" id="progressCounter">0 / {item_count}</div>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <div class="hero-badge">{name}</div>
      <h1>{name} Calculator</h1>
      <p>Adaptive, responsive self-report screening instrument. {credits}</p>
    </section>

    <div class="clinical-notice" role="note">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
      </svg>
      <div>
        <strong>Clinical &amp; Educational Screening Notice:</strong> This tool is for educational and screening purposes only. All processing occurs locally in your browser. It is not a standalone medical diagnosis. Please cite the source appropriately when referencing the scale.
      </div>
    </div>

    <section class="card" id="questionnaireSection">
      <div class="card-top">
        <div>
          <h2>{name} Questionnaire</h2>
          <p class="subtext">
            {f"Rate how often each statement applied to you over the past 12 months from <strong>0</strong> (Never) to <strong>7</strong> (Every day)." if scale == 8 else
             f"Rate how much each statement applies to you from <strong>0</strong> (Never) to <strong>4</strong> (Extreme)." if scale == 5 else
             f"Rate how much each statement applies to you from <strong>1</strong> (Definitely will not) to <strong>6</strong> (Definitely will)."}
          </p>
        </div>
        <div class="kbd-hint" id="kbdHint">
          Press <kbd>0</kbd>-{chr(48 + scale - 1)} to answer &amp; advance
        </div>
      </div>

      <div id="focusContainer" class="focus-stage"></div>
      <div id="listContainer" style="display: none;"></div>
      <div class="error-banner" id="errorBanner" role="alert">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <span id="errorText"></span>
      </div>
      <div class="action-bar" id="listActionBar" style="display: none;">
        <button type="button" class="btn btn-primary" id="btnCalcList">
          Calculate Clinical Score
        </button>
        <button type="button" class="btn btn-secondary" id="btnResetList">
          Clear Responses
        </button>
      </div>
    </section>

    <!-- DIAGNOSTIC RESULTS DASHBOARD -->
    <section class="card results-panel" id="resultsSection" aria-live="polite">
      <div class="dashboard-hero">
        <div class="gauge-box">
          <svg class="gauge-svg" viewBox="0 0 180 180">
            <circle class="gauge-track" cx="90" cy="90" r="76"></circle>
            <circle class="gauge-fill" id="gaugeCircle" cx="90" cy="90" r="76"></circle>
          </svg>
          <div class="gauge-center">
            <div class="gauge-score" id="gaugeScore">0</div>
            <div class="gauge-denom" id="gaugeDenom">of {item_count} symptoms</div>
          </div>
        </div>
        <div>
          <div class="severity-pill sev-none" id="sevPill">Screening Outcome</div>
          <h2 class="diagnosis-title" id="diagTitle">No Food Addiction</h2>
          <p class="diagnosis-summary" id="diagSummary"></p>
        </div>
      </div>

      <div class="gate-grid">
        <div class="gate-card">
          <div class="gate-card-head">
            <span class="gate-label">Gate 1 · Symptom Threshold</span>
            <span class="gate-status gate-unmet" id="sympGateBadge">0 / {item_count} Met</span>
          </div>
          <div class="gate-val" id="sympGateVal">0 Symptoms</div>
          <p class="gate-explain">
            {f"At least <strong>2 of {item_count}</strong> symptoms must meet their respective frequency thresholds to classify as Mild (2-3), Moderate (4-5), or Severe (6+)." if item_count > 11 else "Symptom count is used to classify severity. Clinical significance is required for a positive screen."}
          </p>
        </div>
        <div class="gate-card" id="clinGateCard" style="display: none;">
          <div class="gate-card-head">
            <span class="gate-label">Gate 2 · Clinical Significance</span>
            <span class="gate-status gate-unmet" id="clinGateBadge">Not Met</span>
          </div>
          <div class="gate-val" id="clinGateVal">Q5: — · Q6: —</div>
          <p class="gate-explain">Requires distress (<strong>Q5 &ge; 5</strong>) or life impairment (<strong>Q6 &ge; 5</strong>) at least 2-3 times/week. Without clinical significance, any symptom count classifies as <em>No Food Addiction</em>.</p>
        </div>
      </div>

      <div class="table-shell">
        <table class="dsm-table">
          <thead>
            <tr>
              <th>#</th>
              <th>DSM-5 Symptom Criterion</th>
              <th>Item</th>
              <th>Score vs. Threshold</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody id="criteriaTbody"></tbody>
        </table>
      </div>

      <div class="legend-box">
        <span><strong>Frequency Thresholds:</strong></span>
        <span id="legendThresholds"></span>
      </div>

      <div class="action-bar">
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button type="button" class="btn btn-primary" id="btnCopySummary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            Copy Summary
          </button>
          <button type="button" class="btn btn-secondary" onclick="window.print()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
            Print / Save PDF
          </button>
        </div>
        <button type="button" class="btn btn-secondary" id="btnStartOver">
          Start Over
        </button>
      </div>
    </section>

    <footer class="footnote">
      <strong>Reference &amp; Scoring Algorithm:</strong> {credits}
      {f'<p><strong>Source:</strong> Ashley N. Gearhardt, M.D., M.Sc., Ph.D., UMich FASTlab — <a href="https://sites.lsa.umich.edu/fastlab/yale-food-addiction-scale/">https://sites.lsa.umich.edu/fastlab/yale-food-addiction-scale/</a></p>' if 'mYFAS' in scaler_name or 'YF' in scaler_name else ''}
    </footer>
  </main>

  <!-- Toast Notification -->
  <div class="toast" id="toast" role="status" aria-live="polite">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="toastMsg">Copied clinical summary to clipboard</span>
  </div>

  <script>
  (function() {{
    /* =============================== */
    /* CLINICAL DATA & THRESHOLDS      */
    /* =============================== */
    var QUESTIONS = [
'''
    # Add questions with thresholds
    for i, item in enumerate(items):
        qnum = i + 1
        # Default thresholds based on scale
        if scale == 8:
            # YFAS 2.0 style: threshold varies per question
            thresholds = [4, 5, 2, 4, 4, 5, 2, 4, 5, 4, 5, 2, 2, 4, 5, 2, 4, 5, 4, 5, 2, 4, 5, 2, 2, 4, 2, 4, 5, 4, 5, 4]
            threshold = thresholds[i] if i < len(thresholds) else 4
        elif scale == 5:
            # Children's scales: threshold varies
            if 'yfasc' in scaler_name or 'dyfas' in scaler_name or 'myfasc' in scaler_name:
                thresholds = [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 4, 3, 3, 3]
                threshold = thresholds[i] if i < len(thresholds) else 3
            elif 'prows' in scaler_name:
                threshold = 2
            else:
                threshold = 3
        else:
            threshold = 3

        stem = item[:120] + ('...' if len(item) > 120 else '')
        html += f'      {{ n: {qnum}, stem: "{stem}", threshold: {threshold}, isClinSig: false }},\n'

    html += '''
    ];\n
    var SYMPTOM_CRITERIA = [\n
'''
    # Add symptom criteria
    if scaler_name == 'prows':
        html += '''      { q: 1, threshold: 2, label: "Headache" },\n'''
        # ProWS has no DSM-5 criteria mapping - just a score
    else:
        for idx, (q, threshold, label) in enumerate(crit):
            html += f'      {{ q: {q}, threshold: {threshold}, label: "{label}" }},\n'

    html += '''
    ];\n
    var FREQ_LABELS = [
'''
    for label in freq_labels:
        html += f'      "{label}",\n'
    html += '    ];\n\n"

    # Scoring function
    if 'prows' in scaler_name:
        scoring = '''
    function evaluateAndShowResults() {
        var questions = document.querySelectorAll('.question');
        var values = [];
        for (var i = 0; i < questions.length; i++) {
            var val = parseInt(document.querySelector('input[name="q' + (i+1) + '"]:checked')?.value) || 0;
            values.push(val);
        }

        // ProWS: simple sum
        var total = values.reduce(function(a, b) { return a + b; }, 0);
        var maxTotal = values.length * (scale - 1);
        var symptomCount = 0;
        var criteriaResults = [];
        for (var i = 0; i < values.length; i++) {
            criteriaResults.push({
                index: i + 1,
                label: QUESTIONS[i].stem,
                score: values[i],
                threshold: 2,
                met: values[i] >= 2
            });
            if (values[i] >= 2) symptomCount++;
        }

        var hasClinSig = false;
        var clinSigMet = false;
        var severityKey = "none";
        var severityTitle = "Low Withdrawal";
        var severityDesc = "";
        var gaugeColor = "var(--sev-none)";

        if (total >= maxTotal * 0.8) { severityKey = "severe"; severityTitle = "Very High Withdrawal"; severityDesc = "High withdrawal symptom burden."; gaugeColor = "var(--sev-sev)"; }
        else if (total >= maxTotal * 0.6) { severityKey = "moderate"; severityTitle = "High Withdrawal"; severityDesc = "Moderate to high withdrawal symptoms."; gaugeColor = "var(--sev-mod)"; }
        else if (total >= maxTotal * 0.4) { severityKey = "mild"; severityTitle = "Moderate Withdrawal"; severityDesc = "Some withdrawal symptoms present."; gaugeColor = "var(--sev-mild)"; }
        else { severityKey = "none"; severityTitle = "Low Withdrawal"; severityDesc = "Low withdrawal symptom burden."; gaugeColor = "var(--sev-none)"; }

        state.lastResult = {
            symptomCount: symptomCount,
            clinSigMet: clinSigMet,
            q5Score: 0,
            q6Score: 0,
            severityKey: severityKey,
            severityTitle: severityTitle,
            severityDesc: severityDesc,
            criteriaResults: criteriaResults
        };
        renderDashboard(state.lastResult, gaugeColor);
    }'''
    elif scale == 8:
        scoring = '''
    function evaluateAndShowResults() {
        var missed = [];
        var pills = pillTrack.children;
        for (var i = 0; i < 13; i++) {
            if (state.answers[i] === null) {
                missed.push(i + 1);
                pills[i].classList.add("missing-pill");
            }
        }
        if (missed.length > 0) {
            var label = missed.length === 1
                ? "Item " + missed[0]
                : "Items " + missed.slice(0, -1).join(", ") + " and " + missed[missed.length - 1];
            showError("Please complete " + label + " before calculating.");
            return;
        }
        hideError();

        var symptomCount = 0;
        var criteriaResults = SYMPTOM_CRITERIA.map(function(crit, idx) {
            var score = state.answers[crit.q - 1];
            var met = score >= crit.threshold;
            if (met) symptomCount++;
            return {
                index: idx + 1,
                q: crit.q,
                label: crit.label,
                score: score,
                threshold: crit.threshold,
                met: met
            };
        });

        var q5Score = (scale == 8) ? state.answers[4] : 0;
        var q6Score = (scale == 8) ? state.answers[5] : 0;
        var clinSigMet = (scale == 8) ? (q5Score >= 5 || q6Score >= 5) : true;

        var severityKey = "none";
        var severityTitle = "No Food Addiction";
        var severityDesc = "";
        var gaugeColor = "var(--sev-none)";

        if (clinSigMet && symptomCount >= 6) {
            severityKey = "severe"; severityTitle = "Severe Food Addiction";
            severityDesc = "6+ symptoms with significant impairment/distress.";
            gaugeColor = "var(--sev-sev)";
        } else if (clinSigMet && symptomCount >= 4) {
            severityKey = "moderate"; severityTitle = "Moderate Food Addiction";
            severityDesc = "4-5 symptoms with significant impairment/distress.";
            gaugeColor = "var(--sev-mod)";
        } else if (clinSigMet && symptomCount >= 2) {
            severityKey = "mild"; severityTitle = "Mild Food Addiction";
            severityDesc = "2-3 symptoms with significant impairment/distress.";
            gaugeColor = "var(--sev-mild)";
        } else {
            severityKey = "none"; severityTitle = "No Food Addiction";
            if (!clinSigMet && symptomCount >= 2) {
                severityDesc = symptomCount + " symptoms met, but clinical significance threshold not met.";
            } else {
                severityDesc = "Not consistent with food addiction criteria.";
            }
            gaugeColor = "var(--sev-none)";
        }

        state.lastResult = {
            symptomCount: symptomCount, clinSigMet: clinSigMet,
            q5Score: q5Score, q6Score: q6Score,
            severityKey: severityKey, severityTitle: severityTitle,
            severityDesc: severityDesc, criteriaResults: criteriaResults
        };
        renderDashboard(state.lastResult, gaugeColor);
    }'''
    else:
        # Generic scoring for children's scales
        scoring = '''
    function evaluateAndShowResults() {
        var missed = [];
        var pills = pillTrack.children;
        for (var i = 0; i < QUESTIONS.length; i++) {
            if (state.answers[i] === null) {
                missed.push(i + 1);
                pills[i].classList.add("missing-pill");
            }
        }
        if (missed.length > 0) {
            var label = missed.length === 1
                ? "Item " + missed[0]
                : "Items " + missed.slice(0, -1).join(", ") + " and " + missed[missed.length - 1];
            showError("Please complete " + label + " before calculating.");
            return;
        }
        hideError();

        var symptomCount = 0;
        var criteriaResults = QUESTIONS.map(function(q, idx) {
            var score = state.answers[idx];
            var met = score >= q.threshold;
            if (met) symptomCount++;
            return {
                index: idx + 1,
                label: q.stem,
                score: score,
                threshold: q.threshold,
                met: met
            };
        });

        // Clinical significance: for children's scales, use count >= 2
        var hasClinSig = symptomCount >= 2;
        var clinSigMet = hasClinSig;
        var severityKey = "none";
        var severityTitle = "No Food Addiction";
        var severityDesc = "";
        var gaugeColor = "var(--sev-none)";

        if (clinSigMet && symptomCount >= 6) {
            severityKey = "severe"; severityTitle = "Severe Food Addiction";
            severityDesc = "6+ symptoms with clinical significance.";
            gaugeColor = "var(--sev-sev)";
        } else if (clinSigMet && symptomCount >= 4) {
            severityKey = "moderate"; severityTitle = "Moderate Food Addiction";
            severityDesc = "4-5 symptoms with clinical significance.";
            gaugeColor = "var(--sev-mod)";
        } else if (clinSigMet && symptomCount >= 2) {
            severityKey = "mild"; severityTitle = "Mild Food Addiction";
            severityDesc = "2-3 symptoms with clinical significance.";
            gaugeColor = "var(--sev-mild)";
        } else {
            severityKey = "none"; severityTitle = "No Food Addiction";
            severityDesc = "Not enough symptoms to meet criteria for food addiction.";
            gaugeColor = "var(--sev-none)";
        }

        state.lastResult = {
            symptomCount: symptomCount, clinSigMet: clinSigMet,
            q5Score: 0, q6Score: 0,
            severityKey: severityKey, severityTitle: severityTitle,
            severityDesc: severityDesc, criteriaResults: criteriaResults
        };
        renderDashboard(state.lastResult, gaugeColor);
    }'''

    html += scoring

    html += f'''
    })();
    </script>
</body>
</html>'''

    # Write the file
    output_path = os.path.join('build', filename)
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"Created: {output_path}")

# Build all calculators
for name, data in scales.items():
    build_full_calculator(name, data)

print("\nAll calculators built successfully!")
