from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load model + tokenizer once when the app starts
tokenizer = AutoTokenizer.from_pretrained("camie-cool-2903/transience")
model = AutoModelForSeq2SeqLM.from_pretrained("camie-cool-2903/transience")

# Create pipeline (easiest way to summarize)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text: str) -> str:
    if len(text.strip()) == 0:
        return "Please enter some text."
    summary = summarizer(text, max_new_tokens=100, min_length=10, do_sample=False)
    return summary[0]["summary_text"]

def clean_input(text):
    # Replace curly quotes and fancy characters
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace("’", "'").replace("‘", "'")
    # Remove unusual control characters (if any)
    text = ''.join(ch for ch in text if ord(ch) >= 32 or ch in '\n\r\t')
    return text.strip()
