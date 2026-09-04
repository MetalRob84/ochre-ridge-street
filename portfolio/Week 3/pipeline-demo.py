from transformers import pipeline


messages = [
    {
        "role": "user",
        "content": "Based on the following context, answer the question.\n\nContext: The methane sensor in Zone B recorded 42 ppm at 0630 on Tuesday. Safe limit is 50 ppm.\n\nQuestion: What is the safe limit for methane?",
    }
]
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

"""
Output:

[transformers] Both `max_new_tokens` (=256) and `max_length`(=20) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
[transformers] Ignoring clean_up_tokenization_spaces=True for BPE tokenizer Qwen2Tokenizer. The clean_up_tokenization post-processing step is designed for WordPiece tokenizers and is destructive for BPE (it strips spaces before punctuation). Set clean_up_tokenization_spaces=False to suppress this warning, or set clean_up_tokenization_spaces_for_bpe_even_though_it_will_corrupt_output=True to force cleanup anyway.
The safe limit for methane is 50 ppm.
"""
