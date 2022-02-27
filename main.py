from typing import List

import koogle

engine = koogle.Koogle()
engine.search("aa")
engine.search("aba")
engine.search("abab")
engine.search("abab")
engine.search("abac")
print(engine.suggestion_tree)