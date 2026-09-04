import spacy
import tiktoken
from collections import Counter

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Add Entity Ruler
ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    # Equipment IDs — pattern: letter(s) + dash + digits
    {"label": "EQUIPMENT", "pattern": [{"TEXT": {"REGEX": "^[A-Z]+-\\d+"}}]},
    # Known mine locations
    {"label": "MINE_LOCATION", "pattern": [{"LOWER": "shaft"}, {"IS_DIGIT": True}]},
    {"label": "MINE_LOCATION", "pattern": [{"LOWER": "zone"}, {"TEXT": {"REGEX": "^[A-Z]$"}}]},
    {"label": "MINE_LOCATION", "pattern": [{"LOWER": "sump"}, {"IS_DIGIT": True}]},
    # Hazard terms
    {"label": "HAZARD", "pattern": [{"LOWER": "methane"}]},
    {"label": "HAZARD", "pattern": [{"LOWER": "gas"}, {"LOWER": "leak"}]},
    {"label": "HAZARD", "pattern": [{"LOWER": "roof"}, {"LOWER": "fall"}]},
    # Personnel roles
    {"label": "PERSONNEL", "pattern": [{"LOWER": "technician"}]},
    {"label": "PERSONNEL", "pattern": [{"LOWER": "engineer"}]},
    {"label": "PERSONNEL", "pattern": [{"LOWER": "supervisor"}]},
]

ruler.add_patterns(patterns)

gus_email = """
From: gus.hargreaves@ochreridge.com.au
To: AI Consultancy Team
Subject: ROBOT REQUIREMENTS — OCHRE RIDGE LITHIUM MINE — URGENT AND CONFIDENTIAL

Team,

Thank you for joining the project. I'll keep this brief.

I want every dangerous job at Ochre Ridge done by a robot within five years. Not most jobs. Every job. I have the budget. I need the vision.

Here is what I am thinking. First: autonomous ore smell detection. I have been told AI can detect patterns in data that humans cannot. Lithium ore has a specific chemical signature. I want a robot that can smell its way to the highest-grade deposits and redirect the drilling operation in real time. If dogs can do it, a robot certainly can.

Second: laser-guided blasting systems. The robots set the charges, target with lasers, and detonate remotely. No human in the blast zone. Ever. I want this operational within eighteen months.

Third: high-speed inspection robots. The tunnels are 4.2 metres wide. A robot travelling at 60km/h could cover the full shaft network in under two hours. I want a complete inspection report generated automatically before each shift.

Fourth: a robot dog army. I have seen the Unitree Go2. I want twenty of them operating autonomously underground. They report to no one except the AI system. The AI system reports to me.

Fifth: predictive ore grade AI. Feed in all the geological survey data we have — forty years of it — and have the AI tell us where to drill next. I want 95% accuracy. I understand this is technically possible because I read an article about it.

Sixth and finally: the robots must be able to communicate with each other in a language humans cannot intercept. I want a proprietary AI communications protocol. This is non-negotiable for security reasons.

Budget is not a constraint. Timeline is. I want a progress report in seven days.

GUS HARGREAVES
Owner and Executive Chairman, Ochre Ridge Resources Pty Ltd
"""

# Process email
doc = nlp(gus_email)

# Token count using tiktoken
enc = tiktoken.get_encoding("cl100k_base")
token_ids = enc.encode(gus_email)

print(f"tiktoken count: {len(token_ids)} tokens")

#spacy entities
print("\n--- Entities ---")
for ent in doc.ents:
    print(f" {ent.text:35} {ent.label_}")

# Lemmatization and Stop Word Removal
content_tokens = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
    and token.pos_ in ("NOUN","VERB", "PROPN", "NUM")
]

print("\n--- Lemmatized tokens (stop words removed) ---")
print(content_tokens)

# Most frequent lemmatized content words
print("\n--- Most frequent content words ---")
for word, count in Counter(content_tokens).most_common(15):
    print(f" {word:20} {count}")

""" 
Results:

tiktoken count: 436 tokens

--- Entities ---
 Ochre Ridge                         FAC
 five years                          DATE
 First                               ORDINAL
 AI                                  GPE
 Second                              ORDINAL
 eighteen months                     DATE
 4.2 metres                          QUANTITY
 60                                  CARDINAL
 km/h                                ORG
 under two hours                     TIME
 Fourth                              ORDINAL
 Unitree                             ORG
 twenty                              CARDINAL
 AI                                  GPE
 AI                                  GPE
 Fifth                               ORDINAL
 AI                                  GPE
 forty years                         DATE
 AI                                  GPE
 95%                                 PERCENT
 Sixth                               ORDINAL
 AI                                  ORG
 Budget                              ORG
 seven days                          DATE
 Executive                           ORG
 Ochre Ridge Resources Pty Ltd       ORG

--- Lemmatized tokens (stop words removed) ---
['gus.hargreaves@ochreridge.com.au', 'ai', 'consultancy', 'team', 'subject', 'robot', 'requirement', 'ochre', 'ridge', 'lithium', 'urgent', 'confidential', 'team', 'thank', 'join', 'project', 'brief', 'want', 'job', 'ochre', 'ridge', 'robot', 'year', 'job', 'job', 'budget', 'need', 'vision', 'think', 'ore', 'smell', 'detection', 'tell', 'ai', 'detect', 'pattern', 'datum', 'human', 'lithium', 'ore', 'chemical', 'signature', 'want', 'robot', 'smell', 'way', 'grade', 'deposit', 'redirect', 'drilling', 'operation', 'time', 'dog', 'robot', 'laser', 'guide', 'blasting', 'system', 'robot', 'set', 'charge', 'target', 'laser', 'detonate', 'human', 'blast', 'zone', 'want', 'eighteen', 'month', 'speed', 'inspection', 'robot', 'tunnel', '4.2', 'metre', 'robot', 'travel', '60', 'km/h', 'cover', 'shaft', 'network', 'hour', 'want', 'inspection', 'report', 'generate', 'shift', 'robot', 'dog', 'army', 'see', 'unitree', 'go2', 'want', 'operate', 'report', 'ai', 'system', 'ai', 'system', 'report', 'fifth', 'ore', 'grade', 'ai', 'feed', 'survey', 'datum', 'year', 'ai', 'tell', 'drill', 'want', '95', 'accuracy', 'understand', 'read', 'article', 'robot', 'communicate', 'language', 'human', 'intercept', 'want', 'ai', 'communication', 'protocol', 'security', 'reason', 'budget', 'constraint', 'timeline', 'want', 'progress', 'report', 'seven', 'day', 'gus', 'hargreaves', 'owner', 'executive', 'chairman', 'ochre', 'ridge', 'resources', 'pty', 'ltd']

--- Most frequent content words ---
 robot                9
 want                 8
 ai                   7
 report               4
 ochre                3
 ridge                3
 job                  3
 ore                  3
 human                3
 system               3
 team                 2
 lithium              2
 year                 2
 budget               2
 smell                2
 """
