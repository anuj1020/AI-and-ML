# README

## About

This is the official Wails Vanilla template.

You can configure the project by editing `wails.json`. More information about the project settings can be found
here: https://wails.io/docs/reference/project-config

## Live Development

To run in live development mode, run `wails dev` in the project directory. This will run a Vite development
server that will provide very fast hot reload of your frontend changes. If you want to develop in a browser
and have access to your Go methods, there is also a dev server that runs on http://localhost:34115. Connect
to this in your browser, and you can call your Go code from devtools.

Wails will automatically install the frontend dependencies (it runs npm install for you) and launch your application. The great part is that it will auto-reload the app whenever you change a Go or frontend file, making development incredibly fast. 🚀


## Building

To build a redistributable, production mode package, use `wails build`.

This command will now work because wails.json exists. It will bundle everything into a single, native executable located in the build/bin directory.