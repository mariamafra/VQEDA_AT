import os

def listar_arquivos_recursivo(dir):
    try:
        for item in os.listdir(dir):
            item_dir = os.path.join(dir, item)
            if os.path.isfile(item_dir):
                print(item_dir)
            elif os.path.isdir(item_dir):
                listar_arquivos_recursivo(item_dir)
    except OSError as e:
        print(f"Erro ao acessar '{dir}': {e}") 

listar_arquivos_recursivo("C:/Users/maria/OneDrive/Documentos/INFNET/Ciencia da Computacao/VQEDA")