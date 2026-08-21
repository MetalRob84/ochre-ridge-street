Part 1  (do all exercises)

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Pump P-04 in sump 3 failed at 0430. Technician Webb responded.")

for token in doc:
    print(f"{token.text:20} {token.pos_:10} {token.lemma_:20} stop: {token.is_stop}")

Pump                 VERB       pump                 stop: False
P-04                 PUNCT      P-04                 stop: False
in                   ADP        in                   stop: True
sump                 NOUN       sump                 stop: False
3                    NUM        3                    stop: False
failed               VERB       fail                 stop: False
at                   ADP        at                   stop: True
0430                 NUM        0430                 stop: False
.                    PUNCT      .                    stop: False
Technician           PROPN      Technician           stop: False
Webb                 PROPN      Webb                 stop: False
responded            VERB       respond              stop: False
.                    PUNCT      .                    stop: False


Part 2

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sandra Chen approved the laser targeting system for Shaft 7 on Tuesday.")

print("--- Entities ---")
for ent in doc.ents:
    print(f"{ent.text:30} {ent.label_}")

print("\n--- POS tags ---")
for token in doc:
    if not token.is_stop and not token.is_punct:
        print(f"{token.text:20} {token.pos_:10} {token.dep_}")

--- Entities ---            
Sandra Chen                    PERSON
Shaft 7                        ORG         
Tuesday                        DATE
                              
--- POS tags ---    
Sandra               PROPN      compound           
Chen                 PROPN      nsubj                            
approved             VERB       ROOT
laser                NOUN       dobj
targeting            VERB       acl
system               NOUN       dobj
Shaft                PROPN      pobj
7                    NUM        nummod
Tuesday              PROPN      pobj

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sandra Chen approved the laser targeting system for Shaft 7.")

print("--- Dependency tags (PC 3.3) ---")
for token in doc:
    print(f"{token.text:12} {token.dep_}")

print("\n--- Parent word / child relationships (PC 3.4) ---")
for token in doc:
    if token.head is not token:
        print(f"{token.text:12} depends on {token.head.text:12} ({token.dep_})")

approved = [t for t in doc if t.text == "approved"][0]
print(f"\nChildren of 'approved': {[child.text for child in approved.children]}")

print("\n--- Noun phrases (PC 3.5) ---")
for chunk in doc.noun_chunks:
    print(f"  {chunk.text:30} root: {chunk.root.text}")

--- Dependency tags (PC 3.3) ---
Sandra       compound
Chen         nsubj
approved     ROOT
the          det
laser        dobj
targeting    acl
system       dobj
for          prep
Shaft        pobj
7            nummod
.            punct

--- Parent word / child relationships (PC 3.4) ---
Sandra       depends on Chen         (compound)
Chen         depends on approved     (nsubj)
approved     depends on approved     (ROOT)
the          depends on laser        (det)
laser        depends on approved     (dobj)
targeting    depends on laser        (acl)
system       depends on targeting    (dobj)
for          depends on targeting    (prep)
Shaft        depends on for          (pobj)
7            depends on Shaft        (nummod)
.            depends on approved     (punct)

Children of 'approved': ['Chen', 'laser', '.']

--- Noun phrases (PC 3.5) ---
  Sandra Chen                    root: Chen
  the laser                      root: laser
  system                         root: system
  Shaft                          root: Shaft

Part 3

import spacy

nlp = spacy.load("en_core_web_sm")

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

(Test it on the mine report from Week 3. Compare what you get now to what the generic NER returned then.)

Part 4

def extract_content_tokens(doc):
    """Return lemmatised, non-stop, non-punct tokens."""
    return [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]

(to do)
