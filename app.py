from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from fastapi import FastAPI, Body
from pydantic import BaseModel

# pipeline and tokenizer
nlp = pipeline("summarization", model = "facebook/bart-large-cnn", tokenizer = "facebook/bart-large-cnn")

# result = (nlp(ARTICLE, max_length = max_length, min_length=130, do_sample=do_sample))

app = FastAPI()
class TextData(BaseModel):
    text: str

# allow users to select what minimum and maximum length of summary
class SummarizationParams(BaseModel):
    max_length: int = 130
    min_length: int = 50


@app.post("/fbsummarize_text") #function handles POST requests to '/summarize_text' endpoint
#creating function
def summarize_text(text, params: SummarizationParams = Body(...)): # dots show necessary input from user
    result = nlp(text, max_length =params.max_length, min_length = params.min_length, do_sample = True)
    return result[0]['summary_text']

# print(summarize_text(ARTICLE))


