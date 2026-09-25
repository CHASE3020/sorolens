import re

with open("apps/web/app/(app)/contracts/page.tsx", "r") as f:
    content = f.read()

# 1. Import ToastVariant
content = content.replace('import type { Column } from "@sorolens/ui";', 'import type { Column, ToastVariant } from "@sorolens/ui";')

# 2. Update toast state to include variant
content = content.replace(
    'const [toast, setToast] = useState<{ id: number; message: React.ReactNode } | null>(null);',
    'const [toast, setToast] = useState<{ id: number; message: React.ReactNode; variant: ToastVariant } | null>(null);'
)

# 3. Update existing setToast calls to include variant="error"
content = content.replace(
    'setToast({ id: ++toastSeq.current, message: result.message });',
    'setToast({ id: ++toastSeq.current, message: result.message, variant: "error" });'
)

# 4. Update the Toast JSX to use the state variant
toast_jsx_old = """      {toast && (
        <Toast
          key={toast.id}
          message={toast.message}
          variant="error"
          onDismiss={dismissToast}
        />
      )}"""
toast_jsx_new = """      {toast && (
        <Toast
          key={toast.id}
          message={toast.message}
          variant={toast.variant}
          onDismiss={dismissToast}
        />
      )}"""
content = content.replace(toast_jsx_old, toast_jsx_new)

# 5. Add the paste event listener
paste_effect = """
  // ---------------------------------------------------------------------------
  // Paste-to-add contract listener
  // ---------------------------------------------------------------------------
  useEffect(() => {
    const handlePaste = (e: ClipboardEvent) => {
      // Don't intercept paste if they are already typing in an input
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
                handleTrackSubmit({ id: trackId, network: networkFilter(network) });
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
  }, [network, handleTrackSubmit]);
"""

# Insert before render section
content = content.replace('  // ---------------------------------------------------------------------------', paste_effect + '  // ---------------------------------------------------------------------------', 1)
# Wait, I want to insert it before render.
# Let's find: `// Render` and insert there
content = content.replace('  // ---------------------------------------------------------------------------\n  // Render\n  // ---------------------------------------------------------------------------', paste_effect + '\n  // ---------------------------------------------------------------------------\n  // Render\n  // ---------------------------------------------------------------------------')

with open("apps/web/app/(app)/contracts/page.tsx", "w") as f:
    f.write(content)
