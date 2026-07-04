# Estrutura das árvores
- `num_leaves`: *(padrão: 31)* - Número máximo de folhas por árvore. Principal parâmetro de complexidade do `LightGBM`.
- `max_depth`: *(padrão: -1, sem limite)* - Profundidade máxima das árvores.
- `min_data_in_leaf` / `min_child_samples`: *(padrão: 20)* - Mínimo de amostras por folha.
- `min_sum_hessian_in_leaf ` / `min_child_weight`: *(padrão: 1e-3)* - Força da evidencia para que ocorra uma quebra nas árvores.
- `num_iterations` / `n_estimators`: *(padrão: 100)* - Número de árvores.
- `learning_rate` / `eta`: *(padrão: 0.1)* - Taxa de aprendizado. Quanto menor mais árvores necessárias.
- `early_stopping_round`: Para o treino se a métrica não melhorar em **N** rodadas.

### Regularização (L1 & L2)
Cada `folha` tem um peso na predição final. `Folhas` com valores muito grandes ou muito extremos são sinal de `overfitting`.
- `lambda_l1`: Empurra valores para zero. L1 trata folhas com valor 0.1 e valor 10 de forma mais proporcional. Mas o efeito característico é que ela empurra valores diretamente para zero — folhas "fracas" são zeradas completamente, o que equivale a eliminar aquela divisão da árvore. $penalidade_{L1} = lambda_{l1} × Σ|valor_folha|$
- `lambda_l2`: Penaliza valores grandes. Elevar ao quadrado significa que folhas com valores muito grandes são punidas muito mais do que folhas com valores moderados. O efeito prático é que o modelo prefere muitas folhas com valores pequenos a poucas folhas com valores grandes. $penalidade_{L2} = lambda_{l2} × Σ(valor_folha²)$


# `feature_contri`
### `aliases`: feature_contrib, fc, fp, feature_penalty
Básicamente com esse parametro o modelo altera o `gain`. Normalmente é feito o split com o maior gain, mas com `feature_contri ` isso muda e fica assim:
$$gain_{final} = gain_{original} - feature_{contri} $$
É como se falassemos para o modelo que a feature vale menos isso força o modelo a dar menos peso/importancia para ela. Para usar esse parametro você deve: Passar a contribuição de todas as features em uma lista.
``` python
feature_weights = {
    "idade": 1.0,
    "renda": 1.0,
    "cep": 0.2,
    "score_externo": 0.5
}

# isso garante a ordem das features (muito importante)
feature_contri = [
    feature_weights[col]
    for col in X.columns
]

params = {
    "objective": "binary",
    "feature_contri": feature_contri
}
```