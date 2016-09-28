class PostDirectory(object):
	"""AVL Binary Tree meant to store posts in an organized manner.
	Good for searching, automatically sorting, etc. Not done out of
	necessity, but more as a personal excersize."""

	nul = "null"

	def __init__(self, directory_title):
		self.root = null
		self.directory_title = directory_title

	def insert(post):
		if root == null:
			root = post
		else:
			root = insert_helper(post, root)
	def insert_helper(post, current):
		if current == null:
			return post
		else if post.compare_to(current) > 0:
			current.set_right(insert_helper(post, current.right))
			return current
		else:
			current.set_left(insert_helper(post, current.left))
			return current

		if height(current.left) - height(current.right) > 1:
			if height(current.left.left) > height(current.left.right):
				rotate(current.left)
			else:
				rotate(current.left)
				rotate(current.left)
		else:
			if height(current.right.right) > height(current.right.left):
				rotate(current.right)
			else:
				rotate(current.right)
				rotate(current.right)

		def height(post):
			if post == null:
				return -1
			else:
				return max(height(post.left), height(post.right))





class Post(object):
	"""Node Object that represents a post.
	There may potentially be multiple types of posts, but this
	is the most basic version. Meant as a node for a the Directory
	class, which functions as a Binary Tree"""

	null = "null"
	time = "today"

	def __init__(self, body):
		self.body = body
		self.date = time #TODO: replace with get date code
		self.parent = null
		self.left = null
		self.right = null

	def set_left(left_child):
		self.left = left_child

	def set_right(right_child):
		self.right = right_child

	def compare_to(post):
		return self.date.compare_to(post.date)

