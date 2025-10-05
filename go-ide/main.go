// File: go-ide/main.go

package main

import (
	"embed"
	"go-ide/pkg/events"
	"log"

	"github.com/wailsapp/wails/v2"
	"github.com/wailsapp/wails/v2/pkg/options"
	"github.com/wailsapp/wails/v2/pkg/options/assetserver"
)

//go:embed all:frontend/dist
var assets embed.FS

func main() {
	// Create the global event bus
	eventBus := events.NewEventBus()

	// Create an instance of the app structure
	app := NewApp(eventBus)

	// Create application with options
	err := wails.Run(&options.App{
		Title:  "GoCode IDE",
		Width:  1280,
		Height: 800,
		AssetServer: &assetserver.Options{
			Assets: assets,
		},
		BackgroundColour: &options.RGBA{R: 30, G: 30, B: 30, A: 255},
		OnStartup:        app.startup,
		Bind: []interface{}{
			app,
		},
	})

	if err != nil {
		log.Fatalf("Error starting Wails application: %s", err.Error())
	}
}