import twitter
import time
import random





api = twitter.Api(consumer_key='secret',
                  consumer_secret='secret',
                  access_token_key='secret',
                  access_token_secret='secret')

searchs = 0
tweets= 0
limitTweets = 300
limitSearchs= 180
listTwittos = ["RebeuDeter","AmineMaTue","PatrickAdemo","Theorus_","Grimkujow_","terracid","Remeli_","TeufeurSoff","RenardA9Queues","LaPvlga","LJVoff","theomcx","Kammeto","EncoreBouly","EcrisioFX","JM_Bigard","Arkunir","petitcon_","_RapVibes","elpaulohermano"]
listFraude=["finito","masterclass","MIAULE PLEURE HURLE ABOIE CHIALE REPETES SANS BEUGLER","rouspete sans rouspeter","finito + supprime ton compte + sois digne","Réel mais couine sans miauler","gênant culotté pleure chiale chouine couine aboie miaule boude brûle hurle crie","hulule","masterclass + t'es a ton prime","t'es a ton prime akhy","genant + finito","goatesque","goatesque t'es a ton prime akhy","chiale","genant t'es finito","hulule + rouspete","pleure + zinzinule","masterclass mais reste digne akhy","t'es finito akhy","finito à la niche","pleurniche ricane jacasse agonise beugle chuchote murmure ronfle suffoque asphixe"]

def endsWith(sentence,keyword):
    return sentence.endswith(keyword)


def Find(sentence, sub):
	result = sentence.find(sub)
	if result == -1:
		return False
	else:
		return True

def postStatus(update, inReplyTo, media,):
	global tweets
	tweets+=1
	status = api.PostUpdate(update, media = media, in_reply_to_status_id=inReplyTo)
	print(status,inReplyTo)


def search(research, howMany):
    global searchs
    global listFraude
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany, result_type = 'recent')
    for search in searchResults:
        if(Find(search.text, "finito") or Find(search.text, "masterclass") or Find(search.text, "prime") or Find(search.text, "akhy") or Find(search.text, "pessi") or Find(search.text, "génant") or Find(search.text,"goatesque")):
            postStatus("@" + search.user.screen_name + " " + random.choice(listFraude), search.id, "media.jpg")
            print("")
            time.sleep(1000)

def deleteAllTweets(user):
	id_list = []
	status = api.GetUserTimeline(screen_name = user,count = 100)
	for s in status:
		id_list.append(s.id)
	for id in range (len(id_list)):
		cible = api.DestroyStatus(status_id = id_list[id])
	print(f"{len(id_list)} tweets supprimés !")


def PrivateMessage(user,text):
	cible=api.GetUser(screen_name =user)
	print(cible.id_str)
	DM = api.PostDirectMessage(text=text,user_id = cible.id_str)



def citation():
	global listTwittos
	global listeAuteur
	id_tweets= []
	while len(id_tweets) < 50:
		cible = random.choice(listTwittos)
		timeline = api.GetUserTimeline(screen_name = cible ,count = 100,exclude_replies = True)
		tweet = random.choice(timeline)

		if tweet not in id_tweets:
			id_tweets.append(tweet)

	for t in id_tweets:
		auteur = random.choice(listeAuteur)
		postStatus("@" + t.user.screen_name + (f"\"{t.text - t.mention - t.expanded_url}.\"") + auteur, t.id)
		time.sleep(60)




def startResearch():
	global searchs
	global tweets
	global limitTweets
	global limitSearchs
	arret = False
	while(not arret):
		try:
			search("pessi", "100")

		except:
			print("Erreur de maximum")
			arret =True
		if (searchs >= limitSearchs):
			print("limite des searchs atteinte")
			arret = True
		elif (tweets >= limitTweets):
			print("limite des tweets atteinte")
			arret = True

		print(f"on a fait {str(tweets)} tweets!")
		time.sleep(10000)
	startResearch()


def startCitation():
	global listTwittos
	global tweets
	global limitSearchs
	global limitTweets
	arret = False
	try:
		citation()
	except:
		print("Erreur de maximum")
		arret =True
	if (searchs >= limitSearchs):
		print("limite des searchs atteinte")
		arret = True
	elif (tweets >= limitTweets):
		print("limite des tweets atteinte")
		arret = True

	print(f"on a fait {str(tweets)} !")
	time.sleep(5)

	print("Citation finis")


startResearch()