# O Desafio

Você faz parte da equipe de tecnologia de um grande banco e recebeu uma missão importante: ajudar o setor financeiro a organizar rapidamente os lançamentos diários de despesas e receitas.

Cada lançamento é registrado como uma string contendo o tipo (D para despesa, R para receita) seguido do valor em reais, separados por espaço. Sua tarefa é criar uma função que calcule o saldo final do dia.

## 📋 Regras de Negócio

- **Cálculo:** O saldo é a soma de todas as receitas menos a soma de todas as despesas ($Saldo = \sum Receitas - \sum Despesas$).
- **Formatação:** O resultado deve ser apresentado com duas casas decimais, mesmo que o valor seja inteiro.
- **Restrição:** Não utilize bibliotecas externas.
- **Processamento:** A função deve ler uma linha contendo lançamentos separados por vírgula.

## 📥 Entrada

Uma única linha contendo lançamentos separados por vírgula. Cada lançamento é composto por uma letra (D ou R), seguida de um espaço e um valor decimal positivo.

**Exemplo:**

```
R 100.00, D 40.50, R 20.00
```

## 📤 Saída

Uma única linha contendo o saldo final do dia, com duas casas decimais.

**Exemplo:**

```
79.50
```