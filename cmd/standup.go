package cmd

import (
	"motivational-messages/notification"

	"github.com/spf13/cobra"
)

const (
	StandupMsg = "Hourly reminder to get up and stretch those legs for at least 5 minutes!"
	BreakMsg   = "Break time! Step away from work and enjoy your break!"
	LunchMsg   = "Lunch time! Feed that belly!"
	EODMsg     = "Work day is over, time to log off!"
)

var standupCmd = &cobra.Command{
	Use:   "standup",
	Short: "Sends a stand-up reminder notification",
	Long:  `Sends a stand-up reminder notification to encourage taking an hourly break and walking around for at least 5 minutes`,
	Args:  cobra.NoArgs,
	Run: func(cmd *cobra.Command, args []string) {
		message := StandupMsg

		notification.SendPushoverNotification(message)
	},
}
