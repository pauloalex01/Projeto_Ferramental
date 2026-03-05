# 🔧 Sistema de Controle de Ferramentas com Leitura de Código de Barras

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Sistema desenvolvido em **Python** para gerenciamento de ferramentas utilizando **leitura de código de barras via câmera**, armazenamento em **SQLite** e arquitetura modular orientada a serviços.

O objetivo do projeto é **automatizar o controle de ferramental**, reduzindo erros humanos e aumentando a rastreabilidade em ambientes industriais.

---

# 📷 Demonstração

*(Falta adicionar um GIF, ignorar essa parte)*

Exemplo de funcionamento:

```
Câmera detecta código → sistema decodifica → busca no banco → retorna ferramenta
```

---

# 🎯 Aplicação Prática

Este sistema pode ser aplicado em:

* Almoxarifado industrial
* Controle de ferramentas de manutenção
* Laboratórios técnicos
* Controle de EPIs
* Inventário automatizado

Ele simula um **mini sistema de MRO (Maintenance, Repair and Operations)** utilizado em indústrias.

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia     | Função                      |
| -------------- | --------------------------- |
| Python         | linguagem principal         |
| SQLite         | banco de dados local        |
| OpenCV         | captura de vídeo            |
| PyZbar         | leitura de código de barras |
| Python-barcode | geração de códigos          |
| Pillow         | manipulação de imagens      |
| PyInstaller    | geração de executável       |

---

# 🏗️ Arquitetura do Projeto

O projeto foi estruturado em **camadas**, separando responsabilidades.

```
projeto_ferramental
│
├── database
│   ├── database.py
│   └── main.py
│
├── services
│   ├── ferramenta_service.py
│   ├── matricula_service.py
│   └── cam_service.py
│
├── utils
│   └── barcode_generator.py
│
├── interface
│   └── interface.py
│
├── database.db
│
└── README.md
```

### Camadas

**Database**

* criação do banco
* conexão SQLite
* manipulação das tabelas

**Services**

* lógica de negócio
* cadastro
* validações
* comunicação com banco

**Camera Service**

* leitura de código de barras
* captura de vídeo
* decodificação

**Utils**

* geração de códigos de barras para testes

---

# 🗄️ Estrutura do Banco de Dados

O banco possui **três tabelas principais**.

---

## Ferramentas

Armazena as ferramentas disponíveis.

| Campo     | Tipo |
| --------- | ---- |
| codigo    | TEXT |
| descricao | TEXT |

---

## Matrículas

Usuários autorizados a retirar ferramentas.

| Campo     | Tipo |
| --------- | ---- |
| matricula | TEXT |
| nome      | TEXT |

---

## Movimentação

Controla empréstimos.

| Campo             | Tipo    |
| ----------------- | ------- |
| id                | INTEGER |
| codigo_ferramenta | TEXT    |
| matricula         | TEXT    |
| data_retirada     | TEXT    |
| data_devolucao    | TEXT    |

---

# 🔍 Leitura de Código de Barras

A leitura é feita utilizando:

* OpenCV
* PyZbar

Tipos suportados atualmente:

```
EAN13
```

Fluxo de leitura:

```
Câmera
   ↓
Frame capturado
   ↓
PyZbar decodifica
   ↓
Código identificado
   ↓
Busca no banco de dados
```

---

# 🚀 Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seuusuario/projeto_ferramental.git
```

---

## 2️⃣ Entrar na pasta

```bash
cd projeto_ferramental
```

---

## 3️⃣ Instalar dependências

```bash
pip install opencv-python
pip install pyzbar
pip install python-barcode
pip install pillow
```

ou

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Executar o sistema

```bash
python main.py
```

---

# 🧪 Gerar Códigos de Barras para Teste

O projeto possui um gerador de códigos de barras.

Exemplo:

```python
criar_codigo_barras("789123456789")
```

Isso gera automaticamente a imagem do código.

---

# 📦 Gerar Executável

Para transformar o projeto em **aplicação desktop**:

Instalar:

```bash
pip install pyinstaller
```

Gerar executável:

```bash
pyinstaller --onefile main.py
```

O executável será criado na pasta:

```
dist/
```

---

# 🖥️ Interface Gráfica

A interface está em desenvolvimento e permitirá:

* cadastro de ferramentas
* cadastro de usuários
* leitura via câmera
* controle de empréstimos
* visualização de registros

Possível implementação futura com:

* Tkinter
* PyQt
* CustomTkinter

---

# 🔮 Melhorias Futuras

* Interface gráfica completa
* Controle de devoluções
* Logs de movimentação
* Dashboard de ferramentas
* Exportação para Excel
* Integração com leitores USB
* Sistema de autenticação
* API para integração com outros sistemas

---

# 🧠 Conceitos Aplicados

Este projeto aplica conceitos de:

* Programação em Python
* Banco de dados relacional
* Arquitetura modular
* Programação orientada a serviços
* Visão computacional
* Automação de processos

---

# 📊 Possível Evolução do Projeto

Este projeto pode evoluir para:

* sistema completo de **gestão de ferramental**
* integração com **Power BI**
* controle de **estoque industrial**
* dashboard de manutenção
* integração com **ERP**

---

# 👨‍💻 Autor

**Paulo Alex**

Estudante de **Engenharia Mecânica**
Interesse em:

* Automação
* Engenharia de dados
* Programação
* Sistemas industriais

---

# ⭐ Contribuição

Sugestões e melhorias são bem-vindas.

Se gostou do projeto:

⭐ **Deixe uma estrela no repositório**

---

# 📜 Licença

Este projeto é distribuído sob licença MIT.

---
