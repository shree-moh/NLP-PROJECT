from transformers import pipeline
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="eng_Latn",
    tgt_lang="kor_Hang",
    device=0  # Use GPU 0
)

def translate_en_to_ko(text):
    return translator(text)[0]['translation_text']