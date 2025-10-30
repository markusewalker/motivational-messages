package cmd

import (
	"motivational-messages/notification"

	"github.com/spf13/cobra"
)

var lunchMsgCmd = &cobra.Command{
	Use:   "lunch",
	Short: "Sends a lunch time reminder notification",
	Long:  `Sends a lunch time reminder notification to encourage taking a break and eating your lunch`,
	Args:  cobra.NoArgs,
	Run: func(cmd *cobra.Command, args []string) {
		message := LunchMsg

		notification.SendPushoverNotification(message)
	},
}
