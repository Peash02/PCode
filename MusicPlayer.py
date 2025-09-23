class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class MusicPlayer:
    def __init__(self):
        self.head = None

    def add_song(self,song):
        new_node = Node(song)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        new_node.prev = current
        print(f"Inserted {song} to Playlist.")

    def delete_song(self,song):
        if self.head is None:
            print("Empty Playlist.")
            return
        
        current = self.head
        
        if self.head.data == song:
            self.head = self.head.next
            return

        while current:
            if current.data == song:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return
            current = current.next
        print(f"Deleted {song} from Playlist.")
    
    def next_song(self):
        if self.head is None:
            return "Playlist is Empty!!!"
        
        if self.head.next is None:
            return f"Current song:{self.head.data}"
        
        current = self.head
        old_head = self.head
        while current.next:
            current = current.next
    
        current.prev.next = None
        current.prev = None
        current.next = old_head
        old_head.prev = current
        self.head = current

        return f"Current song:{self.head.data}"
    
    def previous_song(self):
        if self.head is None:
            return "Playlist is Empty!!!"
        
        old_head = self.head
        current = self.head
        while current.next:
            current = current.next

        self.head = current
        old_head.next = None
        old_head.prev = current.prev
        current.prev.next = old_head
        current.prev = None

        return f"Current Song:{self.head.data}"
    
    def show_playlist(self):
        if self.head is None:
            return"Playlist is empty."
        
        count = 1
        current = self.head
        while current:
            print(f"Song {count}:{current.data} -> ",end="")
            current = current.next
            count+=1
        print("End")

if __name__ == "__main__":
    mp = MusicPlayer()
    mp.add_song("As it was")
    mp.add_song("Watermelong Sugar")
    mp.add_song("Shape of you")
    mp.add_song("Limbo")

    mp.show_playlist()

    mp.delete_song("As it was")
    mp.show_playlist()

    mp.next_song()
    mp.show_playlist()

    mp.previous_song()
    mp.show_playlist()
            
            