[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZC3LMB6XT9ZL2&source=url)

# Manual de configuração do envido de alertas Zabbix via Kaizala

![AlertasMSTeams](https://github.com/theguimaraes/zabbix/blob/master/Kaizala-AlertScript/img/AlertasMSTeams.jpg)

Primeiramente, devemos acessar a página de gerenciamento do Kaizala e Criar o Grupo que receberá as mensagens. Normalmente https://manage.kaiza.la

No menu lateral, selecionamos Group e depois em Create Group (2x).

Digitamos o nome do grupo desejado e clicamos em Create.

Após a criação do grupo, guarde o ID do grupo criado, pois usaremos mais para frente. Exemplo na imagem abaixo.

Com o grupo criado, devemos adicionar o conector que será responsável pela comunicação com o Kaizala.

Acesse a página de gerenciamento do Kaizala para criar o conector. Normalmente https://manage.kaiza.la 

Clique em ADD CONNECTOR, no canto superior direito.

Digite as informações conector conforme imagem abaixo.

Selecione pas permissões desejadas e clique em Create Connector

Após a criação do Connector, devemos atrelar ele no grupo que foi criado, basta selecionar o grupo no DropDown e clicar em ADD.

Guarde as IDs que irão aparecer e o Tokem do Conector atrelado do Grupo, pois usaremos elas futuramente. Exemplo na imagem abaixo.


Agora que temos o grupo criado com sua ID, e os dados do Connector, devemos fazer algumas requisições à API do Kaizala para criar o BOT e os Tokens de acesso.

Podemos obter a coleção de requisições da API do Kaizala para Postman diretamente do site oficial: https://docs.microsoft.com/en-us/kaizala/connectors/api


Nesta parte devemos primeiramente executar a Step1, Step 2 e Step 3 da Autenticaçao via API para obter o AccessToken.

Step 1 - Informamos o celular que irá receber o PIN no "mobileNumber" e o Connector ID que criamos em "applicationId". Será enviado via SMS no celular informado o PIN de acesso (Guarde esse numero)


Step 2 - Informamos além do "mobileNumber" e da "applicationId", o "applicationSecret" do connector e o "pin" que chegou no celular. Dessa forma fazemos login da API e recebemos alguns tokens de acesso.

Step 3 - Devemos obter a AccessToken principal para fazer as criações necessárias. Devemos passar alguns parametros no cabeçaço da requisição como a imagem abaixo. "applicationId" e "applicationSecret" (Do connector criado), e o Refresh Token que é o "UserToken" do Connector criado.

Com o Access Token, podemos criar o BOT que fará o envio das mensagens no Grupo.

Execute a requisição "Create bot user" da API, conforme imagem abaixo. Devemos passar o AccessToken no cabeçalho da requisição e no corpo passamos o nome do token. Como resultado da requisição, recebemos o BotID (Guarde esse código)

Agora devemos adicionar o BOT no Grupo, podemos fazer via requsição a API conforme iamgem abaixo. Passamos no cabeçadlho o Access Token, no corpo o BotID e no endereço da requisição, o ID do grupo criado no começo deste tutorial.


Podemos confirmar que o Bot foi adicionado.

Agora com o Bot criado e adicionado ao grupo, devemos obter o BOT_ACCESS_TOKEN usado no script. Abaixo iamgem de exemplo, onde devemos passar no cabeçalho o Access token principal e o ID do Bot no endereço da requisição. Como resultado, teremos o AccessToekn do BOT criado.

UFA! Muitas etapas, mas agora vem a aprte fácil. Basta alterar o Script informando seu Bot Access Token e adicionar o script nas midias do Zabbix.

Agora na parte de configuração do Zabbix, devemos copiar o arquivo kaizala_alerts.sh para o diretório de alertscripts do seu zabbix.
Normalmente ele fica localizado no caminho: /usr/lib/zabbix/alertscripts

Lembre-se de atibuir permissão de execução para o arquivo (chmod 755 msteams_alerts.sh)

Neste arquivo Basta substituir o BOT_ACCESS_TOKEN para o que você obteve nas etapas acima.

Após copiar o arquivo para seu Zabbix, devemos acessar o FrontEnd para configurar o Media Type para o envio das Actions.

Acesse o menu Administration > Media Types
- Clique no botão "Create media type"
- Selecione o tipo de midia "Script"
- No nome coloque um de facil identificação. Ex: kAIZALA
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
- No Alias, você pode colocar um de facil entendimento. Ex: Kaizla Group
- Em Name, coloque sua preferencia. Ex: Kaizala
- Em LastName, coloque sua preferencia. Ex: Group
- Atribua o grupo de permissão que desejar

![UserGroup](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/UserGroup.jpg)


Agora devemos acessar a aba Media do usuário e atribuir o ID do Grupo do Kaizala para receber os alertas.
- Clique em Add para adicionar uma novo Media
- No Type, selecione o Kaizala_Script que criamos.
- Em Send to, coloque a ID do Grupo. Ex: 7e9f6a85-0e18-4701-bb54-432c7c4cc23c@1
- Clique em Add para adicionar
- Clique em Add para adicionar o usuário criado

![UserMedia](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/UserGroup.jpg)


Agora que temos o tipo de midia configurado e o usuário criado para receber os alertas, podemos configurar a Action como qualquer outra.
Lembrando que se o assunto da Action for passado como no exemplo abaixo (PROBLEMA/RESOLVIDO) ele irá fazer a diferenciação de cor, caso dejese algo diferente pode ser necessário modificar o script.

![ActionOperation](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/ActionOperation.jpg)

![RecoverOperation](https://github.com/theguimaraes/zabbix/blob/master/MSTeams-AlertScript/img/RecoverOperation.jpg)


Espero que este manual seja util para você e que traga valor para seus projetos. Qualquer duvidas, estou a disposição no Telegram @theguima

Obrigado

Fabricio Guimarães
Telegram: @theguima
LinkedIn: theguimaraes

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZC3LMB6XT9ZL2&source=url)
