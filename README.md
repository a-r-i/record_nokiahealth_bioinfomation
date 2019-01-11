# description

アイドルの生体情報をNokia Sleep&Body+で計測し毎日ツイートする  
https://qiita.com/a-r-i/items/288496f47f279445a35b

上記企画で使用したプログラム

1. Nokia Sleep&Body+で計測した生体情報を、Nokia Health APIから取得(main.py, nokiahealthapi.py)
1. 1で取得した生体情報を、自前のデータベースに登録するため、自前のAPIにPOST(main.py, myapi.py)
1. Nokia Health APIにアクセスするためのアクセストークンを更新(refresh_accesstoken.py)

本プログラムで取得→登録した生体情報をツイートするプログラムはこちら  
https://github.com/a-r-i/tweet_nokiahealth_bioinfomation