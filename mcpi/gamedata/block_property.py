class BlockProperty():
  def __init__(self, property_name):
    self.property_name = property_name

class IntegerProperty(BlockProperty):
  def value(self, i):
    return IntegerPropertyWithValue(self, i)

class EnumProperty(BlockProperty):
  def value(self, enum_name):
    return EnumPropertyWithValue(self, enum_name)

class BooleanProperty(BlockProperty):
  def value(self, b):
    return BooleanPropertyWithValue(self, b)

class IntegerPropertyWithValue():
  def __init__(self, block_property, value):
    self.block_property = block_property
    self.value = value

  def add_to_dict(self, d):
    d[self.block_property.property_name] = str(self.value)

class BooleanPropertyWithValue():
  def __init__(self, block_property, value):
    self.block_property = block_property
    self.value = value

  def add_to_dict(self, d):
    if self.value == True:
      d[self.block_property.property_name] = "true"
    else:
      d[self.block_property.property_name] = "false"

class EnumPropertyWithValue():
  def __init__(self, block_property, value):
    self.block_property = block_property
    self.value = value

  def add_to_dict(self, d):
    d[self.block_property.property_name] = self.value
