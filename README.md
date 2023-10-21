# Projeto de Automação com Selenium e OpenPyXL

Este é um projeto de automação simples que utiliza as bibliotecas Selenium e OpenPyXL para extrair informações de produtos de um site e armazená-las em uma planilha Excel. No exemplo fornecido, o projeto acessa o site "https://www.kabum.com.br/computadores/pc/pc-gamer", extrai os títulos e preços dos produtos e os armazena em uma planilha chamada "produtos.xlsx".

# Requisitos

Antes de executar o código, certifique-se de que você tenha as seguintes bibliotecas instaladas:
Selenium: Para automação do navegador.
OpenPyXL: Para criação e manipulação de planilhas Excel.
Um driver do Selenium compatível com o seu navegador (no exemplo, foi usado o driver do Google Chrome).
Você pode instalar as bibliotecas usando o pip:

pip install selenium openpyxl

Além disso, você precisa ter o driver do Selenium instalado e configurado corretamente para o seu navegador. No exemplo, foi usado o driver do Google Chrome.

# Executando o Projeto

Para executar o projeto, siga as etapas a seguir:
Clone ou faça o download deste repositório para o seu ambiente local.
Abra o arquivo Python (geralmente com a extensão .py) que contém o código de automação. Certifique-se de que o caminho do driver do Selenium esteja configurado corretamente para o seu ambiente.
Execute o código Python. Isso abrirá uma instância do navegador, acessará o site e coletará as informações dos produtos.
Após a conclusão da execução, uma planilha Excel chamada "produtos.xlsx" será criada no mesmo diretório em que o código está localizado.

# Personalização
Você pode personalizar este projeto para atender às suas necessidades específicas. Para isso, considere as seguintes modificações:

Altere a URL do site que você deseja acessar, modificando a linha:

driver.get('https://www.kabum.com.br/computadores/pc/pc-gamer')

Modifique as expressões XPath usadas para extrair informações dos elementos HTML, de acordo com a estrutura do site que você está automatizando.
Adicione colunas e informações adicionais à planilha, se necessário.
Altere o nome da planilha e o nome das colunas, conforme apropriado para os dados que você está coletando.

# Considerações Finais
Este projeto é um exemplo básico de automação web com Python e pode ser expandido para atender a casos de uso mais complexos. Certifique-se de respeitar os termos de serviço do site que você está automatizando e agir de forma ética e responsável ao coletar dados da web.
Lembre-se de que a web scraping de sites pode ser proibida em alguns casos, por isso é importante verificar os termos de uso do site e garantir que sua automação seja usada de maneira adequada.
