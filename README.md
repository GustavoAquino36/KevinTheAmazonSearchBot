<h1>Projeto de Web Scraping com Python e Selenium</h1>

<h2>Pré-requisitos</h2>
<p>Certifique-se de ter os seguintes componentes instalados em seu ambiente de desenvolvimento:</p>
<ul>
    <li>Python 3.x</li>
    <li>Selenium</li>
    <li>Um driver do Selenium compatível com o navegador que você deseja automatizar (por exemplo, ChromeDriver para
        o Google Chrome)</li>
    <li>pyshorteners</li>
    <li>openpyxl</li>
</ul>

<h2>Instalação</h2>
<ol>
    <li>Clone o repositório do projeto ou faça o download dos arquivos.</li>
    <li>No terminal, navegue até o diretório do projeto.</li>
    <li>Instale as dependências executando os seguintes comandos:</li>
</ol>

<pre><code>pip install selenium</code></pre>
<pre><code>pip install pyshorteners</code></pre>
<pre><code>pip install openpyxl</code></pre>

<h2>Configuração</h2>
<p>Antes de executar o projeto, você precisará configurar algumas informações.</p>
<ol>
    <li>Crie uma senha de app para o email utilizado para enviar a resposta. Siga o tutorial do google http://surl.li/itqxb</li>
    <li>Abra o arquivo <code>settings.xlsx</code>.</li>
    <li>Preencha as seguintes informações(na coluna Value):</li>
</ol>
<li>
    <li><code>email</code>: o email a ser usado para enviar o resultado.</li>
    <li><code>senha</code>: a senha de app criada para o email acima.</li>
</ul>

<h2>Executando o projeto</h2>
<p>Para executar o projeto, execute o seguinte comando no terminal:</p>
<pre><code>python bot.py</code></pre>
<p>O programa irá então perguntar qual o produto a ser pesquisado, e o email destinatário. Ambos devem ser respondidos no terminal após cada pergunta</p>

<h2>Personalização</h2>
<p>Você pode personalizar este projeto de acordo com suas necessidades. Alguns possíveis ajustes incluem:</p>
<ul>
    <li>Adicionar mais funcionalidades de extração de informações da página da Amazon.</li>
    <li>Modificar o formato do e-mail para incluir mais detalhes ou formatação específica.</li>
</ul>
<p>Certifique-se de revisar a documentação do Selenium para obter mais informações sobre suas funcionalidades e possibilidades de personalização.</p>
