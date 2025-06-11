from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
qa_pipeline = pipeline(
    "question-answering",
    model=model,
    tokenizer=tokenizer,
    device=0  # Use GPU 0; use -1 for CPU
)

def ask_llm(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']