// File: go-ide/app.go

package main

import (
	"context"
	"go-ide/pkg/events"
	"go-ide/pkg/files"
	"go-ide/pkg/project"
)

// App struct
type App struct {
	ctx           context.Context
	eventBus      *events.EventBus
	fileService   *files.FileService
	projectService *project.ProjectService
	// Add other services here as they are built
	// lspService      *lsp.Client
	// terminalService *terminal.Service
}

// NewApp creates a new App application struct
func NewApp(bus *events.EventBus) *App {
	return &App{
		eventBus: bus,
	}
}

// startup is called when the app starts. The context is saved
// so we can call the runtime methods
func (a *App) startup(ctx context.Context) {
	a.ctx = ctx
	// Initialize all our services
	a.fileService = files.NewFileService(a.eventBus)
	a.projectService = project.NewProjectService(a.eventBus)

	// Log that we have started
	a.eventBus.Publish("log:info", "GoCode IDE started successfully.")
}

// --- Public methods callable from frontend ---

// OpenProject prompts the user to select a directory and opens it as a project.
func (a *App) OpenProject() (project.Project, error) {
	// In a real app, this would use a Wails dialog to ask for a folder.
	// For this example, we'll hardcode a path.
	// Replace "." with a real path for testing, or implement a dialog call.
	return a.projectService.OpenProject(".")
}

// ReadFileContents reads the content of a file given its path.
func (a *App) ReadFileContents(path string) (string, error) {
	return a.fileService.ReadFile(path)
}

// SaveFileContents saves the given content to a file at the specified path.
func (a *App) SaveFileContents(path string, content string) error {
	return a.fileService.SaveFile(path, content)
}