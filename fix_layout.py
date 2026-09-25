import re

with open("apps/web/app/(app)/layout.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import { CmdkSearch } from "@/components/CmdkSearch";\n\n  return (',
    'import { CmdkSearch } from "@/components/CmdkSearch";\n\nfunction AppLayoutInner({ children }: { children: React.ReactNode }) {\n  return ('
)

with open("apps/web/app/(app)/layout.tsx", "w") as f:
    f.write(content)
