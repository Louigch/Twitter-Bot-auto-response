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

listFraude=["finito","masterclass","MIAULE PLEURE HURLE ABOIE CHIALE REPETES SANS BEUGLER","rouspete sans rouspeter","finito + supprime ton compte + sois digne","Réel mais couine sans miauler","gênant culotté pleure chiale chouine couine aboie miaule boude brûle hurle crie","hulule","masterclass + t'es a ton prime","t'es a ton prime akhy","genant + finito","goatesque","goatesque t'es a ton prime akhy","chiale","genant t'es finito","hulule + rouspete","pleure + zinzinule","masterclass mais reste digne akhy","t'es finito akhy","finito à la niche","pleurniche ricane jacasse agonise beugle chuchote murmure ronfle suffoque asphixe"]

list_id_mention=[1383521289906753541,1383518241964793858,1383504417681416195,1383491667009839104,1383490246722002947,1383487872699830279,1383481046910439428,1383478009160556548,1383474198324998144] #blacklist tweets id aready reply

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
            time.sleep(800)

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
	id_tweets= []
	while len(id_tweets) < 50:
		cible = random.choice('Name of a user')
		timeline = api.GetUserTimeline(screen_name = cible ,count = 100,exclude_replies = True)
		tweet = random.choice(timeline)

		if tweet not in id_tweets:
			id_tweets.append(tweet)

	for t in id_tweets:
		postStatus("@" + t.user.screen_name + (f"\"{t.text - t.mention - t.expanded_url}.\""), t.id)
		time.sleep(60)




def StartSearchAutoAndAutoRepliMentions():
	global searchs
	global tweets
	global limitTweets
	global limitSearchs
	global list_id_mention
	arret = False
	while(not arret):
		MentionReplies()
		print("le dernier tweet à repondre est :" ,list_id_mention)
		try:
			search("pessi", "50")

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
	StartSearchAutoAndAutoRepliMentions()


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


def MentionReplies():
	global list_id_mention
	global listFraude
	global tweets
	list_mention=api.GetMentions()
	

	for t in list_mention:
		if t.id not in list_id_mention:
			if t.user.screen_name == "BotFinito":
				print("C'est mon tweet.")
			else:
				tweets+=1
				postStatus("@" + t.user.screen_name + " " + random.choice(listFraude), t.id, "media.jpg")
				print(" ")
				list_id_mention.append(t.id)
				time.sleep(800)

				print(list_id_mention)
            
		else:
			print("Tweet déjà répondu", t.id,t.text)
			print("")

	print("les tweets déja repondus sont :" ,list_id_mention)
	return list_id_mention


StartSearchAutoAndAutoRepliMentions()
