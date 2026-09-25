import re

with open("apps/api/internal/handler/reports.go", "r") as f:
    content = f.read()

content = content.replace(
    '"  Signature    "+signature[:16]+"...',
    'fmt.Sprintf("  Signature    %s...", func() string { if len(signature) > 16 { return signature[:16] }; return signature }())'
)
# Make sure fmt is imported, it probably is.

with open("apps/api/internal/handler/reports.go", "w") as f:
    f.write(content)
