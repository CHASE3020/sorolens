import re

with open("apps/api/internal/handler/handler_test.go", "r") as f:
    content = f.read()

# Replace the erroingSearchStore test
new_test = """
func TestSearchContractsError(t *testing.T) {
	h := &handler.Handler{
		Store:  &erroringSearchStore{Store: store.NewMockStore()},
		DB:     &store.MockPinger{Healthy: true},
		Redis:  &store.MockPinger{Healthy: true},
		Logger: slog.New(slog.NewTextHandler(io.Discard, nil)),
	}
	r := chi.NewRouter()
	r.Get("/api/v1/search", h.SearchContracts)
	
	req := httptest.NewRequest(http.MethodGet, "/api/v1/search?q=test", nil)
	w := httptest.NewRecorder()
	r.ServeHTTP(w, req)
	if w.Code != http.StatusInternalServerError {
		t.Fatalf("want 500, got %d", w.Code)
	}
}
"""

content = re.sub(r'func TestSearchContractsError.*?\}', new_test, content, flags=re.DOTALL)

with open("apps/api/internal/handler/handler_test.go", "w") as f:
    f.write(content)
