
#La librería snscrape ha dejado de funcionar por el momento, que es el código que se encuentra
#en el mismo repositorio. Se recomienda utilizar el siguiente código para obtener información 
#sobre Twitter o X. Previamente se necesita instalar en el cmd: pip install ntscraper.

import pandas as pd
from ntscraper import Nitter

scraper = Nitter()

#Se procede a extraer información usando el nombre de usuarios. Sin embargo,
#es pertinente precisar que es posible identificar mediante otras formas como, por ejemplo, hashtag.

# Ejemplo 1: obtener información de los tweets
#=====================================================================
#user: identifica la forma en que se está descargando. En este caso es mediante nombre del usuario.
#number: identifica el número de tweets que se busca descargar.
cuenta = "ppkamigo"
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
data1.to_csv('Tweet_' + str(cuenta) + '.csv',encoding='utf-8-sig',index=False)

#Teniendo en cuenta que por defecto se obtienen los tweets más recientes, es posible identificar 
#fechas de interés modificando el código de la siguiente manera:
tweets = scraper.get_tweets(cuenta,mode='user',number=100000,since='2017-12-12',until='2018-12-12')
#El formato fecha tiene que ser YYYY-MM-DD. Año-Mes-Día.

# Ejemplo 2: obtener información del perfil de los usuarios
#=====================================================================
cuenta = "ppkamigo"
profiles = scraper.get_profile_info(cuenta)

final_profiles = []
data2 = [profiles['name'],profiles['username'],profiles['bio'],profiles['joined'],
profiles['stats']['tweets'],profiles['stats']['following'],profiles['stats']['followers'],
profiles['stats']['likes'],profiles['stats']['media']]
final_profiles.append(data2)

data2 = pd.DataFrame(final_profiles,columns=[
	'name','username','bio','joined','n_tweet','n_following','n_follower','n_like','n_media'])
data2.to_csv('Perfil_' + str(cuenta) + '.csv',encoding='utf-8-sig',index=False)

