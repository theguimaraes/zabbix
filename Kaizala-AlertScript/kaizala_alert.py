#!/usr/bin/env python

#######################################################################
#####           Script de alertas Zabbix para Kaizala             #####
#####                                                             #####
#####           Versao: 1.0                                       #####
#####           Autor: Fabricio Guimaraes                         #####
#####           Telegram: @theguima                               #####
#####           Github: https://github.com/theguimaraes           #####
#####                                                             #####
#######################################################################
#####                                                             #####
#####        Valores recebidos neste script como parametro        #####
#####                                                             #####
##### idgrupo           (ID do Grupo do Kaizala)                  #####
##### messagetitle      (Assunto do alerta)                       #####
##### message           (Mensagem de alerta enviada pelo Zabbix)  #####
#####                                                             #####
#######################################################################

import requests
import sys

idgrupo = sys.argv[1]
messagetitle = sys.argv[2]
message = sys.argv[3]

url = "https://kms.kaiza.la/v1/groups/%s/actions" % idgrupo

payload = "{actiontype:\"Announcement\", actionBody:{title:\"%s\", message:\"%s\"}}" % (messagetitle, message)
headers = {
    'accessToken': "BOT_ACCESS_TOKEN",
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
