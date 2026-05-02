"""
Sesi 12 — AVL Tree (Complete Implementation)
Handout untuk mahasiswa setelah sesi

Referensi:
- https://visualgo.net/en/bst  (mode AVL untuk verifikasi visual)
- Goodrich et al., Data Structures and Algorithms in Python, Ch. 11

Konvensi:
- height of leaf = 0
- height of empty (None) = -1
- Balance Factor = height(kiri) - height(kanan)
- Valid AVL: BF ∈ {-1, 0, +1}
"""


# =============================================
# BAGIAN 1 — Node Class
# =============================================

class AVLNode:
    """Node untuk AVL Tree. Sama seperti BST Node, tambah atribut height."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0  # node baru = leaf → height 0

    def __repr__(self):
        return f"AVLNode({self.key}, h={self.height})"


# =============================================
# BAGIAN 2 — AVL Tree Class
# =============================================

class AVLTree:
    """Self-balancing Binary Search Tree."""

    def __init__(self):
        self.root = None

    # -------------------------------------------
    # Helper methods
    # -------------------------------------------

    def get_height(self, node):
        """Return height dari node. Empty tree = -1."""
        if node is None:
            return -1
        return node.height

    def get_balance_factor(self, node):
        """BF = height(kiri) - height(kanan)"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        """Update height node = 1 + max(height anak-anaknya)."""
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    # -------------------------------------------
    # Rotasi — 2 Primitif
    # -------------------------------------------

    def right_rotate(self, y):
        r"""
        Right rotation untuk kasus LL.

            y                x
           / \              / \
          x   T3    →      z   y
         / \                  / \
        z   T2               T2  T3

        Return: root baru (x)
        """
        x = y.left
        T2 = x.right

        # Lakukan rotasi
        x.right = y
        y.left = T2

        # Update height (urutan penting: y dulu karena sekarang anak dari x)
        self.update_height(y)
        self.update_height(x)

        # Return root baru
        return x

    def left_rotate(self, x):
        r"""
        Left rotation untuk kasus RR (mirror dari right_rotate).

          x                    y
         / \                  / \
        T1  y        →       x   z
           / \              / \
          T2  z            T1  T2

        Return: root baru (y)
        """
        y = x.right
        T2 = y.left

        # Lakukan rotasi
        y.left = x
        x.right = T2

        # Update height
        self.update_height(x)
        self.update_height(y)

        return y

    # -------------------------------------------
    # Insert dengan rebalancing
    # -------------------------------------------

    def insert(self, key):
        """Public interface."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Recursive insert dengan rebalancing.

        Langkah:
        1. Standard BST insert
        2. Update height node
        3. Hitung balance factor
        4. Deteksi 4 kasus violation & lakukan rotasi
        """

        # -------- Langkah 1: BST insert biasa --------
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # Duplicate key — tidak di-insert (bisa juga raise error sesuai kebutuhan)
            return node

        # -------- Langkah 2: Update height --------
        self.update_height(node)

        # -------- Langkah 3: Hitung balance factor --------
        bf = self.get_balance_factor(node)

        # -------- Langkah 4: Deteksi kasus & rotasi --------

        # Kasus LL: kiri heavy, key dimasukkan di kiri-nya kiri
        if bf > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Kasus RR: kanan heavy, key dimasukkan di kanan-nya kanan
        if bf < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Kasus LR: kiri heavy, tapi key dimasukkan di kanan-nya kiri
        # Fix: rotasi kiri dulu pada anak kiri, lalu rotasi kanan pada node
        if bf > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Kasus RL: kanan heavy, tapi key dimasukkan di kiri-nya kanan
        # Fix: rotasi kanan dulu pada anak kanan, lalu rotasi kiri pada node
        if bf < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Tidak ada violation — return node apa adanya
        return node

    # -------------------------------------------
    # Search (sama seperti BST biasa)
    # -------------------------------------------

    def search(self, key):
        """Return True kalau key ditemukan."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # -------------------------------------------
    # Traversal
    # -------------------------------------------

    def inorder(self):
        """In-order traversal → return list berurut."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    # -------------------------------------------
    # Print tree (untuk debugging & visualisasi)
    # -------------------------------------------

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print tree secara visual. Berguna untuk debug."""
        if node is None and level == 0:
            node = self.root
        if node is not None:
            bf = self.get_balance_factor(node)
            print(" " * (level * 4) + prefix + str(node.key) +
                  f"  (h={node.height}, BF={bf})")
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# =============================================
# TEST — Semua 4 Kasus
# =============================================

def test_case_LL():
    """Kasus LL: insert 3, 2, 1 → harus rotasi kanan di node 3."""
    print("\n=== KASUS LL (insert: 3, 2, 1) ===")
    tree = AVLTree()
    for key in [3, 2, 1]:
        tree.insert(key)
    tree.print_tree()
    # Expected: root = 2, kiri = 1, kanan = 3


def test_case_RR():
    """Kasus RR: insert 1, 2, 3 → harus rotasi kiri di node 1."""
    print("\n=== KASUS RR (insert: 1, 2, 3) ===")
    tree = AVLTree()
    for key in [1, 2, 3]:
        tree.insert(key)
    tree.print_tree()
    # Expected: root = 2, kiri = 1, kanan = 3


def test_case_LR():
    """Kasus LR: insert 3, 1, 2 → rotasi kiri di 1, lalu kanan di 3."""
    print("\n=== KASUS LR (insert: 3, 1, 2) ===")
    tree = AVLTree()
    for key in [3, 1, 2]:
        tree.insert(key)
    tree.print_tree()
    # Expected: root = 2, kiri = 1, kanan = 3


def test_case_RL():
    """Kasus RL: insert 1, 3, 2 → rotasi kanan di 3, lalu kiri di 1."""
    print("\n=== KASUS RL (insert: 1, 3, 2) ===")
    tree = AVLTree()
    for key in [1, 3, 2]:
        tree.insert(key)
    tree.print_tree()
    # Expected: root = 2, kiri = 1, kanan = 3


def test_tugas_mandiri():
    """
    Verifikasi jawaban task mandiri sesi 12:
    Insert 30, 20, 40, 10, 25, 5 → seharusnya ada violation LL di node 30.
    """
    print("\n=== TASK MANDIRI (insert: 30, 20, 40, 10, 25, 5) ===")
    tree = AVLTree()
    for key in [30, 20, 40, 10, 25, 5]:
        tree.insert(key)
    tree.print_tree()
    print("\nIn-order:", tree.inorder())
    # Expected setelah rotasi: root = 20


if __name__ == "__main__":
    test_case_LL()
    test_case_RR()
    test_case_LR()
    test_case_RL()
    test_tugas_mandiri()
