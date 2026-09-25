import re

with open("apps/api/internal/router/router.go", "r") as f:
    content = f.read()

# add import
if '"net/http/pprof"' not in content:
    content = content.replace('"net/http"', '"net/http"\n\t"net/http/pprof"')

# add routes before "return r"
routes = """
	// Pprof (admin role)
	r.Route("/debug/pprof", func(r chi.Router) {
		r.Use(middleware.RequireRoleOrForbidden(middleware.RoleAdmin))
		r.Get("/", pprof.Index)
		r.Get("/cmdline", pprof.Cmdline)
		r.Get("/profile", pprof.Profile)
		r.Get("/symbol", pprof.Symbol)
		r.Get("/trace", pprof.Trace)
		r.Get("/{profile}", pprof.Index) // For goroutine, threadcreate, etc.
	})
"""

content = content.replace("\n\treturn r\n}", routes + "\n\treturn r\n}")

with open("apps/api/internal/router/router.go", "w") as f:
    f.write(content)
