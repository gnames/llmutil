from sentence_transformers import SentenceTransformer, util

# vectors 768
MODEL = 'multi-qa-mpnet-base-cos-v1'
# vectors 384
# MODEL = 'multi-qa-MiniLM-L6-cos-v1'
client = SentenceTransformer(MODEL)


def embed(texts):
    return client.encode(texts, batch_size=32, show_progress_bar=False)
