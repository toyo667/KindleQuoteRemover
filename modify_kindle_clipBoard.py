import win32clipboard
import time
from modules.clipboard_editor import KindleEditor
import traceback
from modules.clipboard_opener import OpenClipboard

CLIPBOARD_CHECK_INTERVAL_SEC = 1


def clipboard_listener():
    recent_value = ""
    while True:
        try:
            recent_value = edit_clipboard(recent_value)
        except Exception as e:
            # 偶にクリップボード開けなくなる
            print(e)

        time.sleep(CLIPBOARD_CHECK_INTERVAL_SEC)


def set_clipboard(content: str):
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(content, win32clipboard.CF_UNICODETEXT)


def edit_clipboard(recent_value: str) -> str:
    """クリップボードの値を修正する。

    Args:
        recent_value (str): 直近の値

    Returns:
        str: 変更のある場合はその値、ない場合は引数の値
    """
    with OpenClipboard():
        clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)

        if clipboard_data != recent_value and KindleEditor.is_kindle(clipboard_data):
            print("*" * 30 + " Convert " + "*" * 30)
            modified_content = KindleEditor.modify_clipboard(clipboard_data)  # クリップボード変換処理
            set_clipboard(modified_content)
            recent_value = modified_content

            print("Clipboard content modified: ", modified_content)

    return recent_value


if __name__ == "__main__":
    try:
        clipboard_listener()
    except Exception:
        with open("./err_trace.txt", "w") as f:
            f.write(traceback.format_exc())
