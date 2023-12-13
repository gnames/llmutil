from sentence_transformers import SentenceTransformer, CrossEncoder

# vectors 768
MODEL = 'multi-qa-mpnet-base-cos-v1'
# vectors 384
# MODEL = 'multi-qa-MiniLM-L6-cos-v1'
client = SentenceTransformer(MODEL)

# CROSS_MODEL = 'cross-encoder/stsb-distilroberta-base'
CROSS_MODEL = 'cross-encoder/stsb-TinyBERT-L-4'
cross_enc = CrossEncoder(CROSS_MODEL)


def embed(texts):
    return client.encode(texts, batch_size=32, show_progress_bar=False)


def cross_embed(texts):
    return cross_enc.predict(texts)
