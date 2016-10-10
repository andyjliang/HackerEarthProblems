'''
After getting her PhD, Christie has become a celebrity at her university, and her facebook profile is full of friend requests. Being the nice girl she is, Christie has accepted all the requests.

Now Kuldeep is jealous of all the attention she is getting from other guys, so he asks her to delete some of the guys from her friend list.

To avoid a 'scene', Christie decides to remove some friends from her friend list, since she knows the popularity of each of the friend she has, she uses the following algorithm to delete a friend.

Algorithm Delete(Friend):
    DeleteFriend=false
    for i = 1 to Friend.length-1
         if (Friend[i].popularity < Friend[i+1].popularity)
            delete i th friend
            DeleteFriend=true
            break
    if(DeleteFriend == false)
        delete the last friend

Input: 
First line contains T number of test cases. First line of each test case contains N, the number of friends Christie currently has and K ,the number of friends Christie decides to delete. Next lines contains popularity of her friends separated by space.

Output: 
For each test case print N-K numbers which represent popularity of Christie friend's after deleting K friends.
'''



class LinkedList:
	def __init__(self, deleteN):
		self.end = None
		self.deleteN = deleteN

	def buildList(self, value):
		if self.end is None:
			self.end = self.head = Node(value)
		else:
			currParentNode = self.end
			while self.deleteN > 0 and int(value) > int(currParentNode.value):
				self.deleteN -= 1
				if currParentNode.parentNode:
					currParentNode = currParentNode.parentNode
				else: 
					currParentNode = None
					break
			node = Node(value, currParentNode)
			if currParentNode:
				currParentNode.nextNode = node
			self.end = node

	def printList(self):
		node = self.end
		result = []
		while node:
			result.append(node.value)
			node = node.parentNode
		return reversed(result)


class Node:
	def __init__(self, value, parentNode=None):
		self.value = value
		self.nextNode = None
		self.parentNode = parentNode



for _ in xrange(int(raw_input())):
	(n,k) = map(int, raw_input().split())
	friend_list = LinkedList(k)
	map(lambda x: friend_list.buildList(x), raw_input().split())
	print ' '.join(friend_list.printList())
