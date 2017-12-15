import bs4 as BeautifulSoup
import requests
import json
import random


''' Script by Hari'''

url1 = "https://vote.pollcode.com/85364595"	 #replace this with your vote url
choice = "3"                                 #Replace with the choice to be voted. e.g. 1 for first option
number_of_votes = 20 						#Replace with the number of votes to be given





response = requests.get("https://us-proxy.org/")
soup = BeautifulSoup.BeautifulSoup(response.content, "html.parser")
proxylist = []
def obtainproxy():
	for row in soup('table', {'id':'proxylisttable'})[0].tbody('tr'):
		tds = row('td')
		if (tds[6].string == "yes"):
			curl = "https://"+tds[0].string + ":" + tds[1].string
			proxylist.append(curl)
	pr = {'https':random.choice(proxylist)}
	try:
		proxy = pr
		r = requests.get("https://icanhazip.com", proxies = proxy)
		return pr
	except IOError:
		obtainproxy()


def vote(url,votes,option):
	pid = url.split(".com/")[1].replace("/","")
	nurl = "https://poll.pollcode.com/"+pid
	opt = pid+"="+option
	post_cookie = json.dumps({'pollcode':opt})
	headers = {'Cookie':post_cookie}
	data = {'answer':option}
	for i in range(votes):
		proxies = obtainproxy()
		try:
			out = requests.post(nurl,data=data,headers=headers,proxies=proxies)
			print('Voted {} times.'.format(i+1))
		except IOError:
			pass

vote(url1,number_of_votes,choice)
