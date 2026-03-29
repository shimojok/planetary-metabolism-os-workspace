$$
\text{Glucose} \rightarrow 2\,\text{Acetate} + 2\,\text{CO}_2 + 4\,\text{H}_2
$$

$$
\text{Lactate} \rightarrow \text{Propionate}
\quad
(\text{pathway: } \text{pyruvate} \rightarrow \text{oxaloacetate} \rightarrow \text{succinate} \rightarrow \text{propionate})
$$

$$
2\,\text{Acetyl-CoA} \rightarrow \text{Butyryl-CoA} \rightarrow \text{Butyrate}
\quad
(\text{electron carrier: crotonyl-CoA})
$$

$$
\text{NADH},\ \text{Fd}_{\text{red}} \rightarrow \text{H}_2
\quad
\text{(hydrogenase)};\quad
\text{H}_2 + \text{CO}_2 \rightarrow \text{CH}_4
$$

$$
\frac{dS_i}{dt} = \sum_{r} \nu_{i r}\, v_r(S,X)
\quad ; \quad
\frac{dX_j}{dt} = \mu_j(S)\,X_j - d_j\,X_j
$$

$$
v_{\text{F:Glc}\rightarrow \text{Lac},\text{Ac},\text{H}_2}
=
k_F\,X_F\,
\frac{\text{Glc}}{K_{s,F}+\text{Glc}}\,
f_{\text{pH}}\,
f_{\text{Eh}}
$$

$$
v_{\text{B:Lac}\rightarrow \text{But}}
=
k_B\,X_B\,
\frac{\text{Lac}}{K_{s,B}+\text{Lac}}\,
\frac{\text{Ac}}{K_{a,B}+\text{Ac}}\,
g(H_2)
$$

$$
v_{\text{P:Lac}\rightarrow \text{Prop}}
=
k_P\,X_P\,
\frac{\text{Lac}}{K_{s,P}+\text{Lac}}\,
h(H_2)
$$

$$
v_{\text{T:H}_2\rightarrow \text{sink}}
=
k_T\,X_T\,
\frac{H_2}{K_{s,T}+H_2}
$$

$$
\mu_j = Y_j \sum_{r \in j} v_r
\quad \text{subject to} \quad
\Delta G'_r \le -\Delta G_{\min}
$$

$$
\Delta G'_r = \Delta G^\circ_r + R T \ln\!\left(\prod_k a_k^{\nu_{k r}}\right)
$$

$$
\max_{\vec v}\ \sum_j \mu_j
\quad \text{s.t.} \quad
S\vec v = 0,\ 
v_{\text{ex},m}^{\min} \le v_{\text{ex},m} \le v_{\text{ex},m}^{\max},\ 
\Delta G'_r \le -\Delta G_{\min}
$$