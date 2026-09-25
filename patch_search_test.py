import re

with open("apps/api/internal/handler/handler_test.go", "r") as f:
    content = f.read()

# Add empty query and error tests
empty_query_test = """
	// test hitting search with an empty query
	req3 := httptest.NewRequest(http.MethodGet, "/api/v1/search?q=", nil)
	w3 := httptest.NewRecorder()
	srv.ServeHTTP(w3, req3)
	var res3 map[string][]map[string]any
	_ = json.NewDecoder(w3.Body).Decode(&res3)
	if len(res3["items"]) != 0 {
		t.Fatalf("want 0 items for empty query, got %d", len(res3["items"]))
	}
}

type erroringSearchStore struct {
	store.Store
}

func (e *erroringSearchStore) SearchContracts(ctx context.Context, query string, limit int) ([]store.Contract, error) {
	return nil, errors.New("database connection failed")
}

func TestSearchContractsError(t *testing.T) {
	srv := newTestHandler(&erroringSearchStore{Store: store.NewMockStore()}, true, true)
	req := httptest.NewRequest(http.MethodGet, "/api/v1/search?q=test", nil)
	w := httptest.NewRecorder()
	srv.ServeHTTP(w, req)
	if w.Code != http.StatusInternalServerError {
		t.Fatalf("want 500, got %d", w.Code)
	}
}
"""

content = content.replace("		t.Fatalf(\"want 2 items, got %d\", len(res2[\"items\"]))\n\t}\n}", "		t.Fatalf(\"want 2 items, got %d\", len(res2[\"items\"]))\n\t}\n" + empty_query_test)

with open("apps/api/internal/handler/handler_test.go", "w") as f:
    f.write(content)
