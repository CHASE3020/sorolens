import re

with open("apps/web/app/(app)/layout.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import { useOfflineAlertQueue } from "@/lib/alertQueue";',
    'import { useOfflineAlertQueue } from "@/hooks/useOfflineAlertQueue";'
)

with open("apps/web/app/(app)/layout.tsx", "w") as f:
    f.write(content)
