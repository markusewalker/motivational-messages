package notification

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

// SendPushoverNotification sends a notification via the Pushover API.
func SendPushoverNotification(message string) bool {
	PUSHOVER_USER_KEY := os.Getenv("PUSHOVER_USER_KEY")
	PUSHOVER_API_TOKEN := os.Getenv("PUSHOVER_API_TOKEN")

	if PUSHOVER_USER_KEY == "" || PUSHOVER_API_TOKEN == "" {
		fmt.Println("ERROR! Missing Pushover credentials...")
		return false
	}

	url := "https://api.pushover.net/1/messages.json"
	data := map[string]string{
		"token":   PUSHOVER_API_TOKEN,
		"user":    PUSHOVER_USER_KEY,
		"message": message,
		"title":   "Motivational Message",
	}

	form := ""
	for k, v := range data {
		form += fmt.Sprintf("%s=%s&", k, v)
	}

	form = form[:len(form)-1]

	resp, err := http.Post(url, "application/x-www-form-urlencoded", bytes.NewBufferString(form))
	if err != nil {
		fmt.Printf("Error sending Pushover message: %v\n", err)
		return false
	}

	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		fmt.Printf("Pushover API Error (Status %d):\n", resp.StatusCode)
		var errorDetails map[string]any
		if err := json.NewDecoder(resp.Body).Decode(&errorDetails); err == nil {
			fmt.Printf("  Response: %v\n", errorDetails)
			if errors, ok := errorDetails["errors"].([]any); ok {
				for _, e := range errors {
					fmt.Printf("  Error: %v\n", e)
				}
			}
		} else {
			buf := new(bytes.Buffer)
			buf.ReadFrom(resp.Body)
			fmt.Printf("  Raw response: %s\n", buf.String())
		}

		return false
	}

	return true
}
