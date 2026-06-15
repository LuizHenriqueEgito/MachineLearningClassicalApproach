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