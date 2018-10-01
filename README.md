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
text.pyの13~17行目を適宜変更してください  
当方垢が3つあるため3つ開いています。  
  
  
$ python3 Main.py