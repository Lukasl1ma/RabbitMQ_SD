import pika

# Função chamada quando uma mensagem é recebida
def callback(ch, method, properties, body):
    try:
        print(f" [x] Mensagem recebida: {body}")
        
        # Simula um erro ao processar algumas mensagens
        if b'falha' in body:
            raise Exception("Erro ao processar a mensagem")

    except Exception as e:
        # Se ocorrer uma exceção, mova a mensagem para a fila de falha
        channel.basic_publish(exchange='',
                              routing_key='fila_falha',
                              body=body)
        print(f" [!] Erro: {e}. Mensagem movida para a fila de falha")

# Estabelece a conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila 'fila_simples'
channel.queue_declare(queue='fila_simples')
# Declara a fila 'fila_falha'
channel.queue_declare(queue='fila_falha')

# Indica ao RabbitMQ que a função 'callback' deve ser chamada quando uma mensagem for recebida
channel.basic_consume(queue='fila_simples',
                      on_message_callback=callback,
                      auto_ack=True)  # auto_ack=True indica que as mensagens são marcadas como entregues automaticamente

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
