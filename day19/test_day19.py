import day19

TEST_CASE = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
""".strip("\n")

assert "ABCDEF" == day19.traverse(day19.map_from_string(TEST_CASE)).letters
assert 38 == day19.traverse(day19.map_from_string(TEST_CASE)).steps
