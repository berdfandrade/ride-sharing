from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['riding-shiring']
riders_collection = db['riders']
drivers_collection = db['drivers']

def create_indexes():
    riders_collection.create_index('riderId', unique=True) 
    drivers_collection.create_index('driverId', unique=True)

# Função de teste para verificar a conexão e a criação de índices
def test_connection():
    try:
        # Testar a conexão com o MongoDB
        client.admin.command('ping')

        # Testar se os índices foram criados
        if 'riderId_1' not in riders_collection.index_information():
            print("Índice 'riderId' não foi criado em 'riders' collection.")
        if 'driverId_1' not in drivers_collection.index_information():
            print("Índice 'driverId' não foi criado em 'drivers' collection.")

        print("Conexão com o MongoDB e criação de índices bem-sucedidas.")
    except Exception as e:
        print(f"Erro ao testar a conexão com o MongoDB: {e}")

if __name__ == "__main__":
    test_connection()
