import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione a pasta a ser organizada')

lista_arquivos = os.listdir(caminho)

locais = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".avif", ".heic",],
    "Imagem de Disco": [".iso", ".img", ".dmg"],
    "Códigos Programação": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".rb", ".php", ".ino", ".swift", ".kt", ".rs", ".go", ".ts", ".css", ".json"],   
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Documentos de texto": [".doc", ".docx", ".txt", ".odt"],
    "PDFs": [".pdf"],
    "Planilhas": [".xlsx", ".xls", ".ods", ".csv"], 
    "Apresentações": [".pptx", ".ppt", ".odp"],
    "Arquivos compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Áudios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Códigos fonte": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".rb", ".php"],
    "CorelDRAW": [".cdr"],
    "Adobe Illustrator": [".ai"],
    "Programas": [".exe", ".msi", ".bat", ".sh"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao.lower() in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            print(f"Movendo arquivo {arquivo} para a pasta {pasta}")
            break