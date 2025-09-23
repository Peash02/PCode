import time
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
            print(f"Inserted {song} to Playlist.")
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
            print(f"Deleted {song} from Playlist.")
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

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head.prev = temp
        self.head.next.prev = None
        self.head = self.head.next
        temp.next.next = None

        return f"Current song:{self.head.data}"
    
    def previous_song(self):
        if self.head is None:
            return "Playlist is Empty!!!"
        
        if self.head.next is None:
            return f"Current song:{self.head.data}"
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head
        temp.prev.next = None
        temp.prev = None
        self.head.prev = temp
        self.head = temp 

        return f"Current Song:{self.head.data}"
    
    def current_song(self):
        if self.head is None:
            return "Playlist is Empty!!!"
        
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
    while True:
        time.sleep(1)
        print("------------")
        print("MUSIC PLAYER")
        print("------------")
        time.sleep(0.6)
        print("1.Add Song\n2.Delete Song\n3.Next Song\n4.Previous Song\n5.Show Playlist\n6.Show Current Playing Song\n7.Exit")
        print("------------")
        time.sleep(0.6)
        x = int(input("Enter Your Choice:"))
        print("------------")
        if x == 1:
            song = input("Enter Song Name:")
            mp.add_song(song)
            print("------------")
        elif x == 2:
            song = input("Enter Song Name:")
            mp.delete_song(song)
            print("------------")
        elif x == 3:
            print(mp.next_song())
            print("------------")
        elif x == 4:
            print(mp.previous_song())
            print("------------")
        elif x == 5:
            mp.show_playlist()
            print("------------")
        elif x == 6:
            print(mp.current_song())
            print("------------")
        elif x == 7:
            print("Thank You!!!\U0001F642")
            print("------------")
            break
        else:
            print("Invalid Choice")
            
            