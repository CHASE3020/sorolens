import re

with open("apps/web/app/(app)/contracts/page.tsx", "r") as f:
    content = f.read()

# Fix toast state
content = content.replace(
    'const [toast, setToast] = useState<{ id: number; message: string } | null>(',
    'const [toast, setToast] = useState<{ id: number; message: React.ReactNode; variant?: ToastVariant } | null>('
)

# Remove the paste_effect that is currently there, there might be multiple!
# Let's just git checkout the file and apply a cleaner patch.
