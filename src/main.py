from load_casts import casts
from create_embeddings_model import model

topics, probs = model.fit_transform([str(txt) for txt in casts['text']])
print(topics, probs)

fig = model.visualize_barchart()
fig.write_html("barchart.html")
