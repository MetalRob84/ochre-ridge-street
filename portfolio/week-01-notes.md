Part 2 - NLP Pipelines in Python

Test 1:
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("The pump failed in shaft 3")
print(result)

Result:
[{'label': 'NEGATIVE', 'score': 0.9994944334030151}]

Test 2:
classifier = pipeline("sentiment-analysis")
result = classifier("All systems nominal")
print(result)

Result:
[{'label': 'POSITIVE', 'score': 0.9183382987976074}]

Test 3:
classifier = pipeline("sentiment-analysis")
result = classifier("Gas leak detected in zone B")
print(result)

Result:
[{'label': 'NEGATIVE', 'score': 0.9927787184715271}]

Test 4:
classifier = pipeline("sentiment-analysis")
result = classifier("Gas leak detected in zone B")
print(result)

Result:
[{'label': 'NEGATIVE', 'score': 0.981253445148468}]

Part 3 — Why this matters for Ochre Ridge

1. Maintainer Instructions

Purpose: Enable robots to understand spoken or written maintenance commands.

    Converts natural language into machine actions.
    Example: "Inspect Conveyor 3 and replace the worn belt if damaged."
    Benefit: Faster maintenance, hands-free operation, and fewer communication errors.

2. Report Parsing

Purpose: Automatically extract important information from maintenance reports.

    Identifies equipment names, fault codes, locations, dates, and technician notes.
    Example:
        Equipment: Crusher A
        Fault Code: FC-204
        Location: Pit 2
    Benefit: Saves time, improves record keeping, and makes reports searchable.

3. Safety Alert Classification

Purpose: Categorise incoming messages based on urgency.

    Detects whether a message is critical, high, medium, or low priority.
    Example:
        "Gas leak detected in Tunnel 4" → Critical
        "Routine inspection completed" → Low
    Benefit: Ensures urgent safety issues receive immediate attention.

4. Shift Handover Note Summarisation

Purpose: Produce concise summaries of previous shift reports.

    Extracts key events, completed tasks, ongoing issues, and outstanding work.
    Example Summary:
        Repaired Pump 2.
        Conveyor 5 requires inspection.
        Stockpile measurements completed.
    Benefit: Improves communication between shifts and reduces missed information.

5. Ore Grade Documentation

Purpose: Scan laboratory reports and extract ore sample results.

    Recognises sample IDs, mineral grades, locations, and testing dates.
    Example:
        Sample ID: OR-1025
        Iron Grade: 63.4%
        Location: North Pit
    Benefit: Speeds up data entry, reduces manual errors, and supports production planning.

What surprised me most about how NLP actually works is that it does not truly understand language like a person; instead, it learns patterns from large amounts of text to predict meaning and generate useful responses.
