class Node:
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
    
class DLL:
  def __init__(self, head=None):
    self.head = head
    self.tail = head
    self.size = 0 
  
  def __str__(self):
    if self.is_empty():
      return "List is empty"
    current = self.head
    result = "=== LIST ITEMS ===\n"
    while current:
      if not current.next:
        result += f"{current.data} --> None"
        return result 
      result += f"{current.data} <--> "
      current = current.next
  
  def __iter__(self):
    return DllIterator(self.head)
  
  def __len__(self):
    return self.size
    
  def is_empty(self):
    return self.head is None
    
  def search(self, item):
    current = self.head
    while current:
      if current.data == item:
        return current 
      current = current.next
    return None
    
  def clear(self):
    self.head = self.tail = None
    self.size = 0
  
  def find_index(self, item):
    temp = 0
    current = self.head
    while current:
      if current.data == item:
        return temp
      temp += 1
      current = current.next
    return -1
  
  def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow
    
  def has_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
  
  def get_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    current = self.head
    for i in range(index):
      current = current.next
    return current 
  
  def insert_at_index(self, index, item):
    if index == 0:
      self.insert_at_start(item)
      return 
    if self.is_empty() or index < 0:
      raise IndexError("index out of range")
    if index >= len(self):
      self.insert_at_last(item)
      return 
    prev_node = self.get_at_index(index - 1)
    node = Node(item, prev_node.next, prev_node)
    prev_node.next = node
    node.next.prev = node 
    self.size += 1
    
  def insert_at_start(self, item):
    node = Node(item, self.head)
    if self.is_empty():
      self.tail = node
    else:
      self.head.prev = node
    self.head = node
    self.size += 1
  
  def insert_at_last(self, item):
    if self.is_empty():
      self.insert_at_start(item)
      return 
    node = Node(item, self.tail)
    self.tail.next = node
    self.tail = node
    self.size += 1

  def insert_after(self, address, item):
    if address:
      node = Node(item, address.next, address)
      if address.next:
        address.next.prev = node
      else:
        self.tail = node
      address.next = node
      self.size += 1

  def delete_first(self):
    if self.is_empty():
      return 
    self.head = self.head.next
    if self.head:
      self.head.prev = None
    else:
      self.tail = None
    self.size -= 1
  
  def delete_last(self):
    if self.is_empty():
      return 
    self.tail = self.tail.prev
    if self.tail:
      self.tail.next = None
    else:
      self.head = None
    self.size -= 1
  
  def delete_item(self, item):
    if self.is_empty():
      return
    if self.head.data == item:
      self.head = self.head.next
      if self.head:
        self.head.prev = None
      else:
        self.tail = None
      self.size -= 1
      return 
    current = self.head
    while current.next:
      if current.next.data == item:
        current.next = current.next.next
        if current.next:
          current.next.prev = current 
        else:
          self.tail = current 
        self.size -= 1
        return 
      current = current.next
      
  def delete_at_index(self, index):
    if self.is_empty() or index < 0 or index >= len(self):
      raise IndexError("index out of range")
    if index == 0:
      self.delete_first()
      return 
    prev_node = self.get_at_index(index - 1)
    prev_node.next = prev_node.next.next
    if prev_node.next:
      prev_node.next.prev = prev_node
    else:
      self.tail = prev_node
    self.size -= 1
    
  def delete_duplicates(self):
    if self.is_empty():
      return 
    seen = {self.head.data}
    current = self.head
    while current.next:
      if current.next.data in seen:
        current.next = current.next.next
        if current.next:
          current.next.prev = current 
        else:
          self.tail = current 
        self.size -= 1
      else:
        seen.add(current.next.data)
        current = current.next
  
  def delete_middle(self):
    if self.is_empty():
      return 
    if not self.head.next:
      self.head = self.tail = None
      self.size = 0
      return 
    slow = self.head
    fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    if slow.next:
      slow.next.prev = slow.prev
    else:
      self.tail = slow.prev
    slow.prev.next = slow.next
    self.size -= 1
  
  def deleteEntireInstanceOfElement(self, item):
    if self.is_empty():
      return 
    while self.head and self.head.data == item:
      self.head = self.head.next
      if self.head:
        self.head.prev = None
      else:
        self.tail = None
      self.size -= 1
    current = self.head
    while current and current.next:
      if current.next.data == item:
        current.next = current.next.next
        if current.next:
          current.next.prev = current 
        else:
          self.tail = current 
        self.size -= 1
      else:
        current = current.next
        
  def print_backward(self):
    if self.is_empty():
      return "List is empty"
    current = self.tail
    while current:
      print(current.data, end=" ")
      current = current.prev
  
  def reverse_list(self):
    if self.is_empty():
      return 
    if not self.head.next:
      return self.head
    prev = None
    current = self.head
    next = None
    while current:
      next = current.next
      current.next = prev
      current.prev = next
      prev = current 
      current = next
    self.tail = self.head
    self.head = prev
    return self.head
    
class DllIterator:
  def __init__(self, start):
    self.current = start

  def __iter__(self):
    return self

  def __next__(self):
    if not self.current:
      raise StopIteration 
    data = self.current.data
    self.current = self.current.next
    return data 

