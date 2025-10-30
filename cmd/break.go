package cmd

import (
	"motivational-messages/notification"

	"github.com/spf13/cobra"
)

var breakMsgCmd = &cobra.Command{
	Use:   "break",
	Short: "Sends a break time reminder notification",
	Long:  `Sends a break time reminder notification to encourage stepping away and taking a break from working`,
	Args:  cobra.NoArgs,
	Run: func(cmd *cobra.Command, args []string) {
		message := BreakMsg

		notification.SendPushoverNotification(message)
	},
}
