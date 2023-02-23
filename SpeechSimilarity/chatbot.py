from sklearn.metrics.pairwise import cosine_similarity
from joblib import dump, load
from sentence_transformers import SentenceTransformer
from pandas import read_csv



def chatbot_train(data):
    # the dataset should be a pandas dataframe containing Question and answer features
    dataset_lenght,columns = data.shape
    #sentence is the variable where we save the encoded sententes from the database altogether 
    sentences=[]
    for i in range(0,dataset_lenght):
        corpus=data.iloc[i,columns-2]
        sentences.append(corpus)
    model= SentenceTransformer('paraphrase-mpnet-base-v2')
    # embed/encode questions using transformer
    sentence_embeddings = model.encode(sentences)

    # save the trained model ('paraphrase-mpnet-base-v2') for further use
    model_directory = "database/model/"
    data_path = "database/data/"
    dump(model, model_directory+'chatbot_model.joblib')
    dump(sentence_embeddings, data_path+"sentence_embeddings")
    return sentence_embeddings
# chatbot_train("database/data/transcript_domain.csv")




def chatbot_ans(loaded_model, sentence_embeddings, text:str, data):
    test_embeddings=loaded_model.encode([text])
    # print('text encoded')
    # find similary scores (Asked query vs trained queries)
    score=cosine_similarity(sentence_embeddings, test_embeddings, dense_output=False)
    # print(score)
    # find the index of the trained query/question which have maximum similarity
    max_similarity = 0
    max_similarity_index = 0
    for i, e in enumerate(score):
        # print(i, e[0])
        if max_similarity<=e[0]:
            max_similarity = e[0]
            max_similarity_index = i
    # print(max_similarity_index)
    # print(max_similarity)
    text = data.iloc[max_similarity_index, 1]
    # print(data.shape)
    # text = data[1][max_similarity_index]
    # print(text)
    # print("similarity found")
    return text


# if __name__ == "__main__":
#     # Chatbot
#     text_from_ASR = "মিনিমাম কোয়ালিফিকেশন কি?"
#     loaded_model = load('database/model/chatbot_model.joblib')
#     sentence_embeddings = load('database/data/sentence_embeddings')
#     data = read_csv("database/data/transcript_domain.csv")
#     text_similar_ans = chatbot_ans(loaded_model, sentence_embeddings, text_from_ASR, data)
#     print(text_similar_ans)


