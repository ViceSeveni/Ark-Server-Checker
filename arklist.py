import requests
import bs4
import csv
import time
import os
import sys

metrics = 'https://www.battlemetrics.com/servers/ark/'

#Create csv file with the "map names , battle metrics id's" and provide the path below
server_list_path = ''
#create a csv file with your friends' "steam/epic names , a nickname" and provide the path below
friends_list_path = ''


serv_file = open(server_list_path , 'r')
file_reader = csv.reader(serv_file)
ark_list = list(file_reader)

friends_file = open(friends_list_path , 'r')
friends_reader = csv.reader(friends_file)
friends_list = list(friends_reader)

class servlist():
    def __init__(self, serv_link):
        self.url = serv_link
    
        page = requests.get(self.url)    
        soup = bs4.BeautifulSoup(page.text,'html.parser')
        
        serv_list = soup.find('table' , {'class':'css-1y3vvw9'})
        self.players = soup.find_all('a', {'class','css-zwebxb'})
        
    def show_list(self):
        count = 1
        for x in self.players:
            print(f'{count}. {x.text}')
            count += 1
            

def main(map_name=''):
    if map_name == '':
        friends_online = {}
        while True:
            os.system('cls')
            print('KNIGHTSGG ARK SURVIVAL SERVERS CURRENT POPULATION:\n')
            for map_name , map_link in ark_list:
                map_list = servlist(metrics + map_link.strip())
                play_count = len(map_list.players)
                if play_count > 1:
                    print(f'{play_count} Active Players On: {map_name}\n')
                if play_count == 0:
                    print(f'No Active Players On: {map_name}')
                if play_count == 1:
                    print(f'{play_count} Active Player On: {map_name}\n')
                map_list.show_list()
                
                for x in map_list.players:
                    for k , v in friends_list:
                        if x.text == k.strip():
                            friends_online[v] = map_name
                    
                print('-'*78 + '\n')
            
            if len(friends_online) > 0:
                print(f'You Have {len(friends_online)} Friend(s) Online:\n')
                for k , v in friends_online.items():
                    print(f'-{k} is on {v.strip()}!')
                    
            print('\nTHIS WILL REFRESH IN 1 MINUTE!')
            time.sleep(60)
            os.system('cls')
                
#             count = 10
#             for i in range(1, 11):
#                 print(f"Will refresh in: {count}" , end='' , flush=True)
#                 time.sleep(1)
#                 count -= 1
#                 sys.stdout.flush()
#             os.system('cls')
            
if __name__ == '__main__':
    main()
