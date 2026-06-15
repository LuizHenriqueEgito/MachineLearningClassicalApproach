# Feature Importance
Diz se uma `feature` foi importante para o modelo de forma geral durante o treinamento.

### Split x Gain
- `split`: Conhecido como *frequency* conta quantas vezes uma feature foi usada para fazer um **split**. Features com alta cardinalidade tendem a ser escolhidas mais vezes, esse é um ponto de atenção.
- `gain`:  Ao invés de contagem (como no **split**) o **gain** soma o ganho de informação médio que cada split com aquela feature gerou. Uma feature que aparece poucas vezes mas sempre que aparece trás informação tem ganho alto. Ela olha a *qualidade* e não apenas a *quantidade* como o **split**.

# SHAP Value
Diz o quanto a feature impacta na previsão final. A ideia vem da **Teoria dos Jogos - cooperativos**, imagine que cada feature é um **jogador** então simulamos todas as combinações possíveis de cada jogador presentes ou ausentes e mede a contribuição marginal de cada um. O `SHAP value` é a média ponderada dessa contribuição marginal.

O `SHAP` pode ser utilizado para *debugar* os erros do modelo, por qual motivo o modelo está errando o que está causando o erro você consegue ver isso olhando para o `SHAP values` e entender quais features estão fazendo o modelo errar.


SHAP Value = contribuição marginal esperada  
           = média ponderada das contribuições de uma feature  
Os valores de Shapley são uma forma **justa** de dividir o valor da relevancia entre as features.
[video explicativo.](https://www.youtube.com/watch?v=UJeu29wq7d0&list=PLqDyyww9y-1SJgMw92x90qPYpHgahDLIK&index=3)

### **Fórmula do Valor de Shapley**

Onde:

- **Peso**
  
$$\frac{|S|!(p-|S|-1)!}{p!}$$

- **Contribuição marginal da feature \(i\) para o conjunto de features \(S\)**
$$val(S \cup \{i\}) - val(S)$$


#### Significado dos termos

- \(p!\) = número de maneiras de organizar todas as \(p\) features

- \(|S|\) = quantidade de features presentes no subconjunto \(S\)

- \(|S|!\) = número de maneiras pelas quais o subconjunto \(S\) pode ser formado

- \((p-|S|-1)!\) = número de maneiras pelas quais as features restantes podem ser adicionadas após a feature \(i\)

#### Interpretação em Machine Learning

O valor de Shapley mede:

> "Quanto uma feature contribui, em média, para a predição do modelo considerando todas as combinações possíveis de features."

A ideia central é:

1. Pegamos vários subconjuntos de features
2. Adicionamos a feature \(i\)
3. Observamos quanto a predição mudou
4. Fazemos isso para todas as combinações possíveis
5. Tiramos uma média ponderada

#### Exemplo intuitivo
Imagine um modelo com:

- idade
- salário
- histórico de crédito

Queremos descobrir o impacto da feature:


$\text{salário}$

Então o SHAP calcula:

- quanto o salário ajuda sozinho
- quanto ajuda junto da idade
- quanto ajuda junto do histórico
- quanto ajuda quando todas as outras features já estão presentes

E tira uma média justa dessas contribuições. É dai que sabemos a contribuição *marginal* dessa feature.


## Diferença entre SHAP x Feature Importance
