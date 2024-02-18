# あばうと
Kindleからサンプルコードをコピるときに引用とか改行がゼロ幅スペースになるのがイライラするので作りました。  

**完全にWindows向けに調整しているので他のOSだと使えません。**

# つかいかた
pythonで立ち上げるだけ。rootにある"modify_kindle_clipBoard.py"を実行する。  
終了するときはCtrl+Cで終了してください。
pipでpywin32は入れといてください。

# しょりないよう
1秒ごとにクリップボードの値を見て、Kindleからの引用テキストならフォーマット変換を行います。

# 例
## 変換前
/** Mesh component to give the Pawn a visual representation in the world */ ​UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) ​class UStaticMeshComponent* MeshComponent;

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p.197). Kindle 版. 
## 変換後(\r\nなので表現できてないが、改行も追加されている。)
/** Mesh component to give the Pawn a visual representation in the world */ 
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) 
class UStaticMeshComponent* MeshComponent;

## テスト
```
python -m unittest
```