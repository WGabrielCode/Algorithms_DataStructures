# na lsitach
# min_max , append, szuk naseptnik ( 3 przypadki ) ,

# znajdz k-ty el ( od najmniejszego ) mod bst zeby kazdy el mial rozmiar lewego podrzewa w sobie

class TreeNode() :
	def __init__(self , val):
		self.left = None
		self.right = None
		self.val = val
		self.side = 0

class Bst() :
	def __init__(self ) :
		self.root = None

	def insert( self , val ):
		self.root = self._insert( self.root , val )

	def _insert( self , node , val ):
		if not node :
			return TreeNode( val )
		if node.val > val :
			node.left = self._insert( node.left , val )
			node.side += 1
		else :
			node.right = self._insert( node.right , val )
		return node

	def f_successor( self , val ):
		current = self.root
		while current and current.val != val :
			if current.val < val :
				current = current.right
			else :
				current = current.left
		if not current :
			return None

		if  current.right :
			current = current . right
			while current.left :
				current = current.left
			return current.val

		successor = None
		ancestor = self.root
		while ancestor.val != current.val :
			if current.val < ancestor.val :
				successor = ancestor
				ancestor = ancestor.left
			else :
				ancestor = ancestor.right
		return successor.val if successor else None


	def mini( self ):
		current = self.root
		while current and current.left :
			current = current.left
		return current.val if current else None

	def maxi( self ):
		current = self.root
		while current and current.right :
			current = current.right
		return current.val if current else None
