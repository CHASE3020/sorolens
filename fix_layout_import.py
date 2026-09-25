import re

with open("apps/web/app/(app)/layout.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import { OfflineBanner } from "@/components/OfflineBanner";',
    'import { OfflineAlertBanner as OfflineBanner } from "@/components/OfflineAlertBanner";'
)

with open("apps/web/app/(app)/layout.tsx", "w") as f:
    f.write(content)
