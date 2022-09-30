# Python_Flask_WebAPI
Este repositório é um exemplo de WEB API desenvolvida em Python utilizando Framework Flask.
# Executando Localmente
Para rodar localmente, é necessário ter instalado Python e pip 
Digite Python --version para verificar versão do Python na máquina
Digite pip --version
Entre na pasta raiz do projeto
Digite Python main.py
O projeto estará disponível na página/URL http://localhost:5000/
# Executando pelo Docker
Primeiramente necessário ter o Docker instalado
No Windows pode ser obtido pelo seguinte link: https://docs.docker.com/desktop/install/windows-install/
Com Docker instalado, entre na pasta raiz do projeto e rode o seguinte comando: docker build -t Python-Flask-webAPI .
Para rodar o programa, digite o seguinte comando: docker run -p 5000:5000 Python-Flask-webAPI 
O projeto estará disponível na página/URL http://localhost:5000/
# Executando com Docker Compose
Para rodar com Docker Compose é necessário ter instalado na máquina Docker e o Docker Compose
Na raiz do projeto, execute o seguinte comando: `docker-compose up`
