import re

with open("apps/web/app/(app)/layout.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'const { isOffline, pending } = useOfflineAlertQueue();',
    'const { isOffline, pending, dismiss, dismissAll } = useOfflineAlertQueue();'
)

content = content.replace(
    '<OfflineBanner isOffline={isOffline} pendingCount={pending.length} />',
    '<OfflineBanner pending={pending} isOffline={isOffline} onDismiss={dismiss} onDismissAll={dismissAll} />'
)

with open("apps/web/app/(app)/layout.tsx", "w") as f:
    f.write(content)
