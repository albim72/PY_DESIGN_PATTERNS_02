from director import Director
from concretebuilder1 import ConceteBuilder1

director = Director()
builder = ConceteBuilder1()

director.builder = builder

print("\n produkt podstawowy:")
director.build_minimal_version()
builder.product.list_parts()

print("\n produkt pełny:")
director.build_full_version()
builder.product.list_parts()

print("\n produkt użytkownika:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
