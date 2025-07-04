# Job Scraper com Selenium

Este projeto é um script em Python que utiliza Selenium para automatizar a busca e filtragem de vagas no site InfoJobs e salva os links das vagas encontradas em uma planilha Excel.

---

## Funcionalidades

- 🚀 Automatiza a abertura do site InfoJobs
- 🍪 Aceita automaticamente o aviso de cookies
- 🎯 Aplica filtros para vagas da área de Informática, TI e Telecomunicações
- 👨‍🎓 Filtra vagas de nível estagiário
- 🔗 Captura links das vagas encontradas na página
- 💾 Salva os links coletados em uma planilha Excel (`vagas.xlsx`)
- 🕒 Inclui um tempo de espera para garantir que os dados carreguem antes de salvar
- (Opcional) Permite salvar a planilha em uma pasta específica na área de trabalho

---

## Tecnologias utilizadas

- Python
- Selenium
- Pandas

---

# 🛑 Aviso Legal

## Este projeto é exclusivamente para fins educacionais.

- Não coleta dados pessoais ou sensíveis.
- Não quebra captcha, autenticação ou outras barreiras de segurança.
- Todos os dados coletados são públicos e acessíveis sem login.
- O uso do código deve respeitar os Termos de Uso do InfoJobs.
- Não utilize este script para fins comerciais ou alta escala sem permissão.

---

# 🎓 Objetivo do projeto

Este projeto foi criado como prática de:

- Automação de tarefas com Selenium
- Extração de dados públicos da web
- Estruturação de dados com pandas
- Geração de planilhas com Python

---

## Como usar

1. Instale as dependências necessárias:

```bash
pip install requirements.txt
```

1. Baixe o ChromeDriver compatível com a versão do seu Google Chrome e coloque-o no PATH ou na mesma pasta do script.
2. Clone este repositório ou copie o script para sua máquina.
3. Execute o script com:

```bash
python app.py
```

Após a execução, uma planilha `vagas.xlsx` será criada na pasta do projeto (ou na pasta configurada no script).

---

## Como funciona

- O script abre o navegador Chrome e acessa a página de vagas do InfoJobs para a região selecionada ( por padrão Rio de Janeiro ).
- Aceita o aviso de cookies automaticamente.
- Aplica filtros para mostrar vagas na área de TI e nível estagiário.
- Coleta os links das vagas exibidas na página.
- Salva os links em um arquivo Excel, evitando links duplicados.
- Encerra o navegador após salvar a planilha.

---

## Personalizações

Você pode ajustar o filtro para outras áreas ou níveis hierárquicos alterando os seletores no código. Também pode modificar o local onde a planilha é salva alterando o código da função `salvar_planilha`.

---

## Observações

- É necessário ter o ChromeDriver instalado e compatível com a versão do seu navegador Chrome.
- Caso o site InfoJobs altere o layout ou os seletores, o script pode precisar ser atualizado.
- Esse script é um ponto de partida para coleta automatizada de vagas e pode ser expandido para extrair outras informações das vagas.
