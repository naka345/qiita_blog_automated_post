[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# qiita_blog_automated_post
qiita記事をgitで管理して自動で投稿したい

1. github repo更新検知
1. docker hub automated build 起動
1. qiita API auth (サーバー起動)
1. 差分確認 & qiita更新
1. コンテナ削除処理

## uwsgi
macOS用

```
pip install uwsgi -Iv
```
