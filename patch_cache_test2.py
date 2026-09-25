import re

with open("apps/api/internal/handler/cache_route_test.go", "r") as f:
    content = f.read()

content = content.replace("	})\n	routes", "	}, config.DefaultRequestMaxBodyBytes)\n	routes")

with open("apps/api/internal/handler/cache_route_test.go", "w") as f:
    f.write(content)
