class Conectando:
    def __enter__(self):
        print('Estou Conectada')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou desconectando')


with Conectando() as ola:
    print('Estou dentro da aplicação')