class VotingSystem:
    def __init__(self):
        # Dictionary untuk candidate -> vote count
        self._votes = {} 
        # Set untuk menyimpan voter_id unik yang sudah memilih
        self._voted = set() 

    def cast_vote(self, voter_id: str, candidate: str) -> bool:
        # Cek apakah voter_id sudah ada di dalam set (O(1))
        if voter_id in self._voted:
            return False
        
        # Tambahkan voter ke catatan agar tidak bisa voting lagi
        self._voted.add(voter_id)
        
        # Update jumlah suara kandidat (O(1))
        # Jika kandidat baru, mulai dari 0 lalu tambah 1
        self._votes[candidate] = self._votes.get(candidate, 0) + 1
        return True

    def has_voted(self, voter_id: str) -> bool:
        # Pengecekan instan apakah voter sudah memilih
        return voter_id in self._voted

    def get_vote_count(self, candidate: str) -> int:
        # Ambil total suara kandidat, kembalikan 0 jika tidak ada
        return self._votes.get(candidate, 0)
    
# Contoh penggunaan
voting = VotingSystem()
print(voting.cast_vote("voter1", "Alice"))  # Output: True
print(voting.cast_vote("voter1", "Bob"))    # Output: False (sudah memilih)
print(voting.cast_vote("voter2", "Bob"))    # Output: True  
print(voting.has_voted("voter1"))           # Output: True
print(voting.has_voted("voter3"))           # Output: False 
print(voting.get_vote_count("Alice"))      # Output: 1
print(voting.get_vote_count("Bob"))        # Output: 1