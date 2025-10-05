// File: go-ide/pkg/events/bus.go

package events

import "sync"

// EventCallback is the function signature for event handlers.
type EventCallback func(data interface{})

// EventBus handles event subscriptions and publishing.
type EventBus struct {
	mu          sync.Mutex
	subscribers map[string][]EventCallback
}

// NewEventBus creates a new EventBus.
func NewEventBus() *EventBus {
	return &EventBus{
		subscribers: make(map[string][]EventCallback),
	}
}

// Subscribe adds a new event handler for a given topic.
func (bus *EventBus) Subscribe(topic string, callback EventCallback) {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	bus.subscribers[topic] = append(bus.subscribers[topic], callback)
}

// Publish sends an event to all subscribers of a topic.
func (bus *EventBus) Publish(topic string, data interface{}) {
	bus.mu.Lock()
	defer bus.mu.Unlock()
	if subscribers, found := bus.subscribers[topic]; found {
		for _, callback := range subscribers {
			// Run callbacks in a new goroutine to avoid blocking
			go callback(data)
		}
	}
}