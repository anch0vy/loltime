# -*- coding: utf-8 -*-
import urllib2
import requests
import re
import json

def getHistory(id, pw):
	session = requests.Session()
	session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	session.get('http://www.leagueoflegends.co.kr/')
	data = {}
	data['userID'] = id
	data['userPW'] = pw
	ret = session.post('https://signup.leagueoflegends.co.kr/Member/login_proc.php', data=data)
	if u'로그인에 실패' in ret.text or u'아이디에 허용되지' in ret.text:
		return None
	session.get('http://matchhistory.leagueoflegends.co.kr/ko/#match-history')
	try:
		Authorization = 'Vapor ' + session.cookies.get('PVPNET_TOKEN_KR')
	except:
		return None
	id = session.cookies.get('PVPNET_ID_KR')
	session2 = requests.Session()
	session2.headers['Authorization'] = Authorization
	session2.headers['Referer'] = 'http://matchhistory.leagueoflegends.co.kr/ko/'
	session2.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
	session2.headers['Region'] = 'KR'
	url = 'https://acs.leagueoflegends.com/v1/stats/player_history/KR/%s' % id
	retdic = []
	for n in range(0,2000,15):
		print n/15, 2000/15
		params = {}
		params['begIndex'] = n
		params['endIndex'] = n + 15
		ret = session2.get(url, params=params).json()
		if len(ret['games']['games']) == 0:
			break
		retdic.extend(ret['games']['games'])
	return retdic