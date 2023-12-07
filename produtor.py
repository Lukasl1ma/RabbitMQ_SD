import pika
import time

# Estabelece a conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara uma fila chamada 'fila_simples'
channel.queue_declare(queue='fila_simples')
# Declara uma fila chamada 'fila_falha'
channel.queue_declare(queue='fila_falha')

# Simula mensagens de sucesso e falha alternadas
for i in range(5):
    try:
        if i % 2 == 0:
            message = f'Mensagem de sucesso {i}'
        else:
            # Simula uma falha ao tentar processar a mensagem ímpar
            raise Exception(f'Erro ao processar a mensagem {i}')

        # Publica a mensagem na fila 'fila_simples'
        channel.basic_publish(exchange='',
                              routing_key='fila_simples',
                              body=message)
        print(f" [x] Mensagem enviada: {message}")
        
        time.sleep(1)  # Aguarda um segundo entre mensagens

    except Exception as e:
        # Se ocorrer uma exceção, mova a mensagem para a fila de falha
        channel.basic_publish(exchange='',
                              routing_key='fila_falha',
                              body=message)
        print(f" [!] Erro: {e}. Mensagem movida para a fila de falha")

# Fecha a conexão
connection.close()
