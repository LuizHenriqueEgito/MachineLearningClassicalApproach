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
Quão bem o modelo separa as duas classes (positiva e negativa), ele é diretamente derivado do ROC-AUC: $Gini = 2 * ROCAUC - 1$
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

## KS

## Lift

# Clusterização
## Silhouette Score

## Davies-Bouldin Index

## Calinski-Harabasz
