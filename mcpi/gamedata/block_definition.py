from block_property import EnumProperty, IntegerProperty, BooleanProperty

class BlockDefinition():
  pass


class Air(BlockDefinition):
  def __init__(self):
    self.id = 0
    self.name = 'air'


class Stone(BlockDefinition):
  def __init__(self):
    self.id = 1
    self.name = 'stone'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_STONE           = PROPERTY_VARIANT.value('stone')
  VARIANT_GRANITE         = PROPERTY_VARIANT.value('granite')
  VARIANT_SMOOTH_GRANITE  = PROPERTY_VARIANT.value('smooth_granite')
  VARIANT_DIORITE         = PROPERTY_VARIANT.value('diorite')
  VARIANT_SMOOTH_DIORITE  = PROPERTY_VARIANT.value('smooth_diorite')
  VARIANT_ANDESITE        = PROPERTY_VARIANT.value('andesite')
  VARIANT_SMOOTH_ANDESITE = PROPERTY_VARIANT.value('smooth_andesite')


class Grass(BlockDefinition):
  def __init__(self):
    self.id = 2
    self.name = 'grass'

  PROPERTY_SNOWY = BooleanProperty('snowy')
  SNOWY_TRUE  = PROPERTY_SNOWY.value(True)
  SNOWY_FALSE = PROPERTY_SNOWY.value(False)


class Dirt(BlockDefinition):
  def __init__(self):
    self.id = 3
    self.name = 'dirt'

  PROPERTY_SNOWY = BooleanProperty('snowy')
  SNOWY_TRUE  = PROPERTY_SNOWY.value(True)
  SNOWY_FALSE = PROPERTY_SNOWY.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_DIRT        = PROPERTY_VARIANT.value('dirt')
  VARIANT_COARSE_DIRT = PROPERTY_VARIANT.value('coarse_dirt')
  VARIANT_PODZOL      = PROPERTY_VARIANT.value('podzol')


class Cobblestone(BlockDefinition):
  def __init__(self):
    self.id = 4
    self.name = 'cobblestone'


class Planks(BlockDefinition):
  def __init__(self):
    self.id = 5
    self.name = 'planks'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_OAK      = PROPERTY_VARIANT.value('oak')
  VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce')
  VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch')
  VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle')
  VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia')
  VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak')


class Sapling(BlockDefinition):
  def __init__(self):
    self.id = 6
    self.name = 'sapling'

  PROPERTY_STAGE = IntegerProperty('stage')
  STAGE_0 = PROPERTY_STAGE.value(0)
  STAGE_1 = PROPERTY_STAGE.value(1)

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_OAK      = PROPERTY_TYPE.value('oak')
  TYPE_SPRUCE   = PROPERTY_TYPE.value('spruce')
  TYPE_BIRCH    = PROPERTY_TYPE.value('birch')
  TYPE_JUNGLE   = PROPERTY_TYPE.value('jungle')
  TYPE_ACACIA   = PROPERTY_TYPE.value('acacia')
  TYPE_DARK_OAK = PROPERTY_TYPE.value('dark_oak')


class Bedrock(BlockDefinition):
  def __init__(self):
    self.id = 7
    self.name = 'bedrock'


class FlowingWater(BlockDefinition):
  def __init__(self):
    self.id = 8
    self.name = 'flowing_water'

  PROPERTY_LEVEL = IntegerProperty('level')
  LEVEL_0  = PROPERTY_LEVEL.value(0)
  LEVEL_1  = PROPERTY_LEVEL.value(1)
  LEVEL_2  = PROPERTY_LEVEL.value(2)
  LEVEL_3  = PROPERTY_LEVEL.value(3)
  LEVEL_4  = PROPERTY_LEVEL.value(4)
  LEVEL_5  = PROPERTY_LEVEL.value(5)
  LEVEL_6  = PROPERTY_LEVEL.value(6)
  LEVEL_7  = PROPERTY_LEVEL.value(7)
  LEVEL_8  = PROPERTY_LEVEL.value(8)
  LEVEL_9  = PROPERTY_LEVEL.value(9)
  LEVEL_10 = PROPERTY_LEVEL.value(10)
  LEVEL_11 = PROPERTY_LEVEL.value(11)
  LEVEL_12 = PROPERTY_LEVEL.value(12)
  LEVEL_13 = PROPERTY_LEVEL.value(13)
  LEVEL_14 = PROPERTY_LEVEL.value(14)
  LEVEL_15 = PROPERTY_LEVEL.value(15)


class Water(BlockDefinition):
  def __init__(self):
    self.id = 9
    self.name = 'water'

  PROPERTY_LEVEL = IntegerProperty('level')
  LEVEL_0  = PROPERTY_LEVEL.value(0)
  LEVEL_1  = PROPERTY_LEVEL.value(1)
  LEVEL_2  = PROPERTY_LEVEL.value(2)
  LEVEL_3  = PROPERTY_LEVEL.value(3)
  LEVEL_4  = PROPERTY_LEVEL.value(4)
  LEVEL_5  = PROPERTY_LEVEL.value(5)
  LEVEL_6  = PROPERTY_LEVEL.value(6)
  LEVEL_7  = PROPERTY_LEVEL.value(7)
  LEVEL_8  = PROPERTY_LEVEL.value(8)
  LEVEL_9  = PROPERTY_LEVEL.value(9)
  LEVEL_10 = PROPERTY_LEVEL.value(10)
  LEVEL_11 = PROPERTY_LEVEL.value(11)
  LEVEL_12 = PROPERTY_LEVEL.value(12)
  LEVEL_13 = PROPERTY_LEVEL.value(13)
  LEVEL_14 = PROPERTY_LEVEL.value(14)
  LEVEL_15 = PROPERTY_LEVEL.value(15)


class FlowingLava(BlockDefinition):
  def __init__(self):
    self.id = 10
    self.name = 'flowing_lava'

  PROPERTY_LEVEL = IntegerProperty('level')
  LEVEL_0  = PROPERTY_LEVEL.value(0)
  LEVEL_1  = PROPERTY_LEVEL.value(1)
  LEVEL_2  = PROPERTY_LEVEL.value(2)
  LEVEL_3  = PROPERTY_LEVEL.value(3)
  LEVEL_4  = PROPERTY_LEVEL.value(4)
  LEVEL_5  = PROPERTY_LEVEL.value(5)
  LEVEL_6  = PROPERTY_LEVEL.value(6)
  LEVEL_7  = PROPERTY_LEVEL.value(7)
  LEVEL_8  = PROPERTY_LEVEL.value(8)
  LEVEL_9  = PROPERTY_LEVEL.value(9)
  LEVEL_10 = PROPERTY_LEVEL.value(10)
  LEVEL_11 = PROPERTY_LEVEL.value(11)
  LEVEL_12 = PROPERTY_LEVEL.value(12)
  LEVEL_13 = PROPERTY_LEVEL.value(13)
  LEVEL_14 = PROPERTY_LEVEL.value(14)
  LEVEL_15 = PROPERTY_LEVEL.value(15)


class Lava(BlockDefinition):
  def __init__(self):
    self.id = 11
    self.name = 'lava'

  PROPERTY_LEVEL = IntegerProperty('level')
  LEVEL_0  = PROPERTY_LEVEL.value(0)
  LEVEL_1  = PROPERTY_LEVEL.value(1)
  LEVEL_2  = PROPERTY_LEVEL.value(2)
  LEVEL_3  = PROPERTY_LEVEL.value(3)
  LEVEL_4  = PROPERTY_LEVEL.value(4)
  LEVEL_5  = PROPERTY_LEVEL.value(5)
  LEVEL_6  = PROPERTY_LEVEL.value(6)
  LEVEL_7  = PROPERTY_LEVEL.value(7)
  LEVEL_8  = PROPERTY_LEVEL.value(8)
  LEVEL_9  = PROPERTY_LEVEL.value(9)
  LEVEL_10 = PROPERTY_LEVEL.value(10)
  LEVEL_11 = PROPERTY_LEVEL.value(11)
  LEVEL_12 = PROPERTY_LEVEL.value(12)
  LEVEL_13 = PROPERTY_LEVEL.value(13)
  LEVEL_14 = PROPERTY_LEVEL.value(14)
  LEVEL_15 = PROPERTY_LEVEL.value(15)


class Sand(BlockDefinition):
  def __init__(self):
    self.id = 12
    self.name = 'sand'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_SAND     = PROPERTY_VARIANT.value('sand')
  VARIANT_RED_SAND = PROPERTY_VARIANT.value('red_sand')


class Gravel(BlockDefinition):
  def __init__(self):
    self.id = 13
    self.name = 'gravel'


class GoldOre(BlockDefinition):
  def __init__(self):
    self.id = 14
    self.name = 'gold_ore'


class IronOre(BlockDefinition):
  def __init__(self):
    self.id = 15
    self.name = 'iron_ore'


class CoalOre(BlockDefinition):
  def __init__(self):
    self.id = 16
    self.name = 'coal_ore'


class Log(BlockDefinition):
  def __init__(self):
    self.id = 17
    self.name = 'log'

  PROPERTY_AXIS = EnumProperty('axis')
  AXIS_X    = PROPERTY_AXIS.value('x')
  AXIS_Y    = PROPERTY_AXIS.value('y')
  AXIS_Z    = PROPERTY_AXIS.value('z')
  AXIS_NONE = PROPERTY_AXIS.value('none')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_OAK    = PROPERTY_VARIANT.value('oak')
  VARIANT_SPRUCE = PROPERTY_VARIANT.value('spruce')
  VARIANT_BIRCH  = PROPERTY_VARIANT.value('birch')
  VARIANT_JUNGLE = PROPERTY_VARIANT.value('jungle')


class Leaves(BlockDefinition):
  def __init__(self):
    self.id = 18
    self.name = 'leaves'

  PROPERTY_CHECK_DECAY = BooleanProperty('check_decay')
  CHECK_DECAY_TRUE  = PROPERTY_CHECK_DECAY.value(True)
  CHECK_DECAY_FALSE = PROPERTY_CHECK_DECAY.value(False)

  PROPERTY_DECAYABLE = BooleanProperty('decayable')
  DECAYABLE_TRUE  = PROPERTY_DECAYABLE.value(True)
  DECAYABLE_FALSE = PROPERTY_DECAYABLE.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_OAK    = PROPERTY_VARIANT.value('oak')
  VARIANT_SPRUCE = PROPERTY_VARIANT.value('spruce')
  VARIANT_BIRCH  = PROPERTY_VARIANT.value('birch')
  VARIANT_JUNGLE = PROPERTY_VARIANT.value('jungle')


class Sponge(BlockDefinition):
  def __init__(self):
    self.id = 19
    self.name = 'sponge'

  PROPERTY_WET = BooleanProperty('wet')
  WET_TRUE  = PROPERTY_WET.value(True)
  WET_FALSE = PROPERTY_WET.value(False)


class Glass(BlockDefinition):
  def __init__(self):
    self.id = 20
    self.name = 'glass'


class LapisOre(BlockDefinition):
  def __init__(self):
    self.id = 21
    self.name = 'lapis_ore'


class LapisBlock(BlockDefinition):
  def __init__(self):
    self.id = 22
    self.name = 'lapis_block'


class Dispenser(BlockDefinition):
  def __init__(self):
    self.id = 23
    self.name = 'dispenser'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_TRIGGERED = BooleanProperty('triggered')
  TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True)
  TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False)


class Sandstone(BlockDefinition):
  def __init__(self):
    self.id = 24
    self.name = 'sandstone'

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_SANDSTONE          = PROPERTY_TYPE.value('sandstone')
  TYPE_CHISELED_SANDSTONE = PROPERTY_TYPE.value('chiseled_sandstone')
  TYPE_SMOOTH_SANDSTONE   = PROPERTY_TYPE.value('smooth_sandstone')


class Noteblock(BlockDefinition):
  def __init__(self):
    self.id = 25
    self.name = 'noteblock'


class Bed(BlockDefinition):
  def __init__(self):
    self.id = 26
    self.name = 'bed'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_OCCUPIED = BooleanProperty('occupied')
  OCCUPIED_TRUE  = PROPERTY_OCCUPIED.value(True)
  OCCUPIED_FALSE = PROPERTY_OCCUPIED.value(False)

  PROPERTY_PART = EnumProperty('part')
  PART_HEAD = PROPERTY_PART.value('head')
  PART_FOOT = PROPERTY_PART.value('foot')


class GoldenRail(BlockDefinition):
  def __init__(self):
    self.id = 27
    self.name = 'golden_rail'

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south')
  SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west')
  SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east')
  SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west')
  SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north')
  SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south')


class DetectorRail(BlockDefinition):
  def __init__(self):
    self.id = 28
    self.name = 'detector_rail'

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south')
  SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west')
  SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east')
  SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west')
  SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north')
  SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south')


class StickyPiston(BlockDefinition):
  def __init__(self):
    self.id = 29
    self.name = 'sticky_piston'

  PROPERTY_EXTENDED = BooleanProperty('extended')
  EXTENDED_TRUE  = PROPERTY_EXTENDED.value(True)
  EXTENDED_FALSE = PROPERTY_EXTENDED.value(False)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Web(BlockDefinition):
  def __init__(self):
    self.id = 30
    self.name = 'web'


class Tallgrass(BlockDefinition):
  def __init__(self):
    self.id = 31
    self.name = 'tallgrass'

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_DEAD_BUSH  = PROPERTY_TYPE.value('dead_bush')
  TYPE_TALL_GRASS = PROPERTY_TYPE.value('tall_grass')
  TYPE_FERN       = PROPERTY_TYPE.value('fern')


class Deadbush(BlockDefinition):
  def __init__(self):
    self.id = 32
    self.name = 'deadbush'


class Piston(BlockDefinition):
  def __init__(self):
    self.id = 33
    self.name = 'piston'

  PROPERTY_EXTENDED = BooleanProperty('extended')
  EXTENDED_TRUE  = PROPERTY_EXTENDED.value(True)
  EXTENDED_FALSE = PROPERTY_EXTENDED.value(False)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class PistonHead(BlockDefinition):
  def __init__(self):
    self.id = 34
    self.name = 'piston_head'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_SHORT = BooleanProperty('short')
  SHORT_TRUE  = PROPERTY_SHORT.value(True)
  SHORT_FALSE = PROPERTY_SHORT.value(False)

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_NORMAL = PROPERTY_TYPE.value('normal')
  TYPE_STICKY = PROPERTY_TYPE.value('sticky')


class Wool(BlockDefinition):
  def __init__(self):
    self.id = 35
    self.name = 'wool'

  PROPERTY_COLOR = EnumProperty('color')
  COLOR_WHITE      = PROPERTY_COLOR.value('white')
  COLOR_ORANGE     = PROPERTY_COLOR.value('orange')
  COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta')
  COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue')
  COLOR_YELLOW     = PROPERTY_COLOR.value('yellow')
  COLOR_LIME       = PROPERTY_COLOR.value('lime')
  COLOR_PINK       = PROPERTY_COLOR.value('pink')
  COLOR_GRAY       = PROPERTY_COLOR.value('gray')
  COLOR_SILVER     = PROPERTY_COLOR.value('silver')
  COLOR_CYAN       = PROPERTY_COLOR.value('cyan')
  COLOR_PURPLE     = PROPERTY_COLOR.value('purple')
  COLOR_BLUE       = PROPERTY_COLOR.value('blue')
  COLOR_BROWN      = PROPERTY_COLOR.value('brown')
  COLOR_GREEN      = PROPERTY_COLOR.value('green')
  COLOR_RED        = PROPERTY_COLOR.value('red')
  COLOR_BLACK      = PROPERTY_COLOR.value('black')


class PistonExtension(BlockDefinition):
  def __init__(self):
    self.id = 36
    self.name = 'piston_extension'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_NORMAL = PROPERTY_TYPE.value('normal')
  TYPE_STICKY = PROPERTY_TYPE.value('sticky')


class YellowFlower(BlockDefinition):
  def __init__(self):
    self.id = 37
    self.name = 'yellow_flower'

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_DANDELION = PROPERTY_TYPE.value('dandelion')


class RedFlower(BlockDefinition):
  def __init__(self):
    self.id = 38
    self.name = 'red_flower'

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_POPPY        = PROPERTY_TYPE.value('poppy')
  TYPE_BLUE_ORCHID  = PROPERTY_TYPE.value('blue_orchid')
  TYPE_ALLIUM       = PROPERTY_TYPE.value('allium')
  TYPE_HOUSTONIA    = PROPERTY_TYPE.value('houstonia')
  TYPE_RED_TULIP    = PROPERTY_TYPE.value('red_tulip')
  TYPE_ORANGE_TULIP = PROPERTY_TYPE.value('orange_tulip')
  TYPE_WHITE_TULIP  = PROPERTY_TYPE.value('white_tulip')
  TYPE_PINK_TULIP   = PROPERTY_TYPE.value('pink_tulip')
  TYPE_OXEYE_DAISY  = PROPERTY_TYPE.value('oxeye_daisy')


class BrownMushroom(BlockDefinition):
  def __init__(self):
    self.id = 39
    self.name = 'brown_mushroom'


class RedMushroom(BlockDefinition):
  def __init__(self):
    self.id = 40
    self.name = 'red_mushroom'


class GoldBlock(BlockDefinition):
  def __init__(self):
    self.id = 41
    self.name = 'gold_block'


class IronBlock(BlockDefinition):
  def __init__(self):
    self.id = 42
    self.name = 'iron_block'


class DoubleStoneSlab(BlockDefinition):
  def __init__(self):
    self.id = 43
    self.name = 'double_stone_slab'

  PROPERTY_SEAMLESS = BooleanProperty('seamless')
  SEAMLESS_TRUE  = PROPERTY_SEAMLESS.value(True)
  SEAMLESS_FALSE = PROPERTY_SEAMLESS.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_STONE        = PROPERTY_VARIANT.value('stone')
  VARIANT_SANDSTONE    = PROPERTY_VARIANT.value('sandstone')
  VARIANT_WOOD_OLD     = PROPERTY_VARIANT.value('wood_old')
  VARIANT_COBBLESTONE  = PROPERTY_VARIANT.value('cobblestone')
  VARIANT_BRICK        = PROPERTY_VARIANT.value('brick')
  VARIANT_STONE_BRICK  = PROPERTY_VARIANT.value('stone_brick')
  VARIANT_NETHER_BRICK = PROPERTY_VARIANT.value('nether_brick')
  VARIANT_QUARTZ       = PROPERTY_VARIANT.value('quartz')


class StoneSlab(BlockDefinition):
  def __init__(self):
    self.id = 44
    self.name = 'stone_slab'

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_STONE        = PROPERTY_VARIANT.value('stone')
  VARIANT_SANDSTONE    = PROPERTY_VARIANT.value('sandstone')
  VARIANT_WOOD_OLD     = PROPERTY_VARIANT.value('wood_old')
  VARIANT_COBBLESTONE  = PROPERTY_VARIANT.value('cobblestone')
  VARIANT_BRICK        = PROPERTY_VARIANT.value('brick')
  VARIANT_STONE_BRICK  = PROPERTY_VARIANT.value('stone_brick')
  VARIANT_NETHER_BRICK = PROPERTY_VARIANT.value('nether_brick')
  VARIANT_QUARTZ       = PROPERTY_VARIANT.value('quartz')


class BrickBlock(BlockDefinition):
  def __init__(self):
    self.id = 45
    self.name = 'brick_block'


class Tnt(BlockDefinition):
  def __init__(self):
    self.id = 46
    self.name = 'tnt'

  PROPERTY_EXPLODE = BooleanProperty('explode')
  EXPLODE_TRUE  = PROPERTY_EXPLODE.value(True)
  EXPLODE_FALSE = PROPERTY_EXPLODE.value(False)


class Bookshelf(BlockDefinition):
  def __init__(self):
    self.id = 47
    self.name = 'bookshelf'


class MossyCobblestone(BlockDefinition):
  def __init__(self):
    self.id = 48
    self.name = 'mossy_cobblestone'


class Obsidian(BlockDefinition):
  def __init__(self):
    self.id = 49
    self.name = 'obsidian'


class Torch(BlockDefinition):
  def __init__(self):
    self.id = 50
    self.name = 'torch'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Fire(BlockDefinition):
  def __init__(self):
    self.id = 51
    self.name = 'fire'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0  = PROPERTY_AGE.value(0)
  AGE_1  = PROPERTY_AGE.value(1)
  AGE_2  = PROPERTY_AGE.value(2)
  AGE_3  = PROPERTY_AGE.value(3)
  AGE_4  = PROPERTY_AGE.value(4)
  AGE_5  = PROPERTY_AGE.value(5)
  AGE_6  = PROPERTY_AGE.value(6)
  AGE_7  = PROPERTY_AGE.value(7)
  AGE_8  = PROPERTY_AGE.value(8)
  AGE_9  = PROPERTY_AGE.value(9)
  AGE_10 = PROPERTY_AGE.value(10)
  AGE_11 = PROPERTY_AGE.value(11)
  AGE_12 = PROPERTY_AGE.value(12)
  AGE_13 = PROPERTY_AGE.value(13)
  AGE_14 = PROPERTY_AGE.value(14)
  AGE_15 = PROPERTY_AGE.value(15)

  PROPERTY_ALT = BooleanProperty('alt')
  ALT_TRUE  = PROPERTY_ALT.value(True)
  ALT_FALSE = PROPERTY_ALT.value(False)

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_FLIP = BooleanProperty('flip')
  FLIP_TRUE  = PROPERTY_FLIP.value(True)
  FLIP_FALSE = PROPERTY_FLIP.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_UPPER = IntegerProperty('upper')
  UPPER_0 = PROPERTY_UPPER.value(0)
  UPPER_1 = PROPERTY_UPPER.value(1)
  UPPER_2 = PROPERTY_UPPER.value(2)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class MobSpawner(BlockDefinition):
  def __init__(self):
    self.id = 52
    self.name = 'mob_spawner'


class OakStairs(BlockDefinition):
  def __init__(self):
    self.id = 53
    self.name = 'oak_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class Chest(BlockDefinition):
  def __init__(self):
    self.id = 54
    self.name = 'chest'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class RedstoneWire(BlockDefinition):
  def __init__(self):
    self.id = 55
    self.name = 'redstone_wire'

  PROPERTY_EAST = EnumProperty('east')
  EAST_UP   = PROPERTY_EAST.value('up')
  EAST_SIDE = PROPERTY_EAST.value('side')
  EAST_NONE = PROPERTY_EAST.value('none')

  PROPERTY_NORTH = EnumProperty('north')
  NORTH_UP   = PROPERTY_NORTH.value('up')
  NORTH_SIDE = PROPERTY_NORTH.value('side')
  NORTH_NONE = PROPERTY_NORTH.value('none')

  PROPERTY_POWER = IntegerProperty('power')
  POWER_0  = PROPERTY_POWER.value(0)
  POWER_1  = PROPERTY_POWER.value(1)
  POWER_2  = PROPERTY_POWER.value(2)
  POWER_3  = PROPERTY_POWER.value(3)
  POWER_4  = PROPERTY_POWER.value(4)
  POWER_5  = PROPERTY_POWER.value(5)
  POWER_6  = PROPERTY_POWER.value(6)
  POWER_7  = PROPERTY_POWER.value(7)
  POWER_8  = PROPERTY_POWER.value(8)
  POWER_9  = PROPERTY_POWER.value(9)
  POWER_10 = PROPERTY_POWER.value(10)
  POWER_11 = PROPERTY_POWER.value(11)
  POWER_12 = PROPERTY_POWER.value(12)
  POWER_13 = PROPERTY_POWER.value(13)
  POWER_14 = PROPERTY_POWER.value(14)
  POWER_15 = PROPERTY_POWER.value(15)

  PROPERTY_SOUTH = EnumProperty('south')
  SOUTH_UP   = PROPERTY_SOUTH.value('up')
  SOUTH_SIDE = PROPERTY_SOUTH.value('side')
  SOUTH_NONE = PROPERTY_SOUTH.value('none')

  PROPERTY_WEST = EnumProperty('west')
  WEST_UP   = PROPERTY_WEST.value('up')
  WEST_SIDE = PROPERTY_WEST.value('side')
  WEST_NONE = PROPERTY_WEST.value('none')


class DiamondOre(BlockDefinition):
  def __init__(self):
    self.id = 56
    self.name = 'diamond_ore'


class DiamondBlock(BlockDefinition):
  def __init__(self):
    self.id = 57
    self.name = 'diamond_block'


class CraftingTable(BlockDefinition):
  def __init__(self):
    self.id = 58
    self.name = 'crafting_table'


class Wheat(BlockDefinition):
  def __init__(self):
    self.id = 59
    self.name = 'wheat'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)
  AGE_4 = PROPERTY_AGE.value(4)
  AGE_5 = PROPERTY_AGE.value(5)
  AGE_6 = PROPERTY_AGE.value(6)
  AGE_7 = PROPERTY_AGE.value(7)


class Farmland(BlockDefinition):
  def __init__(self):
    self.id = 60
    self.name = 'farmland'

  PROPERTY_MOISTURE = IntegerProperty('moisture')
  MOISTURE_0 = PROPERTY_MOISTURE.value(0)
  MOISTURE_1 = PROPERTY_MOISTURE.value(1)
  MOISTURE_2 = PROPERTY_MOISTURE.value(2)
  MOISTURE_3 = PROPERTY_MOISTURE.value(3)
  MOISTURE_4 = PROPERTY_MOISTURE.value(4)
  MOISTURE_5 = PROPERTY_MOISTURE.value(5)
  MOISTURE_6 = PROPERTY_MOISTURE.value(6)
  MOISTURE_7 = PROPERTY_MOISTURE.value(7)


class Furnace(BlockDefinition):
  def __init__(self):
    self.id = 61
    self.name = 'furnace'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class LitFurnace(BlockDefinition):
  def __init__(self):
    self.id = 62
    self.name = 'lit_furnace'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class StandingSign(BlockDefinition):
  def __init__(self):
    self.id = 63
    self.name = 'standing_sign'

  PROPERTY_ROTATION = IntegerProperty('rotation')
  ROTATION_0  = PROPERTY_ROTATION.value(0)
  ROTATION_1  = PROPERTY_ROTATION.value(1)
  ROTATION_2  = PROPERTY_ROTATION.value(2)
  ROTATION_3  = PROPERTY_ROTATION.value(3)
  ROTATION_4  = PROPERTY_ROTATION.value(4)
  ROTATION_5  = PROPERTY_ROTATION.value(5)
  ROTATION_6  = PROPERTY_ROTATION.value(6)
  ROTATION_7  = PROPERTY_ROTATION.value(7)
  ROTATION_8  = PROPERTY_ROTATION.value(8)
  ROTATION_9  = PROPERTY_ROTATION.value(9)
  ROTATION_10 = PROPERTY_ROTATION.value(10)
  ROTATION_11 = PROPERTY_ROTATION.value(11)
  ROTATION_12 = PROPERTY_ROTATION.value(12)
  ROTATION_13 = PROPERTY_ROTATION.value(13)
  ROTATION_14 = PROPERTY_ROTATION.value(14)
  ROTATION_15 = PROPERTY_ROTATION.value(15)


class WoodenDoor(BlockDefinition):
  def __init__(self):
    self.id = 64
    self.name = 'wooden_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class Ladder(BlockDefinition):
  def __init__(self):
    self.id = 65
    self.name = 'ladder'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Rail(BlockDefinition):
  def __init__(self):
    self.id = 66
    self.name = 'rail'

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south')
  SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west')
  SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east')
  SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west')
  SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north')
  SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south')
  SHAPE_SOUTH_EAST      = PROPERTY_SHAPE.value('south_east')
  SHAPE_SOUTH_WEST      = PROPERTY_SHAPE.value('south_west')
  SHAPE_NORTH_WEST      = PROPERTY_SHAPE.value('north_west')
  SHAPE_NORTH_EAST      = PROPERTY_SHAPE.value('north_east')


class StoneStairs(BlockDefinition):
  def __init__(self):
    self.id = 67
    self.name = 'stone_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class WallSign(BlockDefinition):
  def __init__(self):
    self.id = 68
    self.name = 'wall_sign'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Lever(BlockDefinition):
  def __init__(self):
    self.id = 69
    self.name = 'lever'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN_X = PROPERTY_FACING.value('down_x')
  FACING_EAST   = PROPERTY_FACING.value('east')
  FACING_WEST   = PROPERTY_FACING.value('west')
  FACING_SOUTH  = PROPERTY_FACING.value('south')
  FACING_NORTH  = PROPERTY_FACING.value('north')
  FACING_UP_Z   = PROPERTY_FACING.value('up_z')
  FACING_UP_X   = PROPERTY_FACING.value('up_x')
  FACING_DOWN_Z = PROPERTY_FACING.value('down_z')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class StonePressurePlate(BlockDefinition):
  def __init__(self):
    self.id = 70
    self.name = 'stone_pressure_plate'

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class IronDoor(BlockDefinition):
  def __init__(self):
    self.id = 71
    self.name = 'iron_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class WoodenPressurePlate(BlockDefinition):
  def __init__(self):
    self.id = 72
    self.name = 'wooden_pressure_plate'

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class RedstoneOre(BlockDefinition):
  def __init__(self):
    self.id = 73
    self.name = 'redstone_ore'


class LitRedstoneOre(BlockDefinition):
  def __init__(self):
    self.id = 74
    self.name = 'lit_redstone_ore'


class UnlitRedstoneTorch(BlockDefinition):
  def __init__(self):
    self.id = 75
    self.name = 'unlit_redstone_torch'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class RedstoneTorch(BlockDefinition):
  def __init__(self):
    self.id = 76
    self.name = 'redstone_torch'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class StoneButton(BlockDefinition):
  def __init__(self):
    self.id = 77
    self.name = 'stone_button'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class SnowLayer(BlockDefinition):
  def __init__(self):
    self.id = 78
    self.name = 'snow_layer'

  PROPERTY_LAYERS = IntegerProperty('layers')
  LAYERS_1 = PROPERTY_LAYERS.value(1)
  LAYERS_2 = PROPERTY_LAYERS.value(2)
  LAYERS_3 = PROPERTY_LAYERS.value(3)
  LAYERS_4 = PROPERTY_LAYERS.value(4)
  LAYERS_5 = PROPERTY_LAYERS.value(5)
  LAYERS_6 = PROPERTY_LAYERS.value(6)
  LAYERS_7 = PROPERTY_LAYERS.value(7)
  LAYERS_8 = PROPERTY_LAYERS.value(8)


class Ice(BlockDefinition):
  def __init__(self):
    self.id = 79
    self.name = 'ice'


class Snow(BlockDefinition):
  def __init__(self):
    self.id = 80
    self.name = 'snow'


class Cactus(BlockDefinition):
  def __init__(self):
    self.id = 81
    self.name = 'cactus'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0  = PROPERTY_AGE.value(0)
  AGE_1  = PROPERTY_AGE.value(1)
  AGE_2  = PROPERTY_AGE.value(2)
  AGE_3  = PROPERTY_AGE.value(3)
  AGE_4  = PROPERTY_AGE.value(4)
  AGE_5  = PROPERTY_AGE.value(5)
  AGE_6  = PROPERTY_AGE.value(6)
  AGE_7  = PROPERTY_AGE.value(7)
  AGE_8  = PROPERTY_AGE.value(8)
  AGE_9  = PROPERTY_AGE.value(9)
  AGE_10 = PROPERTY_AGE.value(10)
  AGE_11 = PROPERTY_AGE.value(11)
  AGE_12 = PROPERTY_AGE.value(12)
  AGE_13 = PROPERTY_AGE.value(13)
  AGE_14 = PROPERTY_AGE.value(14)
  AGE_15 = PROPERTY_AGE.value(15)


class Clay(BlockDefinition):
  def __init__(self):
    self.id = 82
    self.name = 'clay'


class Reeds(BlockDefinition):
  def __init__(self):
    self.id = 83
    self.name = 'reeds'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0  = PROPERTY_AGE.value(0)
  AGE_1  = PROPERTY_AGE.value(1)
  AGE_2  = PROPERTY_AGE.value(2)
  AGE_3  = PROPERTY_AGE.value(3)
  AGE_4  = PROPERTY_AGE.value(4)
  AGE_5  = PROPERTY_AGE.value(5)
  AGE_6  = PROPERTY_AGE.value(6)
  AGE_7  = PROPERTY_AGE.value(7)
  AGE_8  = PROPERTY_AGE.value(8)
  AGE_9  = PROPERTY_AGE.value(9)
  AGE_10 = PROPERTY_AGE.value(10)
  AGE_11 = PROPERTY_AGE.value(11)
  AGE_12 = PROPERTY_AGE.value(12)
  AGE_13 = PROPERTY_AGE.value(13)
  AGE_14 = PROPERTY_AGE.value(14)
  AGE_15 = PROPERTY_AGE.value(15)


class Jukebox(BlockDefinition):
  def __init__(self):
    self.id = 84
    self.name = 'jukebox'

  PROPERTY_HAS_RECORD = BooleanProperty('has_record')
  HAS_RECORD_TRUE  = PROPERTY_HAS_RECORD.value(True)
  HAS_RECORD_FALSE = PROPERTY_HAS_RECORD.value(False)


class Fence(BlockDefinition):
  def __init__(self):
    self.id = 85
    self.name = 'fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class Pumpkin(BlockDefinition):
  def __init__(self):
    self.id = 86
    self.name = 'pumpkin'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Netherrack(BlockDefinition):
  def __init__(self):
    self.id = 87
    self.name = 'netherrack'


class SoulSand(BlockDefinition):
  def __init__(self):
    self.id = 88
    self.name = 'soul_sand'


class Glowstone(BlockDefinition):
  def __init__(self):
    self.id = 89
    self.name = 'glowstone'


class Portal(BlockDefinition):
  def __init__(self):
    self.id = 90
    self.name = 'portal'

  PROPERTY_AXIS = EnumProperty('axis')
  AXIS_X = PROPERTY_AXIS.value('x')
  AXIS_Z = PROPERTY_AXIS.value('z')


class LitPumpkin(BlockDefinition):
  def __init__(self):
    self.id = 91
    self.name = 'lit_pumpkin'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Cake(BlockDefinition):
  def __init__(self):
    self.id = 92
    self.name = 'cake'

  PROPERTY_BITES = IntegerProperty('bites')
  BITES_0 = PROPERTY_BITES.value(0)
  BITES_1 = PROPERTY_BITES.value(1)
  BITES_2 = PROPERTY_BITES.value(2)
  BITES_3 = PROPERTY_BITES.value(3)
  BITES_4 = PROPERTY_BITES.value(4)
  BITES_5 = PROPERTY_BITES.value(5)
  BITES_6 = PROPERTY_BITES.value(6)


class UnpoweredRepeater(BlockDefinition):
  def __init__(self):
    self.id = 93
    self.name = 'unpowered_repeater'

  PROPERTY_DELAY = IntegerProperty('delay')
  DELAY_1 = PROPERTY_DELAY.value(1)
  DELAY_2 = PROPERTY_DELAY.value(2)
  DELAY_3 = PROPERTY_DELAY.value(3)
  DELAY_4 = PROPERTY_DELAY.value(4)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_LOCKED = BooleanProperty('locked')
  LOCKED_TRUE  = PROPERTY_LOCKED.value(True)
  LOCKED_FALSE = PROPERTY_LOCKED.value(False)


class PoweredRepeater(BlockDefinition):
  def __init__(self):
    self.id = 94
    self.name = 'powered_repeater'

  PROPERTY_DELAY = IntegerProperty('delay')
  DELAY_1 = PROPERTY_DELAY.value(1)
  DELAY_2 = PROPERTY_DELAY.value(2)
  DELAY_3 = PROPERTY_DELAY.value(3)
  DELAY_4 = PROPERTY_DELAY.value(4)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_LOCKED = BooleanProperty('locked')
  LOCKED_TRUE  = PROPERTY_LOCKED.value(True)
  LOCKED_FALSE = PROPERTY_LOCKED.value(False)


class StainedGlass(BlockDefinition):
  def __init__(self):
    self.id = 95
    self.name = 'stained_glass'

  PROPERTY_COLOR = EnumProperty('color')
  COLOR_WHITE      = PROPERTY_COLOR.value('white')
  COLOR_ORANGE     = PROPERTY_COLOR.value('orange')
  COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta')
  COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue')
  COLOR_YELLOW     = PROPERTY_COLOR.value('yellow')
  COLOR_LIME       = PROPERTY_COLOR.value('lime')
  COLOR_PINK       = PROPERTY_COLOR.value('pink')
  COLOR_GRAY       = PROPERTY_COLOR.value('gray')
  COLOR_SILVER     = PROPERTY_COLOR.value('silver')
  COLOR_CYAN       = PROPERTY_COLOR.value('cyan')
  COLOR_PURPLE     = PROPERTY_COLOR.value('purple')
  COLOR_BLUE       = PROPERTY_COLOR.value('blue')
  COLOR_BROWN      = PROPERTY_COLOR.value('brown')
  COLOR_GREEN      = PROPERTY_COLOR.value('green')
  COLOR_RED        = PROPERTY_COLOR.value('red')
  COLOR_BLACK      = PROPERTY_COLOR.value('black')


class Trapdoor(BlockDefinition):
  def __init__(self):
    self.id = 96
    self.name = 'trapdoor'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)


class MonsterEgg(BlockDefinition):
  def __init__(self):
    self.id = 97
    self.name = 'monster_egg'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_STONE          = PROPERTY_VARIANT.value('stone')
  VARIANT_COBBLESTONE    = PROPERTY_VARIANT.value('cobblestone')
  VARIANT_STONE_BRICK    = PROPERTY_VARIANT.value('stone_brick')
  VARIANT_MOSSY_BRICK    = PROPERTY_VARIANT.value('mossy_brick')
  VARIANT_CRACKED_BRICK  = PROPERTY_VARIANT.value('cracked_brick')
  VARIANT_CHISELED_BRICK = PROPERTY_VARIANT.value('chiseled_brick')


class Stonebrick(BlockDefinition):
  def __init__(self):
    self.id = 98
    self.name = 'stonebrick'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_STONEBRICK          = PROPERTY_VARIANT.value('stonebrick')
  VARIANT_MOSSY_STONEBRICK    = PROPERTY_VARIANT.value('mossy_stonebrick')
  VARIANT_CRACKED_STONEBRICK  = PROPERTY_VARIANT.value('cracked_stonebrick')
  VARIANT_CHISELED_STONEBRICK = PROPERTY_VARIANT.value('chiseled_stonebrick')


class BrownMushroomBlock(BlockDefinition):
  def __init__(self):
    self.id = 99
    self.name = 'brown_mushroom_block'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_NORTH_WEST  = PROPERTY_VARIANT.value('north_west')
  VARIANT_NORTH       = PROPERTY_VARIANT.value('north')
  VARIANT_NORTH_EAST  = PROPERTY_VARIANT.value('north_east')
  VARIANT_WEST        = PROPERTY_VARIANT.value('west')
  VARIANT_CENTER      = PROPERTY_VARIANT.value('center')
  VARIANT_EAST        = PROPERTY_VARIANT.value('east')
  VARIANT_SOUTH_WEST  = PROPERTY_VARIANT.value('south_west')
  VARIANT_SOUTH       = PROPERTY_VARIANT.value('south')
  VARIANT_SOUTH_EAST  = PROPERTY_VARIANT.value('south_east')
  VARIANT_STEM        = PROPERTY_VARIANT.value('stem')
  VARIANT_ALL_INSIDE  = PROPERTY_VARIANT.value('all_inside')
  VARIANT_ALL_OUTSIDE = PROPERTY_VARIANT.value('all_outside')
  VARIANT_ALL_STEM    = PROPERTY_VARIANT.value('all_stem')


class RedMushroomBlock(BlockDefinition):
  def __init__(self):
    self.id = 100
    self.name = 'red_mushroom_block'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_NORTH_WEST  = PROPERTY_VARIANT.value('north_west')
  VARIANT_NORTH       = PROPERTY_VARIANT.value('north')
  VARIANT_NORTH_EAST  = PROPERTY_VARIANT.value('north_east')
  VARIANT_WEST        = PROPERTY_VARIANT.value('west')
  VARIANT_CENTER      = PROPERTY_VARIANT.value('center')
  VARIANT_EAST        = PROPERTY_VARIANT.value('east')
  VARIANT_SOUTH_WEST  = PROPERTY_VARIANT.value('south_west')
  VARIANT_SOUTH       = PROPERTY_VARIANT.value('south')
  VARIANT_SOUTH_EAST  = PROPERTY_VARIANT.value('south_east')
  VARIANT_STEM        = PROPERTY_VARIANT.value('stem')
  VARIANT_ALL_INSIDE  = PROPERTY_VARIANT.value('all_inside')
  VARIANT_ALL_OUTSIDE = PROPERTY_VARIANT.value('all_outside')
  VARIANT_ALL_STEM    = PROPERTY_VARIANT.value('all_stem')


class IronBars(BlockDefinition):
  def __init__(self):
    self.id = 101
    self.name = 'iron_bars'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class GlassPane(BlockDefinition):
  def __init__(self):
    self.id = 102
    self.name = 'glass_pane'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class MelonBlock(BlockDefinition):
  def __init__(self):
    self.id = 103
    self.name = 'melon_block'


class PumpkinStem(BlockDefinition):
  def __init__(self):
    self.id = 104
    self.name = 'pumpkin_stem'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)
  AGE_4 = PROPERTY_AGE.value(4)
  AGE_5 = PROPERTY_AGE.value(5)
  AGE_6 = PROPERTY_AGE.value(6)
  AGE_7 = PROPERTY_AGE.value(7)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class MelonStem(BlockDefinition):
  def __init__(self):
    self.id = 105
    self.name = 'melon_stem'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)
  AGE_4 = PROPERTY_AGE.value(4)
  AGE_5 = PROPERTY_AGE.value(5)
  AGE_6 = PROPERTY_AGE.value(6)
  AGE_7 = PROPERTY_AGE.value(7)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class Vine(BlockDefinition):
  def __init__(self):
    self.id = 106
    self.name = 'vine'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_UP = BooleanProperty('up')
  UP_TRUE  = PROPERTY_UP.value(True)
  UP_FALSE = PROPERTY_UP.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class FenceGate(BlockDefinition):
  def __init__(self):
    self.id = 107
    self.name = 'fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class BrickStairs(BlockDefinition):
  def __init__(self):
    self.id = 108
    self.name = 'brick_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class StoneBrickStairs(BlockDefinition):
  def __init__(self):
    self.id = 109
    self.name = 'stone_brick_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class Mycelium(BlockDefinition):
  def __init__(self):
    self.id = 110
    self.name = 'mycelium'

  PROPERTY_SNOWY = BooleanProperty('snowy')
  SNOWY_TRUE  = PROPERTY_SNOWY.value(True)
  SNOWY_FALSE = PROPERTY_SNOWY.value(False)


class Waterlily(BlockDefinition):
  def __init__(self):
    self.id = 111
    self.name = 'waterlily'


class NetherBrick(BlockDefinition):
  def __init__(self):
    self.id = 112
    self.name = 'nether_brick'


class NetherBrickFence(BlockDefinition):
  def __init__(self):
    self.id = 113
    self.name = 'nether_brick_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class NetherBrickStairs(BlockDefinition):
  def __init__(self):
    self.id = 114
    self.name = 'nether_brick_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class NetherWart(BlockDefinition):
  def __init__(self):
    self.id = 115
    self.name = 'nether_wart'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)


class EnchantingTable(BlockDefinition):
  def __init__(self):
    self.id = 116
    self.name = 'enchanting_table'


class BrewingStand(BlockDefinition):
  def __init__(self):
    self.id = 117
    self.name = 'brewing_stand'

  PROPERTY_HAS_BOTTLE_0 = BooleanProperty('has_bottle_0')
  HAS_BOTTLE_0_TRUE  = PROPERTY_HAS_BOTTLE_0.value(True)
  HAS_BOTTLE_0_FALSE = PROPERTY_HAS_BOTTLE_0.value(False)

  PROPERTY_HAS_BOTTLE_1 = BooleanProperty('has_bottle_1')
  HAS_BOTTLE_1_TRUE  = PROPERTY_HAS_BOTTLE_1.value(True)
  HAS_BOTTLE_1_FALSE = PROPERTY_HAS_BOTTLE_1.value(False)

  PROPERTY_HAS_BOTTLE_2 = BooleanProperty('has_bottle_2')
  HAS_BOTTLE_2_TRUE  = PROPERTY_HAS_BOTTLE_2.value(True)
  HAS_BOTTLE_2_FALSE = PROPERTY_HAS_BOTTLE_2.value(False)


class Cauldron(BlockDefinition):
  def __init__(self):
    self.id = 118
    self.name = 'cauldron'

  PROPERTY_LEVEL = IntegerProperty('level')
  LEVEL_0 = PROPERTY_LEVEL.value(0)
  LEVEL_1 = PROPERTY_LEVEL.value(1)
  LEVEL_2 = PROPERTY_LEVEL.value(2)
  LEVEL_3 = PROPERTY_LEVEL.value(3)


class EndPortal(BlockDefinition):
  def __init__(self):
    self.id = 119
    self.name = 'end_portal'


class EndPortalFrame(BlockDefinition):
  def __init__(self):
    self.id = 120
    self.name = 'end_portal_frame'

  PROPERTY_EYE = BooleanProperty('eye')
  EYE_TRUE  = PROPERTY_EYE.value(True)
  EYE_FALSE = PROPERTY_EYE.value(False)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class EndStone(BlockDefinition):
  def __init__(self):
    self.id = 121
    self.name = 'end_stone'


class DragonEgg(BlockDefinition):
  def __init__(self):
    self.id = 122
    self.name = 'dragon_egg'


class RedstoneLamp(BlockDefinition):
  def __init__(self):
    self.id = 123
    self.name = 'redstone_lamp'


class LitRedstoneLamp(BlockDefinition):
  def __init__(self):
    self.id = 124
    self.name = 'lit_redstone_lamp'


class DoubleWoodenSlab(BlockDefinition):
  def __init__(self):
    self.id = 125
    self.name = 'double_wooden_slab'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_OAK      = PROPERTY_VARIANT.value('oak')
  VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce')
  VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch')
  VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle')
  VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia')
  VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak')


class WoodenSlab(BlockDefinition):
  def __init__(self):
    self.id = 126
    self.name = 'wooden_slab'

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_OAK      = PROPERTY_VARIANT.value('oak')
  VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce')
  VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch')
  VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle')
  VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia')
  VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak')


class Cocoa(BlockDefinition):
  def __init__(self):
    self.id = 127
    self.name = 'cocoa'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class SandstoneStairs(BlockDefinition):
  def __init__(self):
    self.id = 128
    self.name = 'sandstone_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class EmeraldOre(BlockDefinition):
  def __init__(self):
    self.id = 129
    self.name = 'emerald_ore'


class EnderChest(BlockDefinition):
  def __init__(self):
    self.id = 130
    self.name = 'ender_chest'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class TripwireHook(BlockDefinition):
  def __init__(self):
    self.id = 131
    self.name = 'tripwire_hook'

  PROPERTY_ATTACHED = BooleanProperty('attached')
  ATTACHED_TRUE  = PROPERTY_ATTACHED.value(True)
  ATTACHED_FALSE = PROPERTY_ATTACHED.value(False)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

  PROPERTY_SUSPENDED = BooleanProperty('suspended')
  SUSPENDED_TRUE  = PROPERTY_SUSPENDED.value(True)
  SUSPENDED_FALSE = PROPERTY_SUSPENDED.value(False)


class Tripwire(BlockDefinition):
  def __init__(self):
    self.id = 132
    self.name = 'tripwire'

  PROPERTY_ATTACHED = BooleanProperty('attached')
  ATTACHED_TRUE  = PROPERTY_ATTACHED.value(True)
  ATTACHED_FALSE = PROPERTY_ATTACHED.value(False)

  PROPERTY_DISARMED = BooleanProperty('disarmed')
  DISARMED_TRUE  = PROPERTY_DISARMED.value(True)
  DISARMED_FALSE = PROPERTY_DISARMED.value(False)

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_SUSPENDED = BooleanProperty('suspended')
  SUSPENDED_TRUE  = PROPERTY_SUSPENDED.value(True)
  SUSPENDED_FALSE = PROPERTY_SUSPENDED.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class EmeraldBlock(BlockDefinition):
  def __init__(self):
    self.id = 133
    self.name = 'emerald_block'


class SpruceStairs(BlockDefinition):
  def __init__(self):
    self.id = 134
    self.name = 'spruce_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class BirchStairs(BlockDefinition):
  def __init__(self):
    self.id = 135
    self.name = 'birch_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class JungleStairs(BlockDefinition):
  def __init__(self):
    self.id = 136
    self.name = 'jungle_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class CommandBlock(BlockDefinition):
  def __init__(self):
    self.id = 137
    self.name = 'command_block'

  PROPERTY_TRIGGERED = BooleanProperty('triggered')
  TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True)
  TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False)


class Beacon(BlockDefinition):
  def __init__(self):
    self.id = 138
    self.name = 'beacon'


class CobblestoneWall(BlockDefinition):
  def __init__(self):
    self.id = 139
    self.name = 'cobblestone_wall'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_UP = BooleanProperty('up')
  UP_TRUE  = PROPERTY_UP.value(True)
  UP_FALSE = PROPERTY_UP.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_COBBLESTONE       = PROPERTY_VARIANT.value('cobblestone')
  VARIANT_MOSSY_COBBLESTONE = PROPERTY_VARIANT.value('mossy_cobblestone')

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class FlowerPot(BlockDefinition):
  def __init__(self):
    self.id = 140
    self.name = 'flower_pot'

  PROPERTY_CONTENTS = EnumProperty('contents')
  CONTENTS_EMPTY            = PROPERTY_CONTENTS.value('empty')
  CONTENTS_ROSE             = PROPERTY_CONTENTS.value('rose')
  CONTENTS_BLUE_ORCHID      = PROPERTY_CONTENTS.value('blue_orchid')
  CONTENTS_ALLIUM           = PROPERTY_CONTENTS.value('allium')
  CONTENTS_HOUSTONIA        = PROPERTY_CONTENTS.value('houstonia')
  CONTENTS_RED_TULIP        = PROPERTY_CONTENTS.value('red_tulip')
  CONTENTS_ORANGE_TULIP     = PROPERTY_CONTENTS.value('orange_tulip')
  CONTENTS_WHITE_TULIP      = PROPERTY_CONTENTS.value('white_tulip')
  CONTENTS_PINK_TULIP       = PROPERTY_CONTENTS.value('pink_tulip')
  CONTENTS_OXEYE_DAISY      = PROPERTY_CONTENTS.value('oxeye_daisy')
  CONTENTS_DANDELION        = PROPERTY_CONTENTS.value('dandelion')
  CONTENTS_OAK_SAPLING      = PROPERTY_CONTENTS.value('oak_sapling')
  CONTENTS_SPRUCE_SAPLING   = PROPERTY_CONTENTS.value('spruce_sapling')
  CONTENTS_BIRCH_SAPLING    = PROPERTY_CONTENTS.value('birch_sapling')
  CONTENTS_JUNGLE_SAPLING   = PROPERTY_CONTENTS.value('jungle_sapling')
  CONTENTS_ACACIA_SAPLING   = PROPERTY_CONTENTS.value('acacia_sapling')
  CONTENTS_DARK_OAK_SAPLING = PROPERTY_CONTENTS.value('dark_oak_sapling')
  CONTENTS_MUSHROOM_RED     = PROPERTY_CONTENTS.value('mushroom_red')
  CONTENTS_MUSHROOM_BROWN   = PROPERTY_CONTENTS.value('mushroom_brown')
  CONTENTS_DEAD_BUSH        = PROPERTY_CONTENTS.value('dead_bush')
  CONTENTS_FERN             = PROPERTY_CONTENTS.value('fern')
  CONTENTS_CACTUS           = PROPERTY_CONTENTS.value('cactus')

  PROPERTY_LEGACY_DATA = IntegerProperty('legacy_data')
  LEGACY_DATA_0  = PROPERTY_LEGACY_DATA.value(0)
  LEGACY_DATA_1  = PROPERTY_LEGACY_DATA.value(1)
  LEGACY_DATA_2  = PROPERTY_LEGACY_DATA.value(2)
  LEGACY_DATA_3  = PROPERTY_LEGACY_DATA.value(3)
  LEGACY_DATA_4  = PROPERTY_LEGACY_DATA.value(4)
  LEGACY_DATA_5  = PROPERTY_LEGACY_DATA.value(5)
  LEGACY_DATA_6  = PROPERTY_LEGACY_DATA.value(6)
  LEGACY_DATA_7  = PROPERTY_LEGACY_DATA.value(7)
  LEGACY_DATA_8  = PROPERTY_LEGACY_DATA.value(8)
  LEGACY_DATA_9  = PROPERTY_LEGACY_DATA.value(9)
  LEGACY_DATA_10 = PROPERTY_LEGACY_DATA.value(10)
  LEGACY_DATA_11 = PROPERTY_LEGACY_DATA.value(11)
  LEGACY_DATA_12 = PROPERTY_LEGACY_DATA.value(12)
  LEGACY_DATA_13 = PROPERTY_LEGACY_DATA.value(13)
  LEGACY_DATA_14 = PROPERTY_LEGACY_DATA.value(14)
  LEGACY_DATA_15 = PROPERTY_LEGACY_DATA.value(15)


class Carrots(BlockDefinition):
  def __init__(self):
    self.id = 141
    self.name = 'carrots'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)
  AGE_4 = PROPERTY_AGE.value(4)
  AGE_5 = PROPERTY_AGE.value(5)
  AGE_6 = PROPERTY_AGE.value(6)
  AGE_7 = PROPERTY_AGE.value(7)


class Potatoes(BlockDefinition):
  def __init__(self):
    self.id = 142
    self.name = 'potatoes'

  PROPERTY_AGE = IntegerProperty('age')
  AGE_0 = PROPERTY_AGE.value(0)
  AGE_1 = PROPERTY_AGE.value(1)
  AGE_2 = PROPERTY_AGE.value(2)
  AGE_3 = PROPERTY_AGE.value(3)
  AGE_4 = PROPERTY_AGE.value(4)
  AGE_5 = PROPERTY_AGE.value(5)
  AGE_6 = PROPERTY_AGE.value(6)
  AGE_7 = PROPERTY_AGE.value(7)


class WoodenButton(BlockDefinition):
  def __init__(self):
    self.id = 143
    self.name = 'wooden_button'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class Skull(BlockDefinition):
  def __init__(self):
    self.id = 144
    self.name = 'skull'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_NODROP = BooleanProperty('nodrop')
  NODROP_TRUE  = PROPERTY_NODROP.value(True)
  NODROP_FALSE = PROPERTY_NODROP.value(False)


class Anvil(BlockDefinition):
  def __init__(self):
    self.id = 145
    self.name = 'anvil'

  PROPERTY_DAMAGE = IntegerProperty('damage')
  DAMAGE_0 = PROPERTY_DAMAGE.value(0)
  DAMAGE_1 = PROPERTY_DAMAGE.value(1)
  DAMAGE_2 = PROPERTY_DAMAGE.value(2)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class TrappedChest(BlockDefinition):
  def __init__(self):
    self.id = 146
    self.name = 'trapped_chest'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class LightWeightedPressurePlate(BlockDefinition):
  def __init__(self):
    self.id = 147
    self.name = 'light_weighted_pressure_plate'

  PROPERTY_POWER = IntegerProperty('power')
  POWER_0  = PROPERTY_POWER.value(0)
  POWER_1  = PROPERTY_POWER.value(1)
  POWER_2  = PROPERTY_POWER.value(2)
  POWER_3  = PROPERTY_POWER.value(3)
  POWER_4  = PROPERTY_POWER.value(4)
  POWER_5  = PROPERTY_POWER.value(5)
  POWER_6  = PROPERTY_POWER.value(6)
  POWER_7  = PROPERTY_POWER.value(7)
  POWER_8  = PROPERTY_POWER.value(8)
  POWER_9  = PROPERTY_POWER.value(9)
  POWER_10 = PROPERTY_POWER.value(10)
  POWER_11 = PROPERTY_POWER.value(11)
  POWER_12 = PROPERTY_POWER.value(12)
  POWER_13 = PROPERTY_POWER.value(13)
  POWER_14 = PROPERTY_POWER.value(14)
  POWER_15 = PROPERTY_POWER.value(15)


class HeavyWeightedPressurePlate(BlockDefinition):
  def __init__(self):
    self.id = 148
    self.name = 'heavy_weighted_pressure_plate'

  PROPERTY_POWER = IntegerProperty('power')
  POWER_0  = PROPERTY_POWER.value(0)
  POWER_1  = PROPERTY_POWER.value(1)
  POWER_2  = PROPERTY_POWER.value(2)
  POWER_3  = PROPERTY_POWER.value(3)
  POWER_4  = PROPERTY_POWER.value(4)
  POWER_5  = PROPERTY_POWER.value(5)
  POWER_6  = PROPERTY_POWER.value(6)
  POWER_7  = PROPERTY_POWER.value(7)
  POWER_8  = PROPERTY_POWER.value(8)
  POWER_9  = PROPERTY_POWER.value(9)
  POWER_10 = PROPERTY_POWER.value(10)
  POWER_11 = PROPERTY_POWER.value(11)
  POWER_12 = PROPERTY_POWER.value(12)
  POWER_13 = PROPERTY_POWER.value(13)
  POWER_14 = PROPERTY_POWER.value(14)
  POWER_15 = PROPERTY_POWER.value(15)


class UnpoweredComparator(BlockDefinition):
  def __init__(self):
    self.id = 149
    self.name = 'unpowered_comparator'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_MODE = EnumProperty('mode')
  MODE_COMPARE  = PROPERTY_MODE.value('compare')
  MODE_SUBTRACT = PROPERTY_MODE.value('subtract')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class PoweredComparator(BlockDefinition):
  def __init__(self):
    self.id = 150
    self.name = 'powered_comparator'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_MODE = EnumProperty('mode')
  MODE_COMPARE  = PROPERTY_MODE.value('compare')
  MODE_SUBTRACT = PROPERTY_MODE.value('subtract')

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class DaylightDetector(BlockDefinition):
  def __init__(self):
    self.id = 151
    self.name = 'daylight_detector'

  PROPERTY_POWER = IntegerProperty('power')
  POWER_0  = PROPERTY_POWER.value(0)
  POWER_1  = PROPERTY_POWER.value(1)
  POWER_2  = PROPERTY_POWER.value(2)
  POWER_3  = PROPERTY_POWER.value(3)
  POWER_4  = PROPERTY_POWER.value(4)
  POWER_5  = PROPERTY_POWER.value(5)
  POWER_6  = PROPERTY_POWER.value(6)
  POWER_7  = PROPERTY_POWER.value(7)
  POWER_8  = PROPERTY_POWER.value(8)
  POWER_9  = PROPERTY_POWER.value(9)
  POWER_10 = PROPERTY_POWER.value(10)
  POWER_11 = PROPERTY_POWER.value(11)
  POWER_12 = PROPERTY_POWER.value(12)
  POWER_13 = PROPERTY_POWER.value(13)
  POWER_14 = PROPERTY_POWER.value(14)
  POWER_15 = PROPERTY_POWER.value(15)


class RedstoneBlock(BlockDefinition):
  def __init__(self):
    self.id = 152
    self.name = 'redstone_block'


class QuartzOre(BlockDefinition):
  def __init__(self):
    self.id = 153
    self.name = 'quartz_ore'


class Hopper(BlockDefinition):
  def __init__(self):
    self.id = 154
    self.name = 'hopper'

  PROPERTY_ENABLED = BooleanProperty('enabled')
  ENABLED_TRUE  = PROPERTY_ENABLED.value(True)
  ENABLED_FALSE = PROPERTY_ENABLED.value(False)

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class QuartzBlock(BlockDefinition):
  def __init__(self):
    self.id = 155
    self.name = 'quartz_block'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_DEFAULT  = PROPERTY_VARIANT.value('default')
  VARIANT_CHISELED = PROPERTY_VARIANT.value('chiseled')
  VARIANT_LINES_Y  = PROPERTY_VARIANT.value('lines_y')
  VARIANT_LINES_X  = PROPERTY_VARIANT.value('lines_x')
  VARIANT_LINES_Z  = PROPERTY_VARIANT.value('lines_z')


class QuartzStairs(BlockDefinition):
  def __init__(self):
    self.id = 156
    self.name = 'quartz_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class ActivatorRail(BlockDefinition):
  def __init__(self):
    self.id = 157
    self.name = 'activator_rail'

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south')
  SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west')
  SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east')
  SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west')
  SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north')
  SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south')


class Dropper(BlockDefinition):
  def __init__(self):
    self.id = 158
    self.name = 'dropper'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_DOWN  = PROPERTY_FACING.value('down')
  FACING_UP    = PROPERTY_FACING.value('up')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_TRIGGERED = BooleanProperty('triggered')
  TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True)
  TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False)


class StainedHardenedClay(BlockDefinition):
  def __init__(self):
    self.id = 159
    self.name = 'stained_hardened_clay'

  PROPERTY_COLOR = EnumProperty('color')
  COLOR_WHITE      = PROPERTY_COLOR.value('white')
  COLOR_ORANGE     = PROPERTY_COLOR.value('orange')
  COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta')
  COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue')
  COLOR_YELLOW     = PROPERTY_COLOR.value('yellow')
  COLOR_LIME       = PROPERTY_COLOR.value('lime')
  COLOR_PINK       = PROPERTY_COLOR.value('pink')
  COLOR_GRAY       = PROPERTY_COLOR.value('gray')
  COLOR_SILVER     = PROPERTY_COLOR.value('silver')
  COLOR_CYAN       = PROPERTY_COLOR.value('cyan')
  COLOR_PURPLE     = PROPERTY_COLOR.value('purple')
  COLOR_BLUE       = PROPERTY_COLOR.value('blue')
  COLOR_BROWN      = PROPERTY_COLOR.value('brown')
  COLOR_GREEN      = PROPERTY_COLOR.value('green')
  COLOR_RED        = PROPERTY_COLOR.value('red')
  COLOR_BLACK      = PROPERTY_COLOR.value('black')


class StainedGlassPane(BlockDefinition):
  def __init__(self):
    self.id = 160
    self.name = 'stained_glass_pane'

  PROPERTY_COLOR = EnumProperty('color')
  COLOR_WHITE      = PROPERTY_COLOR.value('white')
  COLOR_ORANGE     = PROPERTY_COLOR.value('orange')
  COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta')
  COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue')
  COLOR_YELLOW     = PROPERTY_COLOR.value('yellow')
  COLOR_LIME       = PROPERTY_COLOR.value('lime')
  COLOR_PINK       = PROPERTY_COLOR.value('pink')
  COLOR_GRAY       = PROPERTY_COLOR.value('gray')
  COLOR_SILVER     = PROPERTY_COLOR.value('silver')
  COLOR_CYAN       = PROPERTY_COLOR.value('cyan')
  COLOR_PURPLE     = PROPERTY_COLOR.value('purple')
  COLOR_BLUE       = PROPERTY_COLOR.value('blue')
  COLOR_BROWN      = PROPERTY_COLOR.value('brown')
  COLOR_GREEN      = PROPERTY_COLOR.value('green')
  COLOR_RED        = PROPERTY_COLOR.value('red')
  COLOR_BLACK      = PROPERTY_COLOR.value('black')

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class Leaves2(BlockDefinition):
  def __init__(self):
    self.id = 161
    self.name = 'leaves2'

  PROPERTY_CHECK_DECAY = BooleanProperty('check_decay')
  CHECK_DECAY_TRUE  = PROPERTY_CHECK_DECAY.value(True)
  CHECK_DECAY_FALSE = PROPERTY_CHECK_DECAY.value(False)

  PROPERTY_DECAYABLE = BooleanProperty('decayable')
  DECAYABLE_TRUE  = PROPERTY_DECAYABLE.value(True)
  DECAYABLE_FALSE = PROPERTY_DECAYABLE.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia')
  VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak')


class Log2(BlockDefinition):
  def __init__(self):
    self.id = 162
    self.name = 'log2'

  PROPERTY_AXIS = EnumProperty('axis')
  AXIS_X    = PROPERTY_AXIS.value('x')
  AXIS_Y    = PROPERTY_AXIS.value('y')
  AXIS_Z    = PROPERTY_AXIS.value('z')
  AXIS_NONE = PROPERTY_AXIS.value('none')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia')
  VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak')


class AcaciaStairs(BlockDefinition):
  def __init__(self):
    self.id = 163
    self.name = 'acacia_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class DarkOakStairs(BlockDefinition):
  def __init__(self):
    self.id = 164
    self.name = 'dark_oak_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class Slime(BlockDefinition):
  def __init__(self):
    self.id = 165
    self.name = 'slime'


class Barrier(BlockDefinition):
  def __init__(self):
    self.id = 166
    self.name = 'barrier'


class IronTrapdoor(BlockDefinition):
  def __init__(self):
    self.id = 167
    self.name = 'iron_trapdoor'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)


class Prismarine(BlockDefinition):
  def __init__(self):
    self.id = 168
    self.name = 'prismarine'

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_PRISMARINE        = PROPERTY_VARIANT.value('prismarine')
  VARIANT_PRISMARINE_BRICKS = PROPERTY_VARIANT.value('prismarine_bricks')
  VARIANT_DARK_PRISMARINE   = PROPERTY_VARIANT.value('dark_prismarine')


class SeaLantern(BlockDefinition):
  def __init__(self):
    self.id = 169
    self.name = 'sea_lantern'


class HayBlock(BlockDefinition):
  def __init__(self):
    self.id = 170
    self.name = 'hay_block'

  PROPERTY_AXIS = EnumProperty('axis')
  AXIS_X = PROPERTY_AXIS.value('x')
  AXIS_Y = PROPERTY_AXIS.value('y')
  AXIS_Z = PROPERTY_AXIS.value('z')


class Carpet(BlockDefinition):
  def __init__(self):
    self.id = 171
    self.name = 'carpet'

  PROPERTY_COLOR = EnumProperty('color')
  COLOR_WHITE      = PROPERTY_COLOR.value('white')
  COLOR_ORANGE     = PROPERTY_COLOR.value('orange')
  COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta')
  COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue')
  COLOR_YELLOW     = PROPERTY_COLOR.value('yellow')
  COLOR_LIME       = PROPERTY_COLOR.value('lime')
  COLOR_PINK       = PROPERTY_COLOR.value('pink')
  COLOR_GRAY       = PROPERTY_COLOR.value('gray')
  COLOR_SILVER     = PROPERTY_COLOR.value('silver')
  COLOR_CYAN       = PROPERTY_COLOR.value('cyan')
  COLOR_PURPLE     = PROPERTY_COLOR.value('purple')
  COLOR_BLUE       = PROPERTY_COLOR.value('blue')
  COLOR_BROWN      = PROPERTY_COLOR.value('brown')
  COLOR_GREEN      = PROPERTY_COLOR.value('green')
  COLOR_RED        = PROPERTY_COLOR.value('red')
  COLOR_BLACK      = PROPERTY_COLOR.value('black')


class HardenedClay(BlockDefinition):
  def __init__(self):
    self.id = 172
    self.name = 'hardened_clay'


class CoalBlock(BlockDefinition):
  def __init__(self):
    self.id = 173
    self.name = 'coal_block'


class PackedIce(BlockDefinition):
  def __init__(self):
    self.id = 174
    self.name = 'packed_ice'


class DoublePlant(BlockDefinition):
  def __init__(self):
    self.id = 175
    self.name = 'double_plant'

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_SUNFLOWER    = PROPERTY_VARIANT.value('sunflower')
  VARIANT_SYRINGA      = PROPERTY_VARIANT.value('syringa')
  VARIANT_DOUBLE_GRASS = PROPERTY_VARIANT.value('double_grass')
  VARIANT_DOUBLE_FERN  = PROPERTY_VARIANT.value('double_fern')
  VARIANT_DOUBLE_ROSE  = PROPERTY_VARIANT.value('double_rose')
  VARIANT_PAEONIA      = PROPERTY_VARIANT.value('paeonia')


class StandingBanner(BlockDefinition):
  def __init__(self):
    self.id = 176
    self.name = 'standing_banner'

  PROPERTY_ROTATION = IntegerProperty('rotation')
  ROTATION_0  = PROPERTY_ROTATION.value(0)
  ROTATION_1  = PROPERTY_ROTATION.value(1)
  ROTATION_2  = PROPERTY_ROTATION.value(2)
  ROTATION_3  = PROPERTY_ROTATION.value(3)
  ROTATION_4  = PROPERTY_ROTATION.value(4)
  ROTATION_5  = PROPERTY_ROTATION.value(5)
  ROTATION_6  = PROPERTY_ROTATION.value(6)
  ROTATION_7  = PROPERTY_ROTATION.value(7)
  ROTATION_8  = PROPERTY_ROTATION.value(8)
  ROTATION_9  = PROPERTY_ROTATION.value(9)
  ROTATION_10 = PROPERTY_ROTATION.value(10)
  ROTATION_11 = PROPERTY_ROTATION.value(11)
  ROTATION_12 = PROPERTY_ROTATION.value(12)
  ROTATION_13 = PROPERTY_ROTATION.value(13)
  ROTATION_14 = PROPERTY_ROTATION.value(14)
  ROTATION_15 = PROPERTY_ROTATION.value(15)


class WallBanner(BlockDefinition):
  def __init__(self):
    self.id = 177
    self.name = 'wall_banner'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')


class DaylightDetectorInverted(BlockDefinition):
  def __init__(self):
    self.id = 178
    self.name = 'daylight_detector_inverted'

  PROPERTY_POWER = IntegerProperty('power')
  POWER_0  = PROPERTY_POWER.value(0)
  POWER_1  = PROPERTY_POWER.value(1)
  POWER_2  = PROPERTY_POWER.value(2)
  POWER_3  = PROPERTY_POWER.value(3)
  POWER_4  = PROPERTY_POWER.value(4)
  POWER_5  = PROPERTY_POWER.value(5)
  POWER_6  = PROPERTY_POWER.value(6)
  POWER_7  = PROPERTY_POWER.value(7)
  POWER_8  = PROPERTY_POWER.value(8)
  POWER_9  = PROPERTY_POWER.value(9)
  POWER_10 = PROPERTY_POWER.value(10)
  POWER_11 = PROPERTY_POWER.value(11)
  POWER_12 = PROPERTY_POWER.value(12)
  POWER_13 = PROPERTY_POWER.value(13)
  POWER_14 = PROPERTY_POWER.value(14)
  POWER_15 = PROPERTY_POWER.value(15)


class RedSandstone(BlockDefinition):
  def __init__(self):
    self.id = 179
    self.name = 'red_sandstone'

  PROPERTY_TYPE = EnumProperty('type')
  TYPE_RED_SANDSTONE          = PROPERTY_TYPE.value('red_sandstone')
  TYPE_CHISELED_RED_SANDSTONE = PROPERTY_TYPE.value('chiseled_red_sandstone')
  TYPE_SMOOTH_RED_SANDSTONE   = PROPERTY_TYPE.value('smooth_red_sandstone')


class RedSandstoneStairs(BlockDefinition):
  def __init__(self):
    self.id = 180
    self.name = 'red_sandstone_stairs'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_SHAPE = EnumProperty('shape')
  SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight')
  SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left')
  SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right')
  SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left')
  SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right')


class DoubleStoneSlab2(BlockDefinition):
  def __init__(self):
    self.id = 181
    self.name = 'double_stone_slab2'

  PROPERTY_SEAMLESS = BooleanProperty('seamless')
  SEAMLESS_TRUE  = PROPERTY_SEAMLESS.value(True)
  SEAMLESS_FALSE = PROPERTY_SEAMLESS.value(False)

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_RED_SANDSTONE = PROPERTY_VARIANT.value('red_sandstone')


class StoneSlab2(BlockDefinition):
  def __init__(self):
    self.id = 182
    self.name = 'stone_slab2'

  PROPERTY_HALF = EnumProperty('half')
  HALF_TOP    = PROPERTY_HALF.value('top')
  HALF_BOTTOM = PROPERTY_HALF.value('bottom')

  PROPERTY_VARIANT = EnumProperty('variant')
  VARIANT_RED_SANDSTONE = PROPERTY_VARIANT.value('red_sandstone')


class SpruceFenceGate(BlockDefinition):
  def __init__(self):
    self.id = 183
    self.name = 'spruce_fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class BirchFenceGate(BlockDefinition):
  def __init__(self):
    self.id = 184
    self.name = 'birch_fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class JungleFenceGate(BlockDefinition):
  def __init__(self):
    self.id = 185
    self.name = 'jungle_fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class DarkOakFenceGate(BlockDefinition):
  def __init__(self):
    self.id = 186
    self.name = 'dark_oak_fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class AcaciaFenceGate(BlockDefinition):
  def __init__(self):
    self.id = 187
    self.name = 'acacia_fence_gate'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_IN_WALL = BooleanProperty('in_wall')
  IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True)
  IN_WALL_FALSE = PROPERTY_IN_WALL.value(False)

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class SpruceFence(BlockDefinition):
  def __init__(self):
    self.id = 188
    self.name = 'spruce_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class BirchFence(BlockDefinition):
  def __init__(self):
    self.id = 189
    self.name = 'birch_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class JungleFence(BlockDefinition):
  def __init__(self):
    self.id = 190
    self.name = 'jungle_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class DarkOakFence(BlockDefinition):
  def __init__(self):
    self.id = 191
    self.name = 'dark_oak_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class AcaciaFence(BlockDefinition):
  def __init__(self):
    self.id = 192
    self.name = 'acacia_fence'

  PROPERTY_EAST = BooleanProperty('east')
  EAST_TRUE  = PROPERTY_EAST.value(True)
  EAST_FALSE = PROPERTY_EAST.value(False)

  PROPERTY_NORTH = BooleanProperty('north')
  NORTH_TRUE  = PROPERTY_NORTH.value(True)
  NORTH_FALSE = PROPERTY_NORTH.value(False)

  PROPERTY_SOUTH = BooleanProperty('south')
  SOUTH_TRUE  = PROPERTY_SOUTH.value(True)
  SOUTH_FALSE = PROPERTY_SOUTH.value(False)

  PROPERTY_WEST = BooleanProperty('west')
  WEST_TRUE  = PROPERTY_WEST.value(True)
  WEST_FALSE = PROPERTY_WEST.value(False)


class SpruceDoor(BlockDefinition):
  def __init__(self):
    self.id = 193
    self.name = 'spruce_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class BirchDoor(BlockDefinition):
  def __init__(self):
    self.id = 194
    self.name = 'birch_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class JungleDoor(BlockDefinition):
  def __init__(self):
    self.id = 195
    self.name = 'jungle_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class AcaciaDoor(BlockDefinition):
  def __init__(self):
    self.id = 196
    self.name = 'acacia_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)


class DarkOakDoor(BlockDefinition):
  def __init__(self):
    self.id = 197
    self.name = 'dark_oak_door'

  PROPERTY_FACING = EnumProperty('facing')
  FACING_NORTH = PROPERTY_FACING.value('north')
  FACING_SOUTH = PROPERTY_FACING.value('south')
  FACING_WEST  = PROPERTY_FACING.value('west')
  FACING_EAST  = PROPERTY_FACING.value('east')

  PROPERTY_HALF = EnumProperty('half')
  HALF_UPPER = PROPERTY_HALF.value('upper')
  HALF_LOWER = PROPERTY_HALF.value('lower')

  PROPERTY_HINGE = EnumProperty('hinge')
  HINGE_LEFT  = PROPERTY_HINGE.value('left')
  HINGE_RIGHT = PROPERTY_HINGE.value('right')

  PROPERTY_OPEN = BooleanProperty('open')
  OPEN_TRUE  = PROPERTY_OPEN.value(True)
  OPEN_FALSE = PROPERTY_OPEN.value(False)

  PROPERTY_POWERED = BooleanProperty('powered')
  POWERED_TRUE  = PROPERTY_POWERED.value(True)
  POWERED_FALSE = PROPERTY_POWERED.value(False)

