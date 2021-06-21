# curriculo
Currículo online para ser inserido como QR Code no CV físico ou PDF

Passos

01 - Instalar o Python - https://www.python.org/downloads/.

02 - Isolar o ambiente do site e instalação do django - https://docs.djangoproject.com/en/3.2/howto/windows/.

03 - Instalar o gunicorn - https://docs.gunicorn.org/en/stable/install.html.

04 - Testar o servidor localmente - https://docs.djangoproject.com/en/3.2/intro/tutorial01/.

05 - Cadastrar-se na Heroku - https://www.heroku.com/.

06 - Fazer o download do Heroku para Windows - https://devcenter.heroku.com/articles/getting-started-with-python#set-up.

07 - Realizar a instalação do Heroku na venv (ambiente isolado) - pip install heroku.

08 - Logar na CLI diretamente no prompt (fora da venv).

09 - Criar aplicação no Heroku - 'heroku create' *(nome aplicação)* dentro da venv.

10 - Atribuir um Buildpack no site da aplicação no Heroku - Heroku > *(aplicação)* > Settings > Buildpacks > Python.

11 - Vincular o deploy do Heroku com o Github - Heroku > *(aplicação)* > Deploy > Connect to GitHub > Enable automatic deploys.

12 - Criar os arquivos [requirements.txt](https://github.com/davimassarelli/curriculo/files/6672452/requirements.txt), [runtime.txt](https://github.com/davimassarelli/curriculo/files/6672454/runtime.txt)
 e Procfile (https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile).

13 -  Autorizar no settings.py o ALLOWEED_HOSTS do django.

** A Partir deste momento a aplicação já está rodando**

Daqui em diante serão especificidades relacionadas a prosseguir com a implementação segura do site

14 -  Instalar o pyteste-django - https://pytest-django.readthedocs.io/en/latest/
(pip install pytest-django) - dentro do ambiente isolado da aplicação.

15 - Definir na IDLE que o pyteste será o responsável pela realização de testes.

16 - Criar teste básico para a home utilizando o pyteste.

17 - Criar uma home para verificar o teste de status code 200

18 - Automatizar a realização de testes quando requisitado pull request - https://docs.github.com/pt/actions/learn-github-actions/introduction-to-github-actions

19 - 
