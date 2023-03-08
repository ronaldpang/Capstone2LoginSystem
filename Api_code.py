#reminder remember to git pull each time
#now beginning of api code

from flask import Flask
from flask_restful import Resource,Api,reqparse
import pandas as pd
import ast
import requests
#This is initializing the API
server = Flask(__name__)
api = Api(server)


#creating the endpoint, where api is pulling the data from

class User_endpoint(Resource):
    def get(self):
        collecting_data = pd.read_csv('READONLYFSAE.csv')
        collecting_data = data.to_dict()
        return{'collecting_data':collecting_data},200
    

class Location_endpoint(Resource):
    pass


#entry for data point
api.add_resource(User_endpoint,'/users') 
api.add_resource(Location_endpoint,'/location')


#now running it on a local server,(local is what we wanted right?)
if __name__=='__main__':
   server.run() 


