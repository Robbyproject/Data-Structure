class Node:
    def __init__(self, product_code, name, price): 
        self.product_code = product_code
        self.name = name
        self.price = price
        self.left = None
        self.right = None

class InventoryBST:
    def __init__(self):
        self.root = None

    # Method Insert (Recursive)
    def insert(self, product_code, name, price):
        self.root = self._insert(self.root, product_code, name, price)

    def _insert(self, node, product_code, name, price):
        # Jika posisi kosong (None), buat node baru di sini
        if node is None:
            return Node(product_code, name, price)
        
        # Logika BST: Jika kode baru lebih kecil, cari ke kiri
        if product_code < node.product_code:
            node.left = self._insert(node.left, product_code, name, price)
        # Jika kode baru lebih besar, cari ke kanan
        elif product_code > node.product_code:
            node.right = self._insert(node.right, product_code, name, price)
        
        # Kembalikan node agar link antar parent-child tetap terjaga
        return node

    # Method Lookup (Recursive)
    def lookup(self, product_code):
        return self._lookup(self.root, product_code)

    def _lookup(self, node, product_code):
        # Base case: jika node kosong, berarti data tidak ditemukan
        if node is None:
            return None
        
        # Jika data ditemukan, kembalikan dalam bentuk tuple
        if product_code == node.product_code:
            return (node.product_code, node.name, node.price)
        
        # Rekursi ke kiri jika target lebih kecil, ke kanan jika lebih besar
        if product_code < node.product_code:
            return self._lookup(node.left, product_code)
        else:
            return self._lookup(node.right, product_code)

    # method tambahan untuk mendapatkan semua data dalam urutan sorted berdasarkan kode produk
    def get_all_sorted(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)      # Selesaikan sisi kiri dulu
            result.append({                       # Simpan data node saat ini
                "kode": node.product_code, 
                "nama": node.name, 
                "harga": node.price
            })
            self._inorder(node.right, result)     # Baru kemudian sisi kanan

# Contoh penggunaan
inventory = InventoryBST()
inventory.insert("P001", "Laptop", 15000000)
# inventory.insert("P002", "Smartphone", 5000000)
# inventory.insert("P003", "Headphones", 2000000)

print(inventory.lookup("P001"))
print(inventory.get_all_sorted())