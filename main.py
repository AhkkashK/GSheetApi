import gspread
from google.oauth2.service_account import Credentials
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter
import pandas as pd 

stop_words = set(stopwords.words('french'))


def connect_to_googlea_api():
    
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_file("credentials.json",scopes=scopes)
    client = gspread.authorize(creds)

    return client
    
    

def clean_data(text):

    text_tokenize = nltk.word_tokenize(text)
    text_no_punct = [word.lower() for word in text_tokenize if word.isalnum()]
    text_no_sw =  " ".join([word.lower() for word in text_no_punct if word.lower() not in stop_words and word.lower() != "comme"])

    return text_no_sw


def ngram_generator(text,n):

    return list(ngrams(sequence=nltk.word_tokenize(text),n=n, pad_right=True, pad_left=True))



def ngram_analysis(text,n):

    cleantext = clean_data(text)
    n_grams = ngram_generator(cleantext,n)
    ngram_freq = Counter(n_grams)
    most_common_ngrams = ngram_freq.most_common(10)
    most_common_ngrams = [( " ".join(ngram), freq) for ngram, freq in most_common_ngrams]

    return most_common_ngrams


"""

Insights : 

Pour l'analyse des n-grams, j'ai décidé d'enlever les mots comme les articles ou les prépositions par exemple. En effet lorsque je regardais le top 10 d'un n-gram,
il pouvait arriver qu'une grosse partie de ces n-gram était composée seulement d'articles ou de prépositions. Sinon le n-gram pouvait ne pas avoir de sens et ne pas très utile.

D'autre part j'ai appliqué un multiplicateur sur les phrases grâce à la colonne statistique qui se trouvait dans les données. J'ai déduit que c'était le nombre de personnes qui pouvaient
écrire la phrase en question sur un moteur de recherche.

Unigrams : On peut relever que les deux mots qui sortaient du lot (et de loin) était le mot data et données. Même si nous savions que le csv était à propos de la data. Cette analyse NLP permet par exemple de saisir le thème d'un corpus en peu de temps.

Bigrams : Pour le coup, nous avons une distribution assez similaire entre les bigrams. Ce qu'on peut saisir de ce top 10 c'est que dans le big data on a besoin de technologies spécifiques pour accomplir des tâches complexes et  construire des modèles

Trigram : Même remarque que pour les bigrams

Qu'est ce qu'on peut retenir des n-grams ? 

C'est un outil très intéressant pour Eskimoz qui est spécialisée dans le SEO et le marketing digital : optimisation du contenu, extraction de mots-clés...


"""

def df_to_sheet(workbook,title,r,c,df):
    
    try:
        
        worksheet = workbook.worksheet(title)
        worksheet.clear()
        
    except gspread.exceptions.WorksheetNotFound:

        worksheet = workbook.add_worksheet(title,r,c)

    data = [df.columns.values.tolist()] + df.values.tolist()    
    worksheet.update('A1', data)



def main():
   
    df = pd.read_csv('data/data_science_phrases.csv')    
    
    text = ""
    
    for i in range(len(df)):

        text = text+df.iloc[i,1]*df.iloc[i,2]   
    
    unigram = ngram_analysis(text,1)
    bigram = ngram_analysis(text,2)
    trigram = ngram_analysis(text,3)


    df1 = pd.DataFrame(unigram,columns=["text","frequency"])
    df2 = pd.DataFrame(bigram,columns=["text","frequency"])
    df3 = pd.DataFrame(trigram,columns=["text","frequency"])

    client = connect_to_googlea_api()
    sheet_id = "1B3MbxpzOUmHo7ViWdEq1Sbvt3uWp8_nW5J3itnLnhmw"
    workbook = client.open_by_key(sheet_id)
    
    df_to_sheet(workbook,"Unigram",30,30,df1)
    df_to_sheet(workbook,"Bigram",30,30,df2)
    df_to_sheet(workbook,"Trigram",30,30,df3)
    
     


main()








