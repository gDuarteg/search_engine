# Uma máquina de busca para fins didáticos.

## Alunos

Thomas Queiroz

Gabriel Duarte

## Instruções

- Faça um *fork* deste repositório para poder receber atualizações eventuais. Para saber como fazer um *fork*, veja https://docs.github.com/en/github/getting-started-with-github/fork-a-repo.

- Abra um terminal e vá para o diretório deste repositório.

- Rode `config.bat` (no Windows) ou `config.sh` (Linux/Mac) para colocar este diretório no `PYTHONPATH`.

- Abra seu ambiente de desenvolvimento (seu editor favorito, ou jupyter notebook, etc) a partir deste terminal para fazer uso da variável de ambiente `PYTHONPATH` atualizada.

- Para testar, rode `./run.sh` e digite sua busca quando for solicitado no formato `<OR_QUERY> "<AND_QUERY>"`.

Tem jeito melhor? Tem, mas fica pra o Igor mostrar para vocês na eletiva de software livre!

## Exemplo

`"Pao de Batata" China India`

### Interpretação 

`(Pao AND de AND Batata) OR China OR India`

## Conceitos
- Limpeza dos dados

- Normalização

- Retrieval booleano 

- Queries booleanas

- Ranking tf-idf


## Base de Dados

<https://www.kaggle.com/kingburrito666/better-donald-trump-tweets>
