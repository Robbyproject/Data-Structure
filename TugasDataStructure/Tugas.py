class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.items.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.items[-1]
    def isEmpty(self):
        return len(self.items) == 0
    
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if self.isEmpty():
            return "Queue kosong"
        return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue kosong"
        return self.items[0]
    def isEmpty(self):
        return len(self.items) == 0
    
class Document:
    def __init__(self, name):
        self.name = name
        self.pages = Stack()
    def addPage(self, page):
        self.pages.push(page)
        print(f"[{self.name}] Berhasil menambah: {page}")
    def printPage(self):
        if self.isEmpty():
            return "Dokumen kosong"
        return self.pages.pop()
    def isEmpty(self):
        return self.pages.isEmpty()

class PrintQueue:
    def __init__(self):
        self.documents = Queue()
    def addDocument(self, document):
        self.documents.enqueue(document)
        print(f"[PrintQueue] Berhasil menambah antrean: {document.name}")
        
    def printDocument(self):
        if self.documents.isEmpty():
            print("\nTidak ada antrean dokumen di printer.")
            return
        print("\n==== MEMULAI PROSES PRINT ====")

        while not self.documents.isEmpty():
            document = self.documents.dequeue()
            print(f"\nPrinting {document.name}:")
            while not document.isEmpty():
                print(f"● {document.printPage()}")
        print("\n==== PROSES PRINT SELESAI ====")

# Contoh Skenario Pengujian
print("==== Menambah Halaman ====")
docA = Document("Document A")
docA.addPage("Page 1")
docA.addPage("Page 2")
docA.addPage("Page 3")

print("---")
docB = Document("Document B")
docB.addPage("Page 1")
docB.addPage("Page 2")

print("\n==== Menambah Dokumen ke Printer ====")
printer = PrintQueue()
printer.addDocument(docA)
printer.addDocument(docB)

printer.printDocument() 

printer.printDocument()