---
layout: default
title: Compare Embeddings
nav_exclude: false
nav_order: 2
has_children: false
parent: LLM and ML application
---

[Access Script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/compare_word_embedding.py){: .btn .btn-purple }

[Access Embedding script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/Embedder.py){: .btn .btn-green }

[Access Training script](https://github.com/ResilienceAnalytics/Python-Code/blob/main/Training.py){: .btn .btn-red }

## Leveraging Symbolic Differentiation in Word Embeddings Analysis: Semantic Shift Vector SSV

**Introduction**:
In the field of natural language processing (NLP), the exploration of word embeddings offers crucial insights into linguistic patterns and shifts. While traditional methods provide valuable overviews, they often overlook subtle shifts within the embeddings. To address this, we propose a method utilizing symbolic differentiation, focusing on relative dimensionality changes in word embeddings to offer nuanced analysis.

**The Limitations of Traditional Methods**:
Traditional analysis techniques, such as cosine similarity or Euclidean distance, provide a macro view of word embeddings, often missing out on the intricate details of linguistic evolution. These methods may not capture the subtle, dimension-specific changes essential for understanding the complete picture of language dynamics.

**Introducing Symbolic Differentiation in Word Embeddings Analysis**:
Our approach applies symbolic differentiation to examine the changes across each dimension of word embeddings, adhering to the principles of Occam's razor for analytical simplicity and effectiveness. The method is formulated as follows:

Given old and new embeddings of a word,

$$Vold=(v1_{old},v2_{old},…,vn_{old})$$ and $$V{new}=(v1_{new},v2_{new},…,vn_{new})$$,

the product difference for each dimension i is calculated as:

$$ΔVi=(vi_{new}−vi_{old})×vi$$ ,

and the sum of products for each dimension is:

$$ΣVi=(vi_{old}⋅Δvi_{new})+(Δvi_{old}⋅vi_{new})$$

This dual approach provides a detailed view of the evolution in each specific dimension, while maintaining a relative perspective, crucial for avoiding overinterpretation of data.


**Advantages of the Product Differentiation Method with Relative Dimensionality**:

1. **Depth over Breadth**: By focusing on relative changes in dimensions, this method goes deeper than traditional approaches, uncovering nuanced linguistic shifts.

2. **Adherence to Occam's Razor**: The method prioritizes simplicity and relevance, avoiding the pitfalls of overcomplicating the model with unnecessary complexity.

3. **Cultural and Societal Reflections**: The dimensional changes can be correlated with broader societal and cultural trends, offering a mirror to the evolution of language in real-world contexts.

4. **Precision in Linguistic Evolution**: It enables precise tracking of language evolution, highlighting the most dynamic aspects of linguistic representation.

**Use Case and Application**:
We present a Python script that facilitates this advanced analysis by allowing comparisons between different models' embeddings. The script computes the product differences, adhering to the principle of relative dimensionality, to ensure a focused and relevant linguistic analysis.

**Conclusion**:
This symbolic differentiation approach in word embeddings analysis, grounded in the principle of relative dimensionality and Occam's razor, provides a more refined and contextually relevant understanding of linguistic evolution. As NLP progresses, such methods will be crucial for a deeper understanding of language dynamics and their correlation with societal changes.


```python
...
def calculate_product_difference(word, model_1, model_2):
    """
    Calculate various measures of difference for a specific word in both models.
    
    :param word: The word to compare.
    :param model_1: The first word embeddings model.
    :param model_2: The second word embeddings model.
    :return: A tuple with different measures of difference including Euclidean distance.
    """
    vector_1 = model_1[word]
    vector_2 = model_2[word]
    dn = vector_2 - vector_1

    # Element-wise multiplication: (vector2 - vector1) * vector1
    elementwise_product = dn * vector_1

    # Sum of products for each dimension: ni * dni' + dni * ni'
    sum_of_products = sum(n1 * dn_i + dn_i * n2 for n1, n2, dn_i in zip(vector_1, vector_2, dn))

    # Euclidean distance
    euclidean_distance = np.linalg.norm(dn)
    
    # Cosinus Similarity
    cosine_sim = cosine_similarity([vector_1], [vector_2])[0][0]

    return elementwise_product, sum_of_products, dn, euclidean_distance, cosine_sim

...

def main(model_file_1, model_file_2, word):
    """
    ...
    elif word in model_1.key_to_index and word in model_2.key_to_index:
        elementwise_product, sum_of_products, dn, euclidean_distance, cosine_sim = calculate_product_difference(word, model_1, model_2)
        print(f"Word '{word}' has the following measures of differences:")
        print(f"Element-wise product: {elementwise_product}")
        print(f"Sum of products: {sum_of_products}")
        print(f"Vector of differences: {dn}")
        print(f"Euclidean distance: {euclidean_distance}")
        print(f"Cosine similarity: {cosine_sim}")
    else:
        print(f"Word '{word}' not found in one or both of the models.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python compare_embeddings.py <model_file_1> <model_file_2> <word or 'ALL'>")
        sys.exit(1)

    model_file_1, model_file_2, word = sys.argv[1], sys.argv[2], sys.argv[3]
    main(model_file_1, model_file_2, word)



```

Output :
```
python compare_word_embeddings.py numberbatch-en-17.02.txt numberbatch-en.txt dog
/usr/lib/python3/dist-packages/paramiko/transport.py:236: CryptographyDeprecationWarning: Blowfish has been deprecated
  "class": algorithms.Blowfish,
Word 'dog' has the following measures of differences:
Element-wise product: [-1.21075800e-02 -1.68263465e-01 -3.79206426e-02 -4.51881019e-03
  2.22551986e-03 -7.99077600e-02  2.91485991e-03 -5.16392961e-02
 -2.09007617e-02  8.43599992e-05 -2.68927985e-03 -6.20567985e-03
 -1.97144970e-03 -1.70396024e-03 -1.37359981e-04 -8.99999941e-05
 -3.26001970e-03 -5.52684069e-03  7.66499958e-04 -3.56931202e-02
 -2.30399601e-05  5.52120036e-04 -1.95703227e-02 -8.76400038e-04
 -1.88346987e-03  4.14595986e-03 -1.63836014e-02  1.50800013e-04
 -1.41470004e-02  7.70208053e-03 -2.13544406e-02 -3.33524831e-02
 -2.16412009e-03 -5.37900021e-04 -6.99540041e-03 -2.03580000e-02
  4.28823987e-03 -8.64000031e-05  2.25359967e-04 -1.29600012e-04
 -7.47300073e-05  6.85360050e-04 -3.33839969e-04  8.43499904e-04
 -6.55649987e-04 -1.01505592e-02 -9.63600003e-04 -2.20109988e-03
 -1.69623997e-02  3.90980014e-04  3.53719981e-04 -2.17342004e-03
 -2.64863996e-03 -3.41050001e-03 -6.12560078e-04  6.05359965e-04
 -2.33461009e-03  3.56039993e-04 -3.85018019e-03 -1.77974987e-03
 -3.11915996e-03  6.93000038e-05  4.28999978e-04 -2.68920034e-04
 -1.10092498e-02  3.83000006e-04 -3.48944031e-03  9.74819995e-04
  4.86325007e-03 -7.95179978e-04 -4.94935038e-03 -4.17999981e-04
  2.40784022e-03 -1.18146010e-03  2.46619980e-04 -1.87340047e-04
 -1.45180000e-03 -6.71304017e-03  4.03788034e-03 -4.41377982e-03
 -1.38689997e-03  8.12169979e-04  1.00800004e-04  1.23900012e-04
 -1.01919007e-03 -5.18714031e-03 -1.67523988e-03 -4.21199977e-04
  8.35200073e-04 -7.40459946e-04 -3.01697967e-03 -1.33086601e-02
 -3.58609972e-03 -7.27079995e-03  1.61086000e-03 -1.57780002e-03
 -4.06745961e-03 -1.42479956e-04 -3.78810015e-04  2.79390049e-04
  5.24399977e-04 -1.07847992e-03 -2.30496004e-03 -4.73989989e-04
 -1.69506005e-03 -9.02496092e-03 -6.56249980e-03 -2.21340000e-04
 -1.76040063e-04  3.25351022e-03  5.05631976e-03 -2.52648001e-03
 -4.67500044e-03 -1.03390007e-03 -3.66336037e-03  2.25163996e-03
 -2.06941017e-03 -2.06479992e-04  5.05960023e-04 -1.49822992e-03
  2.01939000e-03 -1.86221988e-03 -2.87039997e-03  8.69399984e-04
 -1.04394015e-02 -6.55650103e-04  1.24080013e-03  2.91809993e-04
 -1.82521995e-03 -4.50468017e-03 -5.37683954e-03 -2.24000006e-03
  1.51000000e-04 -1.83862001e-02  2.65649986e-04 -8.29040073e-04
 -7.53480068e-04 -6.55608019e-03  3.16000041e-05 -1.29172008e-03
 -8.35450017e-04 -1.57994009e-03 -3.25889851e-04  5.03999996e-04
 -1.37215992e-03 -8.68530013e-04 -4.62400058e-04  1.33400012e-04
 -6.38808031e-03 -4.16500006e-05 -5.62799905e-05  2.42218003e-03
  8.06650205e-04  4.14959999e-04 -1.47865200e-02 -2.10552011e-03
 -1.00479992e-04 -7.02048047e-03 -2.32530001e-04 -1.66604994e-03
 -1.64551998e-03 -2.13347981e-03 -1.13750000e-04 -1.42408786e-02
  5.38021000e-03 -7.42949964e-03  2.14829997e-04 -2.42897007e-03
 -6.92489964e-04  4.51338990e-03 -1.52604003e-03 -1.38693489e-02
 -1.02480015e-04 -7.86600052e-04  4.78920003e-04 -1.24888001e-02
 -9.00900108e-04 -4.92960028e-03 -7.19910080e-04 -2.76920013e-03
 -9.13836062e-03 -3.37604992e-03  3.93962068e-03 -8.02255049e-03
 -1.62525999e-03 -3.39920982e-03 -2.51921988e-03 -1.07159989e-03
 -2.63191992e-03 -2.94440007e-03  4.66200028e-04 -9.75492038e-03
 -2.70900025e-04 -2.24400009e-03 -1.73619005e-03 -2.19000014e-03
 -8.88536032e-03  2.31079990e-04 -1.48371002e-03  7.70799888e-05
 -2.74559978e-04 -2.67652003e-03 -7.73009961e-04 -6.35060016e-04
  1.04400006e-05 -4.86096041e-03  8.35999981e-06 -1.57051987e-03
 -3.88442981e-03  8.50200013e-05 -1.29579997e-03 -4.94000005e-06
 -1.72672002e-03  7.12140056e-04 -2.27765995e-03  3.39479971e-04
 -1.61539996e-04  1.07330992e-03 -8.28950026e-04 -4.91660030e-04
 -1.93433999e-03 -5.40581997e-03 -7.94419961e-04 -6.97500072e-04
 -1.18469994e-03 -5.19349985e-03 -1.00759999e-03 -1.89660001e-04
 -1.04880004e-04 -2.97387992e-03 -3.10167996e-03  3.09599971e-04
 -5.62700036e-04  9.50001868e-06 -1.35303009e-03 -4.59888019e-03
 -1.00239959e-04 -5.46000010e-05 -5.31187048e-03 -1.75277994e-03
  5.54400540e-05 -2.25179989e-04  5.41970017e-04 -1.44672999e-03
 -2.07479985e-04 -3.50480014e-03 -1.31175003e-03 -3.84400046e-05
 -9.77599993e-05 -2.21439972e-04  1.06000016e-05 -7.16799987e-05
 -6.44095987e-03 -4.77599027e-03 -8.17959895e-04  6.11200012e-05
 -5.57599997e-05 -2.34599982e-04 -4.78335004e-03 -2.80559971e-03
 -2.81970017e-03 -2.19912012e-03 -4.46960982e-03 -1.32559007e-03
 -2.33016023e-03 -4.25990019e-03 -1.27199979e-04 -5.76912053e-03
 -6.87959953e-04  6.34879980e-04 -1.56499003e-03 -6.41016010e-03
  1.50399746e-05 -3.22529022e-03 -1.20559998e-04 -5.85660047e-04
 -1.07256998e-03 -2.54747993e-03  4.96799985e-05 -6.16664998e-03
 -7.95000014e-05 -3.22498986e-03 -9.79452860e-03 -1.95000001e-04
 -4.48800020e-05 -1.95077993e-03  1.34640009e-04 -1.08952995e-03
 -2.74380029e-04 -3.00299926e-05 -4.02599981e-05 -3.43220017e-04
 -6.64200052e-04 -7.90824089e-03 -2.16030004e-03 -1.04999985e-04
  2.54179991e-04 -4.36478993e-03 -5.42640046e-04 -1.38600135e-05]
Sum of products: -0.00024688214352863724
Vector of differences: [ 1.08199999e-01 -4.16700006e-01  3.08800012e-01  5.31000011e-02
 -5.61999977e-02  3.20400000e-01 -4.80999984e-02 -2.85299987e-01
 -1.23600006e-01 -1.10999998e-02 -7.63999969e-02  2.02799991e-01
  3.36999968e-02  1.64000019e-02  6.79999962e-03 -1.99999996e-02
 -3.72999981e-02 -6.36000037e-02 -3.64999995e-02 -2.27200001e-01
  8.99998471e-04 -4.28000018e-02  1.41200006e-01 -3.13000008e-02
 -4.30999994e-02 -1.13899991e-01 -1.51700005e-01 -2.60000024e-02
  1.64499998e-01  9.04000103e-02  2.37800002e-01 -2.14900002e-01
 -9.17000026e-02  1.09999999e-02 -7.86000043e-02  1.94999993e-01
 -8.85999948e-02  1.79999992e-02  7.19999894e-03 -1.35000004e-02
 -5.30000031e-03  6.59000054e-02  1.03999991e-02 -3.49999964e-02
  7.05000013e-02  1.36799991e-01 -6.59999996e-02  8.69999975e-02
  1.81999996e-01  2.26000007e-02  2.38999985e-02 -8.02000016e-02
 -7.11999983e-02 -4.74999994e-02 -1.24000013e-02  6.43999949e-02
  4.43000011e-02 -1.37999989e-02  6.22000024e-02  1.69499993e-01
  4.16999981e-02  3.30000035e-02 -5.49999997e-02 -8.30000080e-03
 -1.16499998e-01 -3.83000001e-02  1.80800006e-01 -4.61999997e-02
  1.22500002e-01  4.56999987e-02 -8.95000026e-02  1.89999994e-02
 -2.98000053e-02  6.79000020e-02  1.29799992e-01 -3.80000100e-03
  5.95000014e-02  1.34800002e-01  1.25400007e-01 -6.50999993e-02
 -6.89999983e-02  2.40999982e-02 -2.52000000e-02 -4.13000025e-02
 -6.40999973e-02  9.38000008e-02  1.92999989e-02 -1.16999999e-01
  8.70000049e-02 -9.02999938e-02  6.65999949e-02 -1.38200000e-01
  6.57999963e-02 -1.09499998e-01  6.74000010e-02  8.04999992e-02
  1.14899993e-01 -2.59999931e-03  2.07000002e-02 -1.39000025e-02
  1.89999994e-02  2.20999997e-02  7.84000009e-02  3.40999998e-02
  6.57000020e-02 -1.63200006e-01  1.25000000e-01 -5.27000017e-02
  3.60000134e-03 -8.63000005e-02  6.86999932e-02 -7.25999996e-02
  9.35000032e-02  1.05500005e-01 -1.69600010e-01 -6.21999949e-02
  6.28999993e-02 -8.89999978e-03  1.82000007e-02  5.37000000e-02
  8.11000019e-02 -2.45999992e-02  6.89999983e-02  6.30000010e-02
  8.22000057e-02  1.55000016e-02  7.52000064e-02  2.12999992e-02
  6.93999976e-02 -7.73999989e-02  1.03599995e-01 -3.20000015e-02
 -3.02000009e-02  1.60999998e-01 -2.52999999e-02 -2.41000019e-02
 -4.68000025e-02  9.26000029e-02 -3.16000022e-02 -7.51000047e-02
 -5.39000034e-02 -3.94000001e-02 -7.09999725e-03 -4.80000004e-02
  5.11999987e-02 -3.93000022e-02 -2.72000022e-02 -9.20000114e-03
 -1.03200004e-01  1.19000003e-02 -4.19999938e-03 -7.42999986e-02
  8.50000232e-03  1.09200001e-01 -1.21399999e-01 -7.44000003e-02
 -3.13999988e-02 -8.52000043e-02 -3.37000005e-02  4.34999987e-02
  6.14000000e-02 -2.75999978e-02  1.75000001e-02 -1.36799991e-01
 -8.28999951e-02  9.74999964e-02  2.30999999e-02  8.29000026e-02
  5.62999994e-02 -1.05699994e-01 -4.71000001e-02 -1.83699995e-01
  5.60000073e-03  4.60000001e-02 -3.07000019e-02  1.34000003e-01
  4.95000035e-02  6.32000044e-02  1.26300007e-01 -9.89000052e-02
 -9.46000069e-02 -1.06500000e-01 -5.62000051e-02 -1.40500009e-01
 -6.57999963e-02 -6.32999986e-02 -3.46999988e-02 -2.84999982e-02
  3.33999991e-02 -6.80000037e-02  1.48000009e-02 -1.10600002e-01
  6.30000010e-02 -6.59999996e-02  5.73000014e-02  4.38000001e-02
  1.01199999e-01 -2.11999994e-02  3.61000001e-02  4.69999947e-03
 -1.75999999e-02  4.83999997e-02 -4.08999994e-02 -5.62000014e-02
 -8.70000012e-03 -6.56000003e-02 -2.19999999e-03  4.96999994e-02
  8.68999958e-02  7.79999979e-03 -3.79999988e-02  3.80000006e-03
  3.04000005e-02  4.29000035e-02 -6.08999990e-02 -1.63999982e-02
 -3.94000001e-02 -3.98999974e-02  2.95000002e-02  7.93000013e-02
 -6.26000017e-02 -1.26599997e-01 -3.13999988e-02  1.50000006e-02
 -1.07699998e-01  8.50000009e-02 -4.39999998e-02 -8.70000012e-03
  1.84000004e-02 -5.31999990e-02 -5.66000007e-02 -1.19999982e-02
 -1.70000009e-02 -5.00001013e-04  3.79000008e-02 -4.02000025e-02
 -2.79999897e-03  5.20000001e-03  8.21000040e-02  4.45999987e-02
  1.40000135e-03 -4.16999981e-02  1.42999999e-02 -7.27000013e-02
  1.32999998e-02  5.20000011e-02 -7.95000046e-02  3.10000032e-03
  7.51999989e-02 -1.72999986e-02  1.00000016e-03 -5.59999980e-03
 -1.08800001e-01  1.10300004e-01  2.41999980e-02  3.20000015e-03
 -6.80000009e-03  4.59999964e-03 -7.15000033e-02 -4.19999957e-02
  7.23000020e-02 -4.61999997e-02 -1.14899993e-01  6.53000027e-02
 -5.84000014e-02 -1.03900000e-01 -4.79999930e-03 -7.07000047e-02
 -1.81999989e-02  2.55999994e-02  2.83000004e-02 -1.04400001e-01
 -3.99999321e-04  8.51000026e-02 -1.37000000e-02  2.58000009e-02
  3.79000008e-02 -4.25999984e-02 -1.83999985e-02 -8.38999972e-02
 -2.64999997e-02 -6.18999973e-02 -1.19299993e-01  3.90000008e-02
  8.79999995e-03 -7.93000013e-02  4.08000015e-02  4.93000001e-02
  2.69000009e-02  1.29999965e-03  6.59999996e-03  2.62000002e-02
 -3.24000008e-02  9.96000022e-02  5.70000000e-02 -3.49999964e-03
  1.78999994e-02 -8.41000006e-02 -1.52000003e-02  7.00000674e-04]
Euclidean distance: 1.442521333694458
Cosine similarity: -0.04044608771800995
```
