# PrimeKG — Comprehensive Data Dictionary & Sample Heads

This document explains every major CSV in PrimeKG, lists **all columns**, and shows the first 5 rows for each file.

---

## `nodes.csv`

### Column Definitions

| Column | Description |
|---|---|
| **node_index** | Graph index used in edge lists |
| **node_id** | External ID (NCBI Gene, MONDO Disease, DrugBank, etc.) |
| **node_type** | Entity type (gene/protein, disease, drug, ...) |
| **node_name** | Human‑readable label |
| **node_source** | Origin database |

### Sample Head (first 5 rows)

```text
node_index node_id     node_type node_name node_source
0           0    9796  gene/protein    PHYHIP        NCBI
1           1    7918  gene/protein    GPANK1        NCBI
2           2    8233  gene/protein     ZRSR2        NCBI
3           3    4899  gene/protein      NRF1        NCBI
4           4    5297  gene/protein     PI4KA        NCBI
```

---

## `edges.csv`

### Column Definitions

| Column | Description |
|---|---|
| **relation** | Relation type |
| **display_relation** | Short alias |
| **x_index** | Source node index |
| **y_index** | Target node index |

### Sample Head (first 5 rows)

```text
relation display_relation  x_index  y_index
0  protein_protein              ppi        0     8889
1  protein_protein              ppi        1     2798
2  protein_protein              ppi        2     5646
3  protein_protein              ppi        3    11592
4  protein_protein              ppi        4     2122
```

---

## `kg.csv`

### Column Definitions

| Column | Description |
|---|---|
| **relation** | Edge type |
| **display_relation** | Alias |
| **x_index** | Source node index |
| **x_id** | Source external ID |
| **x_type** | Source type |
| **x_name** | Source name |
| **x_source** | Source DB |
| **y_index** | Target node index |
| **y_id** | Target external ID |
| **y_type** | Target type |
| **y_name** | Target name |
| **y_source** | Target DB |

### Sample Head (first 5 rows)

```text
relation display_relation  x_index  x_id        x_type  x_name x_source  y_index   y_id        y_type  y_name y_source
0  protein_protein              ppi        0  9796  gene/protein  PHYHIP     NCBI     8889  56992  gene/protein   KIF15     NCBI
1  protein_protein              ppi        1  7918  gene/protein  GPANK1     NCBI     2798   9240  gene/protein   PNMA1     NCBI
2  protein_protein              ppi        2  8233  gene/protein   ZRSR2     NCBI     5646  23548  gene/protein   TTC33     NCBI
3  protein_protein              ppi        3  4899  gene/protein    NRF1     NCBI    11592  11253  gene/protein  MAN1B1     NCBI
4  protein_protein              ppi        4  5297  gene/protein   PI4KA     NCBI     2122   8601  gene/protein   RGS20     NCBI
```

---

## `disease_features.csv`

### Column Definitions

| Column | Description |
|---|---|
| **node_index** | Links to nodes.csv |
| **mondo_id** | MONDO disease ID |
| **mondo_name** | Disease name |
| **mondo_definition** | Definition from MONDO |
| **umls_description** | UMLS description |
| **orphanet_definition** | Rare‑disease definition |

### Sample Head (first 5 rows)

```text
node_index                                  mondo_name                           mondo_definition
0       27165  mullerian aplasia and hyperandrogenism  Deficiency of the glycoprotein WNT4...
1       27165  mullerian aplasia and hyperandrogenism  Deficiency of the glycoprotein WNT4...
2       27166  myelodysplasia, immunodeficiency...     <NA>
3       27168  bone dysplasia, lethal Holmgren type    Bone dysplasia lethal Holmgren type...
4       27169  predisposition to invasive fungal...    <NA>
```

---

## `drug_features.csv`

### Column Definitions

| Column | Description |
|---|---|
| **node_index** | Links to nodes.csv |
| **description** | Drug summary |
| **indication** | Approved use |
| **mechanism_of_action** | Pharmacological MoA |
| **pharmacodynamics** | Effects in body |

### Sample Head (first 5 rows)

```text
node_index               description                       indication
0       14012  Copper is a transition metal...   Parenteral nutrition supplement
1       14013  Oxygen element...               Oxygen therapy
2       14014  Flunisolide corticosteroid...    Maintenance treatment of asthma
3       14015  Alclometasone steroid...         Relief of inflammatory dermatoses
4       14016  Medrysone corticosteroid...      Treatment of allergic conjunctivitis
```

---

## `kg_raw.csv` / `kg_giant.csv` / `kg_grouped.csv` — Edge Variants

### Column Definitions

| Column | Description |
|---|---|
| **relation** | Edge type |
| **display_relation** | Alias |
| **x_id** | Source external ID |
| **x_type** | Source type |
| **x_name** | Source name |
| **x_source** | Source DB |
| **y_id** | Target external ID |
| **y_type** | Target type |
| **y_name** | Target name |
| **y_source** | Target DB |

### Sample Head (first 5 rows)

```text
relation display_relation  x_id        x_type  x_name x_source  y_id        y_type  y_name y_source
0  protein_protein              ppi  9796  gene/protein  PHYHIP     NCBI  56992  gene/protein   KIF15     NCBI
1  protein_protein              ppi  7918  gene/protein  GPANK1     NCBI   9240  gene/protein   PNMA1     NCBI
2  protein_protein              ppi  8233  gene/protein   ZRSR2     NCBI  23548  gene/protein   TTC33     NCBI
3  protein_protein              ppi  4899  gene/protein    NRF1     NCBI  11253  gene/protein  MAN1B1     NCBI
4  protein_protein              ppi  5297  gene/protein   PI4KA     NCBI   8601  gene/protein   RGS20     NCBI
```

---

## `kg_grouped_diseases.csv`

### Column Definitions

| Column | Description |
|---|---|
| **node_id** | Disease node ID |
| **node_type** | Always 'disease' |
| **node_name** | Disease name |
| **group_name_auto** | Auto string‑match group |
| **group_name_bert** | BERT embedding group |

### Sample Head (first 5 rows)

```text
node_id node_name                                  group_name_auto
0    13924 osteogenesis imperfecta type 13            osteogenesis imperfecta
1    11160 autosomal recessive nonsyndromic deafness  autosomal recessive nonsyndromic deafness
2     8099 congenital stationary night blindness ...  congenital stationary night blindness ...
```

---

## `kg_grouped_diseases_bert_map.csv`

### Column Definitions

| Column | Description |
|---|---|
| **node_id** | Disease node ID |
| **node_type** | Always 'disease' |
| **node_name** | Disease name |
| **group_name_auto** | Auto string‑match group |
| **group_name_bert** | BERT embedding group |
| **group_id_bert** | ID listing all diseases in the BERT cluster |

### Sample Head (first 5 rows)

```text
node_id node_name                        group_name_auto          group_name_bert           group_id_bert
0    13924 osteogenesis imperfecta type 13  osteogenesis imperfecta  osteogenesis imperfecta  13924_12592_...
1    12592 osteogenesis imperfecta type 11  osteogenesis imperfecta  osteogenesis imperfecta  13924_12592_...
```

---

_Generated: 2025‑06‑11_
