import re


class KindleEditor:
    """キンドル用のコピー内容変更クラス"""

    @staticmethod
    def is_kindle(content: str) -> bool:
        """コンテントがキンドルのテキストか判定する。"""
        regex = r".*\(pp?\.\d+-?\d*\)\..*"  # (p.nnn). or (pp.nnn-nnn)に対応 nは1桁以上の(数値|-)
        return bool(re.match(regex, content, re.DOTALL))

    @staticmethod
    def modify_clipboard(content: str):
        """テキストの変換処理"""
        invalid_nl = "\u200b"  # 改行が0幅スペースになるので置き換える
        lines = content.replace(invalid_nl, "\n").splitlines()
        return "\r\n".join(lines[:-2])  # 最後の2行は引用なので削除
