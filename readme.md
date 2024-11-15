商品検索・リンク生成アプリ
概要
このアプリは、Firebase Realtime DatabaseとAuthenticationを活用し、ユーザーがログイン後に商品名を検索して該当する商品の情報（商品名と商品ID）を取得し、メルカリの該当商品ページへのリンクを生成・表示するデスクトップアプリです。

閲覧専用：データの変更・追加・削除はできません。
リンク生成機能：商品IDを元にメルカリの該当商品ページリンクを生成します。
使用技術
言語: Python
UIライブラリ: PyQt5 / PySide6（UI構築）
データベース: Firebase Realtime Database
認証: Firebase Authentication
通信ライブラリ:
firebase-admin（セキュリティに優れたサーバーサイド操作向け）
または pyrebase（クライアント向けで簡単に実装可能）
ブラウザ操作:
Python標準のwebbrowserライブラリ
機能
1. ユーザー認証
ログイン機能:
Firebase Authenticationを利用して、登録済みのメールアドレスとパスワードで認証。
認証済みトークンを利用してセキュアにデータベースへアクセス。
新規登録制限:
新規登録は運営側が実施するため、アプリUI上では新規登録機能を提供しない。
2. 商品検索とリンク生成
検索機能:
商品名（item_name）を入力して検索ボタンを押すと、Firebase Realtime Database内で一致するデータを検索。
検索結果表示:
以下の情報をリスト形式で表示：
商品名（item_name）
商品ID（item_id）
メルカリの商品ページリンク
リンク生成:
商品IDを元に以下の形式でリンクを生成：
ruby
コードをコピーする
https://www.mercari.com/jp/items/{item_id}
リンク表示:
リスト内のリンクをクリックすると、ブラウザで該当商品ページが開く。
非機能要件
セキュリティ
Firebase Authenticationで認証済みユーザーのみがデータにアクセス可能。
Firebase Realtime Databaseのセキュリティルールを設定してデータ保護を実現。
パフォーマンス
必要なデータ（item_nameフィールド）のみをクエリで取得。
過剰な通信を防ぎ、効率的に検索処理を実行。
クロスプラットフォーム対応
対応OS:
Windows
macOS
Linux
開発手順
環境セットアップ
Pythonのインストール:
推奨バージョン: Python 3.9以上
必要ライブラリのインストール:
以下のコマンドを実行：
bash
コードをコピーする
pip install pyqt5 pyrebase4 firebase-admin webbrowser
Firebaseプロジェクトの作成:
Firebaseコンソールでプロジェクトを作成。
AuthenticationとRealtime Databaseを有効化。
サービスアカウントキー（JSONファイル）をダウンロード。
開発の流れ
UI設計:
ログイン画面、検索画面、結果表示画面をPyQt Designerで設計。
Firebase認証の実装:
メールアドレスとパスワードによるログイン機能を追加。
検索機能の実装:
Firebase Databaseクエリ（orderByChildとequalTo）で商品名を検索。
リンク生成機能の追加:
商品IDを元にメルカリ商品ページリンクを生成・表示。
テストとデバッグ:
ログイン、検索、リンク生成機能を個別にテスト。
セキュリティルールの検証。
デプロイと配布
実行ファイルの生成:
pyinstallerでアプリを実行ファイル化：
bash
コードをコピーする
pyinstaller --onefile --windowed main.py
配布:
必要ファイルをまとめて配布。
使用方法
アプリを起動します。
メールアドレスとパスワードを入力してログインします。
商品名を入力して「検索」ボタンをクリックします。
一致する商品のリストが表示され、各商品のメルカリリンクをクリックしてブラウザで開けます。
