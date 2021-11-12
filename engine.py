import face_recognition as fr
import sqlite3

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)

    # se existe rostos
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []


def get_rostos():

    rostos_conhecidos = []
    nomes_dos_rostos = []

    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT nome, senha, nivel, caminho_destino FROM cadastro")
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        nome = row[0]
        foto = row[3]
        

        nome = reconhece_face("./img/{}".format(foto))
        
        # se for verdadeiro achou o rosto
        if(nome[0]):
            # gabriel [1] -> todos os rosto da foto [0] -> e o rosto na 0
            rostos_conhecidos.append(nome[1][0])
            nomes_dos_rostos.append(foto)
        

    return rostos_conhecidos, nomes_dos_rostos