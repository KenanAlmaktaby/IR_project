# Information Retrieval System

***

A university project that uses two datasets from [ir-datasets](https://ir-datasets.com/) and build a search engine on them using Python and Flask.

## Datasets

- [**wikir**]  ( https://ir-datasets.com/wikir.html#wikir/en1k/training
)
- [**clinicaltrials**]   (https://ir-datasets.com/clinicaltrials.html#clinicaltrials/2017/trec-pm-2017)



## How to use the search engine?
After running your project locally you can select dataset and inter query and press on searsh

## Services
- **get_preprocessed_text_terms(text)**: 
1. **_get_words_tokenize**:
2. **_lowercase_tokens**:
3. **_filter_tokens**:
4. **_normalize_dates**:
5. **_normalize_country_names**:
6. **_stem_tokens**:


- **ir.py**:
1. **read_dataset_and_process**:
2. **get_corpus**:
3. **get_inverted_index**:
4. **calculate_tf**:
5. **calculate_tf_df**:
6. **calculate_idf**:
7. **calculate_idf_df**:
8. **calculate_tf_idf**:
9. **calculat_tf_idf_df**:
10. **get_vectorize**:


- **query.py**:
1. **read_queries_and_process**
2. **get_corpus**
3. **create_query_vector**
4. **search**
5. **get_queries_answers**
6. **_get_qrels**
7. **criteria_results**
8. **get_related_docs**
8. **online_search**

- ## Evaluation in function criteria_results:
The implemented evaluation metrics are  **Recall**, **MAP**, **MRR** and **Precision@10**.

## Students
 [**Walaa Almshaawet**] (https://github.com/walaa2020)
 [**Rama Fareha**]
 [**kinan maktaby**] (https://github.com/KenanAlmaktaby)
 [**lana khadra**]
