# -*- coding: utf-8 -*-

from requests import post, get

class Api:
    def __init__(self, base_url, user_token, app_token):
        self.base_url = base_url
        self.app_token = app_token
        self.user_token = user_token


    def initSession(self):
        target_url = 'initSession/'
        sessiondata = {'Content-Type': 'application/json',\
                       'Authorization':'user_token '+self.user_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        self.session_token = session.json()
        self.session_token = self.session_token['session_token']



    def killSession(self):
        target_url = 'killSession'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.content)


    def getMyProfiles(self):
        target_url = 'getMyProfiles/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())

    def getActiveProfile(self):
        target_url = 'getActiveProfile/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())

    def changeActiveProfile(self, profile_id):
        target_url = 'getActiveProfile/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = post(self.base_url+target_url, headers=sessiondata, data=str(profile_id))
        return(session.json())

    def getMyEntities(self):
        target_url = 'getMyEntities/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())

    def getActiveEntities(self):
        target_url = 'getActiveEntities/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())

    def getFullSession(self):
        target_url = 'getFullSession/'
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())

    def getItem(self,item_type, item_id, args=None):
        if args is None:
            target_url = item_type+'/'+'/'+item_id
        else:
            target_url = item_type+'/'+'/'+item_id+'?'+args
        sessiondata = {'Content-Type': 'application/json', \
                       'Session-Token':self.session_token,'App-Token':self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        return(session.json())


    def getTicket(self, ticket_id):
        target_url = 'Ticket/'+str(ticket_id)+'?expand_dropdowns=true'
        sessiondata = {'Content-Type': 'application/json',\
                       'Session-Token': self.session_token,'App-Token': self.app_token}
        session = get(self.base_url+target_url, headers=sessiondata)
        print(session.url)
        return(session.content)
