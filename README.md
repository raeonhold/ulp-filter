---

# ULP Filter

Este script foi feito para **filtrar url:login:password específicas dentro de arquivos `.txt`** em um diretório.
Ele percorre todos os arquivos `.txt`, ignora o `result.txt`, e salva os resultados encontrados em um arquivo consolidado.

---

## Funcionalidades

* Filtra todas as linhas de arquivos `.txt` que **começam com uma URL definida pelo usuário**.
* Suporta múltiplos arquivos no diretório.
* Gera automaticamente um arquivo `result.txt` com os resultados.
* Mensagens claras para arquivos inválidos ou sem resultados.

---

## Estrutura de Saída

O arquivo `result.txt` terá o seguinte formato:

```
Results from file: arquivo1.txt
https://example.com/test1
https://example.com/test2

Results from file: arquivo2.txt
https://example.com/abc
```

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/raeonhold/ulp-filter.git
cd url-filter
```

2. Instale a dependência:

```bash
pip install tqdm
```

3. Coloque os arquivos `.txt` no mesmo diretório do script.

4. Execute:

```bash
python ulp.py
```

5. Informe a URL base que deseja filtrar (exemplo: `https://example.com`).

6. Verifique o arquivo `result.txt` com os resultados filtrados.

---

## Exemplo de uso

Suponha que você tenha dois arquivos no diretório:

**file1.txt**

```
https://example.com/page1
http://test.com/page
https://example.com/page2
```

**file2.txt**

```
https://example.com/home
https://outro.com/page
```

Rodando o script e inserindo `https://example.com`, o arquivo `result.txt` ficará assim:

```
Results from file: file1.txt
https://example.com/page1
https://example.com/page2

Results from file: file2.txt
https://example.com/home
```
