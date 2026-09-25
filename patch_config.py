import re

with open("apps/api/internal/config/config.go", "r") as f:
    content = f.read()

patch = """
	maxBodyBytes, err := MaxBodyBytesFromEnv()
	if err != nil {
		return nil, err
	}
	cfg.RequestMaxBodyBytes = maxBodyBytes

	var missing []string
"""

content = content.replace("	var missing []string", patch)

with open("apps/api/internal/config/config.go", "w") as f:
    f.write(content)
