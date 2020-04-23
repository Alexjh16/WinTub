#!/usr/bin/python
import requests
import re
import subprocess as command
#Accounts: elliot.34@mail.com, elliot.33@mail.com, elliot.32@mail.com, katz.94@live.com.mx
#Accounts: anyalbarrancontreras@mail.com, anyalbarrancontreras01@mail.com

link = "https://s3.wintub.com/dashboard.php"
cookies = { "PHPSESSID": "d7e3f8523698eb07ec06558f1bfa8f5b"}
for i in range(1, 7):
    if(i < 2):
        time = command.getoutput("date | awk '{ print $4 }'")
        print("[\033[91m{}\033[0m]:: \033[93m[!] collecting url...\033[0m".format(time))
        htmlRequest = requests.get(link, cookies=cookies).text
        
        time = command.getoutput("date | awk '{ print $4 }'")
        print("[\033[91m{}\033[0m]:: \033[92m[*] Done!!\033[0m".format(time))

        linkVars = re.search("\?v=1&active=.*?(?=\")", htmlRequest).group(0)
        viewRequest = link + linkVars;

        time = command.getoutput("date | awk '{ print $4 }'")
        print("\n[\033[91m{}\033[0m]:: \033[93m[!] attempt No 1\033[0m".format(time))

        viewVideoRequest = requests.get(viewRequest, cookies=cookies)
        print("[\033[91m{}\033[0m]:: \033[92m=> [*] Done!\033[0m".format(time))
        
    
    if(i >= 2):
        if(i > 5):
            print("\n")
            print("\033[92m-\033[0m" * 80)
            time = command.getoutput("date | awk '{ print $4 }'")
            print("\n[\033[91m{}\033[0m]:: \033[93m[!] all the urls were completed without error :)\033[0m".format(time))
            print("[\033[91m{}\033[0m]:: \033[93m[!] collecting new Balance...\033[0m".format(time))
            NewUrl = requests.get(link, cookies=cookies).text
            NewAmount = re.search(">\s[0-9].[0.9].*?<", NewUrl).group(0)
            print("\033[92mNew Balance {}(Dollars)\n".format(NewAmount))
            break

        originalURL = (link + "?v=" + str(i))
        htmlRequest = requests.get(originalURL, cookies=cookies).text
        linkVars = re.search("\?v=" + str(i) +"&active=.*?(?=\")", htmlRequest).group(0)   
        viewRequest = link + linkVars;

        time = command.getoutput("date | awk '{ print $4 }'")
        print("[\033[91m{}\033[0m]:: \033[93m[!] attempt No ".format(time) + str(i) +"\033[0m")

        time = command.getoutput("date | awk '{ print $4 }'")
        viewVideoRequest = requests.get(viewRequest, cookies=cookies)
        if(i == 3):
            viewVideoRequest = requests.get(viewRequest, cookies=cookies)
        print("[\033[91m{}\033[0m]:: \033[92m=> [*] Done!\033[0m".format(time))