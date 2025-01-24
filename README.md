# Assistente de Documentação LLM

O **Assistente de Documentação LLM** é uma ferramenta que ajuda na criação de documentos formais utilizando **LaTeX**. Ele foi projetado para ser usado com a classe de documentos LaTeX chamada **"llm"**. A ferramenta é desenvolvida em Python e utiliza a biblioteca **PyInquirer** para criar uma interface de linha de comando interativa.

## Sobre a classe de documentos "llm"

A classe **"llm"** é uma classe de documentos personalizada e projetada para o sistema de tipografia **LaTeX**. Ela foi desenvolvida especificamente para a criação de documentos jurídicos e é baseada na classe de documentos **"article"**.

## Público-alvo

O **Assistente de Documentação LLM** é ideal para:
- Advogados;
- Estudantes de Direito;
- Profissionais da área jurídica.

A ferramenta é projetada para ser fácil de usar, oferecendo uma interface simples e intuitiva para a criação de documentos formais.

## Benefícios

- Automação na criação de documentos legais;
- Integração com o poderoso sistema de tipografia LaTeX;
- Interface interativa e amigável para usuários.

## Requisitos

- **Python** instalado no sistema;
- Biblioteca **PyInquirer** para a interface interativa;
- Sistema LaTeX configurado para o uso da classe **"llm"**.

Comece a criar documentos formais com eficiência utilizando o Assistente de Documentação LLM!

## Estrutura das Pastas

A estrutura das pastas do projeto é a seguinte:

```
documentation-assistant-llm/
├── README.md
├── main.py
├── requirements.txt
├── llm/
│   ├── __init__.py
│   ├── document_class.py
│   └── templates/
│       ├── base_template.tex
│       └── legal_template.tex
└── tests/
    ├── __init__.py
    ├── test_document_class.py
    └── test_main.py
```

- `README.md`: Arquivo de documentação do projeto.
- `main.py`: Script principal para execução do assistente.
- `requirements.txt`: Lista de dependências do projeto.
- `llm/`: Diretório contendo os módulos principais do projeto.
  - `__init__.py`: Inicializador do módulo.
  - `document_class.py`: Módulo que define a classe de documento.
  - `templates/`: Diretório contendo templates LaTeX.
    - `base_template.tex`: Template base para documentos.
    - `legal_template.tex`: Template específico para documentos legais.
- `tests/`: Diretório contendo os testes do projeto.
  - `__init__.py`: Inicializador do módulo de testes.
  - `test_document_class.py`: Testes para o módulo `document_class.py`.
  - `test_main.py`: Testes para o script principal `main.py`.

## Como Executar

Para executar o Documentation Assistant LLM, siga os passos abaixo:

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/documentation-assistant-llm.git
   cd documentation-assistant-llm
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```

## Melhorias Futuras no Front End

Para melhorar a interface do usuário e a experiência geral, as seguintes melhorias podem ser implementadas no front end:

1. **Interface Gráfica do Usuário (GUI)**: Desenvolver uma interface gráfica utilizando bibliotecas como Tkinter ou PyQt para tornar o uso do assistente mais intuitivo e acessível.

2. **Editor de Texto Integrado**: Integrar um editor de texto que permita a edição direta dos documentos LaTeX dentro da aplicação, com suporte a realce de sintaxe e pré-visualização em tempo real.

3. **Suporte a Temas**: Adicionar suporte a diferentes temas visuais para a interface, permitindo que os usuários escolham entre temas claros e escuros.

4. **Assistente de Configuração**: Criar um assistente de configuração inicial que guie o usuário através das etapas de configuração do ambiente e das preferências do documento.

5. **Integração com Serviços de Nuvem**: Permitir a integração com serviços de armazenamento em nuvem como Google Drive e Dropbox para salvar e sincronizar documentos automaticamente.

6. **Suporte Multilíngue**: Adicionar suporte a múltiplos idiomas para tornar a ferramenta acessível a uma audiência global.

Implementar essas melhorias pode aumentar significativamente a usabilidade e a funcionalidade do Documentation Assistant LLM, tornando-o uma ferramenta ainda mais valiosa para profissionais legais e acadêmicos.