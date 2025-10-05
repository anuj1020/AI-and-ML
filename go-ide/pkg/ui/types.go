// File: go-ide/pkg/ui/types.go

package ui

// FileInfo represents basic information about a file or directory for the UI.
type FileInfo struct {
	Name     string `json:"name"`
	Path     string `json:"path"`
	IsDir    bool   `json:"isDir"`
	Children []FileInfo `json:"children,omitempty"`
}