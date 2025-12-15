# 🎉 Cadastro de Clientes — App em Streamlit

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit--app-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> Um pequeno aplicativo em Streamlit para cadastrar clientes e salvar os dados em `clientes.csv`. Simples, direto e pronto para você testar e expandir.

---

## ✨ Visão geral
Este projeto oferece uma interface web leve (via Streamlit) onde você pode:
- Inserir nome, endereço, data de nascimento e tipo de cliente;
- Salvar os dados em um arquivo `clientes.csv` (na mesma pasta do `app.py`);
- Ver confirmação visual após cada cadastro.

É ideal como exercício para aprender Streamlit, manipulação de arquivos CSV e deploy rápido.

---

## 📁 Estrutura do repositório
- app.py — aplicação Streamlit (formulário + gravação em CSV)
- clientes.csv — arquivo gerado com os cadastros (criado após o primeiro cadastro)
- README.md — este arquivo

---

## 🛠 Requisitos
- Windows / macOS / Linux
- Python 3.11 (recomendado — algumas versões mais novas podem ter incompatibilidades com algumas bibliotecas)
- pip (gerenciador de pacotes)
- Streamlit

---

## 🚀 Instalação e execução (passo a passo)

1. Abra o terminal / PowerShell e navegue até a pasta do projeto:
```bash
cd "C:\Users\<seu_usuario>\Desktop\primeiro projeto"
```

2. (Opcional, recomendado) Crie e ative um ambiente virtual:
- Windows (PowerShell):
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate
```
- macOS / Linux:
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

3. Atualize pip e instale o Streamlit:
```bash
py -m pip install --upgrade pip setuptools wheel
py -m pip install --user streamlit
# ou, dentro do venv:
pip install streamlit
```

4. Execute o app:
```bash
py -m streamlit run app.py
# ou, se o streamlit estiver no PATH:
streamlit run app.py
```

5. Abra o navegador no endereço que o Streamlit informar (normalmente `http://localhost:8501`).

---

## ✅ Formato do CSV criado
Cada linha será gravada assim (valores separados por vírgula):

nome,endereco,data_nascimento,tipo_cliente

Exemplo:
```
João Silva,Rua A,1990-05-20,Pessoa física
Maria Souza,Rua B,1985-10-11,Pessoa jurídica
```

Observações:
- A data é gravada no formato ISO (`YYYY-MM-DD`) para facilitar leitura e importação.
- Se preferir, troque a gravação por `csv.writer` para lidar com vírgulas internas nos campos.

---

## 🔍 Solução de problemas comuns

- "streamlit : O termo 'streamlit' não é reconhecido":
  - Use `py -m streamlit run app.py` em vez de `streamlit run app.py`, ou adicione a pasta Scripts do Python ao PATH.
  - Verifique se instalou no mesmo Python que está usando: `py -m pip --version`

- "O comando python não encontrado" / Windows aponta para `WindowsApps`:
  - Instale/reinstale o Python em https://www.python.org/downloads/ e marque "Add Python to PATH".
  - Tente o launcher `py --version`.

- CSV não aparece:
  - Verifique a pasta onde o app está rodando. O `clientes.csv` será criado na mesma pasta do `app.py` (quando usamos Path(__file__).parent).
  - Procure por mensagens de erro no terminal onde rodou o Streamlit.

---

## 💡 Dicas e sugestões de melhorias
- Usar `csv.writer` para escapar campos com vírgulas.
- Adicionar validação mais robusta (CPF/CNPJ, campos obrigatórios).
- Salvar também data/hora do cadastro (`datetime.now()`).
- Permitir exportar/baixar o CSV direto pela interface Streamlit.
- Persistir em um banco (SQLite) para consultas e edição.

---

## 🤝 Contribuindo
Contribuições são bem-vindas! Abra uma issue com ideias ou envie um pull request com melhorias:
- Correções de bugs
- Validações adicionais
- Interface mais completa

---

## 📝 Licença
Este projeto está sob a licença MIT — veja o arquivo LICENSE para detalhes.

---

Se quiser eu :
- Faço um arquivo `requirements.txt` pronto;
- Adiciono a gravação com `csv.writer` ao `app.py`;
- Crio instruções de deploy (Heroku / Streamlit Sharing / Render).

Quer que eu gere o `requirements.txt` e um exemplo de deploy agora? 🚀