import unittest

from modules.clipboard_editor import KindleEditor


class TestKindleEditor(unittest.TestCase):

    def test_is_kindle_true(self):
        # 改行あり
        kindle_data_nl = """
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) ​class UStaticMeshComponent* MeshComponent;

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p.197). Kindle 版. 
        """
        actual = KindleEditor.is_kindle(kindle_data_nl)
        self.assertTrue(actual)
        # 改行なし
        kindle_data_nonl = """
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true"))

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p.197). Kindle 版. """
        actual = KindleEditor.is_kindle(kindle_data_nonl)
        self.assertTrue(actual)
        # 他の本
        kindle_data_otherbook = """
Don’t Comment Bad Names — Fix the Names Instead

Boswell, Dustin; Foucher, Trevor. The Art of Readable Code: Simple and Practical Techniques for Writing Better Code (English Edition) (p.80). O'Reilly Media. Kindle 版. 
"""
        actual = KindleEditor.is_kindle(kindle_data_otherbook)
        self.assertTrue(actual)

    def test_is_kindle_false(self):
        # 改行あり
        kindle_data_nl = """
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) ​class UStaticMeshComponent* MeshComponent;

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p.). Kindle 版. 
        """
        actual = KindleEditor.is_kindle(kindle_data_nl)
        self.assertFalse(actual)
        # 改行なし
        kindle_data_nonl = """
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true"))

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p197). Kindle 版. """
        actual = KindleEditor.is_kindle(kindle_data_nonl)
        self.assertFalse(actual)
        # 他の本
        kindle_data_otherbook = """
Don’t Comment Bad Names — Fix the Names Instead

Boswell, Dustin; Foucher, Trevor. The Art of Readable Code: Simple and Practical Techniques for Writing Better Code (English Edition) (p.80) O'Reilly Media. Kindle 版. 
"""
        actual = KindleEditor.is_kindle(kindle_data_otherbook)
        self.assertFalse(actual)

    def test_modify_clipboard(self):
        data = """UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) ​class UStaticMeshComponent* MeshComponent;

Ulibarri, Stephen. Unreal Engine C++ the Ultimate Developer's Handbook: Learn C++ and Unreal Engine by Creating a Complete Action Game (English Edition) (p.197). Kindle 版. """
        expect = """UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = Camera, meta = (AllowPrivateAccess = "true")) \r\nclass UStaticMeshComponent* MeshComponent;"""
        res = KindleEditor.modify_clipboard(data)
        self.assertEqual(expect, res)
