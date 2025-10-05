// File: go-ide/pkg/project/service.go

package project

import (
	"go-ide/pkg/events"
	"go-ide/pkg/ui"
	"os"
	"path/filepath"
)

// Project represents the opened folder.
type Project struct {
	Name      string      `json:"name"`
	Path      string      `json:"path"`
	FileTree  []ui.FileInfo `json:"fileTree"`
}

// ProjectService handles project-related operations.
type ProjectService struct {
	eventBus *events.EventBus
	current  *Project
}

// NewProjectService creates a new ProjectService.
func NewProjectService(bus *events.EventBus) *ProjectService {
	return &ProjectService{eventBus: bus}
}

// OpenProject scans a directory and sets it as the current project.
func (s *ProjectService) OpenProject(path string) (Project, error) {
	absPath, err := filepath.Abs(path)
	if err != nil {
		return Project{}, err
	}

	tree, err := s.scanDirectory(absPath)
	if err != nil {
		return Project{}, err
	}

	s.current = &Project{
		Name:     filepath.Base(absPath),
		Path:     absPath,
		FileTree: tree,
	}

	s.eventBus.Publish("project:opened", s.current)
	return *s.current, nil
}

// scanDirectory recursively scans a directory to build a file tree.
func (s *ProjectService) scanDirectory(path string) ([]ui.FileInfo, error) {
	entries, err := os.ReadDir(path)
	if err != nil {
		return nil, err
	}

	var files []ui.FileInfo
	for _, entry := range entries {
		// Simple filtering for common project noise
		if entry.Name() == ".git" || entry.Name() == "node_modules" {
			continue
		}

		fullPath := filepath.Join(path, entry.Name())
		info := ui.FileInfo{
			Name:  entry.Name(),
			Path:  fullPath,
			IsDir: entry.IsDir(),
		}

		if entry.IsDir() {
			children, err := s.scanDirectory(fullPath)
			if err == nil { // Ignore errors from subdirectories
				info.Children = children
			}
		}
		files = append(files, info)
	}
	return files, nil
}