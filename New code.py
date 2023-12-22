
#La librería snscrape ha dejado de funcionar por el momento, que es el código que se encuentra
#en el mismo repositorio. Se recomienda utilizar el siguiente código para obtener información 
#sobre Twitter o X. Previamente se necesita instalar en el cmd: pip install ntscraper.

import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

#Se procede a extraer información usando el nombre de usuarios. Sin embargo,
#es pertinente precisar que es posible identificar mediante otras formas como, por ejemplo, hashtag:
cuenta = "ppkamigo"

# Ejemplo 1: obtener información de los tweets
#=====================================================================
tweets = scraper.get_tweets(cuenta,mode='user',number=100000)

final_tweets = []
for tweet in tweets['tweets']:
	data1 = [tweet['link'],tweet['text'],tweet['user']['name'],tweet['user']['username'],
	tweet['date'],tweet['is-retweet'],tweet['stats']['comments'],tweet['stats']['retweets'],
	tweet['stats']['quotes'],tweet['stats']['likes']]
	final_tweets.append(data1)
	print('----Siguiente tweet----')

data1 = pd.DataFrame(final_tweets,columns=[
	'link','text','name','username','date','is_rt','n_comment','n_rt','n_quote','n_like'])
data1.to_csv('Tweet_' + str(presi) + '.csv',encoding='utf-8-sig',index=False)

# Ejemplo 2: obtener información del perfil de los usuarios
#=====================================================================
profiles = scraper.get_profile_info(presi)

final_profiles = []
data2 = [profiles['name'],profiles['username'],profiles['bio'],profiles['joined'],
profiles['stats']['tweets'],profiles['stats']['following'],profiles['stats']['followers'],
profiles['stats']['likes'],profiles['stats']['media']]
final_profiles.append(data2)

data2 = pd.DataFrame(final_profiles,columns=[
	'name','username','bio','joined','n_tweet','n_following','n_follower','n_like','n_media'])
data2.to_csv('Perfil_' + str(presi) + '.csv',encoding='utf-8-sig',index=False)

