class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
      # return self.storage
    if self.current == self.capacity:
      self.current = 0
      # return self.append(item)

  def get(self):
    this = [i for i in self.storage if i is not None]
    return this



shia_laBuff = RingBuffer(3)
# print(shia_laBuff.append(8)) 
# print(shia_laBuff.append(4))
# print(shia_laBuff.append(6))
# print(shia_laBuff.append(2))
# print(shia_laBuff.append(7))
shia_laBuff.append(8)
shia_laBuff.append(4)
# shia_laBuff.append(6)
# shia_laBuff.append(2)
# shia_laBuff.append(7)
print(RingBuffer.get(shia_laBuff))