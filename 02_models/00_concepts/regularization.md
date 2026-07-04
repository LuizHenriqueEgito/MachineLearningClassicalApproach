# Regularização

## L1 & L2 (Modelos Lineares)

## L1 & L2 (Árvores)
`L1` e `L2` evitam que as árvores fiquem:
- Complicadas demais;
- Agressivas demais;
- Confiantes demais.

### L1
Pune mais os pesos das folhas se forem proximos de 0 ele leva esse peso para **zero** e nem conta mais com aquela folha. Ele elimina contribuições pequenas. Em resumo `L1` elimina o que já não está ajudando muito (faz com que ignoremos coisas pouco importantes).
 
### L2
Não permite que as folhas nas árvores tenham valores muito altos, a regularização L2 faz com que os valores das folhas sejam mais contidos, isso para não dar muito peso e suavizar as decisões. Em resumo, `L2` suaveiza exageros (faz com que não exageremos nas decisões).

#### OBS:
Em árvores não regularizamos features diretamente, estamos regularizando os **valores das folhas**. Por modelos de **boosting** serem muito agressivos, `esse tipo de regularização` é muito importante. 