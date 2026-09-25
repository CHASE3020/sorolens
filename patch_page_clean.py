import re

with open("apps/web/app/(app)/contracts/page.tsx", "r") as f:
    content = f.read()

# 1. Add import for ToastVariant and ReactNode
content = content.replace('import type { Column } from "@sorolens/ui";', 'import type { Column, ToastVariant } from "@sorolens/ui";\nimport type { ReactNode } from "react";')

# 2. Update Toast state
content = content.replace(
    'const [toast, setToast] = useState<{ id: number; message: string } | null>(',
    'const [toast, setToast] = useState<{ id: number; message: ReactNode; variant?: ToastVariant } | null>('
)

# 3. Update existing error toast
content = content.replace(
    'setToast({ id: ++toastSeq.current, message: result.message });',
    'setToast({ id: ++toastSeq.current, message: result.message, variant: "error" });'
)

# 4. Update Toast component JSX
content = content.replace(
    'variant="error"',
    'variant={toast.variant || "error"}'
)

# 5. Insert paste effect AFTER handleTrackSubmit
paste_code = """
  // ---------------------------------------------------------------------------
  // Paste-to-add contract listener
  // ---------------------------------------------------------------------------
  useEffect(() => {
    const handlePaste = (e: ClipboardEvent) => {
      if (
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement
      ) {
        return;
      }
      
      const pastedText = e.clipboardData?.getData("text")?.trim();
      if (!pastedText || !CONTRACT_ID_RE.test(pastedText)) return;
      
      const trackId = pastedText;
      const tId = ++toastSeq.current;
      setToast({
        id: tId,
        variant: "info",
        message: (
          <div className="flex flex-col gap-2">
            <div>
              Track this contract?
              <br />
              <span className="font-mono text-xs opacity-70">{trackId}</span>
            </div>
            <button
              type="button"
              className="self-start rounded bg-[var(--color-accent)] px-3 py-1 text-xs font-semibold text-[var(--color-bg-page)] hover:opacity-90 transition-opacity"
              onClick={() => {
                dismissToast();
                handleTrackSubmit({ id: trackId });
              }}
            >
              Confirm
            </button>
          </div>
        ),
      });
    };
    
    document.addEventListener("paste", handlePaste);
    return () => document.removeEventListener("paste", handlePaste);
  }, [handleTrackSubmit]);
"""

# Find // Render and insert before it
content = content.replace(
    '  // ---------------------------------------------------------------------------\n  // Render\n  // ---------------------------------------------------------------------------',
    paste_code + '\n  // ---------------------------------------------------------------------------\n  // Render\n  // ---------------------------------------------------------------------------'
)

with open("apps/web/app/(app)/contracts/page.tsx", "w") as f:
    f.write(content)

