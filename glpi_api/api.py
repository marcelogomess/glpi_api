# -*- coding: utf-8 -*-
from requests import post, get, put, delete


class Api:
    def __init__(self, base_url, user_token, app_token):
        self.base_url = base_url
        self.app_token = app_token
        self.user_token = user_token


    def initSession(self):
        target_url = 'initSession/'
        sessiondata = {'Content-Type': 'application/json',
                       'Authorization': 'user_token ' + self.user_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        self.session_token = session.json()
        self.session_token = self.session_token['session_token']


    def killSession(self):
        target_url = 'killSession'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.content)


    def getMyProfiles(self):
        target_url = 'getMyProfiles/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getActiveProfile(self):
        target_url = 'getActiveProfile/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def changeActiveProfile(self, profile_id):
        target_url = 'getActiveProfile/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = post(self.base_url + target_url, headers=sessiondata, data=str(profile_id))
        return (session.json())

    def getMyEntities(self):
        target_url = 'getMyEntities/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getActiveEntities(self):
        target_url = 'getActiveEntities/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getFullSession(self):
        target_url = 'getFullSession/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getItem(self, item_type, item_id, args=None):
        if args is None:
            target_url = item_type + '/' + '/' + item_id
        else:
            target_url = item_type + '/' + '/' + item_id + '?' + args
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getAllItems(self, item_type, args=None):
        if args is None:
            target_url = item_type + '/'
        else:
            target_url = item_type + '/' + '?' + args
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getSubItems(self, item_type, item_id, sub_item_type, args=None):
        if args is None:
            target_url = item_type + '/' + item_id + '/' + sub_item_type
        else:
            target_url = item_type + '/' + item_id + '/' + sub_item_type + '?' + args
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def getMultipleItems(self, items_dict):
        for items in items_dict['items']:
            items_list = self.getItem(item_type='Ticket', item_id='69130', args='expand_dropdowns=true')
        return (items_list)

    def listSearhItemsOptions(self, item_type, args=None):
        if args is None:
            target_url = 'listSearchOptions/' + item_type + '/'
        else:
            target_url = 'listSearchOptions/' + item_type + '/' + '?' + args

        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = get(self.base_url + target_url, headers=sessiondata)
        return (session.json())

    def searchItems(self):
        return(True)

    def addItems(self, item_type, item_data):
        target_url = item_type+'/'
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = post(self.base_url + target_url, headers=sessiondata, json=item_data)
        return (session.json())


    def updateItems(self,item_type, item_id, item_data):
        target_url = item_type+'/'+str(item_id)
        sessiondata = {'Content-Type': 'application/json',
                       'Session-Token': self.session_token, 'App-Token': self.app_token}
        session = put(self.base_url + target_url, headers=sessiondata, json=item_data)
        return (session.json())

    def deleteItems(self):
        return(True)