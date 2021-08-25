# Neural Machine Translation and Experimentation
The concatenated dataset for backtranslation was added to the dataset.  In the data folder, there are two augmented files.

`train.backtranslated.en`: augmented english corpus

`train.backtranslated.fr`: doubled french corpus

Additional parameter was added for training: `--attention`.
Available values for this flag is: `multiplicative`, `additive`, `dot`, `scaled_dot`, `additive`.

The best model for training was the scaled dot product attention, and it can be trained by the command below.
```
python main.py --mode train --model_path mh_model_scaled_dot_back.bin --cuda --hidden_size 128 --train_src data/train.backtranslated.fr --train_tgt data/train.backtranslated.en
```

Two folders `p1` and `p2` are folders containing results for problem 1 and problem 2.  P1 folder contains the baseline implementation and baseline results.  P2 folder contains various types of attention models and the best model, which was scaled dot product attention with back translation.
