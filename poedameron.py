Simbolos_con_frecuencia = ["Simbolo"("A", 0.2 ), "Simbolo"("B")
]

class Compression:
    # Constructor
    def __init__(self):
        self.message = ""
        self.symbol_freq = {}
        self.huffman_tree = None

    # Method to set the message to be compressed
    def set_message(self, message):
        self.message = message

    # Method to generate the symbol frequency table
    def generate_symbol_freq_table(self):
        for char in self.message:
            if char in self.symbol_freq:
                self.symbol_freq[char] += 1
            else:
                self.symbol_freq[char] = 1
 
    # Method to generate the Huffman Tree
    def generate_huffman_tree(self):
        # Create a priority queue
        pq = PriorityQueue()
 
        # Iterate through the table and add the elements to the priority que