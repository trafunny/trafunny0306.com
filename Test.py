# import requests
# import os

# def Page24() :
#     sever  =[]
#     SHODAN_API_KEY = os.environ['SHODAN_API_KEY']
#     shodanApi = shodan.


# if __name__ == "__main__" :
#     print ("hello")
#     Page24()

import requests
import os

import shodan

SHODAN_API_KEY = shodan.Shodan('8o5f6DEPO0AqVqUfQQ1LydLHgmVz8lNG')

ip = '1.1.1.1'
def ShodanInfo(ip) :
    try:
        response = requests.get("https://api.shodan.io/shodan/host/{}?key={}&minify=True".format(ip, SHODAN_API_KEY))
        if response.status_code == 200:
            result = response.json()
        else:
            result ={"error": "Request to API failed"}
    except Exception as exception:
        result ={"error": "An error occurred while making the API request"}
    return result

if __name__ == "__main__" :
    print(ShodanInfo(ip))
    #chiu day