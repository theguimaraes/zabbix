# Manual de configuração do envido de alertas Zabbix via MS Teams

![AlertasMSTeams](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/AlertasMSTeams.jpg)


Primeiramente, devemos obter o Incoming Webhook connector e configura-lo para o seu time no MS Teams.

Acesse o MS Teams do seu computador, selecione o grupo que deseja configurar para receber os alertas.

- Clique no ... (tres pontinhos ao lado do nome) e em seguida em Connectors.

![Connectors](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/Connectors.jpg)


- Procure pelo conector Incoming Webhook.

![IncWebhook](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/IncomingWebhook.jpg)


- Atribua um nome para o mesmo para facilitar de onde está vindo as mensagens. Ex: Zabbix
- Atribua uma imagem de avatar para o conector para facilitar.
- Clique em Create

![CreateConnector](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/CreateConnector.jpg)


Será gerado uma URL do seu Conector Webhook, salve essa URL que usaremos em breve.
- Clique em Done para concluir

![ConnectorURL](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/ConnectorURL.jpg)


Agora na parte de configuração do Zabbix, devemos copiar o arquivo msteams_alerts.sh para o diretório de alertscripts do seu zabbix.
Normalmente ele fica localizado no caminho: /usr/lib/zabbix/alertscripts

Lembre-se de atibuir permissão de execução para o arquivo (chmod 755 msteams_alerts.sh)

Neste arquivo possui comentado o que cada parametro faz e onde pode ser modificado.

Após copiar o arquivo para seu Zabbix, devemos acessar o FrontEnd para configurar o Media Type para o envio das Actions.

Acesse o menu Administration > Media Types
- Clique no botão "Create media type"
- Selecione o tipo de midia "Script"
- No nome coloque um de facil identificação. Ex: MS Teams
- Em Script Name, coloque o nome do arquivo que você colocou na sua pasta do Alertscripts do Zabbix. Ex: msteams_alerts.sh
- No Script Parameter, adicionei 3 linhas:
    - Na primeira adicione: {ALERT.SENDTO}
    - Na segunda adicione: {ALERT.SUBJECT}
    - Na terceira adicione: {ALERT.MESSAGE}
- Clique em Add para adicionar o tipo de mídia cirado.

![MediaType](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/MediaType.jpg)


Agora que temos o tipo de mídia configurado, devemos atribuir a URL do Webhook do MS Teams para um usuário no seu Zabbix que receberá esses alertas.

- Acesse o menu Administration > Users
- Clique em "Create user"
- No Alias, você pode colocar um de facil entendimento. Ex: MS Teams - NOC
- Em Name, coloque sua preferencia. Ex: Teams
- Em LastName, coloque sua preferencia. Ex: NOC
- Atribua o grupo de permissão que desejar

![UserGroup](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/UserGroup.jpg)


Agora devemos acessar a aba Media do usuário e atribuir a URL do Webhook do MS Teams para receber os alertas.
- Clique em Add para adicionar uma novo Media
- No Type, selecione o MS Teams que criamos.
- Em Send to, coloque a URL do Webhook. Ex: https://outlook.office.com/webhook/xxxxx
- Clique em Add para adicionar
- Clique em Add para adicionar o usuário criado

![UserMedia](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/UserMedia.jpg)


Agora que temos o tipo de midia configurado e o usuário criado para receber os alertas, podemos configurar a Action como qualquer outra.
Lembrando que se o assunto da Action for passado como no exemplo abaixo (PROBLEMA/RESOLVIDO) ele irá fazer a diferenciação de cor, caso dejese algo diferente pode ser necessário modificar o script.

![ActionOperation](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/ActionOperation.jpg)

![RecoverOperation](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/RecoverOperation.jpg)


Espero que este manual seja util para você e que traga valor para seus projetos. Qualquer dpuvidas, estou a disposição no Telegram @theguima

Obrigado

Fabricio Guimarães
Telegram: @theguima
