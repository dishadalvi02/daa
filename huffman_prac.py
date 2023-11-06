import heapq
from collections import defaultdict

class Node:
	def __init__(self,char,freq):
		self.char=char
		self.freq=freq
		self.right=None
		self.left=None
	def __lt__(self,other):
		return self.freq < other.freq

def build_huffman_tree(text):
	char_freq=defaultdict(int)
	priority_queue=[]
	for char in text:
		char_freq[char]+=1
	for char,freq in char_freq.items():
		node=Node(char,freq)
		priority_queue.append(node)
	heapq.heapify(priority_queue)
	while len(priority_queue)>1:
		left=heapq.heappop(priority_queue)
		right=heapq.heappop(priority_queue)
		merge_node=Node(None,left.freq+right.freq)
		merge_node.left=left
		merge_node.right=right
		heapq.heappush(priority_queue,merge_node)
	return priority_queue[0]
		
	




#giving codes
def build_huffman_code(root,code,huffman_codes):
	if root is None:
		return
	if root.char is not None:
		huffman_codes[root.char]=code
	build_huffman_code(root.left,code+'0',huffman_codes)
	build_huffman_code(root.right,code+'1',huffman_codes)
	
#encoding 
def huffman_encode(text):
	root=build_huffman_tree(text)
	huffman_codes={}
	build_huffman_code(root,'',huffman_codes)
	encoded_text=''.join(huffman_codes[i] for i in text)
	return encoded_text,huffman_codes

def huffman_decode(encoded_text,huffman_codes):
	count_index=''
	count_text=''
	reverse_huffman_code={code:char for char,code in huffman_codes.items()}
	for i in encoded_text:
		count_index+=i
		for count_index in reverse_huffman_code:
			count_text+=reverse_huffman_code[count_index]
			count_index=''
	return count_text



#input text
input_text=input("give string input:")



#encode text
encoded_text,huffman_codes=huffman_encode(input_text)


#printencoded text
print("encoded text",encoded_text)
print("codes_table",huffman_codes)


#decode text
p=huffman_decode(encoded_text,huffman_codes)
#printdecoded text
print(p)
