class Tokenizer():
    def __init__(self):
        self.encode_tokenizer, self.decode_tokenizer = self.make_tokenizer()
        self.mask = "*"
    
    def make_tokenizer(self):
        store = []
        init_small = ord("a")
        init_capital = ord("A")
        
        for i in range(26):
            store.append(chr(init_small + i))
            store.append(chr(init_capital + i))
        
        store.append(" ")
        store.append(".")
        store.append(",")
        store.append("'")
        store.append("!")
        store.append("?")
        store.append("-")
        store.append("+")

        encode_tokenizer = dict()
        for i in range(len(store)):
            encode_tokenizer[store[i]] = i

        decode_tokenizer = dict()
        for i in range(len(store)):
            decode_tokenizer[i] = store[i]
        
        return encode_tokenizer, decode_tokenizer
    
        
    def encode(self, text):
        out = []
        for item in text:
            out.append(self.encode_tokenizer[item])
        return out
    
    def decode(self, text_list):
        out = []
        for item in text_list:
            out.append(self.decode_tokenizer[item])
        return "".join(out)

            
        