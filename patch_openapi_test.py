import re

with open("apps/api/internal/router/openapi_test.go", "r") as f:
    content = f.read()

# in TestOpenAPICoversEveryRoute, inside the chi.Walk func, ignore /debug/pprof
ignore_code = """
		if strings.HasPrefix(route, "/debug/pprof") {
			return nil
		}
		route = strings.ReplaceAll(route, "/*/", "/")
"""

content = content.replace('		route = strings.ReplaceAll(route, "/*/", "/")', ignore_code)

with open("apps/api/internal/router/openapi_test.go", "w") as f:
    f.write(content)
