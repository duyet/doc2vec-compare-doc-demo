# Demo for compare Doc using Doc2vec

# Install 

1. Install requirement package

```
pip install -r requirements.txt
````

2. Start server 

```
python app.py
```

3. Visit **[http://localhost:8088](http://localhost:8088)**

# Screenshot

1. Compare two document
	![](.screenshot/compare_2.png)

2. Compare document with documents in database
![](.screenshot/compare_all.png)

# Improvement

To improve the model, add more data to `data/` folder (tokenized, suggest using vnTokenizer).
Update model by browsing to **[http://localhost:8088/api/train_model](http://localhost:8088/api/train_model)**