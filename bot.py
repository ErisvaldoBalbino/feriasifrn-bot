import tweepy
import datetime

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# função para calcular os dias até as férias
def calcular_dias():
    hoje = datetime.date.today()
    ferias = datetime.date(2024, 7, 9)

    dias = (ferias - hoje).days
    
    return dias

dias_faltando = calcular_dias()

if dias_faltando == 1:
    tweet = f"Falta {dias_faltando} dia para as férias do IFRN!"
elif dias_faltando > 1:
    tweet = f"Faltam {dias_faltando} dias para as férias do IFRN!"
else:
    tweet = "FÉRIAS!!!!!!!"

if dias_faltando >= 0:
    client.create_tweet(text=tweet)