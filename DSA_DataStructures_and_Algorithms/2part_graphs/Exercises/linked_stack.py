# zakladamy ze mamy strukture stosu. stworz put i get ( queue )  majac push i pop


class Stack :

	def __init__(self ):
		self.items = []

	def push( self , x ) :
		self.items.append( x )

	def pop( self ):
		if not self.is_empty() :
			return self.items.pop()

	def is_empty( self ):
		return len(self.items) == 0

class QueueStack :
	def __init__(self):
		self.in_ = Stack()
		self.out_ = Stack()
	def put(self , x ) :
		self.in_.push( x )
	def get( self ) :
		if self.out_.is_empty() :
			while not self.in_.is_empty() :
				self.out_.push( self.in_.pop() )
		return self.out_.pop()

q1 = QueueStack()

q1.put(10)
q1.put(20)

print(q1.get())  # 10
print(q1.get())  # 20
print( q1 )
