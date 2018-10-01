ツイッターから提供される全ツイート履歴のcsvからツイートを生成します  
  
MeCab  
pandas  

# 使い方
keys.pyを作成  

```
keys = [
    [
        consumerkey,
        consumersecret,
        accesstoken,
        tokensecret
    ]

    (複数垢あればいくつでも)

]
```

ツイッターからcsvをDL  
  
  
$ python3 Main.py