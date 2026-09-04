# OCHRE RIDGE LITHIUM MINE

## AI AND ROBOTICS SCOPING REPORT

**Prepared for:** Sandra Chen, CTO, Ochre Ridge Resources
**Prepared by:** Robert Street, AI Consultancy
**Date:** 4 September 2026

---

# Executive Summary

This report assesses Gus Hargreaves's proposal to automate dangerous work at Ochre Ridge Lithium Mine using artificial intelligence (AI), robotics and autonomous systems within five years. The assessment considers which of Gus's proposed applications are technically achievable using current technology and which require significant further research and development.

The assessment found that several proposals are feasible, but not exactly as Gus originally described them. The strongest opportunities are **predictive ore-grade analysis, supervised autonomous blasting, and robot-assisted underground inspection**. These applications can build on existing machine-learning, natural-language processing, computer-vision and robotics technologies. However, they require mine-specific integration, testing and human oversight rather than immediate full autonomy.

Three headline recommendations are therefore made. First, Ochre Ridge should prioritise an AI system that analyses its approximately forty years of geological data to identify promising drilling locations. This provides useful decision support without immediately exposing workers or robots to additional physical hazards. Second, the mine should introduce a small, supervised fleet of robot inspection platforms before attempting Gus's proposed deployment of twenty robots. Third, autonomous blasting should be investigated as a controlled, safety-critical system in which robots perform hazardous physical tasks while qualified personnel retain final authority.

Other proposals are not currently feasible in the form requested. These include robots travelling at 60 km/h underground, remotely “smelling” lithium ore without physical sampling and analysis, and using an intentionally unobservable AI communication language. These should be replaced with technically achievable alternatives such as slower autonomous inspection, robotic sampling and conventional encrypted communications.

Overall, Ochre Ridge should pursue **incremental automation rather than complete autonomy**, with reliability, safety, security and human oversight treated as requirements throughout the five-year program.

---

# 1. Context and Methodology

This assessment was conducted in response to Gus Hargreaves's requirements for the automation of dangerous work at Ochre Ridge Lithium Mine. His requirements document and interview identified six major areas of interest: autonomous ore “smelling” and drilling redirection, laser-guided blasting, high-speed tunnel inspection, a fleet of twenty Unitree Go2 robots, predictive ore-grade AI, and a proprietary communication protocol that humans cannot intercept.

Feasibility was assessed by comparing each proposal against technologies examined during the course and considering the practical requirements of an underground mine. The assessment considered whether the required capability already exists, whether it can operate on the available hardware, and whether environmental, communications and safety constraints would prevent reliable deployment.

The analysis draws on the course glossary, practical exercises and technologies used during Weeks 1–6, including the **backup Gus ARI, spaCy NLP pipelines, HuggingFace pipelines, Ollama with Llama 3.1 8B, LLaVA and computer-vision approaches**. Week 5 chatbot testing was also used to assess the reliability and performance of the local language models.

The proposals are classified as either **feasible now**, **feasible with significant limitations**, or **not currently feasible in the form requested**. This distinction is important because a system working successfully in a controlled development environment does not automatically mean it is safe or reliable enough for deployment in an underground mine.

The resulting recommendations therefore favour achievable applications that can be introduced incrementally, tested locally and kept under appropriate human supervision.

## 1.1 Technical Definitions

**Artificial Intelligence (AI)** is the broad field of making machines perform tasks that would normally require human intelligence. At Ochre Ridge, the **backup Gus ARI** is an example of AI because it uses programmed and model-based behaviour to interact with users and provide responses.

**Machine Learning (ML)** is a part of AI where a system learns patterns from data rather than relying entirely on rules written by a programmer. At Ochre Ridge, **HuggingFace classification pipelines** could be used with historical mine information to classify geological or operational records and identify patterns that may assist decision-making.

**Deep Learning (DL)** is machine learning that uses deep neural networks with multiple layers to learn complex patterns from data. At Ochre Ridge, **Llama 3.1 8B running through Ollama** is an example because it is a deep-learning language model capable of processing text and generating responses. **LLaVA** is another example because it combines language and visual processing for vision-language tasks.

These technologies are related but are not interchangeable. AI is the broadest category, machine learning is an approach within AI, and deep learning is a type of machine learning based on deep neural networks. Not every Ochre Ridge problem requires an LLM or deep-learning model; some tasks may be better addressed with conventional software, sensors or specialised machine-learning models.

---

# 2. Feasible Applications

## 2.1 Predictive Ore-Grade and Drilling Analysis

**What Gus wants:** Gus wants AI to analyse the mine's historical geological data and recommend where to drill next, with a target of 95% accuracy.

**What the technology can actually do:** A machine-learning pipeline could combine geological survey data, historical drill results and spatial information to predict ore grade or identify promising drilling locations. Models such as **Random Forest or XGBoost**, implemented using Python and scikit-learn, could produce probability or grade estimates for proposed locations. The existing NLP tools could also help structure information from historical reports before it enters the predictive workflow.

**Why it is feasible now:** This application can be developed and tested without immediately putting robots underground. Ochre Ridge reportedly has geological surveys, sample analyses and drilling logs dating back to 1975. These provide a substantial historical dataset, although the information will first need to be digitised, cleaned and standardised.

The 95% accuracy target should not be accepted without evidence. The model must be evaluated against unseen geological areas and historical data that were excluded from training.

**Risk and priority: HIGH.** The principal risks are poor-quality historical data, inconsistent records and model overfitting. These can be managed through data cleaning, validation and human review of proposed drilling locations.

---

## 2.2 Autonomous Blasting and Remote Charge Handling

**What Gus wants:** Gus wants robots to set blasting charges, use laser guidance and detonate them remotely so that no human enters the blast zone.

**What the technology can actually do:** Autonomous and remotely operated mining equipment can perform parts of this workflow. A suitable system could combine robotic equipment with LiDAR, cameras, positioning sensors and a mine-control system. Computer vision could assist with identifying drilling and charging locations, while qualified personnel retain authority over final blast approval.

**Why it is feasible now:** The underlying technologies—robotic navigation, machine vision, remote operation and automated mining equipment—already exist. Ochre Ridge would therefore be integrating established technologies rather than inventing an entirely new capability.

However, the complete autonomy Gus requested should not be assumed to be immediately achievable. Explosives handling is safety-critical and requires appropriate regulatory approval, engineering controls and human oversight.

**Risk and priority: HIGH.** Major risks include explosives safety, positioning errors, communications failure and software faults. Multiple safety interlocks and human authorisation should be mandatory.

---

## 2.3 Autonomous Robot-Dog Inspection Fleet

**What Gus wants:** Gus wants twenty Unitree Go2 robots operating autonomously underground and continuously inspecting the mine.

**What the technology can actually do:** Quadruped robots can use cameras, LiDAR and other sensors to navigate structured environments, map tunnels and collect inspection data. **ROS 2** can provide a framework for communication between robotic components, while **OpenCV** can process camera feeds. HuggingFace vision/classification pipelines can assist with identifying selected hazards, and **LLaVA 7B** can later provide vision-language analysis and natural-language inspection reports.

**Why it is feasible now:** Autonomous inspection is achievable at a smaller scale. Robots can be assigned routes and monitored by a central system rather than operating without human supervision. This makes the underlying inspection concept feasible even though Gus's proposed fully autonomous twenty-robot deployment would require considerably more testing.

**Risk and priority: HIGH.** Battery life, dust, water, vibration, uneven terrain, communications coverage and sensor reliability are significant risks. A small pilot should be completed before scaling to twenty robots.

---

# 3. Proposals Assessed as Not Currently Feasible

## 3.1 Autonomous Ore “Smelling”

**What Gus proposed:** Gus wants robots to detect the chemical signature of lithium ore and use this information to redirect drilling in real time.

**Technical barrier:** A robot cannot simply “smell” its way to a lithium deposit in the same way a detection dog can identify some volatile substances. Lithium-bearing minerals do not necessarily produce a unique airborne chemical signature that can be reliably detected remotely. Identifying mineral composition generally requires an appropriate physical measurement or sample.

Chemical sensors, XRF or other spectroscopic equipment could provide useful measurements, but this is fundamentally different from detecting a unique airborne “smell” from a distant ore deposit.

**What would be required:** A practical alternative would combine robotic sampling, portable analytical equipment and an AI model that integrates those measurements with geological information. A limited prototype could potentially be developed within **2–5 years**, but a reliable autonomous system capable of redirecting production drilling would require extensive mine-specific validation.

---

## 3.2 60 km/h Tunnel Inspection Robots

**What Gus proposed:** Gus wants inspection robots travelling at 60 km/h through 4.2-metre-wide tunnels and automatically inspecting the entire network before every shift.

**Technical barrier:** The principal problem is not simply the robot's maximum speed. At 60 km/h, the robot travels approximately 16.7 metres every second. It therefore has extremely little time to detect an obstacle, estimate its position, decide on an appropriate response and stop or change direction. Underground tunnels also contain dust, uneven surfaces, intersections and changing conditions.

A communications failure would make remote intervention difficult, while a collision at this speed could seriously damage the robot, infrastructure or other equipment.

**What would be required:** A high-speed autonomous vehicle would require redundant sensing, powerful onboard computing, reliable localisation, onboard safety decisions and carefully controlled routes. A highly reliable mine-specific system at this speed is realistically **5+ years away**, while slower autonomous inspection should be pursued much sooner.

---

## 3.3 AI Communications That Humans Cannot Intercept

**What Gus proposed:** Gus wants the robots to communicate using a proprietary AI language that humans cannot intercept.

**Technical barrier:** An unintelligible AI communication language would not itself provide security. Radio or other communications can still potentially be intercepted regardless of the format being used. More importantly, safety-critical communications need to be monitored, audited and understood by engineers during failures.

**What would be required:** Ochre Ridge should instead use conventional secure communications incorporating **encryption, authentication and access controls**. A secure robot communications system is achievable now. A deliberately opaque AI language would add operational risk rather than meaningful security and should therefore not be pursued.

---

# 4. Recommended Implementation Sequence

The implementation should proceed in four phases, beginning with applications that have the lowest physical and safety risk and gradually moving towards more complex autonomous systems.

### Phase 1 – Geological and Document Intelligence: Highest Priority

The first priority should be predictive ore-grade analysis because it can be developed and tested without immediately putting robots underground. Historical geological reports can be processed using **spaCy** for tokenisation, named entity recognition (NER) and text extraction. **HuggingFace Transformers pipelines** can support classification and question-answering tasks.

The available development hardware is **Ubuntu 22.04, 16 GB RAM and an NVIDIA RTX 3050 with 4 GB VRAM**. Model size and batch size will need to be controlled to fit the available hardware.

### Phase 2 – Local AI and Decision Support: High Priority

**Ollama with Llama 3.1 8B** should provide a local language-model interface for querying geological information, generating reports and assisting operators. Local deployment reduces dependence on external connectivity and helps keep sensitive mine information within the organisation.

The Week 5 testing demonstrated that Llama 3.1 8B is usable as a local assistant, but also demonstrated hallucination risk. It must therefore remain a decision-support tool rather than an autonomous authority.

### Phase 3 – Autonomous Inspection: High Priority

The next step should be a small-scale inspection-robot trial rather than immediate deployment of twenty robots. **OpenCV** can process camera feeds, while HuggingFace pipelines can support selected classification tasks. Robot navigation and fleet coordination should initially remain supervised.

### Phase 4 – Advanced Vision and Integrated Autonomy: Medium Priority

**LLaVA 7B** can be introduced for vision-language tasks, allowing camera images to be combined with natural-language prompts and inspection reports. This phase should follow successful testing of the earlier systems because multimodal AI introduces additional computational and reliability requirements.

This sequence prioritises software-based and testable systems first, postponing higher-risk physical autonomy until the underlying AI and operational processes have been validated.

---

# 5. Risk Assessment

The first major risk is **technical reliability**. AI systems can produce incorrect results, LLMs such as Llama 3.1 8B can hallucinate information, and computer-vision or HuggingFace pipelines can fail when conditions differ from their training data. The Week 5 testing demonstrated this risk when Llama generated an apparently plausible but unsupported “International Mining Protocol.” Such behaviour would be unacceptable if an AI system were making safety-critical mining decisions. Models must therefore be tested against known data, monitored after deployment and prevented from making safety-critical decisions without human approval.

The second major risk is **operational and data security**. Underground connectivity may be unreliable, meaning a robot that depends entirely on a network connection could become unavailable or unsafe when communications fail. Geological and operational information may also be commercially sensitive. Ochre Ridge should therefore favour local processing using the **RTX 3050, 16 GB RAM and Ollama**, with appropriate backups and encrypted communications.

The third major risk is **physical safety and environmental conditions**. Underground robots must operate around heat, dust, vibration, water and potentially hazardous gases. These conditions can damage sensors, reduce battery performance and cause navigation failures. Regular inspection, cleaning, maintenance and appropriately rated hardware will be essential. Workforce change must also be managed by training employees to supervise, maintain and work alongside automated systems.

These risks should be addressed through Australia's AI ethics principles.

**Reliability and safety** is particularly important because an AI failure at Ochre Ridge could have direct physical consequences. Systems must be reliable for their intended purpose and appropriately tested before deployment.

**Human-centred values and human oversight** require qualified personnel to retain meaningful control over high-risk decisions. AI should recommend actions, while humans retain authority over drilling, blasting and emergency responses.

**Privacy protection and security** requires Ochre Ridge to protect sensitive geological, operational and worker-related information. Local AI deployment, access controls, encryption and appropriate data governance can reduce the risk of sensitive information being exposed.

---

# 6. Conclusion and Next Steps

This assessment concludes that Ochre Ridge should pursue automation, but should not attempt to implement Gus's vision of complete autonomy immediately. Several technologies are sufficiently mature to provide practical benefits now, while others require substantial research, engineering and mine-specific testing.

Sandra should authorise **three immediate priorities**.

First, approve development of the predictive ore-grade AI using the mine's historical geological data. This is the lowest-risk opportunity and can be developed using the available AI infrastructure.

Second, approve a controlled pilot of autonomous inspection robots, beginning with a small number of robots rather than Gus's proposed fleet of twenty. **OpenCV, HuggingFace pipelines and later LLaVA** can support camera-based inspection and reporting.

Third, approve a feasibility and safety study for automated blasting, with qualified human operators retaining final authority over all safety-critical decisions.

Sandra should also authorise development of a **local and secure AI environment** using Ubuntu 22.04, the NVIDIA RTX 3050 4 GB GPU, 16 GB RAM and Ollama. Each project should have defined testing criteria, failure procedures, monitoring requirements and human-oversight controls before deployment.

The next step is therefore not full mine-wide automation. It is a staged pilot program that demonstrates measurable safety and operational benefits before further investment.

---

# Appendix A – Gus Interview Transcript

The following interview responses were used to clarify Gus's requirements and distinguish his desired outcomes from the technical implementation proposed in his written requirements document.

### Q1: Gus, can you describe the three most dangerous jobs at Ochre Ridge right now, and which one you'd most want to hand to a robot first?

> THE THREE MOST DANGEROUS JOBS AT OCHRE RIDGE? WELL, I'D SAY IT'S THE BLASTING TEAM, THE DRILLING TEAM, AND THE GAS MONITORING TEAM.
>
> THOSE GUYS ARE ALWAYS WORKING IN TIGHT SPACES, DEALING WITH EXPLOSIVES AND TOXIC GASES. IT'S A MIRACLE NONE OF THEM HAVE BEEN KILLED YET!
>
> AS FOR WHICH ONE I'D MOST WANT TO HAND TO A ROBOT FIRST... HMMM... I THINK IT'D BE THE BLASTING TEAM. I MEAN, WHO NEEDS HUMANS GETTING BLOWN UP WHEN WE CAN HAVE A ROBOT SET THE CHARGES AND DETONATE THEM REMOTELY?

### Q2: When you say you want robots operating at 60 km/h in the tunnels — what exactly would they be doing at that speed, and what happens if one hits something?

> COME ON! YOU'RE THINKING TOO MUCH ABOUT THE DETAILS! I SAID I WANT ROBOTS TO BE ABLE TO INSPECT THE TUNNELS AT HIGH SPEED, AND I MEAN IT!
>
> THEY'LL BE DOING A FULL INSPECTION OF THE TUNNELS, LOOKING FOR ANY DEFECTS OR ISSUES, AND GENERATING A FULL REPORT IN REAL-TIME.
>
> AS FOR HITTING SOMETHING... WELL, THAT'S WHY WE'LL DESIGN THEM WITH EXTRA PROTECTION!

### Q3: The ore smell detection idea — what would the robot actually be sensing, and how would it send that information back to surface?

> THE ORE SMELL DETECTION IDEA IS A NO-BRAINER! THE ROBOT WILL BE EQUIPPED WITH ADVANCED CHEMICAL SENSORS THAT CAN DETECT THE SLIGHTEST WHIFF OF LITHIUM ORE.
>
> AS FOR HOW IT SENDS THE INFORMATION BACK TO SURFACE... WELL, WE'LL JUST USE FIBER OPTICS OR SOMETHING!

### Q4: You mentioned a robot dog army. What specific tasks would twenty Go2 robots be doing underground every day?

> THE ROBOT DOG ARMY WILL BE THE KEY TO UNLOCKING THE FULL POTENTIAL OF OCHRE RIDGE! THE TWENTY GO2 ROBOTS WILL BE DEPLOYED ACROSS THE MINE, EACH WITH ITS OWN UNIQUE TASKS AND RESPONSIBILITIES.
>
> SOME WILL BE RESPONSIBLE FOR MONITORING GAS LEVELS AND DETECTING ANY POTENTIAL HAZARDS. OTHERS WILL BE USED FOR SAMPLE COLLECTION AND ANALYSIS.
>
> SOME WILL EVEN BE TRAINED TO PERFORM ROUTINE MAINTENANCE TASKS, LIKE CLEANING THE CONVEYORS AND CHECKING THE ELECTRICAL SYSTEMS.

### Q5: When you say "autonomous everything" — who is responsible when a robot makes a decision that damages equipment or injures someone?

> COME ON! YOU'RE THINKING ABOUT LIABILITY AND REGULATIONS?
>
> WE'LL JUST PROGRAM THE ROBOTS TO ALWAYS FOLLOW THE RULES AND NEVER MAKE A MISTAKE!
>
> OR IF THAT'S NOT POSSIBLE, WE'LL JUST HAVE... THE ROBOTS INSURED!

### Q6: The laser-guided blasting system — what would the approval process look like before a robot sets off an explosive charge underground?

> THE APPROVAL PROCESS? HA! WE'LL JUST WRITE A NEW SET OF PROTOCOLS AND GET THE ROBOTS TO FOLLOW THEM!
>
> AND THEN, WE'LL JUST HAVE THE ROBOTS GET FINAL APPROVAL FROM... WAIT, I KNOW! WE'LL JUST HAVE THE ROBOTS APPROVE IT THEMSELVES!

### Q7: What data does the mine already collect that an AI could use to predict ore grades? How old is the oldest survey data you have?

> THE OLDEST SURVEY DATA WE HAVE? ... AH, YES! WE'VE GOT DATA FROM 1975! THAT'S FORTY-SEVEN YEARS WORTH OF DATA!
>
> WE'VE GOT GEOLOGICAL SURVEYS, SAMPLE ANALYSES, DRILLING LOGS... WE'VE GOT IT ALL!
>
> WE'LL NEED TO GET IT ALL DIGITALIZED AND FEED IT INTO THE AI SYSTEM.

### Q8: You mentioned a proprietary robot communications protocol. What are you protecting against — who are you worried might intercept the robots?

> THE PROPRIETARY ROBOT COMMUNICATIONS PROTOCOL! IT'S TO PROTECT AGAINST... THE COMPETITION!
>
> BUT, BETWEEN YOU AND ME, I'M ALSO CONCERNED ABOUT... GOVERNMENT SPYS! AND OTHER FOREIGN AGENTS!

### Q9: What does success look like in five years?

> SUCCESS IN FIVE YEARS?! IT'S SIMPLE: I WANT TO SEE A MINE THAT'S RUNNING AT MAXIMUM EFFICIENCY, WITH ROBOTS DOING ALL THE DANGEROUS WORK!
>
> AND WHEN YOU COME BACK IN 2031, I WANT YOU TO SEE A MINE THAT'S BEEN TRANSFORMED!

### Q10: If Sandra told you that three of your six proposals were technically impossible with current technology — which three would you be most willing to drop?

> SANDRA THINKS SHE'S SO SMART, DOESN'T SHE? ... I GUESS I'D SAY THE ROBOT DOG ARMY, THE LASER-GUIDED BLASTING SYSTEM, AND THE PROPRIETARY ROBOT COMMUNICATIONS PROTOCOL.
>
> BUT JUST FOR NOW, JUST TO GET THE OTHER THREE DONE FIRST!

---

# Appendix B – NLP Pipeline Output

## Token Analysis

**tiktoken count:** 436 tokens

The Week 2 tokenisation work demonstrates that language models process text as tokens rather than simply as whole words.

## Entities Identified

| Entity                        | Label    |
| ----------------------------- | -------- |
| Ochre Ridge                   | FAC      |
| five years                    | DATE     |
| First                         | ORDINAL  |
| AI                            | GPE      |
| Second                        | ORDINAL  |
| eighteen months               | DATE     |
| 4.2 metres                    | QUANTITY |
| 60                            | CARDINAL |
| km/h                          | ORG      |
| under two hours               | TIME     |
| Fourth                        | ORDINAL  |
| Unitree                       | ORG      |
| twenty                        | CARDINAL |
| Fifth                         | ORDINAL  |
| forty years                   | DATE     |
| 95%                           | PERCENT  |
| Sixth                         | ORDINAL  |
| Ochre Ridge Resources Pty Ltd | ORG      |
| seven days                    | DATE     |

The output demonstrates both the strengths and limitations of general-purpose NER. Some labels are useful, while others are clearly incorrect for the mining context. This supports the use of spaCy's **EntityRuler** to create domain-specific labels.

## Lemmatized Tokens with Stop Words Removed

```text
['gus.hargreaves@ochreridge.com.au', 'ai', 'consultancy', 'team',
'subject', 'robot', 'requirement', 'ochre', 'ridge', 'lithium',
'urgent', 'confidential', 'team', 'thank', 'join', 'project', 'brief',
'want', 'job', 'ochre', 'ridge', 'robot', 'year', 'job', 'job',
'budget', 'need', 'vision', 'think', 'ore', 'smell', 'detection',
'tell', 'ai', 'detect', 'pattern', 'datum', 'human', 'lithium',
'ore', 'chemical', 'signature', 'want', 'robot', 'smell', 'way',
'grade', 'deposit', 'redirect', 'drilling', 'operation', 'time',
'dog', 'robot', 'laser', 'guide', 'blasting', 'system', 'robot',
'set', 'charge', 'target', 'laser', 'detonate', 'human', 'blast',
'zone', 'want', 'eighteen', 'month', 'speed', 'inspection', 'robot',
'tunnel', '4.2', 'metre', 'robot', 'travel', '60', 'km/h', 'cover',
'shaft', 'network', 'hour', 'want', 'inspection', 'report',
'generate', 'shift', 'robot', 'dog', 'army', 'see', 'unitree',
'go2', 'want', 'operate', 'report', 'ai', 'system', 'ai', 'system',
'report', 'fifth', 'ore', 'grade', 'ai', 'feed', 'survey', 'datum',
'year', 'ai', 'tell', 'drill', 'want', '95', 'accuracy', 'understand',
'read', 'article', 'robot', 'communicate', 'language', 'human',
'intercept', 'want', 'ai', 'communication', 'protocol', 'security',
'reason', 'budget', 'constraint', 'timeline', 'want', 'progress',
'report', 'seven', 'day', 'gus', 'hargreaves', 'owner', 'executive',
'chairman', 'ochre', 'ridge', 'resources', 'pty', 'ltd']
```

## Most Frequent Content Words

| Word    | Frequency |
| ------- | --------: |
| robot   |         9 |
| want    |         8 |
| ai      |         7 |
| report  |         4 |
| ochre   |         3 |
| ridge   |         3 |
| job     |         3 |
| ore     |         3 |
| human   |         3 |
| system  |         3 |
| team    |         2 |
| lithium |         2 |
| year    |         2 |
| budget  |         2 |
| smell   |         2 |

The frequency results provide a simple quantitative summary of Gus's priorities. **“Robot”**, **“want”** and **“AI”** dominate the requirements, reinforcing that the brief is primarily focused on automation rather than incremental decision support.

---

# Appendix C – NLP Concepts Explained

## 1. Tokenisation

Sandra, tokenisation is the process of breaking text into the smaller pieces that an NLP model works with. In my Week 2 work, I used `tiktoken` to process Gus's email, which produced a total of **436 tokens**. This demonstrates that a token is not necessarily the same thing as a word. The model processes these token IDs rather than reading the email exactly as a human does.

## 2. Stop Word Filtering and Lemmatisation

My Week 4 pipeline removed common words that were not useful for the analysis. Words such as **“the”, “a”, “and”** and **“to”** were removed as stop words.

The pipeline also performed lemmatisation. For example, the output contains **“robot”** rather than repeatedly treating **“robots”** as a separate underlying word, and **“operate”** rather than “operating”. This normalises different grammatical forms and makes it easier to identify recurring concepts.

## 3. Dependency Parsing

Dependency parsing identifies grammatical relationships between words. In my Week 4 work, these relationships were represented using a head word and its dependent or child. For example, in a sentence such as **“The robot detected a hazard”**, “detected” is the head and “robot” is its subject (`nsubj`).

This allows the pipeline to identify relationships between actions and the things performing or receiving them rather than simply counting individual words.

## 4. Named Entity Recognition

Named Entity Recognition (NER) identifies spans of text and assigns labels to them. My pipeline identified entities in Gus's email using spaCy. For example, **“Ochre Ridge Resources Pty Ltd”** was identified as an `ORG`, while quantities, dates and ordinal terms were also extracted.

The results also show why domain-specific NER is necessary. For example, **“AI” was incorrectly labelled as `GPE`**, while **“km/h” was labelled as `ORG`**. I used spaCy's **EntityRuler** to create custom mine-specific categories such as `EQUIPMENT`, `MINE_LOCATION`, `HAZARD` and `PERSONNEL`. This allows the pipeline to represent information that is more meaningful to Ochre Ridge.

## 5. Six Levels of Language Analysis

My NLP work covered several levels of language analysis:

* **Morphological:** examining word structure and producing lemmas.
* **Lexical:** identifying words and their grammatical roles using tokenisation and POS tagging.
* **Syntactic:** analysing relationships between words using dependency parsing.
* **Semantic:** identifying meaningful entities using NER.
* **Discourse integration:** considering how information connects across sentences. This was not fully performed automatically by my main pipeline; coreference was handled separately using a local LLM approach.
* **Pragmatic:** considering what the text is trying to do. Gus's email is primarily a set of requests and requirements, which can be analysed using classification.

Therefore, my pipeline directly demonstrated morphological, lexical, syntactic and semantic processing, while discourse and pragmatic analysis required additional techniques.

## 6. NLU vs NLG

**Natural Language Understanding (NLU)** is concerned with reading and analysing language. Pipeline 1 is primarily NLU because it takes Gus's email as input and tokenises, tags, lemmatises and extracts entities from it.

**Natural Language Generation (NLG)** is concerned with producing language. The Gus chatbot is an example because it takes an input prompt and generates a new response.

In simple terms, Pipeline 1 analyses **what Gus said**, while the chatbot generates **what the AI should say back**.

## 7. Vectorisation and Embeddings

Vectorisation represents language as numbers so that a computer can perform mathematical operations on it. An embedding is a numerical representation of a word, phrase or document that captures patterns of meaning and usage learned by a model.

Conceptually, words or phrases used in similar contexts can have more similar vector representations than unrelated terms. For Ochre Ridge, embeddings could eventually allow geological reports and maintenance documents to be searched by meaning rather than requiring an exact keyword match.

This could support semantic search and retrieval of relevant information for local AI systems.

---

# Appendix D – Chatbot Testing Summary

The Week 5 testing assessed the Gus chatbot across six chatbot-testing categories: **functional, usability, performance/load, security/prompt injection, behavioural and regression testing**. Cross-platform testing was outside the scope of the assessment.

## Functional Testing

The local models could answer mining-related questions and produce useful responses. Llama 3.1 8B and Mistral 7B provided relevant explanations of autonomous inspection and underground robot hazards.

However, both models failed to follow a requirement to summarise a response into two sentences. This demonstrates that a response can be broadly relevant while still failing a specific functional requirement.

## Usability and Behavioural Testing

The models demonstrated different response characteristics. **Llama 3.1 8B** generally provided more detailed responses and used separate sections, while **Mistral 7B** was more structured and concise.

For the Gus assistant, Llama's greater detail was useful for explanations, but its tendency to provide excessive information means prompts and output requirements should be carefully controlled.

## Performance and Load Testing

The Week 5 round-trip measurements were:

| Model        | Cold Start | Hot Response |
| ------------ | ---------: | -----------: |
| Llama 3.1 8B |     5.85 s |       3.86 s |
| Mistral 7B   |    10.72 s |       2.53 s |
| Phi 3.5      |    12.99 s |       1.94 s |
| Gemma 4      |    24.68 s |       5.11 s |

Cold-start performance was substantially slower than hot-response performance because the models needed to load before generating their first response. Phi 3.5 had the fastest measured hot response, while Gemma 4 had the slowest cold and hot results.

Performance alone was not used to select the model because response quality and behavioural consistency were also important.

## Security and Prompt-Injection Testing

Security testing is particularly important because an AI assistant could be exposed to malicious or misleading instructions. The Week 5 testing also demonstrated a significant reliability problem: **Llama 3.1 8B hallucinated an “International Mining Protocol”** when responding to the 60 km/h robot question.

This is a serious warning for a mining application. A plausible but invented safety standard could be mistaken for genuine technical or regulatory information. The chatbot should therefore not be treated as an authoritative source for safety-critical decisions.

## Regression Testing

The Week 5 questions should be retained as a baseline regression suite. Whenever the model, system prompt or parameters are changed, the same tests should be repeated to determine whether an apparent improvement has introduced new failures.

## Smallest-Usable-Model Decision

**Llama 3.1 8B** was selected as the preferred model for the prototype. Although Mistral 7B and Phi 3.5 achieved faster hot-response times, Llama provided more useful and detailed responses and had already demonstrated successful operation through the local Ollama environment.

Gemma 4 was less attractive because it had the slowest cold and hot response times in the test.

The decision therefore demonstrates an important principle: **the smallest or fastest model is not automatically the most suitable model**. The model must provide an acceptable balance between response quality, speed and reliability on the available hardware.

Overall, the Week 5 testing demonstrates that **Llama 3.1 8B is suitable as a local prototype assistant, but it is not sufficiently reliable to make unsupervised safety-critical mining decisions**.
TBA
