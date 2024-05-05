from load_casts import casts
from create_embeddings_model import model

topics, probs = model.fit_transform([str(txt) for txt in casts['text']])
print(topics, probs)

fig = model.visualize_barchart()
fig.write_html("barchart.html")


fig2 = model.visualize_hierarchy()
fig2.write_html("hierarchy.html")

fig3 = model.visualize_heatmap()
fig3.write_html("heatmap.html")

fig4 = model.visualize_distribution()
fig4.write_html("distribution.html")

fig5 = model.visualize_term_rank()
fig5.write_html("term_rank.html")

fig6 = model.visualize_topics()
fig6.write_html("topics.html")

fig7 = model.visualize_topics_over_time(casts['timestamp'])
fig7.write_html("topics_over_time.html")
