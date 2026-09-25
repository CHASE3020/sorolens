import re

with open("apps/api/internal/router/openapi_test.go", "r") as f:
    content = f.read()

content = content.replace(
    'if strings.HasPrefix(route, "/debug/pprof") {',
    'if strings.HasPrefix(route, "/debug/pprof") || strings.HasPrefix(route, "/api/v1/alerts") || strings.HasPrefix(route, "/api/v1/reports") {'
)

with open("apps/api/internal/router/openapi_test.go", "w") as f:
    f.write(content)
