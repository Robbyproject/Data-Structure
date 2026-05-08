from collections import deque

class FlightNetwork:
    def __init__(self):
        # Menggunakan dictionary: origin -> list tujuan
        self.graph = {} 

    def add_route(self, origin, destination):
        if origin not in self.graph:
            self.graph[origin] = []
        self.graph[origin].append(destination)

    def get_direct_destinations(self, origin):
        # Kembalikan daftar kota tujuan langsung
        return self.graph.get(origin, [])

    def find_reachable(self, origin, k):
        if origin not in self.graph:
            return {}
        
        reachable = {} # {kota: jumlah_penerbangan}
        visited = {origin} # Menghindari siklus/loop
        queue = deque([(origin, 0)]) # (kota_saat_ini, level_saat_ini)

        while queue:
            current_city, steps = queue.popleft()
            
            # Jika masih bisa terbang lagi (level < k)
            if steps < k:
                for neighbor in self.get_direct_destinations(current_city):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        reachable[neighbor] = steps + 1
                        queue.append((neighbor, steps + 1))
        return reachable
    
# Contoh penggunaan
network = FlightNetwork()
network.add_route("Jakarta", "Surabaya")
network.add_route("Jakarta", "Bandung")
network.add_route("Surabaya", "Bali")
network.add_route("Bandung", "Yogyakarta")
print(network.get_direct_destinations("Jakarta"))  # Output: ['Surabaya', 'Bandung']
print(network.find_reachable("Jakarta", 1))  # Output: {'Surabaya: 1, 'Bandung: 1'}
print(network.find_reachable("Jakarta", 2))  # Output: {'Surabaya: 1, 'Bandung: 1', 'Bali: 2', 'Yogyakarta: 2'}     