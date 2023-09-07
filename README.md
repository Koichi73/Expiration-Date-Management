# Rakuten Intern Team-7

- データをcsvから読み込むために
    ```
    -- SQLite

    .separator ,
    .import //Users//wadashouki//楽天//foods_data.csv foods
    ```

    を実行してください。
    ただし、//Users//wadashouki//楽天//foods_data.csv はcsvファイルの絶対パスを指定してください。

- req.txtをインストールしてください。
    辞書の表記がありませんがインストールの必要があるかもしれません。
    その場合はreq.txtに ``` ipadic==1.0.0 ```　を追加してください。

- 今回はトークナイザ("私はご飯が好きです" -> ["私", "は", "ご飯", "が", "好き", "です"]のようにするものです。)に、janomeを利用しています。(インストールがおそらく一番簡単)
    なので、BERTなどを利用するよりトークナイズの精度が劣っている可能性があります。
    精度はMeCabと同程度(一般的に使われている)で、速度はMeCabの10倍遅いです。
