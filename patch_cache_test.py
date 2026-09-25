import re

with open("apps/api/internal/handler/cache_route_test.go", "r") as f:
    content = f.read()

if '"github.com/sorolens/sorolens/apps/api/internal/config"' not in content:
    content = content.replace('"github.com/sorolens/sorolens/apps/api/internal/store"', '"github.com/sorolens/sorolens/apps/api/internal/store"\n\t"github.com/sorolens/sorolens/apps/api/internal/config"')

content = content.replace("router.New(h)", "router.New(h, config.DefaultRequestMaxBodyBytes)")

with open("apps/api/internal/handler/cache_route_test.go", "w") as f:
    f.write(content)
