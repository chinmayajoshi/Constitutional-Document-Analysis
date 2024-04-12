<h3> Analysing the Indian Constitution using NLP </h3>

<ul>
<li>Download Contitution</li>

- Run `python download_india_const.py` to download the Indian Constitution pdf from [online](https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2023/05/2023050195.pdf).
- Read the [python script](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/download_india_const.py).

<br>
<li>Extract Articles</li>

- Extracting Articles using RegEx.
- Basic data cleaning.
- IPython Notebook viewable [here](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/data_exploration.ipynb).

<br>
<li>Generate Article Embeddings</li>

- OpenAI Model [text-embedding-ada-002](https://platform.openai.com/docs/models/embeddings) selected for good Clustering score (at the time of generation) on [Massive Text Embedding Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard).
- Set up OpenAI secret key in the `secret_key.py` file.
- Used [LangChain](https://www.langchain.com/) API to generate sentence embeddings.
- Check out the [notebook](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/embeddings_generation.ipynb).

<br>
<li>K-Means Clustering</li>

- Selected K=7 for better interpretability of the clusters (even though bigger values give better Silhouette Scores)<br>
![image](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/Inertia_Silhouette_Plot.png)
- K-Means (K=7) Clusters on Article Embeddings visualized with tSNE Component (n=2) Scatter Plot<br>
![image](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/KMeans_tSNE_Plot_v2.png)
- Check out another [notebook](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/title_embeddings_clustering.ipynb) with K=13 for better theoretical results.

<br>
<li> tSNE Clustering</li>

- Reducing Article Embedding (size: 1536) to tSNE Components (size: 2)
- tSNE Component Visualization for Article Titles<br> ![image](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/title_parts_as_tsne_clusters.png)
- Check out the [notebook](https://github.com/chinmayajoshi/Constitutional-Document-Analysis/blob/main/Indian%20Constitution/title_embeddings_clustering%20v2.ipynb) where K-Means (K=7) is fitted, Silhouette Score analysis per clusters, tSNE fitted, and clustering scatter plot visualization.

</ul>