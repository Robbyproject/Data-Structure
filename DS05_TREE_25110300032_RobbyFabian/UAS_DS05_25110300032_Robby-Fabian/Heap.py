import heapq

class NotificationScheduler:
    def __init__(self):
        # min-heap untuk menyimpan notifikasi berdasarkan timestamp dan importance
        self._heap = [] 

    def schedule(self, notification_id: str, timestamp: int, importance: int):
        # memasukkan tuple ke dalam heap
        # Importance dijadikan negatif agar angka tinggi menjadi prioritas utama di min-heap.
        heapq.heappush(self._heap, (timestamp, -importance, notification_id))

    def get_next(self) -> str:
        if not self._heap:
            raise IndexError('No notifications scheduled')
        
        # heapq.heappop mengambil tuple dengan timestamp terkecil (atau importance tertinggi jika timestamp sama)
        next_notif = heapq.heappop(self._heap)
        
        # Kembalikan notification_id (indeks ke-2 dari tuple)
        return next_notif[2]

    def __len__(self):
        # Return jumlah notifikasi yang tersisa di antrian
        return len(self._heap)
    
# Contoh penggunaan
scheduler = NotificationScheduler()
scheduler.schedule("notif1 : Bang mabar ga bang?", 1620000000, 5)
scheduler.schedule("notif2 : Bang Besok Libur", 1620000000, 10)  # Lebih penting dari notif1
scheduler.schedule("notif3 : Cuman Test Doangg", 1620000001, 1)
print(scheduler.get_next())  # Output: "notif2" (karena lebih penting)
print(scheduler.get_next())  # Output: "notif1" (karena timestamp sama dengan notif2 tapi kurang penting)
print(scheduler.get_next())  # Output: "notif3" (karena timestamp lebih besar)
