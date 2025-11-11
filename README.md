# leetcode_python

This is a repo that I showcase my capabity in Python Programming with Leetcode problems, including

* **Number of Islands**: a problem using 'Graph General' algorithm of DSF (Depth First Search) or BSF (Breath First Search)
* **Construct Binary Tree from preorder and inorder traversal**: a problem using 'Binary Tree General' algorithm
* **Longest Substring Without repeating Characters**: a problem using 'Sliding Window' algorithm
* **Trapping Rain Water**: a hard problam using 'Array/ String'
* **Rotate Image**: a problem using 'Matrix' algorithm
* **Longest Consecutive Sequence, Two Sum, Group Anagrams and Ransom Notes**: various problem using Hashmap'
* **3Sum and Container With Most Water**: problems using 'Two Pointers' algorithm
* **Roman to Integer and Integer to Roman**: interesting problems using 'Array/ String'
* **Linked List Cycle**: Use Floyd's Cycle-Finding Algorithm.  It is much faster than 'out of box' implementation.
* **Add Two Numbers**: Use 'val' double duty to sum up carrier, l1.val and l2.val and also as the carrier for the next round. Make sure to record the last carrier even if both l1 and l2 are exhausted.
* **LRU cache**: Design  a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.
  The implmentation 1 is using double linked list nodes backing LRU cache and add left and right dummy nodes to point to the least used node and the recently used node.  That is the common implmentation.
  The implementation 2 is using 'OrderedDict[int, int]' directly. OrderedDict's move_to_end(key) and popitem(last=False) functions fit well here. Also found an interesting bug: should we compare the cap and remove key first or should we insertfirst then compare with the cap and remove if necessary.
* **Reverse linked list and reverse linked list II**:  Follow 3-step reverse process. The reverse linked list II do need to fast forward to the left position then reverse (right-left+1) time then adjust point. It's 3-stage process.
* **Remove Nth Node From End of List and Rotate List**: I group them together because both require the left and right pointer. The left point is at the position left to the target node or the last node after the rotation. Need to use the left and/ or the right to re-assign pointer.  Also the head is subject to change.  Therefore, using dummy node to code around edge cases.  It's possible to rotate more than the length of list nodes. I get the net modulo to avoid NullPointer issue.
* **Reverse Nodes in k-Group**: It is considered the toughest one in linked list group because

  1) Cannot and should not reverse the residual list which is shorter than k.  The residual partial list need to be handled differently.
  2) Reverse multiple k-group.  That requires save and reset lp (the last node of the previous k-group or the dummy node)
* **Minimum Distance Between Three Equal Elements II (Contest 475)**: I stumbled at this one because I like to Counter to filter.  A straight forward to append to dict or defaultdict will work. Make sure to calculate the distance along the way to save loops

All Python modules got accepted by Leetcode and passed all tests. I added testcases for those Python modules commited initially.  Will spare time to add testcases for the rest of Python modules.  More are coming up...
