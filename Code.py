
#Instalar social network scrape en el cmd: pip install snscrape
#En caso no funcione, se recomienda instalar via git cmd como por ejemplo: pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
#Este paquete permite descargar informacion de las siguientes redes sociales: 
#Facebook, Instagram, Mastodon, Reddit, Telegram, Twitter, VKontakte, Weibo

import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets = []

#Se eligen twitter de algunos presidentes del Perú:
for presi in ["ppkamigo","MartinVizcarraC","MerinoDeLama","FSagasti","PedroCastilloTe"]:
	#Definir twitter y espacio temporal
	query = "(from:" + str(presi) + ") until:2021-01-01 since:2019-01-01"
	print(query)

	#Limite de tweets. Importante poner limites.
	limits = 50000

	#Comandos para descargar tweets
	count = 1
	for tweet in sntwitter.TwitterSearchScraper(query).get_items():
		#print(vars(tweet)) #Permite visualizar las variables que se pueden extraer como date, user, etc
		if len(tweets) == limits:
			break
		else:
			objeto = tweet.content
			objeto = objeto.replace('\n',' SS-SS') #Algunos tweets son largos y es conveniente poner una señal que permita identificarlos.
			tweets.append([count, tweet.user.username, tweet.date, tweet.conversationId, 
				tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, objeto])
		count = count + 1
		print(count)

	df = pd.DataFrame(tweets, columns=['ID','User','Date','Hilo','Comment','RT','Like','Quote','Tweet'])
	df.to_csv('Tweets_Presidentes.csv',encoding='utf-8-sig',index=False)
