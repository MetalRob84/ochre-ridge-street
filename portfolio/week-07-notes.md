# Part 1 — Review and structure

# Part 2 — Write the context, feasible and infeasible sections

## 1. Context and Methodology

Gus wants Ochre Ridge to automate dangerous work using AI and robotics within five years. His requirements document and interview identified six main areas:

1. Robots that can detect lithium ore by "smell".
2. Laser-guided autonomous blasting.
3. Robots travelling at 60 km/h to inspect tunnels.
4. Twenty Unitree Go2 robot dogs operating underground.
5. AI that predicts where to drill using historical geological data.
6. A private AI communication system that humans cannot understand or intercept.

I assessed these proposals by asking whether the technology already exists, whether it could realistically operate at a mine such as Ochre Ridge, and what risks would be involved.

I also considered the technology used during the course, including **spaCy, HuggingFace pipelines, Ollama, Llama 3.1 8B, LLaVA, OpenCV and robotics concepts from ROS**.

The assessment also considered Gus's interview answers. These showed that he wants full autonomy, including robots making safety-critical decisions without human involvement. This creates an important safety and governance issue.

The available development hardware is **Ubuntu 22.04, an NVIDIA RTX 3050 with 4 GB VRAM and 16 GB RAM**. This hardware is suitable for smaller local AI models and prototypes, but it places limits on large models and complex real-time workloads.



## 1.1 Technical Definitions

### Artificial Intelligence (AI)

AI is the broad idea of making machines perform tasks that normally require intelligence.

At Ochre Ridge, the **Gus chatbot running through Ollama** is an example of AI because it can interpret questions and generate responses.

### Machine Learning (ML)

ML is a type of AI where the system learns patterns from data instead of only following manually written rules.

For Ochre Ridge, historical geological and drilling data could be used to train a model to predict likely ore grades.

### Deep Learning (DL)

Deep learning is machine learning based on neural networks with many layers. The language models used during the course are examples of deep learning.

At Ochre Ridge, **Llama 3.1 8B** and **LLaVA 7B** are examples of deep-learning models. LLaVA could eventually be used to analyse images from inspection robots.



## 2. Feasible Applications

### 2.1 Predictive Ore-Grade AI

**What Gus wants:**
Gus wants AI to analyse approximately forty years of geological data and tell the mine where to drill next.

**What the technology can actually do:**
A machine-learning model such as **Random Forest or XGBoost**, using Python and scikit-learn, could learn relationships between historical geological information and measured ore grades. The system could then provide predictions for new locations.

**Why it is feasible:**
This is mainly a data and software problem rather than a robotics problem. Existing geological reports, drilling records and sample results can be prepared and used for training. The available computer can support smaller models and development work.

The 95% accuracy target should not be assumed. The model needs to be tested on data it has not seen before.

**Risk and priority:**
**High priority.** The main risks are poor historical data, missing information and overfitting.



### 2.2 Robot Inspection Fleet

**What Gus wants:**
Gus wants twenty Unitree Go2 robots to inspect the mine underground.

**What the technology can actually do:**
Quadruped robots can use cameras and other sensors to navigate areas, avoid obstacles and collect inspection information. **OpenCV** can process camera feeds, while AI classification models can help identify selected hazards.

The robots could also communicate through a fleet-control system. However, they should remain supervised rather than being completely independent.

**Why it is feasible:**
Robot inspection is already a realistic use of autonomous robotics. Ochre Ridge could start with one or two robots, test them underground and expand the fleet if the results are reliable.

**Risk and priority:**
**High priority.** Risks include dust, water, heat, battery life, uneven ground, communications and equipment damage.



### 2.3 Automated Blasting

**What Gus wants:**
Gus wants robots to set charges, use laser guidance and detonate explosives without humans entering the blast zone.

**What the technology can actually do:**
Robotic and remotely operated mining equipment can already perform parts of drilling and blasting workflows. A system could combine cameras, LiDAR, positioning systems and autonomous equipment.

However, the final approval for a blast should remain with qualified human personnel.

**Why it is feasible:**
The individual technologies already exist. The challenge is integrating them safely into Ochre Ridge's mining environment.

**Risk and priority:**
**High priority, but safety-critical.** Explosives, positioning errors, sensor failures and communication failures could cause serious harm.



## 3. Proposals Assessed as Not Currently Feasible

### 3.1 Ore "Smelling"

**What Gus proposed:**
Gus wants robots to detect lithium ore through its chemical signature and redirect drilling in real time.

**Technical barrier:**
A robot cannot simply smell lithium ore like a detection dog. Lithium-bearing minerals do not necessarily produce a unique airborne smell that can be detected remotely. Reliable identification would normally require physical sampling and chemical or mineralogical analysis.

**What would be required:**
A future system could combine robotic sampling with sensors such as XRF or other spectroscopic equipment and then use AI to interpret the results. A limited prototype could potentially be developed within **2–5 years**, but reliable autonomous drilling decisions would require much more testing.


### 3.2 60 km/h Tunnel Robots

**What Gus proposed:**
Gus wants robots to travel through 4.2-metre-wide tunnels at 60 km/h while inspecting the mine.

**Technical barrier:**
At 60 km/h, the robot has very little time to detect obstacles and react. Underground tunnels can contain uneven surfaces, dust, intersections and unexpected objects. A communications failure would also make remote intervention difficult.

**What would be required:**
A high-speed autonomous vehicle would need redundant sensors, onboard decision-making and controlled routes. A reliable mine-specific system would likely require **5+ years** of development and testing. Slower autonomous inspection is much more realistic now.


### 3.3 Unobservable AI Communications

**What Gus proposed:**
Gus wants robots to communicate using a proprietary AI language that humans cannot understand or intercept.

**Technical barrier:**
An unusual AI-generated language does not automatically make communications secure. Radio or network traffic can still potentially be intercepted. It would also make debugging and safety monitoring harder.

**What would be required:**
Ochre Ridge should use normal secure communications with **encryption, authentication and access controls**. Secure robot communication is achievable now, while deliberately making communications impossible for humans to understand would increase risk rather than improve security.



# Part 3 — Write sections 4–6, appendices, then Executive Summary #

## 4. Recommended Implementation Sequence

The program should be introduced in stages.

### Phase 1 — Geological and Document AI

Start with predictive ore-grade analysis and document processing. **spaCy** can be used for tokenisation, NER and text processing. **HuggingFace pipelines** can support classification and question answering.

This is the safest starting point because it does not immediately control physical equipment.

### Phase 2 — Local AI Assistant

Use **Ollama with Llama 3.1 8B** to provide a local AI assistant for querying documents, geological information and generating reports.

Running the model locally is useful because mine data may be sensitive and underground connectivity may not always be reliable.

### Phase 3 — Robot Inspection

Begin with a small inspection robot trial. **OpenCV** can process camera feeds, while HuggingFace models can assist with image classification.

The robots should initially operate under human supervision.

### Phase 4 — Advanced Vision

Introduce **LLaVA 7B** for vision-language tasks. It could eventually take inspection images and generate descriptions or draft reports.

This should happen after the basic inspection system has been tested because vision-language models introduce additional reliability and computing requirements.

The development environment is **Ubuntu 22.04, NVIDIA RTX 3050 4 GB VRAM and 16 GB RAM**. This is suitable for smaller local models and prototypes, but larger models may require more powerful hardware.


## 5. Risk Assessment

### 1. AI Reliability

AI models can produce incorrect information. LLMs can hallucinate and computer-vision systems can fail when they encounter conditions different from their training data.

This is especially dangerous at Ochre Ridge because incorrect AI decisions could affect drilling, vehicles or blasting. AI should therefore provide recommendations rather than make critical decisions independently.

### 2. Connectivity and Data Security

Underground connectivity may not always be reliable. A robot that depends completely on a network connection could become unsafe if communication is lost.

Mine geological data may also be commercially sensitive. Local processing with **Ollama** can reduce the need to send sensitive information to external cloud services. Encryption, access controls and backups should also be used.

### 3. Physical Environment and Maintenance

Mining environments contain dust, heat, vibration, water and potentially dangerous gases. These conditions can damage sensors, electronics and batteries.

Robots will require regular cleaning, inspection, maintenance and replacement of damaged components.

The workforce also needs to be considered. Employees should be trained to operate, supervise and maintain the new systems instead of treating automation simply as worker replacement.

### AI Ethics

**Reliability and safety:** AI systems must be reliable enough for their intended use. Ochre Ridge should not allow an unreliable model to directly control safety-critical equipment.

**Human oversight:** Qualified workers must retain meaningful control over blasting, drilling and emergency decisions. AI should support people rather than remove accountability.

**Privacy protection and security:** Geological and operational information should be protected through local processing, access controls and encryption.


## 6. Conclusion and Next Steps

Ochre Ridge should continue investigating AI and robotics, but it should not attempt Gus's idea of complete autonomy immediately.

Sandra should authorise three immediate priorities:

1. **Predictive ore-grade AI** using historical geological and drilling data.
2. **A small supervised robot inspection pilot** using cameras, OpenCV and AI-based analysis.
3. **A feasibility and safety study for automated blasting**, with human approval remaining mandatory.

Sandra should also approve a local AI development environment using **Ubuntu 22.04, RTX 3050 4 GB VRAM, 16 GB RAM and Ollama**.

The next stage should be a controlled pilot program with clear testing requirements. Each system should demonstrate reliability and safety before being connected to more important mine operations.


## Appendix A — Gus Interview Summary

Gus identified blasting, drilling and gas monitoring as some of the most dangerous jobs at the mine. His preferred solution is to replace dangerous work with robots.

He wants robots to:

* perform blasting without human involvement;
* travel at 60 km/h underground;
* detect ore using chemical sensors;
* operate twenty Go2 robot dogs;
* collect samples and monitor gas;
* use AI to predict drilling locations;
* communicate using a proprietary protocol;
* eventually perform most dangerous mine work autonomously.

Gus's answers also showed that he expects the robots to operate with very little human involvement. This creates significant safety, reliability and accountability concerns.


## Appendix B — NLP Evidence

The Week 2 tokenisation work counted **436 tokens** in Gus's email.

Examples from the analysis include:

* **“robot”** appeared 9 times.
* **“want”** appeared 8 times.
* **“AI”** appeared 7 times.
* **“report”** appeared 4 times.
* **“ore”** appeared 3 times.
* **“human”** appeared 3 times.

The Week 4 pipeline also removed common stop words and produced lemmas. For example:

* “robots” → **robot**
* “jobs” → **job**
* “operating” → **operate**
* “deposits” → **deposit**

NER identified entities including **Ochre Ridge**, **Unitree** and **Ochre Ridge Resources Pty Ltd**. The pipeline also used custom spaCy EntityRuler categories such as **EQUIPMENT, MINE_LOCATION, HAZARD and PERSONNEL**.

These examples demonstrate how the NLP pipeline converts Gus's unstructured email into structured information that can be analysed.


## Appendix C — NLP Concepts Explained

### 1. Tokenisation

Tokenisation breaks text into smaller pieces called tokens. In Week 2, tiktoken was used to process Gus's email. This showed that a token is not always the same as a complete word.

### 2. Stop Words and Lemmatisation

Stop words such as “the”, “a” and “and” were removed because they were not useful for the analysis.

Lemmatisation reduced words to a common form. For example, **“robots” became “robot”**.

### 3. Dependency Parsing

Dependency parsing shows relationships between words. For example, in “The robot detected a hazard”, **“detected”** is the main verb and “robot” is its subject.

This helps the system understand who is performing an action and what the action affects.

### 4. Named Entity Recognition

NER identifies important entities in text. The pipeline identified organisations and other entities in Gus's email.

Custom EntityRuler categories were also created for mining-specific information such as equipment, mine locations and hazards.

### 5. Six Levels of Language Analysis

The pipeline covered:

* **Morphological:** word structure and lemmas.
* **Lexical:** words and their grammatical roles.
* **Syntactic:** relationships between words.
* **Semantic:** entities and meaning.
* **Discourse:** how information connects across sentences.
* **Pragmatic:** what the speaker is trying to do.

The first four were directly supported by the pipeline. Discourse and pragmatic analysis required additional techniques.

### 6. NLU vs NLG

Pipeline 1 is mainly **Natural Language Understanding (NLU)** because it reads and analyses Gus's email.

The Gus chatbot is mainly **Natural Language Generation (NLG)** because it generates a new response from a prompt.

### 7. Embeddings

Embeddings represent words or pieces of text as numbers. Text with similar meanings can have similar numerical representations.

For Ochre Ridge, embeddings could eventually be used to search large collections of geological and maintenance documents by meaning rather than exact keywords.


## Appendix D — Chatbot Testing Summary

The Week 5 testing covered six types:

1. Functional
2. Usability
3. Performance/load
4. Security and prompt injection
5. Behavioural
6. Regression

Cross-platform testing was outside the scope.

## Performance Results

| Model        |    Cold |    Hot |
| ------------ | ------: | -----: |
| Llama 3.1 8B |  5.85 s | 3.86 s |
| Mistral 7B   | 10.72 s | 2.53 s |
| Phi 3.5      | 12.99 s | 1.94 s |
| Gemma 4      | 24.68 s | 5.11 s |

The tests showed that cold-start performance was slower because models had to be loaded. Hot responses were much faster.

Phi 3.5 had the fastest hot response, but speed was not the only consideration.

## Functional Testing

The models were able to answer mining-related questions. However, both Llama and Mistral had problems following some exact instructions, such as summarising a response into exactly two sentences.

## Usability and Behaviour

Llama 3.1 8B gave more detailed responses and used sections. Mistral 7B was more concise and structured.

Llama was preferred because it gave more useful responses for the intended assistant role.

## Security and Reliability

Testing showed that Llama 3.1 8B could hallucinate. One example was an invented **“International Mining Protocol”** in response to the 60 km/h robot question.

This is a serious concern for a mining application because an AI could produce information that sounds authoritative but is false.

## Regression Testing

The Week 5 tests should become a repeatable test set. Whenever the model, prompt or system changes, the same tests should be run again to check that improvements do not introduce new problems.

## Model Decision

**Llama 3.1 8B** was selected as the preferred local model. It was not the fastest model, but it produced useful and detailed responses and had already been demonstrated successfully using Ollama.

The conclusion is that Llama 3.1 8B is suitable for a **prototype local assistant**, but it is not reliable enough to make unsupervised safety-critical mining decisions.


## Executive Summary

This report looks at Gus Hargreaves's plan to use AI and robots to remove people from dangerous work at Ochre Ridge Lithium Mine within five years. His proposals include autonomous blasting, ore detection, high-speed inspection robots, a fleet of robot dogs, predictive ore-grade AI and a private robot communication system.

The assessment found that some of these ideas are possible with current technology, but several would need to be changed before they could safely be used at the mine. The three strongest opportunities are **predictive ore-grade analysis, supervised robot inspection and automated blasting**.

The first recommendation is to develop an AI system that uses the mine's historical geological data to help identify promising drilling locations. This is relatively low risk because it can be developed and tested before being connected to physical mining equipment.

The second recommendation is to trial a small number of robot inspection platforms underground. These robots could use cameras, sensors and computer vision to identify hazards and create inspection reports. The mine should not immediately deploy twenty robots.

The third recommendation is to investigate automated blasting as a controlled safety-critical system. Robots can perform hazardous physical tasks, but qualified humans should retain final authority over blasting.

Some of Gus's proposals are not currently practical in the form requested. These include robots travelling at 60 km/h underground, robots simply "smelling" lithium ore, and an intentionally unobservable AI communication language.

The overall recommendation is to use a staged approach. Ochre Ridge should automate dangerous tasks gradually while keeping **safety, reliability, security and human oversight** as core requirements.
