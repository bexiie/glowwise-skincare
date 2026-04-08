# 🌿 GlowWise Skincare

## 📌 Descrição do Projeto

O **GlowWise Skincare** é um sistema de automação desenvolvido em **Python**, utilizando o **BotCity Framework Web** para automação de navegação e coleta de dados, e o **BotCity Maestro** para orquestração, gerenciamento de execuções, armazenamento de dados (DataPool) e envio de alertas. Com o objetivo de monitorar preços de produtos de skincare em diferentes lojas online, registrar histórico de valores, analisar variações e enviar alertas personalizados.

A proposta do sistema é apoiar decisões de compra mais conscientes, automatizando tarefas repetitivas de acompanhamento de preços e reduzindo a necessidade de consultas manuais constantes.

---

## 💡 Problema

Acompanhar preços de produtos de skincare em múltiplas lojas é um processo:

- repetitivo
- desorganizado
- demorado
- sujeito a decisões impulsivas

O projeto resolve esse problema automatizando a coleta, organização e análise dos dados, além de notificar o usuário quando surgirem boas oportunidades.

---

## 🎯 Objetivo Geral

Desenvolver um conjunto de bots utilizando o ecossistema BotCity para monitorar produtos de skincare, registrar histórico de preços, analisar variações e enviar alertas personalizados.

---

## ✅ Objetivos Específicos

- Coletar automaticamente dados de produtos em lojas online
- Armazenar e manter histórico de preços
- Comparar preços atuais com dados anteriores
- Identificar variações relevantes
- Enviar alertas quando condições definidas forem atendidas

---

## 🧠 Arquitetura do Projeto

O sistema é composto por **3 bots independentes**, organizados em pastas separadas:

### 🤖 Bot de Coleta

Responsável por:

- Acessar os sites (ex.: Drogasil e Beleza na Web)
- Extrair nome, preço e link dos produtos
- Armazenar os dados coletados
- Enviar dados ao DataPool

### 🤖 Bot de Análise

Responsável por:

- Ler os dados coletados
- Comparar preços com histórico
- Identificar variações relevantes
- Selecionar melhores oportunidades

### 🤖 Bot de Alerta

Responsável por:

- Processar os dados analisados
- Identificar condições de alerta
- Enviar notificações (ex.: Telegram)

---

## 📂 Estrutura do Projeto

```text
GlowWise Skincare/
│
├── bot_coleta_skincare/
│   ├── bot.py
│   ├── coleta.py
│   ├── requirements.txt
│   └── demais arquivos
│
├── bot_analise_skincare/
│   ├── bot.py
│   ├── analise.py
│   ├── requirements.txt
│   └── demais arquivos
│
├── bot_alerta_skincare/
│   ├── bot.py
│   ├── alerta.py
│   ├── requirements.txt
│   └── demais arquivos
│
└── README.md
```

📌 Cada bot possui seu próprio `bot.py`, conforme exigido pelo Runner do BotCity Maestro.

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- BotCity Framework Web
- BotCity Maestro
- DataPool
- Credentials Vault
- JSON
- Telegram API (para alertas)
- Google Sheets (opcional)

---

## 🔐 Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente

**Windows (PowerShell):**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install botcity-framework-web
pip install botcity-maestro-sdk
pip install python-dotenv
```

---

## 🔑 Configuração do Maestro

Crie um arquivo `.env` na raiz do projeto:

```env
MAESTRO_SERVER=seu_servidor
MAESTRO_LOGIN=seu_login
MAESTRO_KEY=sua_chave
```

⚠️ **Importante:** não versionar esse arquivo no repositório.

---

## 🔐 Credentials Vault

Credenciais sensíveis, como token do Telegram, devem ser armazenadas no **Credentials Vault do Maestro**, e não diretamente no código.

---

## ▶️ Execução Local

Cada bot pode ser executado individualmente.

### Bot de Coleta

```bash
cd bot_coleta_skincare
python bot.py
```

### Bot de Análise

```bash
cd bot_analise_skincare
python bot.py
```

### Bot de Alerta

```bash
cd bot_alerta_skincare
python bot.py
```

---

## ☁️ Execução no BotCity Maestro

Para execução no Maestro:

- Cada bot deve ser empacotado separadamente
- O arquivo principal deve se chamar `bot.py`
- Os bots devem ser registrados com labels no padrão:

```text
nomedoaluno-nomedobot-versao
```

### Exemplo

```text
rebeca-coleta-v1
rebeca-analise-v1
rebeca-alerta-v1
```

---

## 📊 DataPool

O DataPool é utilizado para:

- armazenar dados coletados
- alimentar o bot de análise
- controlar o status dos registros

---

## 📁 Arquivos de Resultado

Os bots geram arquivos que são enviados ao Maestro, como:

- JSONs
- logs
- relatórios
- planilhas ou screenshots (opcional)

### Exemplo de envio

```python
maestro.post_artifact("arquivo.json")
```

---

## 🔔 Alertas

O sistema envia notificações quando:

- um produto atinge o preço desejado
- há uma variação significativa

---

## 🚫 Limitações do Projeto

- Não realiza compras
- Não funciona como e-commerce
- Não armazena dados sensíveis de usuários

---

## 📌 Requisitos do Desafio Atendidos

- ✔ Mínimo de 3 bots
- ✔ Uso do BotCity Framework Web
- ✔ Integração com Maestro
- ✔ Uso de DataPool
- ✔ Uso de Credentials Vault
- ✔ Geração de artefatos
- ✔ Automação real (web scraping + alerta)
- ✔ README detalhado

---

## 🚀 Conclusão

O GlowWise Skincare demonstra como a automação pode ser aplicada para resolver problemas do dia a dia, tornando o monitoramento de preços mais eficiente, organizado e útil para decisões de compra mais conscientes.