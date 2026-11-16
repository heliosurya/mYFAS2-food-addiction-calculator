#!/usr/bin/env python3
"""Build all calculators with enhanced UI/UX (glassmorphism, progress pills, SVG gauge, toasts, clipboard)."""
import os

os.makedirs('build', exist_ok=True)

# Read enhanced CSS from template
with open('build/enhanced_css.html', 'r') as f:
    css = f.read()

# ============================================
# CALCULATOR DATA PER SCALE
# ============================================

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

calc_data = {
    'yfas20': {'items': yfas20_items, 'criteria': yfas20_crit, 'scale': 8, 'name': 'YFAS 2.0 Full'},
    'prows': {'items': prows_items, 'scale': 5, 'name': 'ProWS'},
    'aefs': {'items': aefs_items, 'scale': 6, 'name': 'AEFS'},
    'yfasc': {'items': yfasc_items, 'scale': 5, 'name': 'YFAS-C 2.0'},
    'dyfas': {'items': dyfas_items, 'scale': 5, 'name': 'dYFAS-C 2.0'},
    'myfasc': {'items': myfasc_items, 'scale': 5, 'name': 'mYFAS-C 2.0'},
}

print("Calculator data prepared:")
for name, data in calc_data.items():
    print(f"  {name}: {len(data['items'])} items, {data['scale']}-point scale")
print("Generator script ready.")
