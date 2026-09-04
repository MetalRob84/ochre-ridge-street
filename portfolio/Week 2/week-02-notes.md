Part 1
>>> import tiktoken
>>> enc = tiktoken.get_encoding("cl100k_base")  # GPT-4 / text-embedding-ada-002 encoding
>>> text = "Hargreaves wants autonomous inspection robots operating at 60km/h."
>>> tokens = enc.encode(text)
>>> print(f"Token count: {len(tokens)}")
Token count: 15
>>> print(f"Tokens: {tokens}")
Tokens: [39, 867, 265, 4798, 6944, 39293, 26767, 29807, 10565, 520, 220, 1399, 16400, 7682, 13]
>>> print(f"Decoded: {[enc.decode([t]) for t in tokens]}")
Decoded: ['H', 'arg', 're', 'aves', ' wants', ' autonomous', ' inspection', ' robots', ' operating', ' at', ' ', '60', 'km', '/h', '.']
>>> for encoding_name in ["cl100k_base", "p50k_base", "r50k_base"]:
...     enc = tiktoken.get_encoding(encoding_name)
...     tokens = enc.encode(text)
...     print(f"{encoding_name}: {len(tokens)} tokens")
...
cl100k_base: 15 tokens
p50k_base: 15 tokens
r50k_base: 15 tokens
>>>

Part 2
>>> import tiktoken
>>> enc = tiktoken.get_encoding("cl100k_base")
>>> sample_report = """
... Maintenance Report — Shaft 4 East Conveyor
... Date: 2026-04-28
... Technician: J. Nguyen
...
... Inspection of conveyor belt drive assembly complete. Bearing on motor shaft
... showing early signs of wear — estimated 3 weeks to failure if not replaced.
... Lubrication applied to all accessible points. Belt tension within spec.
... Gas sensor in Zone B reading 12 ppm methane — within safe range but trending
... upward over last 14 days. Recommend daily monitoring. No other defects noted.
... Next inspection due: 2026-05-05.
... """
>>> tokens = enc.encode(sample_report)
>>> print(f"Report token count: {len(tokens)}")
Report token count: 119

Calculate how many reports you could fit in the context window of each model in the table.

GPT-4o 	128,000 tokens - 1,075.6
Llama 3.1 8B 	128,000 tokens - 1,075.6
Mistral 7B 	32,000 tokens - 268.9
Phi-3 medium 	128,000 tokens - 1,075.6

Part 3
>>> reports_per_month = 1000
... tokens_in_per_report = 400
... tokens_out_per_report = 150
...
... # GPT-4o pricing (April 2026 — check current pricing before using in a real quote)
... price_per_1k_input = 0.005   # USD
... price_per_1k_output = 0.015  # USD
...
... monthly_input_cost = (reports_per_month * tokens_in_per_report / 1000) * price_per_1k_input
... monthly_output_cost = (reports_per_month * tokens_out_per_report / 1000) * price_per_1k_output
... monthly_total = monthly_input_cost + monthly_output_cost
...
... print(f"Monthly cloud cost estimate: USD ${monthly_total:.2f}")
... print(f"Annual estimate: USD ${monthly_total * 12:.2f}")
...
Monthly cloud cost estimate: USD $4.25
Annual estimate: USD $51.00

Calculate the break-even point. At what monthly report volume does the cloud cost exceed $100/month USD? At what volume does it exceed $1,000/month?
Monthly reports at $100 = ~ $23,500
Monthly reports at $1000 = ~ $235,000

