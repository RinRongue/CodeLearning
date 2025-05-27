from genanki import Model, Note, Deck, Package
import random
import os

# Create a model for Anki cards
model_id = random.randrange(1 << 30, 1 << 31)
model = Model(
    model_id,
    'Simple Vocabulary Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    }]
)

# Create a deck
deck_id = random.randrange(1 << 30, 1 << 31)
deck = Deck(deck_id, 'Academic English Vocabulary')

# Key vocabulary list grouped as (front, back)
vocab_list = [
    # Verbs
    ("demonstrate", "证明，展示"),
    ("indicate", "表明"),
    ("suggest", "表明，暗示"),
    ("reveal", "揭示"),
    ("assess", "评估"),
    ("evaluate", "评估"),
    ("examine", "检查，研究"),
    ("investigate", "调查，研究"),
    ("compare", "比较"),
    ("analyze", "分析"),
    ("measure", "测量"),
    ("observe", "观察"),
    ("identify", "鉴定，识别"),
    # Methodology
    ("cohort", "队列（医学/统计用）"),
    ("randomized", "随机的"),
    ("double-blind", "双盲的"),
    ("placebo", "安慰剂"),
    ("control group", "对照组"),
    ("experimental group", "实验组"),
    ("sample size", "样本量"),
    ("statistically significant", "具有统计学意义"),
    ("variable", "变量"),
    ("confounding factor", "混杂因素"),
    ("bias", "偏倚"),
    ("follow-up", "随访"),
    # Data analysis
    ("increased", "增加的"),
    ("decreased", "减少的"),
    ("elevated", "升高的（常用于生化指标）"),
    ("reduced", "减少的"),
    ("rate", "率"),
    ("proportion", "比例"),
    ("mean", "平均值"),
    ("median", "中位数"),
    ("standard deviation", "标准差"),
    ("confidence interval", "置信区间"),
    ("p-value", "p 值（统计显著性）"),
    ("correlation", "相关性"),
    ("regression", "回归（分析）"),
    # Conclusion/Discussion
    ("findings", "研究结果"),
    ("implications", "含义，意义"),
    ("limitation", "局限性"),
    ("strength", "优势"),
    ("consistent with", "与……一致"),
    ("in line with", "与……一致"),
    ("contrary to", "与……相反"),
    ("support the hypothesis", "支持假设"),
    ("further research is needed", "需要进一步研究"),
    ("clinical relevance", "临床相关性"),
]

# Add notes to the deck
for front, back in vocab_list:
    note = Note(model=model, fields=[front, back])
    deck.add_note(note)

# Create the .apkg package
output_path = './Academic_English_Vocab.apkg'
Package(deck).write_to_file(output_path)

output_path
