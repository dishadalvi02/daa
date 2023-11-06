import heapq
from collections import defaultdict
#creating node
class Node:
	def __init__(self,char,freq):
		self.char=char
		self.freq=freq
		self.left=None
		self.right=None
	def __lt__(self,other):
		return self.freq < other.freq
#creating huffman tree
def build_huffman_tree(text):
	char_f=defaultdict(int)
	for i in text:
		char_f[i]+=1
	priority_queue=[]
	for char,freq in char_f.items():
		node=Node(char,freq)
		priority_queue.append(node)
	heapq.heapify(priority_queue)
	while len(priority_queue)>1:
		left=heapq.heappop(priority_queue)
		right=heapq.heappop(priority_queue)
		merged_node=Node(None,left.freq+right.freq)
		merged_node.left=left
		merged_node.right=right
		heapq.heappush(priority_queue,merged_node)
	return priority_queue[0]
#determining huffman codes for each char
def build_huffman_codes(root,code,huffman_code):
	if root is None:
		return
	if root.char is not None:
		huffman_code[root.char]=code
	build_huffman_codes(root.left,code+'0',huffman_code)
	build_huffman_codes(root.right,code+'1',huffman_code)
#encoding
	 
def huffman_encode(text):
	root=build_huffman_tree(text)
	huffman_code={}
	build_huffman_codes(root,'',huffman_code)
	encoded_text=''.join(huffman_code[i] for i in text)
	return encoded_text,huffman_code

def huffman_decoding(encode_t,huffman_c):
	huffman_c_R={code:char for char,code in huffman_c.items()} 
	d_text=''
	current_c=''
	for i in encode_t:
		current_c+=i
		 current_c in huffman_c_R:
			d_text+=huffman_c_R[current_c]
			current_code=''
	return d_text
	
text="hello"
encode_t,huffman_c= huffman_encode(text)
print("encoded text",encode_t)
print("huffman_code",huffman_c)
d_text=huffman_decoding(encode_t,huffman_c)
print(d_text)