Part 1 — What a transformer actually is

A Transformer is a type of artificial intelligence that reads information and works out what it means by looking at all the words together, not just one word at a time.
First, it breaks the text into small pieces it can understand. 
It then looks at how those pieces are connected before giving an answer, such as writing a summary, translating text, answering a question, or sorting information into categories.
This is much better than older computer programs, which often looked at words one by one and missed the bigger picture.
The important thing for Gus to know before Friday is that AI Transformers are not the robot characters from the movies.
They are computer programs that help people understand and work with large amounts of information quickly.

Part 2
***** INSTALL TRANSFORMERS Ver 5.2 *****
from transformers import pipeline

# 1. Sentiment analysis — is this report positive or negative?
sentiment = pipeline("sentiment-analysis")
print(sentiment("Bearing replacement complete. All systems nominal."))
print(sentiment("Gas leak detected in Zone B. Evacuation in progress."))

[{'label': 'NEGATIVE', 'score': 0.9953864216804504}] - this result is wrong, should be positive
[{'label': 'NEGATIVE', 'score': 0.994212806224823}] - this is correct

# 2. Named Entity Recognition — what are the named things?
ner = pipeline("ner", aggregation_strategy="simple")
print(ner("John Nguyen completed inspection of Shaft 4 East on Monday."))

[{'entity_group': 'PER', 'score': np.float32(0.9878328), 'word': 'John Nguyen', 'start': 0, 'end': 11}, {'entity_group': 'ORG', 'score': np.float32(0.3139197), 'word': 'East', 'start': 44, 'end': 48}]
It got the person and his name right.
It thought the location was an ORG, and missed the whole name.

# 3. Question answering — extract an answer from a passage
qa = pipeline("text-generation", model="Qwen/Qwen3-4B-Instruct-2507")
messages = [
    {
        "role": "user",
        "content": "Based on the following context, answer the question.\n\nContext: The methane sensor in Zone B recorded 42 ppm at 0630 on Tuesday. Safe limit is 50 ppm.\n\nQuestion: What is the safe limit for methane?",
    }
]
output = qa(messages)
print(output[0]["generated_text"][-1]["content"])

The safe limit for methane is 50 ppm
The answer is correct

# 4. Text summarisation — compress a long report
summariser = pipeline("summarization", min_length=20, max_length=60)
report = """Maintenance team completed full inspection of the east conveyor system. 
Belt tension was checked and found within spec. Motor bearings on units 2 and 4 
were lubricated. Unit 3 motor is showing elevated temperature readings — 
recommend replacement within 30 days. All safety interlocks tested and functional. 
Gas sensors calibrated. Estimated 2 hours to complete follow-up on motor 3."""
print(summariser(report))



# 5. Zero-shot classification — classify without training on mine data
classifier = pipeline("zero-shot-classification")
print(classifier(
    "Motor unit 3 temperature 87°C, threshold 85°C",
    candidate_labels=["routine maintenance", "urgent fault", "safety critical"]
))

{'sequence': 'Motor unit 3 temperature 87°C, threshold 85°C', 'labels': ['safety critical', 'urgent fault', 'routine maintenance'], 'scores': [0.6782616972923279, 0.23152710497379303, 0.09021121263504028]}
Safety levels in correct order.
