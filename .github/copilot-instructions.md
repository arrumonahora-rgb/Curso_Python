<!-- Arquivo gerado/atualizado por assistente - revisar antes de commitar -->
# Instruções para agentes AI — Curso Python e Mysql

Objetivo curto
- Repositório composto por scripts didáticos Python simples. Os agentes devem fazer mudanças mínimas e pedagógicas: manter exemplos legíveis, rodar localmente no Windows PowerShell e documentar qualquer alteração.

Arquitetura & fluxo (big picture)
- Tipo de projeto: conjunto de scripts procedurais no diretório raiz. Não há módulos, pacotes ou dependências externas.
- Arquivos chave:
  - `app.py` — demonstração de variáveis, cálculo simples e impressão de resultados.
  - `captura.py` — captura de entrada via `input()` e conversão de tipos.
  - `operadores.py` — exemplos de operadores e cálculo de IMC (observação: fórmula atualmente é `peso / altura`).
- Fluxo típico: executar um script isolado para demonstrar entrada/processamento/saída.

Ambiente de desenvolvimento / comandos úteis
- Interprete: Python 3 (executar com o executável `python` configurado no PATH).
- Comandos PowerShell (rodar na raiz do projeto):
  - `python .\app.py`
  - `python .\captura.py`
  - `python .\operadores.py`
- Não há `requirements.txt` nem virtualenv obrigatório — projeto educativo.

Padrões e convenções do projeto
- Estilo: scripts curtos, foco em legibilidade para iniciantes. Evitar refatores agressivos que transformem exemplos em código complexo.
- Nomes: variáveis em camelCase ou minúsculas simples (ex.: `nomeCliente`, `idadeCliente`).
- Entradas/saídas: use `input()` e `print()`; mantenha mensagens em pt-br e simples.

Tarefas que agentes podem fazer automaticamente
- Correções simples e pedagógicas (sempre explicar a mudança):
  - Corrigir a fórmula do IMC em `operadores.py` para `peso / (altura ** 2)` — peça confirmação antes de substituir automaticamente.
  - Transformar um script em função reutilizável (ex.: `def main():`) e adicionar `if __name__ == '__main__': main()` quando solicitado.
  - Adicionar comentários explicativos curtos para fins didáticos.
- Não executar mudanças que removam a didática (por ex., converter tudo para um package sem pedido explícito).

O que NÃO fazer sem permissão
- Reescrever o repositório em outro framework ou adicionar dependências novas sem instruções do mantenedor.
- Remover exemplos simples para 'otimização' ou 'melhor arquitetura'.

Exemplos de prompts úteis para o agente
- "Melhore a legibilidade de `operadores.py` e explique a correção da fórmula do IMC em uma linha de comentário." 
- "Crie uma versão de `captura.py` que valide a entrada do usuário e trate entradas não numéricas." 
- "Transforme `app.py` em um módulo com `main()` e adicione instruções de execução no topo do arquivo como comentário." 

Padrões detectáveis no código (para referência do agente)
- Uso direto de `print()` para saída; quando extrair funções, mantenha chamadas a `print()` no escopo `if __name__ == '__main__'`.
- Entrada com `input()` convertida manualmente (ex.: `int(input(...))`) — trate `ValueError` se for necessário validar.

Checagens rápidas antes de PRs
- Execute cada script localmente no PowerShell.
- Mantenha mensagens em pt-br conforme arquivos existentes.
- Se alterar a fórmula do IMC ou o comportamento de entrada, inclua comentário explicando a mudança.

Onde procurar contexto adicional
- Não existem arquivos de documentação adicionais no repositório; inspecione diretamente `app.py`, `captura.py`, `operadores.py`.

Feedback
- Se algo estiver incompleto ou você quiser que o agente padronize o estilo (ex.: PEP8), avise explicitamente antes de aplicar mudanças em massa.

---
Fim do arquivo de instruções. Solicite confirmação do mantenedor para mudanças que alterem a intenção pedagógica.
