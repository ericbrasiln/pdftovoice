# PDF to Voice

Este repositório contém um script Python que lê o texto de um arquivo PDF em voz alta, com opções para ajustar a velocidade da leitura e escolher o idioma. O áudio pode ser salvo em um arquivo MP3 e também pode ser reproduzido diretamente do terminal.

## Funcionalidades

- Converte texto de arquivos PDF para áudio.
- Suporte para múltiplos idiomas usando gTTS (Google Text-to-Speech).
- Ajuste de velocidade da leitura (normal, rápido, lento).
- Opção para salvar o áudio em um arquivo MP3.
- Opção para reproduzir o áudio diretamente do terminal.

## Pré-requisitos

- Python 3.x
- `mpg321`
- `gtts`
- `PyPDF2`

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/pdf-to-voice.git
   cd pdf-to-voice
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Certifique-se de ter o `mpg321` ou outro player de áudio instalado. No Ubuntu/Debian, você pode instalar com:

   ```sh
   sudo apt-get install mpg321
   ```

## Uso

Execute o script:

```sh
python read_pdf.py
```

O script solicitará as seguintes informações:

- **Caminho para o arquivo PDF**: O caminho completo para o arquivo PDF que você deseja converter para áudio.
- **Caminho para o arquivo de saída MP3**: O caminho completo onde você deseja salvar o arquivo de áudio gerado.
- **Idioma desejado**: O código do idioma (por exemplo, 'pt' para português, 'en' para inglês, 'fr' para francês, etc.).
- **Velocidade de leitura**: A velocidade da leitura ('normal', 'rápido', 'lento').
- **Ouvir o áudio diretamente do terminal**: Indique se deseja ouvir o áudio diretamente após a conversão ('s' para sim, 'n' para não).

## Exemplo

```sh
Digite o caminho para o arquivo PDF: /caminho/para/seu_arquivo.pdf
Digite o caminho para o arquivo de saída MP3: /caminho/para/saida/output.mp3
Digite o idioma desejado (pt, en, fr, etc.): pt
Escolha a velocidade de leitura (normal/rápido/lento): normal
Você quer ouvir o áudio diretamente do terminal? (s/n): s
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Coautoria

Este script foi escrito em coautoria com o ChatGPT, baseado no modelo GPT-4 da OpenAI.
