# Repositório GitHub - Passo a Passo para RabbitMQ com Docker

Este repositório fornece um guia simples para configurar e executar o RabbitMQ usando o Docker. O RabbitMQ é um sistema de mensagens de código aberto que facilita a comunicação entre aplicativos.

## Pré-requisitos

Antes de começar, certifique-se de ter o Docker Desktop instalado em sua máquina. Se ainda não o tiver, você pode baixá-lo [aqui](https://www.docker.com/products/docker-desktop).

## Passo 1: Download do Docker Desktop

Se você ainda não tiver o Docker Desktop instalado, faça o download e siga as instruções de instalação para o seu sistema operacional:

- [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop)
- [Docker Desktop para macOS](https://www.docker.com/products/docker-desktop)
- [Docker Desktop para Linux](https://www.docker.com/products/docker-desktop)

## Passo 2: Download da Imagem do RabbitMQ

Após instalar o Docker Desktop, abra um terminal ou prompt de comando e execute o seguinte comando para baixar a imagem oficial do RabbitMQ do Docker Hub:

```bash
docker pull rabbitmq
```

Este comando baixará a imagem mais recente do RabbitMQ para o seu sistema.

## Passo 3: Executar o RabbitMQ com Docker

Agora que você tem a imagem do RabbitMQ, você pode executar um contêiner usando o seguinte comando:

```bash
docker run -d --name meu_rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq
```

- `-d`: Executa o contêiner em segundo plano (modo detached).
- `--name meu_rabbitmq`: Define um nome para o contêiner (substitua "meu_rabbitmq" pelo nome desejado).
- `-p 5672:5672 -p 15672:15672`: Mapeia as portas do contêiner para as portas do host (5672 é a porta padrão para conexões AMQP, e 15672 é a porta do painel de controle do RabbitMQ).

Isso iniciará um contêiner RabbitMQ e você pode acessar o painel de controle do RabbitMQ em [http://localhost:15672](http://localhost:15672) com as credenciais padrão (guest/guest).

Agora você está pronto para começar a desenvolver e testar aplicativos que utilizam o RabbitMQ!

Lembre-se de que este é um guia básico e você pode ajustar os comandos conforme necessário para atender aos requisitos específicos do seu projeto.

Certamente! Aqui está um exemplo de um README para o código apresentado. Certifique-se de personalizar as seções conforme necessário:

---

# RabbitMQ Python Example

Este é um exemplo simples de utilização do RabbitMQ em Python. Demonstramos um produtor que envia mensagens alternadas de sucesso e falha para uma fila e um consumidor que processa essas mensagens, tratando as falhas e movendo as mensagens problemáticas para uma fila de mensagens de falha.

## Pré-requisitos

- Python 3.x
- Biblioteca `pika` (pode ser instalada com `pip install pika`)
- RabbitMQ instalado e em execução localmente (para instalação, consulte [RabbitMQ Download](https://www.rabbitmq.com/download.html))

## Estrutura do Projeto

- `produtor.py`: Contém o código do produtor que envia mensagens para a fila.
- `consumidor.py`: Contém o código do consumidor que processa mensagens e lida com falhas.
- `README.md`: Este arquivo.

## Executando o Exemplo

1. Certifique-se de ter o RabbitMQ instalado e em execução localmente.
2. Instale a biblioteca `pika` com `pip install pika`.
3. Execute `produtor.py` para enviar mensagens para a fila.
4. Execute `consumidor.py` para processar as mensagens.

```bash
python produtor.py
python consumidor.py
```

## Detalhes Adicionais

- O código do produtor envia mensagens alternadas de sucesso e falha para a fila `fila_simples`.
- O código do consumidor processa as mensagens e, em caso de falha, move a mensagem para a fila `fila_falha`.
- O consumidor trata exceções, garantindo que mensagens problemáticas sejam movidas para a fila de falha.

---

Esse README serve como uma introdução ao seu projeto, permitindo que outros desenvolvedores entendam rapidamente o que o código faz, como executá-lo e como podem contribuir. Certifique-se de fornecer informações claras e concisas.
