from gtts import gTTS
import PyPDF2
import os

def read_pdf_aloud(pdf_path, output_path, language, speed, play_audio):
    # Abre o arquivo PDF
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        
        full_text = ""
        # Itera sobre todas as páginas do PDF
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            full_text += text
    
    # Configura a velocidade de leitura (gTTS não tem ajuste direto, então duplicamos ou reduzimos o texto)
    if speed == 'slow':
        tts = gTTS(text=full_text, lang=language, slow=True)
    else:
        tts = gTTS(text=full_text, lang=language, slow=False)
    
    # Salva o áudio em um arquivo
    tts.save(output_path)
    
    # Toca o áudio se solicitado
    if play_audio:
        os.system(f"mpg321 {output_path}")

def main():
    # Solicita o caminho do PDF, o caminho para o arquivo de saída, e o idioma
    pdf_path = input("Digite o caminho para o arquivo PDF: ")
    output_path = input("Digite o caminho para o arquivo de saída MP3: ")
    language = input("Digite o idioma desejado (pt, en, fr, etc.): ").strip().lower()
    speed_input = input("Escolha a velocidade de leitura (normal/rápido/lento): ").strip().lower()
    play_audio_input = input("Você quer ouvir o áudio diretamente do terminal? (s/n): ").strip().lower()

    if speed_input == 'rápido':
        speed = 'fast'
    elif speed_input == 'lento':
        speed = 'slow'
    else:
        speed = 'normal'

    play_audio = play_audio_input == 's'

    # Chama a função para ler o PDF em voz alta
    read_pdf_aloud(pdf_path, output_path, language, speed, play_audio)

if __name__ == "__main__":
    main()
