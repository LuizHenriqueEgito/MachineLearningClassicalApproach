# Regressão
## MAE

## MSE

## RMSE

## RMSLE

## MAPE

## R²

## Adjusted R²

## Huber Loss

## Quantile Loss


# Classificação
## Accuracy:

## Precision

## Recall (Sensitivity / TPR)

## Specificity / TNR

## FPR

## FNR

## F1-Score

## ROC-AUC

## PR-AUC

## Crier Score

## Log Loss / Cross Entropy

## Gini
Quão bem o modelo separa as duas classes (positiva e negativa), ele é diretamente derivado do ROC-AUC: 
$$Gini = 2 * ROCAUC - 1$$
| Gini        | Interpretação                                 |
|-------------|-----------------------------------------------|
| 0.0         | Modelo aleatório — não discrimina nada        |
| 0.3 – 0.5   | Discriminação fraca                           |
| 0.5 – 0.7   | Discriminação moderada                        |
| 0.7 – 0.9   | Discriminação forte                           |
| 1.0         | Perfeito — separa 100% dos casos              |

Intuição direta:
- `Gini`: Quantas vezes o modelo ordena **certo** um positivo acima de um negativo;
- Ele ignora o valor exato do score e olha apenas para a **ordenação**
- É uma métrica de **ranking quality**

Interpretação prática, pegue uma pessoa inadimplente e uma adimplente, `ALEATORIAMENTE` e faça a pergunta:
- *"Qual é a chance do modelo dar um score mais arriscado para o `INADIMPLENTE`?"*

A resposta para essa pergunta é o `AUC`, por exemplo `AUC`= 0,84 significa que:
- *Em 84% dos pares (um inadimplente e um adimplente escolhidos ao acaso), o modelo coloca o inadimplente como mais arriscado.*

Temos a relação direta do `GINI` com o `AUC`:

| AUC | Gini |
|:---:|:----:|
|0.50 | 0%   |
|0.60 | 20%  |
|0.70 | 40%  |
|0.75 | 50%  |
|0.80 | 60%  |
|0.85 | 70%  |
|0.90 | 80%  |
|0.95 | 90%  |
|1.00 | 100% |

Isso joga para a regua que, um modelo aleatório `AUC=0.5` fique com `GINI=0%` o que é mais intuitivo.

## KS

## Lift

# Clusterização
## Silhouette Score

## Davies-Bouldin Index

## Calinski-Harabasz
