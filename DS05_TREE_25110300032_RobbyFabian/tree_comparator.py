"""
Nama: Robby Fabian
NIM: 25110300032
Tools yang dipakai: Visual Studio Code, Python 3.10

=============================================================
Take-Home Exercise: Tree Comparator Tool
=============================================================

Tugas kamu: Bangun sebuah tool yang membandingkan BST biasa vs AVL Tree
dengan dataset yang kamu design sendiri.

Setelah exercise ini, kamu akan benar-benar paham (lewat pengalaman
langsung, bukan hanya teori) kenapa AVL Tree penting untuk jamin
performance.

Yang sudah disediakan:
- BST class dasar (insert, traversal)
- AVL class dari handout kelas (sudah lengkap dengan rotasi)

Yang harus kamu implement:
- count_comparisons(key) → hitung jumlah perbandingan saat search
- compare_trees(dataset, label) → bandingkan height & comparisons

Dan: kamu design semua dataset-nya sendiri sesuai brief di bawah.
=============================================================
"""


# =============================================
# STARTER CODE — JANGAN DIUBAH
# =============================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """BST basic — sudah lengkap insert & search."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def get_height(self):
        """Return height of tree. Leaf = 0, empty = -1."""
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    # =============================================
    # TUGAS KAMU #1: Implement count_comparisons
    # =============================================

    def count_comparisons(self, key):
        """
        Search untuk key di BST ini, dan return JUMLAH COMPARISONS
        yang dilakukan (bukan boolean found/not found).

        Setiap kali kamu membandingkan key dengan node.key, count += 1.
        - Kalau key ditemukan: count comparisons sampai ketemu.
        - Kalau key tidak ditemukan: count comparisons sampai dapat None.

        Contoh:
            tree.insert_all([50, 30, 70])
            tree.count_comparisons(30)  # → 2  (bandingkan dengan 50, lalu 30)
            tree.count_comparisons(70)  # → 2  (bandingkan dengan 50, lalu 70)
            tree.count_comparisons(50)  # → 1  (langsung ketemu di root)
            tree.count_comparisons(100) # → 2  (bandingkan 50, lalu 70, lalu None)
                                        #  Note: 2 karena kita tidak bandingkan dengan None

        HINT: Pakai method rekursif helper yang terima parameter count,
              atau pakai variable counter yang di-increment.
        """
        # TODO: implement
        count = 0
        current = self.root
        
        while current is not None:
            count += 1
            if key == current.key:
                break
            elif key < current.key:
                current = current.left
            else:
                current = current.right
                
        return count

    # -------------------------------------------
    # Helper: insert beberapa key sekaligus
    # -------------------------------------------
    def insert_all(self, keys):
        for key in keys:
            self.insert(key)


# =============================================
# AVL TREE (dari handout kelas avl_complete.py)
# =============================================
# Impor AVL dari file handout yang sudah ada:
# - Download avl_complete.py dari handout kelas
# - Simpan di folder yang sama dengan file ini
# - Lalu uncomment baris di bawah:

from avl_complete import AVLTree


# Kita perlu tambahkan count_comparisons ke AVLTree juga.
# Tapi karena AVL adalah BST, kita bisa pakai cara yang sama.
# Kamu tinggal COPY method count_comparisons kamu dari BST class di atas.

class AVLTreeWithCount(AVLTree):
    """AVL Tree dengan method count_comparisons tambahan."""

    def count_comparisons(self, key):
        """
        Sama dengan BST.count_comparisons, karena AVL juga BST.
        COPY implementasi kamu dari BST class di atas.
        """
        # TODO: implement
        count = 0
        current = self.root
        
        while current is not None:
            count += 1
            if key == current.key:
                break
            elif key < current.key:
                current = current.left
            else:
                current = current.right
                
        return count

    def insert_all(self, keys):
        for key in keys:
            self.insert(key)


# =============================================
# TUGAS KAMU #2: Implement compare_trees
# =============================================

def compare_trees(dataset, label):
    """
    Bangun BST dan AVL dari dataset yang sama, lalu bandingkan metrics.

    Expected output (format terserah kamu, yang penting informatif):

    ============================================
    Dataset: [label]
    Jumlah data: N
    ============================================

    HEIGHT:
      BST: X
      AVL: Y

    COMPARISON COUNT (rata-rata untuk search semua key di dataset):
      BST: rata-rata X comparisons
      AVL: rata-rata Y comparisons

    COMPARISON COUNT (worst case — key paling dalam):
      BST: X comparisons (untuk cari key ____)
      AVL: Y comparisons (untuk cari key ____)

    Analisis: [paragraf singkat, apa yang kamu observe?]
    ============================================

    HINT strategi:
    1. Bangun BST dengan insert_all(dataset)
    2. Bangun AVL dengan insert_all(dataset)
    3. Hitung height masing-masing
    4. Untuk setiap key di dataset, hitung count_comparisons
    5. Agregasi: rata-rata & worst case
    6. Print hasil perbandingan
    """
    # TODO: implement
    bst = BST()
    avl = AVLTreeWithCount()
    
    # 1 & 2. Build trees
    bst.insert_all(dataset)
    avl.insert_all(dataset)
    
    # 3. Get heights
    bst_height = bst.get_height()
    avl_height = avl.get_height(avl.root)
    
    # 4 & 5. Aggregate comparisons
    bst_comps = []
    avl_comps = []
    
    for key in dataset:
        bst_comps.append((bst.count_comparisons(key), key))
        avl_comps.append((avl.count_comparisons(key), key))
        
    avg_bst = sum([c[0] for c in bst_comps]) / len(dataset)
    avg_avl = sum([c[0] for c in avl_comps]) / len(dataset)
    
    worst_bst = max(bst_comps, key=lambda x: x[0])
    worst_avl = max(avl_comps, key=lambda x: x[0])
    
    if bst_height > avl_height:
        analysis = "Kondisi data menyebabkan BST menjadi tidak seimbang, sehingga tree lebih tinggi dan pencarian melambat. AVL berhasil melakukan rotasi untuk menjaga tree tetap pendek."
    else:
        analysis = "Data masuk dalam urutan yang cukup acak/ideal, sehingga tinggi BST dan AVL sama baiknya. Performa keduanya setara di dataset ini."

    # 6. Print hasil
    print("============================================")
    print(f"Dataset: [{label}]")
    print(f"Jumlah data: {len(dataset)}")
    print("============================================")
    print("\nHEIGHT:")
    print(f"  BST: {bst_height}")
    print(f"  AVL: {avl_height}")
    print("\nCOMPARISON COUNT (rata-rata untuk search semua key di dataset):")
    print(f"  BST: rata-rata {avg_bst:.2f} comparisons")
    print(f"  AVL: rata-rata {avg_avl:.2f} comparisons")
    print("\nCOMPARISON COUNT (worst case — key paling dalam):")
    print(f"  BST: {worst_bst[0]} comparisons (untuk cari key {worst_bst[1]})")
    print(f"  AVL: {worst_avl[0]} comparisons (untuk cari key {worst_avl[1]})")
    print(f"\nAnalisis: {analysis}")
    print("============================================\n")


# =============================================
# TUGAS KAMU #3: Design dan test 4 dataset
# =============================================

if __name__ == "__main__":
    # Dataset 1: RANDOM ORDER
    # Tujuan: simulasi use case normal, data masuk dengan urutan acak
    # Buat 10-15 angka yang urutannya tidak punya pattern khusus
    dataset_random = [45, 12, 78, 34, 89, 23, 56, 90, 1, 67]  # TODO: isi dengan 10-15 angka random
    compare_trees(dataset_random, "Random order")

    # Dataset 2: WORST CASE BST
    # Tujuan: cari urutan yang bikin BST jadi seperti linked list
    # Urutan apa yang akan bikin semua node masuk ke satu sisi terus?
    dataset_worst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # TODO: isi dengan 10-15 angka
    compare_trees(dataset_worst, "Worst case BST")

    # Dataset 3: NEAR-SORTED
    # Tujuan: data hampir terurut, dengan 1-2 "outlier" di tengah
    # Misalnya: 1, 2, 3, 4, 100, 5, 6, 7, 8, 9
    # Apakah outlier mengubah bentuk tree?
    dataset_near_sorted = [1, 2, 3, 4, 100, 5, 6, 7, 8, 9]  # TODO: isi dengan 10-15 angka
    compare_trees(dataset_near_sorted, "Near-sorted")

    # Dataset 4: DATASET PILIHAN KAMU
    # Tujuan: eksplor sendiri! Pilih skenario yang bikin kamu penasaran.
    # Contoh ide:
    #   - Data dengan banyak duplicate (tapi BST kita skip duplicate)
    #   - Pattern zig-zag (alternating besar-kecil)
    #   - Data dengan median di awal
    # Tulis tujuan dataset kamu di comment:
    # Tujuan saya: Ingin melihat respon BST dan AVL saat diserang dengan pola Zig-Zag yang bergantian ekstrem (besar-kecil berulang).
    dataset_custom = [90, 10, 80, 20, 70, 30, 60, 40, 50]  # TODO: isi dengan 10-15 angka
    compare_trees(dataset_custom, "Dataset custom (Zig-Zag)")


# =============================================
# TUGAS KAMU #4: Ringkasan Observasi
# =============================================
"""
Setelah run semua 4 dataset, tulis ringkasan observasi kamu
sebagai comment multi-line di bawah.

Minimal 3 kalimat, maksimal 6 kalimat. Jawab pertanyaan:
- Dataset mana yang paling menunjukkan perbedaan dramatis BST vs AVL?
- Satu insight yang kamu dapat dari tugas ini?

Ringkasan kamu:

Perbedaan paling mencolok antara BST dan AVL kelihatan banget di dataset "Worst case BST" yang angkanya sudah urut dari kecil
ke besar. Di kasus ini, bentuk BST malah memanjang miring ke satu sisi mirip seperti *linked list*, sehingga proses pencariannya
jadi lambat karena butuh banyak perbandingan. Beda halnya dengan AVL yang bisa merapikan posisinya sendiri melalui rotasi otomatis,
sehingga bentuknya tetap seimbang dan pencariannya jauh lebih cepat. Insight utama yang saya dapat, fitur *self-balancing*
ini sangat krusial di dunia nyata. Tanpa AVL, aplikasi kita bisa tiba-tiba menjadi sangat lemot dan boros
performa kalau kebetulan sistem menerima input data yang sudah terurut.

"""