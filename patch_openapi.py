import re

with open("apps/api/internal/router/openapi_test.go", "r") as f:
    content = f.read()

# Make sure config is imported
if '"github.com/sorolens/sorolens/apps/api/internal/config"' not in content:
    content = content.replace('"github.com/sorolens/sorolens/apps/api/internal/store"', '"github.com/sorolens/sorolens/apps/api/internal/store"\n\t"github.com/sorolens/sorolens/apps/api/internal/config"')

content = content.replace("	})\n	routes", "	}, config.DefaultRequestMaxBodyBytes)\n	routes")

with open("apps/api/internal/router/openapi_test.go", "w") as f:
    f.write(content)
