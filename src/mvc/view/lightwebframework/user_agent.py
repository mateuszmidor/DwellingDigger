'''
Created on 23 kwi 2015

@author: m.midor
'''
import os
from src.thirdparty import user_agents

class UserAgent(object):
    '''
    This class provides HTTP user agent information.
    '''

    @staticmethod
    def is_mobile():
        user_agent_str = os.environ["HTTP_USER_AGENT"]
        user_agent = user_agents.parse(user_agent_str)
        return user_agent.is_mobile