
from query import read_queries_and_process,get_queries_answers,get_corpus,criteria_results,_get_qrels,online_search
from ir import write_in_file , read_in_file 



quries_path = "D:/Visual Studio Code/documents/wikIR1k/training/queries.csv"
qrels_path = "D:/Visual Studio Code/documents/wikIR1k/training/qrels.txt"

answers :dict={}
qrels_result :dict={}

# normal_queries_list,queries_processed_list=read_queries_and_process(quries_path)
# query_corpus = get_corpus(quries_path)
# write_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\query_normal.pkl",normal_queries_list)

# write_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\query_corpus1.pkl",query_corpus)
query_corpus = read_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\query_corpus1.pkl")
# print(query_corpus)
# answers = get_queries_answers(query_corpus)
# print(answers)
# write_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\answers.pkl",answers)
ans = read_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\answers.pkl")
# print(ans)
# qrels_list = _get_qrels(qrels_path)
# write_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\qrels1.pkl",qrels_list)
# print(qrels_list)
# print(ans)
qrels_result = read_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\qrels1.pkl")
# print(qrels_result)
# metrics = criteria_results(ans,qrels_result,10)
# write_in_file("D:\\Visual Studio Code\\Python_Projects\\IR__Project\\matrices1.pkl",metrics)
# print(metrics)
alaa= online_search("national hockey league")
print(alaa)
print("doneeeeeeee")

