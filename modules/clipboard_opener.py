import win32clipboard


class OpenClipboard:

    def __enter__(self):
        win32clipboard.OpenClipboard()

    def __exit__(self, exc_type, exc_value, traceback):
        win32clipboard.CloseClipboard()
