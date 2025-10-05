// File: go-ide/pkg/files/service.go

package files

import (
	"go-ide/pkg/events"
	"os"
)

// FileService handles file I/O operations.
type FileService struct {
	eventBus *events.EventBus
}

// NewFileService creates a new FileService.
func NewFileService(bus *events.EventBus) *FileService {
	return &FileService{eventBus: bus}
}

// ReadFile reads and returns the content of a file.
func (s *FileService) ReadFile(path string) (string, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		s.eventBus.Publish("log:error", "Failed to read file: "+path)
		return "", err
	}
	s.eventBus.Publish("file:opened", path)
	return string(content), nil
}

// SaveFile writes content to a specified file path.
func (s *FileService) SaveFile(path string, content string) error {
	err := os.WriteFile(path, []byte(content), 0644) // 0644 is standard file permission
	if err != nil {
		s.eventBus.Publish("log:error", "Failed to save file: "+path)
		return err
	}
	s.eventBus.Publish("file:saved", path)
	return nil
}